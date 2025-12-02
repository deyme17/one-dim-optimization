from PyQt6.QtWidgets import (
    QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton, QTabWidget, QMessageBox
)
from PyQt6.QtGui import QFont
from typing import Dict
from utils.interfaces import IIntervalBracketer, IOptimizer

from utils import AppConstants, StyleSheet
from . import InputSection, ResultSection


class OneDimOptApp(QMainWindow):
    """Main application window for one-dimensional optimization app"""
    def __init__(self, input_section: InputSection, results_section: ResultSection,
                 bracketers: Dict[str, IIntervalBracketer], optimizers: Dict[str, IOptimizer]) -> None:
        super().__init__()
        self.input_section = input_section
        self.results_section = results_section
        self.bracketers = bracketers
        self.optimizers = optimizers
        
        self._setup_window()
        self.init_ui()

    def _setup_window(self) -> None:
        self.setWindowTitle(AppConstants.WINDOW_TITLE)
        self.setMinimumSize(AppConstants.WINDOW_SIZE[0], AppConstants.WINDOW_SIZE[1])
        self.setStyleSheet(StyleSheet.DARK_STYLE)
        
    def init_ui(self) -> None:
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        main_layout = QVBoxLayout(central_widget)
        main_layout.setSpacing(15)
        main_layout.setContentsMargins(15, 15, 15, 15)
        title = self._create_title()
        main_layout.addWidget(title)
        
        self.tabs = QTabWidget()
        # input section
        input_tab = QWidget()
        input_layout = QVBoxLayout(input_tab)
        input_layout.addWidget(self.input_section)
        input_layout.addStretch()
        self.tabs.addTab(input_tab, "Configuration")
        # result section
        results_tab = QWidget()
        results_layout = QVBoxLayout(results_tab)
        results_layout.addWidget(self.results_section)
        self.tabs.addTab(results_tab, "Results & Graph")
        
        main_layout.addWidget(self.tabs)
        buttons_layout = self._create_buttons_layout()
        main_layout.addLayout(buttons_layout)
    
    def _create_title(self) -> QLabel:
        title = QLabel("One-dimensional Optimization")
        title_font = QFont()
        title_font.setPointSize(18)
        title_font.setBold(True)
        title.setFont(title_font)
        title.setStyleSheet("color: #333; margin-bottom: 5px;")
        return title
    
    def _create_buttons_layout(self) -> QHBoxLayout:
        layout = QHBoxLayout()
        layout.setSpacing(20)
        self.btn_clear = self._create_button("Clear", 45, 12)
        self.btn_clear.clicked.connect(self.on_clear)
        self.btn_optimize = self._create_button("Find optimum", 45, 12)
        self.btn_optimize.setStyleSheet("background-color: #0078D7; color: white; border-radius: 4px;")
        self.btn_optimize.clicked.connect(self.on_optimize)
        layout.addStretch()
        layout.addWidget(self.btn_clear)
        layout.addWidget(self.btn_optimize)
        return layout
    
    @staticmethod
    def _create_button(text: str, height: int, font_size: int) -> QPushButton:
        button = QPushButton(text)
        button.setMinimumHeight(height)
        button.setMinimumWidth(100)
        font = QFont()
        font.setPointSize(font_size)
        font.setBold(True)
        button.setFont(font)
        return button

    def on_optimize(self) -> None:
        """Handle solve button click: Execute Svenn -> Optimize -> Plot"""
        try:
            problem, success, error_msg = self.input_section.get_data()
            if not success:
                self._show_error(error_msg)
                return

            # interval
            bracketer = self.bracketers.get(problem.bracketer_name)
            if not bracketer:
                raise ValueError(f"Bracketer '{problem.bracketer_name}' not found")
            interval_result = bracketer.find_interval(problem.obj_func, problem.x_0, problem.h)
            
            # optimization
            optimizer = self.optimizers.get(problem.method_name)
            if not optimizer:
                raise ValueError(f"Optimizer '{problem.method_name}' not found")
            opt_result = optimizer.optimize(problem.obj_func, interval_result, problem.epsilon)

            # result
            self.results_section.display_results(opt_result, interval_result, problem.obj_func)
            self.tabs.setCurrentIndex(1)

        except Exception as e:
            self._show_error(str(e))

    def on_clear(self):
        self.results_section.clear()
        self.tabs.setCurrentIndex(0)

    def _show_error(self, message: str) -> None:
        QMessageBox.warning(self, "Calculation Error", message)