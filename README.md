# Unkindness.ai

**A parliament of opinions.**

A swarm intelligence simulation framework named for the collective noun of ravens.

## Overview

Unkindness.ai provides tools for modeling emergent behaviors in distributed agent systems. Each "raven" is an autonomous agent that can sense, communicate, and act within a shared environment.

## Installation

```bash
pip install -e .
```

## Quick Start

```python
from unkindness.core import BaseRaven, Swarm, Environment

# Create environment
env = Environment(dimensions=2)

# Create swarm
swarm = Swarm(environment=env)

# Add ravens
for i in range(10):
    raven = BaseRaven(name=f"Raven-{i}")
    swarm.add_raven(raven)

# Run simulation
for step in range(100):
    metrics = swarm.step()
    print(f"Step {step}: {metrics['population']} ravens")
```

## Core Concepts

### Raven
The base agent class. Each raven has:
- Position and velocity in n-dimensional space
- Perception and communication radii
- Memory of observations
- Belief system for state tracking
- Behavior stack for action selection

### Swarm
Manages a collection of ravens:
- Lifecycle management (birth, death)
- Message routing between ravens
- Simulation stepping
- Metrics collection

### Environment
The world ravens inhabit:
- Spatial boundaries
- Resource distribution
- Obstacles and terrain
- Global data sharing

## Behaviors

Built-in behaviors:
- `ForagingBehavior` - Seek and collect resources
- `FlockingBehavior` - Reynolds-style coordinated movement
- `ConsensusBehavior` - Distributed decision making

## Visualization

```python
from unkindness.visualization import SwarmRenderer

renderer = SwarmRenderer()
print(renderer.render_ascii(swarm, step))
```

## License

MIT