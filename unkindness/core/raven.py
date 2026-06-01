"""
BaseRaven - The foundational agent class for unkindness simulations.

A Raven is an autonomous agent with:
- Position and velocity in n-dimensional space
- Perception radius for local sensing
- Communication capabilities with nearby ravens
- Behavior stack for action selection
- Memory of observations and interactions
"""

from __future__ import annotations
import uuid
import time
from typing import Dict, List, Optional, Callable, Any
from dataclasses import dataclass, field
from enum import Enum, auto


class RavenState(Enum):
    """Possible states a raven can be in."""
    IDLE = auto()
    FORAGING = auto()
    FLOCKING = auto()
    COMMUNICATING = auto()
    ALERT = auto()
    RESTING = auto()


@dataclass
class Observation:
    """A single observation made by a raven."""
    timestamp: float
    position: tuple
    nearby_ravens: List[str]  # IDs of nearby ravens
    environmental_data: Dict[str, Any]
    message_received: Optional[str] = None


@dataclass  
class RavenConfig:
    """Configuration for a raven's capabilities."""
    perception_radius: float = 50.0
    communication_radius: float = 100.0
    max_speed: float = 5.0
    max_acceleration: float = 2.0
    memory_size: int = 100
    energy_decay: float = 0.01
    dimensions: int = 2


class BaseRaven:
    """
    The foundational raven agent.
    
    All specialized ravens inherit from this base class.
    Implements core mechanics: movement, sensing, communication, memory.
    """
    
    def __init__(self, config: Optional[RavenConfig] = None, name: Optional[str] = None):
        self.id = str(uuid.uuid4())[:8]
        self.name = name or f"Raven-{self.id}"
        self.config = config or RavenConfig()
        
        # Physical state
        self.position = [0.0] * self.config.dimensions
        self.velocity = [0.0] * self.config.dimensions
        self.acceleration = [0.0] * self.config.dimensions
        
        # Agent state
        self.state = RavenState.IDLE
        self.energy = 100.0
        self.alive = True
        
        # Memory and cognition
        self.memory: List[Observation] = []
        self.beliefs: Dict[str, Any] = {}
        self.message_queue: List[str] = []
        
        # Behavior stack
        self.behaviors: List[Callable] = []
        self.current_behavior: Optional[Callable] = None
        
        # Statistics
        self.birth_time = time.time()
        self.messages_sent = 0
        self.messages_received = 0
        self.distance_traveled = 0.0
    
    def sense(self, environment: Any) -> Observation:
        """Sense the local environment."""
        nearby = environment.get_nearby_ravens(self, self.config.perception_radius)
        env_data = environment.get_local_data(self.position)
        
        observation = Observation(
            timestamp=time.time(),
            position=tuple(self.position),
            nearby_ravens=[r.id for r in nearby],
            environmental_data=env_data,
            message_received=self.message_queue.pop(0) if self.message_queue else None
        )
        
        self.memory.append(observation)
        if len(self.memory) > self.config.memory_size:
            self.memory.pop(0)
        
        return observation
    
    def think(self, observation: Observation) -> None:
        """Process observations and update beliefs."""
        if observation.nearby_ravens:
            self.beliefs['last_seen_ravens'] = observation.nearby_ravens
            self.beliefs['last_social_contact'] = observation.timestamp
        
        if observation.message_received:
            self.process_message(observation.message_received)
    
    def process_message(self, message: str) -> None:
        """Process a received message. Override for custom protocols."""
        self.messages_received += 1
        if 'messages' not in self.beliefs:
            self.beliefs['messages'] = []
        self.beliefs['messages'].append({
            'content': message,
            'timestamp': time.time()
        })
    
    def act(self) -> Dict[str, Any]:
        """Execute actions based on current state and behavior."""
        action = {'acceleration': [0.0] * self.config.dimensions}
        
        if self.current_behavior:
            behavior_action = self.current_behavior(self)
            if behavior_action:
                action.update(behavior_action)
        
        self.energy -= self.config.energy_decay
        if self.energy <= 0:
            self.alive = False
        
        return action
    
    def send_message(self, content: str) -> None:
        """Queue a message to be sent."""
        self.messages_sent += 1
    
    def receive_message(self, content: str, sender: BaseRaven) -> None:
        """Receive a message from another raven."""
        self.message_queue.append(f"{sender.name}: {content}")
    
    def update_physics(self, dt: float = 1.0) -> None:
        """Update physical state based on current acceleration."""
        for i in range(self.config.dimensions):
            self.velocity[i] += self.acceleration[i] * dt
            speed = sum(v**2 for v in self.velocity) ** 0.5
            if speed > self.config.max_speed:
                scale = self.config.max_speed / speed
                self.velocity[i] *= scale
            
            old_pos = self.position[i]
            self.position[i] += self.velocity[i] * dt
            self.distance_traveled += abs(self.position[i] - old_pos)
    
    def distance_to(self, other: BaseRaven) -> float:
        """Calculate distance to another raven."""
        return sum((a - b) ** 2 for a, b in zip(self.position, other.position)) ** 0.5
    
    def get_stats(self) -> Dict[str, Any]:
        """Get raven statistics."""
        return {
            'id': self.id,
            'name': self.name,
            'state': self.state.name,
            'energy': self.energy,
            'alive': self.alive,
            'age': time.time() - self.birth_time,
            'messages_sent': self.messages_sent,
            'messages_received': self.messages_received,
            'distance_traveled': self.distance_traveled,
            'memory_size': len(self.memory),
            'position': tuple(self.position),
            'velocity': tuple(self.velocity)
        }
    
    def __repr__(self) -> str:
        return f"<Raven {self.name} ({self.state.name})>"