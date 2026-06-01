"""Swarm visualization renderer."""

from typing import List, Dict, Any, Optional
import json


class SwarmRenderer:
    """
    Renders swarm state for visualization.
    
    Outputs formats:
    - JSON for web-based rendering
    - ASCII art for terminal
    - Coordinate lists for plotting
    """
    
    def __init__(self, width: int = 80, height: int = 24):
        self.width = width
        self.height = height
    
    def render_json(self, swarm, step: int) -> str:
        """Render swarm state as JSON."""
        data = {
            'step': step,
            'ravens': [
                {
                    'id': r.id,
                    'name': r.name,
                    'position': list(r.position),
                    'velocity': list(r.velocity),
                    'state': r.state.name,
                    'energy': r.energy
                }
                for r in swarm.ravens.values()
            ],
            'metrics': swarm.get_metrics()
        }
        return json.dumps(data)
    
    def render_ascii(self, swarm, step: int) -> str:
        """Render swarm state as ASCII art."""
        # Create grid
        grid = [[' ' for _ in range(self.width)] for _ in range(self.height)]
        
        # Scale factors
        max_coord = 1000
        scale_x = self.width / max_coord
        scale_y = self.height / max_coord
        
        # Place ravens
        for raven in swarm.ravens.values():
            x = int(raven.position[0] * scale_x) if raven.config.dimensions >= 1 else self.width // 2
            y = int(raven.position[1] * scale_y) if raven.config.dimensions >= 2 else self.height // 2
            
            x = max(0, min(self.width - 1, x))
            y = max(0, min(self.height - 1, y))
            
            # Different symbols for different states
            symbols = {
                'IDLE': '·',
                'FORAGING': '*',
                'FLOCKING': '+',
                'COMMUNICATING': '@',
                'ALERT': '!',
                'RESTING': '-'
            }
            grid[y][x] = symbols.get(raven.state.name, '?')
        
        # Build output
        lines = [f"=== Step {step} ==="]
        for row in grid:
            lines.append(''.join(row))
        
        metrics = swarm.get_metrics()
        lines.append(f"Pop: {metrics['population']} | Msgs: {metrics['total_messages']}")
        
        return '\n'.join(lines)
    
    def get_positions(self, swarm) -> Dict[str, List[List[float]]]:
        """Get all positions as lists for external plotting."""
        return {
            'positions': [list(r.position) for r in swarm.ravens.values()],
            'velocities': [list(r.velocity) for r in swarm.ravens.values()],
            'energies': [r.energy for r in swarm.ravens.values()]
        }
    
    def __repr__(self) -> str:
        return f"<SwarmRenderer {self.width}x{self.height}>"