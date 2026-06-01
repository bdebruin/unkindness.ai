"""Metrics plotting utilities."""

from typing import List, Dict, Any
import json


class MetricsPlotter:
    """
    Formats metrics data for plotting libraries.
    
    Supports:
    - JSON output for Chart.js, D3, etc.
    - CSV export for spreadsheet analysis
    - Terminal-friendly text charts
    """
    
    def to_chart_json(self, metrics_history: List[Dict[str, Any]]) -> str:
        """Format metrics for Chart.js or similar."""
        return json.dumps({
            'labels': [m['step'] for m in metrics_history],
            'datasets': [
                {
                    'label': 'Population',
                    'data': [m['population'] for m in metrics_history]
                },
                {
                    'label': 'Average Energy',
                    'data': [m.get('avg_energy', 0) for m in metrics_history]
                }
            ]
        })
    
    def to_csv(self, metrics_history: List[Dict[str, Any]]) -> str:
        """Export metrics as CSV."""
        if not metrics_history:
            return ""
        
        headers = ['step', 'population', 'avg_energy', 'total_messages']
        lines = [','.join(headers)]
        
        for m in metrics_history:
            row = [
                str(m.get('step', '')),
                str(m.get('population', '')),
                str(m.get('avg_energy', '')),
                str(m.get('total_messages', ''))
            ]
            lines.append(','.join(row))
        
        return '\n'.join(lines)
    
    def to_text_chart(self, values: List[float], width: int = 50, height: int = 10) -> str:
        """Create a simple text-based bar chart."""
        if not values:
            return ""
        
        max_val = max(values)
        min_val = min(values)
        range_val = max_val - min_val if max_val != min_val else 1
        
        lines = []
        for v in values:
            normalized = (v - min_val) / range_val
            bar_len = int(normalized * width)
            lines.append('█' * bar_len + f' {v:.2f}')
        
        return '\n'.join(reversed(lines))
    
    def __repr__(self) -> str:
        return "<MetricsPlotter>"