from enum import Enum

class SolutionStatus(Enum):
    OPTIMAL = 'optimal'
    NOT_CONVERGED = 'not_converged'
    MAX_ITERATIONS = 'max_iterations'
    ERROR = 'error'
    UNKNOWN = 'unknown'

class StatusColor(Enum):
    OPTIMAL = '#4CAF50'
    NOT_CONVERGED = '#FF9800'
    MAX_ITERATIONS = "#D34D00"
    ERROR = "#ff1100"
    UNKNOWN = '#aaaaaa'
    
    @staticmethod
    def get_color(status: SolutionStatus) -> str:
        """Get color for given status"""
        color_map = {
            SolutionStatus.OPTIMAL: StatusColor.OPTIMAL.value,
            SolutionStatus.NOT_CONVERGED: StatusColor.NOT_CONVERGED.value,
            SolutionStatus.MAX_ITERATIONS: StatusColor.NOT_CONVERGED.value,
            SolutionStatus.ERROR: StatusColor.ERROR.value,
            SolutionStatus.UNKNOWN: StatusColor.UNKNOWN.value,
        }
        return color_map.get(status, StatusColor.UNKNOWN.value)

class StatusMessages:
    LABELS = {
        SolutionStatus.OPTIMAL: "Optimal Solution Found",
        SolutionStatus.NOT_CONVERGED: "Not Converged",
        SolutionStatus.MAX_ITERATIONS: "Maximum Iterations Reached",
        SolutionStatus.ERROR: "Error Occurred",
        SolutionStatus.UNKNOWN: "Unknown Status",
    }
    
    @staticmethod
    def get_message(status: SolutionStatus) -> str:
        """Get message for given status"""
        return StatusMessages.LABELS.get(status, "Unknown Status")
    
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
    BACKGROUND = "#0A0A0A60"