"""
Unkindness.ai - A swarm intelligence simulation framework.

Named for the collective noun of ravens, this framework models emergent
behaviors in distributed agent systems.
"""

__version__ = "0.1.0"
__author__ = "Unkindness.ai"

from .core.raven import BaseRaven
from .core.swarm import Swarm
from .core.environment import Environment

__all__ = ["BaseRaven", "Swarm", "Environment"]