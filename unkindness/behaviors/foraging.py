"""Foraging behavior for ravens seeking resources."""

from typing import Dict, Any, TYPE_CHECKING

if TYPE_CHECKING:
    from ..core.raven import BaseRaven


class ForagingBehavior:
    """
    Implements foraging behavior where ravens seek and collect resources.
    
    Resources are environmental markers that ravens can collect for energy.
    """
    
    def __init__(self, energy_gain: float = 10.0, detection_radius: float = 100.0):
        self.energy_gain = energy_gain
        self.detection_radius = detection_radius
    
    def __call__(self, raven: 'BaseRaven') -> Dict[str, Any]:
        """Execute foraging behavior."""
        # Check for nearby resources in environment data
        if 'resource' in raven.beliefs.get('current_env', {}):
            resource = raven.beliefs['current_env']['resource']
            raven.energy = min(100.0, raven.energy + self.energy_gain * resource * 0.1)
        
        # Default: move toward center if lost
        return {
            'acceleration': [0.1, 0.1] if raven.config.dimensions >= 2 else [0.1]
        }