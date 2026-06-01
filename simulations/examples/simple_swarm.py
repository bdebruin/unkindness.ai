"""Simple example: Basic swarm simulation."""

from unkindness.core import BaseRaven, Swarm, Environment
from unkindness.core.raven import RavenConfig
from unkindness.behaviors import FlockingBehavior
from unkindness.visualization import SwarmRenderer


def main():
    # Create environment
    env = Environment(dimensions=2, bounds=((0, 500), (0, 500)))
    
    # Add some resources
    for i in range(5):
        import random
        x, y = random.randint(50, 450), random.randint(50, 450)
        env.add_resource((x // 10 * 10, y // 10 * 10), 50.0)
    
    # Create swarm
    swarm = Swarm(environment=env)
    
    # Add ravens
    for i in range(10):
        config = RavenConfig(
            perception_radius=80,
            communication_radius=120,
            max_speed=4.0
        )
        raven = BaseRaven(config=config, name=f"Raven-{i+1}")
        # Random starting position
        import random
        raven.position = [random.uniform(50, 450), random.uniform(50, 450)]
        # Set flocking behavior
        raven.current_behavior = FlockingBehavior()
        swarm.add_raven(raven)
    
    # Create renderer
    renderer = SwarmRenderer(width=60, height=20)
    
    # Run simulation
    print("Starting swarm simulation...")
    print("=" * 60)
    
    for step in range(20):
        metrics = swarm.step()
        
        if step % 5 == 0:
            print(renderer.render_ascii(swarm, step))
            print(f"Step {step}: Pop={metrics['population']}, Avg Energy={metrics['avg_energy']:.1f}")
            print("-" * 60)
    
    print("\nSimulation complete!")
    print(f"Final metrics: {swarm.get_metrics()}")


if __name__ == "__main__":
    main()