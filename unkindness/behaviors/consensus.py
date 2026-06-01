"""Consensus behavior for distributed decision making."""

from typing import Dict, Any, List, TYPE_CHECKING
import math

if TYPE_CHECKING:
    from ..core.raven import BaseRaven


class ConsensusBehavior:
    """
    Implements distributed consensus among ravens.
    
    Ravens share opinions and gradually align through repeated
    communication, inspired by voter models and consensus algorithms.
    """
    
    def __init__(self, influence_radius: float = 100.0, opinion_stability: float = 0.95):
        self.influence_radius = influence_radius
        self.opinion_stability = opinion_stability
        self.opinions: Dict[str, str] = {}  # raven_id -> opinion
    
    def __call__(self, raven: 'BaseRaven') -> Dict[str, Any]:
        """Execute consensus behavior."""
        # Collect opinions from nearby ravens
        nearby = [r for r in raven.memory[-1].nearby_ravens if hasattr(r, 'beliefs')]
        
        if not nearby:
            return {}
        
        # Simple majority opinion update
        opinions = [r.beliefs.get('opinion', 'neutral') for r in nearby]
        if opinions:
            from collections import Counter
            most_common = Counter(opinions).most_common(1)[0][0]
            
            # Blend toward majority with stability factor
            current = raven.beliefs.get('opinion', 'neutral')
            raven.beliefs['opinion'] = (
                self.opinion_stability * current +
                (1 - self.opinion_stability) * most_common
            )
        
        return {'message': f"opinion:{raven.beliefs.get('opinion', 'neutral')}"}