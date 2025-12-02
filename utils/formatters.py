from typing import Tuple
from utils.constants import SolutionStatus, StatusColor, StatusFormatter


class ResultFormatter:
    """Formats optimization results for display"""
    
    @staticmethod
    def format_status(status: str) -> Tuple[str, str]:
        """
        Format status text and return corresponding color.
        Args:
            status: Status string (will be converted to SolutionStatus)
        Returns:
            Tuple of (formatted_status, color_hex)
        """
        try:
            status_enum = SolutionStatus(status.lower())
            status_str = StatusFormatter.STATUS_LABELS.get(status_enum, status.capitalize())
            status_color = StatusColor.get_color(status_enum)
            return status_str, status_color
        except (ValueError, AttributeError):
            return status.capitalize(), StatusColor.UNKNOWN.value
    
    @staticmethod
    def format_optimal_value(value: float) -> str:
        """
        Format optimal value for display.
        Args:
            value: Optimal objective value
        Returns:
            Formatted string
        """
        return f"Total Transportation Cost: {value:.2f}"