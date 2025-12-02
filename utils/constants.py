from enum import Enum

class SolutionStatus(Enum):
    OPTIMAL = 'optimal'
    ERROR = 'error'
    UNKNOWN = 'unknown'

class StatusColor(Enum):
    OPTIMAL = '#4CAF50'
    INFEASIBLE = '#f44336'
    UNBOUNDED = '#FF9800'
    ERROR = '#f44336'
    UNKNOWN = '#aaaaaa'
    PENDING = '#aaaaaa'
    
    @staticmethod
    def get_color(status: SolutionStatus) -> str:
        """Get color for given status"""
        return StatusColor[status.name].value

class StatusFormatter:
    """Status formatting utilities"""
    STATUS_LABELS = {
        SolutionStatus.OPTIMAL: "Optimal Solution Found",
        SolutionStatus.ERROR: "Error",
        SolutionStatus.UNKNOWN: "Unknown Status",
    }

# app
class AppConstants:
    WINDOW_TITLE = "One dimensional optimization"
    WINDOW_SIZE = (900, 700)
    TITLE_FONT_SIZE = 16
    BUTTON_HEIGHT = 40
    BUTTON_FONT_SIZE = 12
    LAYOUT_SPACING = 15
    LAYOUT_MARGINS = 15

# input widget
class InputWidgetConstants:
    DEFAULT_FUNC = "(x + 1.4)**1.51 + 3*sin(1.06*x)"
    DEFAULT_X0 = -1.0
    DEFAULT_H = 0.1
    DEFAULT_EPS = 0.001

# result widget
class ResultWidgetConstants:
    FONT_FAMILY = "Segoe UI"
    HEADER_SIZE = 12
    VALUE_SIZE = 24

# plot
class PlotColors:
    FUNCTION_LINE = '#0078D7'
    INTERVAL_LINE = '#FF9800'
    MINIMUM_POINT = '#4CAF50'
    BACKGROUND = '#f0f0f0'