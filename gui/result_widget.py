import numpy as np
from typing import Callable
from PyQt6.QtWidgets import (
    QGroupBox, QVBoxLayout, QLabel, QFrame, QGridLayout, QSizePolicy
)
from PyQt6.QtCore import Qt

from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg
from matplotlib.figure import Figure
from utils import OptimizationResult, IntervalResult


class ResultSection(QGroupBox):
    """Widget for displaying function optimization results and plot"""
    def __init__(self) -> None:
        super().__init__("Optimization Results")
        self._init_ui()
    
    def _init_ui(self) -> None:
        layout = QVBoxLayout(self)
        layout.setSpacing(10)
        
        self.status_label = QLabel("Ready")
        self.status_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.status_label.setStyleSheet("font-weight: bold; font-size: 14px; padding: 5px; "
                                        "background-color: #e0e0e0; border-radius: 4px; color: #333;")
        layout.addWidget(self.status_label)

        self.result_card = QFrame()
        self.result_card.setStyleSheet("background-color: #2b2b2b; border-radius: 8px; border: 1px solid #3d3d3d;")
        card_layout = QVBoxLayout(self.result_card)
        
        # min
        self.lbl_xmin_val = QLabel("-")
        self.lbl_xmin_val.setStyleSheet("color: #4CAF50; font-size: 24px; font-weight: bold;")
        self.lbl_xmin_val.setAlignment(Qt.AlignmentFlag.AlignCenter)
        card_layout.addWidget(QLabel("Minimum Point (x*):", alignment=Qt.AlignmentFlag.AlignHCenter))
        card_layout.addWidget(self.lbl_xmin_val)
        # min value
        self.lbl_fmin_val = QLabel("-")
        self.lbl_fmin_val.setStyleSheet("color: #4CAF50; font-size: 18px;")
        self.lbl_fmin_val.setAlignment(Qt.AlignmentFlag.AlignCenter)
        card_layout.addWidget(QLabel("Function Value f(x*):", alignment=Qt.AlignmentFlag.AlignHCenter))
        card_layout.addWidget(self.lbl_fmin_val)
        
        layout.addWidget(self.result_card)

        # details
        details_layout = QGridLayout()
        self.lbl_iters = QLabel("Iterations: -")
        self.lbl_final_eps = QLabel("Precision: -")
        details_layout.addWidget(self.lbl_iters, 0, 0)
        details_layout.addWidget(self.lbl_final_eps, 0, 1)
        layout.addLayout(details_layout)

        # graph
        self.figure = Figure(figsize=(5, 4), dpi=100)
        self.figure.patch.set_facecolor('#f0f0f0') 
        self.canvas = FigureCanvasQTAgg(self.figure)
        self.canvas.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        layout.addWidget(self.canvas)

    def display_results(self, opt_result: OptimizationResult, interval_result: IntervalResult, func_callable: Callable[[float], float]) -> None:
        """Display text results and plot the graph"""
        self.status_label.setText("Solution Found")
        self.status_label.setStyleSheet("font-weight: bold; font-size: 14px; padding: 5px; "
                                        "background-color: #4CAF50; border-radius: 4px; color: white;")
        self.lbl_xmin_val.setText(f"{opt_result.x_min:.6f}")
        self.lbl_fmin_val.setText(f"{opt_result.value:.6f}")
        self.lbl_iters.setText(f"Iterations: {opt_result.iterations}")
        self.lbl_final_eps.setText(f"Precision: {opt_result.final_epsilon:.2e}")
        self.result_card.show()

        # update graph
        self.plot_graph(func_callable, interval_result, opt_result)

    def plot_graph(self, func, interval_res: IntervalResult, opt_res: OptimizationResult) -> None:
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
            ax.plot(x, y, label='f(x)', color='#0078D7', linewidth=2)
            # interval
            ax.axvline(a, color='#FF5722', linestyle='--', alpha=0.7, label='Interval')
            ax.axvline(b, color='#FF5722', linestyle='--', alpha=0.7)
            # min point
            ax.plot(opt_res.x_min, opt_res.value, 'o', color='#4CAF50', markersize=8, zorder=5, label='Minimum')

            ax.grid(True, linestyle=':', alpha=0.6)
            ax.legend(fontsize='small')
            ax.set_title("Optimization Visualization")
            
            self.canvas.draw()
        except Exception as e:
            raise Exception(str(e))

    def clear(self) -> None:
        self.status_label.setText("Ready")
        self.status_label.setStyleSheet("background-color: #e0e0e0; border-radius: 4px; color: #333;")
        self.lbl_xmin_val.setText("-")
        self.lbl_fmin_val.setText("-")
        self.figure.clear()
        self.canvas.draw()