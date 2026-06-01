"""
Environment - The world in which ravens exist.
"""

from typing import Dict, List, Optional, Any, Tuple
from .raven import BaseRaven


class Environment:
    """
    Simulation environment.
    
    Manages:
    - Spatial boundaries
    - Resource distribution
    - Environmental data at positions
    - Raven boundary enforcement
    """
    
    def __init__(self, dimensions: int = 2, bounds: Optional[Tuple] = None):
        self.dimensions = dimensions
        self.bounds = bounds or ((0, 1000),) * dimensions
        self.resources: Dict[Tuple, float] = {}
        self.obstacles: List[Dict] = []
        self.global_data: Dict[str, Any] = {}
    
    def get_local_data(self, position: List[float]) -> Dict[str, Any]:
        """Get environmental data at a position."""
        data = dict(self.global_data)
        
        pos_key = tuple(int(p / 10) * 10 for p in position)
        if pos_key in self.resources:
            data['resource'] = self.resources[pos_key]
        
        return data
    
    def add_resource(self, position: Tuple, amount: float) -> None:
        """Add a resource at a position."""
        self.resources[position] = amount
    
    def add_obstacle(self, position: Tuple, radius: float) -> None:
        """Add an obstacle at a position."""
        self.obstacles.append({'position': position, 'radius': radius})
    
    def enforce_boundaries(self, raven: BaseRaven) -> None:
        """Keep raven within bounds."""
        for i in range(self.dimensions):
            low, high = self.bounds[i]
            if raven.position[i] < low:
                raven.position[i] = low
                raven.velocity[i] *= -0.5
            elif raven.position[i] > high:
                raven.position[i] = high
                raven.velocity[i] *= -0.5
    
    def get_nearby_ravens(self, raven: BaseRaven, radius: float) -> List[BaseRaven]:
        """Get all ravens within radius of a given raven."""
        return []  # Handled by Swarm
    
    def __repr__(self) -> str:
        return f"<Environment dims={self.dimensions} resources={len(self.resources)}>"