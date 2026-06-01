"""Metrics collection and analysis for swarm simulations."""

from typing import Dict, List, Any
from collections import defaultdict
import time


class SwarmMetrics:
    """
    Collects and analyzes metrics from swarm simulations.
    
    Tracks:
    - Population over time
    - Energy distribution
    - Communication patterns
    - State transitions
    """
    
    def __init__(self):
        self.history: List[Dict[str, Any]] = []
        self.state_transitions: Dict[str, int] = defaultdict(int)
        self.birth_events: List[Dict] = []
        self.death_events: List[Dict] = []
        self.start_time = time.time()
    
    def record_step(self, metrics: Dict[str, Any]) -> None:
        """Record metrics from a simulation step."""
        record = {
            'step': metrics.get('step', len(self.history)),
            'timestamp': time.time() - self.start_time,
            'population': metrics.get('population', 0),
            'avg_energy': metrics.get('avg_energy', 0),
            'total_messages': metrics.get('total_messages', 0),
            'states': dict(metrics.get('states', {}))
        }
        self.history.append(record)
    
    def record_birth(self, raven_id: str, step: int) -> None:
        """Record a raven birth."""
        self.birth_events.append({'raven_id': raven_id, 'step': step})
    
    def record_death(self, raven_id: str, step: int, reason: str = 'energy') -> None:
        """Record a raven death."""
        self.death_events.append({
            'raven_id': raven_id,
            'step': step,
            'reason': reason
        })
    
    def get_population_history(self) -> List[int]:
        """Get population over time."""
        return [h['population'] for h in self.history]
    
    def get_energy_history(self) -> List[float]:
        """Get average energy over time."""
        return [h['avg_energy'] for h in self.history]
    
    def get_state_distribution(self) -> Dict[str, int]:
        """Get current state distribution."""
        if not self.history:
            return {}
        return self.history[-1].get('states', {})
    
    def get_summary(self) -> Dict[str, Any]:
        """Get a summary of all metrics."""
        if not self.history:
            return {}
        
        pop_history = self.get_population_history()
        return {
            'total_steps': len(self.history),
            'initial_population': pop_history[0] if pop_history else 0,
            'final_population': pop_history[-1] if pop_history else 0,
            'peak_population': max(pop_history) if pop_history else 0,
            'avg_energy_final': self.history[-1].get('avg_energy', 0),
            'total_births': len(self.birth_events),
            'total_deaths': len(self.death_events),
            'total_messages': self.history[-1].get('total_messages', 0) if self.history else 0
        }
    
    def __repr__(self) -> str:
        summary = self.get_summary()
        return f"<SwarmMetrics steps={summary.get('total_steps', 0)} pop={summary.get('final_population', 0)}>"