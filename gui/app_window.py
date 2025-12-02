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
        """
        Initialize the main application window.
        Args:
            input_section: InputSection widget instance for problem setup
            results_section: ResultSection widget instance for displaying results
            ...
            ...
        """
        super().__init__()
        self.input_section = input_section
        self.results_section = results_section
        
        self._setup_window()
        self.init_ui()

    def _setup_window(self) -> None:
        """Set ups window settings"""
        self.setWindowTitle(AppConstants.WINDOW_TITLE)
        self.setMinimumSize(AppConstants.WINDOW_SIZE[0], AppConstants.WINDOW_SIZE[1])
        self.setStyleSheet(StyleSheet.DARK_STYLE)

    def init_ui(self) -> None:
        """Initialize the user interface layout and components"""
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        main_layout = QVBoxLayout(central_widget)
        main_layout.setSpacing(15)
        main_layout.setContentsMargins(15, 15, 15, 15)
        
        # title
        title = self._create_title()
        main_layout.addWidget(title)
        
        # tabs
        self.tabs = QTabWidget()
        
        # input tab
        input_tab = QWidget()
        input_layout = QVBoxLayout(input_tab)
        input_layout.addWidget(self.input_section)
        self.tabs.addTab(input_tab, "Input")
        
        # results tab
        results_tab = QWidget()
        results_layout = QVBoxLayout(results_tab)
        results_layout.addWidget(self.results_section)
        self.tabs.addTab(results_tab, "Results")
        
        main_layout.addWidget(self.tabs)
        
        # controls
        buttons_layout = self._create_buttons_layout()
        main_layout.addLayout(buttons_layout)
    
    def _create_title(self) -> QLabel:
        """Create and configure the title label"""
        title = QLabel("One-dimensional Optimization")
        title_font = QFont()
        title_font.setPointSize(16)
        title_font.setBold(True)
        title.setFont(title_font)
        return title
    
    def _create_buttons_layout(self) -> QHBoxLayout:
        """Create and configure the control buttons layout"""
        pass # TODO
    
    @staticmethod
    def _create_button(text: str, height: int, font_size: int) -> QPushButton:
        """Create a styled button"""
        button = QPushButton(text)
        button.setMinimumHeight(height)
        
        font = QFont()
        font.setPointSize(font_size)
        font.setBold(True)
        button.setFont(font)
        
        return button

    def on_solve(self) -> None:
        """Handle solve button click"""
        try:
            problem_data, success, error_msg = self.input_section.get_data()
            if success and problem_data:
                pass # TODO
            else:
                self._show_error(error_msg)
        except Exception as e:
            self._show_error(str(e))

    def _show_error(self, message: str) -> None:
        """Show error message to user"""
        QMessageBox.warning(self, "Error", message)