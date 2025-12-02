from typing import List
from PyQt6.QtWidgets import (
    QGroupBox, QVBoxLayout, QLabel,
    QScrollArea, QWidget, QGridLayout, QTextEdit
)
from PyQt6.QtCore import Qt
from utils import UIHelper, ResultWidgetConstants, ResultFormatter, OptimizationResult


class ResultSection(QGroupBox):
    """Widget for displaying function optimization results"""
    def __init__(self) -> None:
        super().__init__("Results")
        self._init_ui()
    
    def _init_ui(self) -> None:
        """Initialize the results section UI"""
        layout = QVBoxLayout(self)
        layout.setSpacing(15)
        
        # status section
        self.status_label = self._create_status_label()
        layout.addWidget(self.status_label)
        
        # optimal value section
        self.optimal_value_label = self._create_optimal_value_label()
        layout.addWidget(self.optimal_value_label)
        
        layout.addStretch()
    
    def _create_status_label(self) -> QLabel:
        """Create status label"""
        label = QLabel("No results yet")
        label.setStyleSheet(
            "font-size: 14pt; font-weight: bold; padding: 10px; "
            "background-color: #3a3a3a; border-radius: 5px;"
        )
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        return label
    
    def _create_optimal_value_label(self) -> QLabel:
        """Create optimal value label"""
        label = QLabel("")
        label.setStyleSheet(
            "font-size: 13pt; padding: 8px; "
            "background-color: #2d2d2d; border-radius: 5px;"
        )
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        return label
    
    def display_results(self, result: OptimizationResult) -> None:
        """
        Display optimization results.
        Args:
            result: OptimizationResult object containing solution data
        """
        self._update_status(result)
        self._update_optimum(result)
        
        pass # TODO
    
    def _update_status(self, result: OptimizationResult) -> None:
        """Update status label"""
        pass # TODO
    
    def _update_optimum(self, result: OptimizationResult) -> None:
        """Update optimal value label"""
        pass # TODO
    
    def clear(self) -> None:
        """Clear all results"""
        self.status_label.setText("No results yet")
        self.status_label.setStyleSheet(
            "font-size: 14pt; font-weight: bold; padding: 10px; "
            "background-color: #3a3a3a; border-radius: 5px;"
        )
        self.optimal_value_label.hide()