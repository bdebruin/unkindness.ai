"""Flocking behavior for coordinated group movement."""

from typing import Dict, Any, List, TYPE_CHECKING
import math

if TYPE_CHECKING:
    from ..core.raven import BaseRaven


class FlockingBehavior:
    """
    Implements Reynolds' boids-style flocking.
    
    Three rules:
    1. Separation: Avoid crowding neighbors
    2. Alignment: Steer toward average heading
    3. Cohesion: Steer toward center of mass
    """
    
    def __init__(self, separation_weight: float = 1.5,
                 alignment_weight: float = 1.0,
                 cohesion_weight: float = 1.0,
                 neighbor_radius: float = 50.0):
        self.separation_weight = separation_weight
        self.alignment_weight = alignment_weight
        self.cohesion_weight = cohesion_weight
        self.neighbor_radius = neighbor_radius
    
    def __call__(self, raven: 'BaseRaven') -> Dict[str, Any]:
        """Execute flocking behavior."""
        nearby = [r for r in raven.memory[-1].nearby_ravens if hasattr(r, 'position')]
        
        if not nearby:
            return {'acceleration': [0.0] * raven.config.dimensions}
        
        # Separation: steer away from crowded areas
        separation = [0.0] * raven.config.dimensions
        for other in nearby:
            dist = raven.distance_to(other)
            if dist < self.neighbor_radius and dist > 0:
                diff = [a - b for a, b in zip(raven.position, other.position)]
                separation = [s + d / dist for s, d in zip(separation, diff)]
        
        # Alignment: match velocity of neighbors
        alignment = [0.0] * raven.config.dimensions
        if nearby:
            avg_vel = [sum(v[i] for v in [r.velocity for r in nearby]) / len(nearby) 
                      for i in range(raven.config.dimensions)]
            alignment = [a - v for a, v in zip(avg_vel, raven.velocity)]
        
        # Cohesion: steer toward center of mass
        cohesion = [0.0] * raven.config.dimensions
        if nearby:
            center = [sum(p[i] for p in [r.position for r in nearby]) / len(nearby)
                     for i in range(raven.config.dimensions)]
            cohesion = [c - p for c, p in zip(center, raven.position)]
        
        # Combine forces
        acceleration = [
            (separation[i] * self.separation_weight +
             alignment[i] * self.alignment_weight +
             cohesion[i] * self.cohesion_weight) * 0.1
            for i in range(raven.config.dimensions)
        ]
        
        return {'acceleration': acceleration}