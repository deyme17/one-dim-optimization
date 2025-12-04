import numpy as np
from typing import Callable
from PyQt6.QtWidgets import (
    QGroupBox, QVBoxLayout, QFrame, QGridLayout, QSizePolicy
)
from PyQt6.QtCore import Qt

from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg
from matplotlib.figure import Figure
from utils import (OptimizationResult, IntervalResult, ResultWidgetConstants, 
                   UIHelper, PlotColors, StatusMessages, StatusColor, SolutionStatus)


class ResultSection(QGroupBox):
    """Widget for displaying function optimization results and plot"""
    def __init__(self) -> None:
        super().__init__("Optimization Results")
        self._init_ui()
    
    def _init_ui(self) -> None:
        layout = QVBoxLayout(self)
        layout.setSpacing(10)

        self.status_label = UIHelper.create_label("Ready",
            style="font-weight: bold; font-size: 14px; padding: 5px;")
        self.status_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.status_label)

        self.result_card = QFrame()
        self.result_card.setStyleSheet("background-color: #2b2b2b; border-radius: 8px; border: 1px solid #3d3d3d;")
        card_layout = QVBoxLayout(self.result_card)
        
        value_style = f"color: #4CAF50; font-size: {ResultWidgetConstants.VALUE_SIZE}px; font-weight: bold; font-family: {ResultWidgetConstants.FONT_FAMILY};"
        header_style = f"font-size: {ResultWidgetConstants.HEADER_SIZE}px; font-family: {ResultWidgetConstants.FONT_FAMILY};"
        
        # min
        card_layout.addWidget(UIHelper.create_label("Minimum Point (x*):", style=header_style))
        self.lbl_xmin_val = UIHelper.create_label("-", style=value_style)
        self.lbl_xmin_val.setAlignment(Qt.AlignmentFlag.AlignCenter)
        card_layout.addWidget(self.lbl_xmin_val)
        # min value
        card_layout.addWidget(UIHelper.create_label("Function Value f(x*):", style=header_style))
        self.lbl_fmin_val = UIHelper.create_label("-", style=value_style.replace("bold", "normal"))
        self.lbl_fmin_val.setAlignment(Qt.AlignmentFlag.AlignCenter)
        card_layout.addWidget(self.lbl_fmin_val)
        
        layout.addWidget(self.result_card)

        # Details
        details_layout = QGridLayout()
        self.lbl_iters = UIHelper.create_label("Iterations: -")
        self.lbl_final_eps = UIHelper.create_label("Precision: -")
        details_layout.addWidget(self.lbl_iters, 0, 0)
        details_layout.addWidget(self.lbl_final_eps, 0, 1)
        layout.addLayout(details_layout)

        # graph
        self.figure = Figure(figsize=(5, 4), dpi=100)
        self.figure.patch.set_facecolor(PlotColors.BACKGROUND) 
        self.canvas = FigureCanvasQTAgg(self.figure)
        self.canvas.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        layout.addWidget(self.canvas)

    def display_results(self, opt_result: OptimizationResult, interval_result: IntervalResult, func: Callable[[float], float]) -> None:
        """Display text results and plot the graph"""
        status = opt_result.status or SolutionStatus.UNKNOWN.value
        status_text = StatusMessages.get_message(status)
        status_color = StatusColor.get_color(status)
        self.status_label.setText(status_text)
        self.status_label.setStyleSheet(
            f"font-weight: bold; font-size: 14px; padding: 5px; "
            f"background-color: {status_color}; border-radius: 4px; color: white;"
        )
        # update values
        if status == SolutionStatus.OPTIMAL.value:
            self.lbl_xmin_val.setText(f"{opt_result.x_min:.5f}")
            self.lbl_fmin_val.setText(f"{opt_result.value:.5f}")
        else:
            self.lbl_xmin_val.setText("N/A")
            self.lbl_fmin_val.setText("N/A")
            
        self.lbl_iters.setText(f"Iterations: {opt_result.iterations}")
        self.lbl_final_eps.setText(f"Precision: {opt_result.final_epsilon:.5f}")
        self.result_card.show()

        if status == SolutionStatus.OPTIMAL.value:
            self.plot_graph(func, interval_result, opt_result)

    def plot_graph(self, func: Callable[[float], float], interval_res: IntervalResult, opt_res: OptimizationResult) -> None:
        """Draws function, uncertainty interval, and minimum point"""
        try:
            self.figure.clear()
            ax = self.figure.add_subplot(111)

            a, b = interval_res.interval
            margin = max((b - a) * 0.5, 1.0)
            x_start = a - margin
            x_end = b + margin
            
            # generate points
            x = np.linspace(x_start, x_end, 200)
            y = np.array([func(xi) for xi in x])

            # plot
            ax.plot(x, y, label='f(x)', color=PlotColors.FUNCTION_LINE, linewidth=2)
            # interval
            ax.axvline(a, color=PlotColors.INTERVAL_LINE, linestyle='--', alpha=0.7, label='Interval')
            ax.axvline(b, color=PlotColors.INTERVAL_LINE, linestyle='--', alpha=0.7)
            # min point
            ax.plot(opt_res.x_min, opt_res.value, 'o', color=PlotColors.MINIMUM_POINT, markersize=8, zorder=5, label='Minimum')

            ax.grid(True, linestyle=':', alpha=0.6)
            ax.legend(fontsize='small')
            ax.set_title("Optimization Visualization")
            
            self.figure.patch.set_facecolor("#FFFFFF")
            self.canvas.draw()
        except Exception as e:
            self.figure.patch.set_facecolor(PlotColors.BACKGROUND)
            raise Exception(str(e))

    def clear(self) -> None:
        self.status_label.setText("Ready")
        self.status_label.setStyleSheet("font-weight: bold; font-size: 14px; padding: 5px;")
        self.figure.patch.set_facecolor(PlotColors.BACKGROUND)
        self.lbl_xmin_val.setText("-")
        self.lbl_fmin_val.setText("-")
        self.figure.clear()
        self.canvas.draw()