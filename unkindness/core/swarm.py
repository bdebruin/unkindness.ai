"""
Swarm - Manages a collection of ravens and their interactions.
"""

from typing import List, Dict, Optional, Callable, Any
from .raven import BaseRaven
from .environment import Environment


class Swarm:
    """
    A swarm of ravens.
    
    Manages:
    - Raven lifecycle (birth, death)
    - Message routing between ravens
    - Simulation stepping
    - Metrics collection
    """
    
    def __init__(self, environment: Optional[Environment] = None):
        self.ravens: Dict[str, BaseRaven] = {}
        self.environment = environment
        self.step_count = 0
        self.message_log: List[Dict] = []
        self.hooks: Dict[str, List[Callable]] = {
            'pre_step': [],
            'post_step': [],
            'raven_born': [],
            'raven_died': []
        }
    
    def add_raven(self, raven: BaseRaven) -> None:
        """Add a raven to the swarm."""
        self.ravens[raven.id] = raven
        self._run_hooks('raven_born', raven)
    
    def remove_raven(self, raven_id: str) -> Optional[BaseRaven]:
        """Remove a raven from the swarm."""
        raven = self.ravens.pop(raven_id, None)
        if raven:
            self._run_hooks('raven_died', raven)
        return raven
    
    def get_nearby_ravens(self, raven: BaseRaven, radius: float) -> List[BaseRaven]:
        """Get all ravens within radius of a given raven."""
        nearby = []
        for other in self.ravens.values():
            if other.id != raven.id and raven.distance_to(other) <= radius:
                nearby.append(other)
        return nearby
    
    def broadcast(self, sender: BaseRaven, message: str, radius: Optional[float] = None) -> int:
        """Broadcast a message to nearby ravens."""
        radius = radius or sender.config.communication_radius
        recipients = self.get_nearby_ravens(sender, radius)
        
        for recipient in recipients:
            recipient.receive_message(message, sender)
        
        self.message_log.append({
            'step': self.step_count,
            'sender': sender.id,
            'recipients': [r.id for r in recipients],
            'content': message
        })
        
        return len(recipients)
    
    def step(self) -> Dict[str, Any]:
        """Execute one simulation step."""
        self._run_hooks('pre_step', self.step_count)
        
        for raven in list(self.ravens.values()):
            if not raven.alive:
                self.remove_raven(raven.id)
                continue
            
            if self.environment:
                observation = raven.sense(self.environment)
                raven.think(observation)
            
            action = raven.act()
            
            if 'acceleration' in action:
                raven.acceleration = action['acceleration']
            
            if 'message' in action:
                self.broadcast(raven, action['message'])
            
            raven.update_physics()
            
            if self.environment:
                self.environment.enforce_boundaries(raven)
        
        self.step_count += 1
        self._run_hooks('post_step', self.step_count)
        
        return self.get_metrics()
    
    def run(self, steps: int) -> List[Dict[str, Any]]:
        """Run simulation for N steps."""
        metrics = []
        for _ in range(steps):
            metrics.append(self.step())
        return metrics
    
    def get_metrics(self) -> Dict[str, Any]:
        """Get current swarm metrics."""
        alive_ravens = [r for r in self.ravens.values() if r.alive]
        return {
            'step': self.step_count,
            'population': len(alive_ravens),
            'avg_energy': sum(r.energy for r in alive_ravens) / len(alive_ravens) if alive_ravens else 0,
            'total_messages': len(self.message_log),
            'states': {state.name: sum(1 for r in alive_ravens if r.state.name == state.name) 
                      for state in set(r.state for r in alive_ravens)}
        }
    
    def add_hook(self, event: str, callback: Callable) -> None:
        """Add a hook for simulation events."""
        if event in self.hooks:
            self.hooks[event].append(callback)
    
    def _run_hooks(self, event: str, *args) -> None:
        """Run all hooks for an event."""
        for hook in self.hooks.get(event, []):
            try:
                hook(*args)
            except Exception as e:
                print(f"Hook error ({event}): {e}")
    
    def __len__(self) -> int:
        return len(self.ravens)
    
    def __repr__(self) -> str:
        return f"<Swarm population={len(self.ravens)} steps={self.step_count}>"