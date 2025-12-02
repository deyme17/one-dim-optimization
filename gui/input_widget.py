import math
from typing import Tuple, List
from PyQt6.QtWidgets import QGroupBox, QVBoxLayout, QLineEdit, QComboBox, QFormLayout
from utils import InputWidgetConstants, OptimizationProblem, UIHelper


class InputSection(QGroupBox):
    """Widget for function optimization input and configuration"""
    def __init__(self, opt_methods_names: List[str], bracketer_names: List[str]) -> None:
        super().__init__("Optimization Configuration")
        self.opt_methods_names = opt_methods_names
        self.bracketer_names = bracketer_names
        self._init_ui()
    
    def _init_ui(self) -> None:
        """Initialize the input section UI using Form Layout"""
        main_layout = QVBoxLayout(self)
        main_layout.setSpacing(15)

        form_layout = QFormLayout()
        form_layout.setLabelAlignment(float(0))
        form_layout.setSpacing(10)

        # func
        self.func_input = QLineEdit()
        self.func_input.setPlaceholderText("e.g. x**2 + 2*x + 1")
        self.func_input.setText(InputWidgetConstants.DEFAULT_FUNC)
        form_layout.addRow(UIHelper.create_label("Objective Function f(x):"), self.func_input)
        # bracketer algorithm selection
        self.bracketer_combo = QComboBox()
        self.bracketer_combo.addItems(self.bracketer_names)
        form_layout.addRow(UIHelper.create_label("'Bracketing' algorithm:"), self.bracketer_combo)
        # optimization method selection
        self.opt_method_combo = QComboBox()
        self.opt_method_combo.addItems(self.opt_methods_names)
        form_layout.addRow(UIHelper.create_label("Optimization Method:"), self.opt_method_combo)
        main_layout.addLayout(form_layout)

        # params
        params_group = QGroupBox("Parameters")
        params_layout = QFormLayout(params_group)
        
        # x0
        self.x0_input = UIHelper.create_double_spinbox(
            -10000.0, 10000.0, 
            InputWidgetConstants.DEFAULT_X0, 
            0.5)
        params_layout.addRow(UIHelper.create_label("Start Point (x₀):"),
                             self.x0_input)
        # h
        self.h_input = UIHelper.create_double_spinbox(
            0.0001, 100.0,
            InputWidgetConstants.DEFAULT_H,
            0.1)
        params_layout.addRow(UIHelper.create_label("Initial Step (h):"), self.h_input)
        # eps
        self.eps_input = UIHelper.create_double_spinbox(
            0.000001, 1.0,
            InputWidgetConstants.DEFAULT_EPS,
            0.001, decimals=6)
        params_layout.addRow(UIHelper.create_label("Precision (ε):"), self.eps_input)
        main_layout.addWidget(params_group)
        main_layout.addStretch()

    def get_data(self) -> Tuple[OptimizationProblem, bool, str]:
        """Extract and validate input data."""
        try:
            # validation
            func_str = self.func_input.text().strip()
            if not func_str:
                return None, False, "Function cannot be empty."
            
            # allow math funcs
            safe_dict = {k: v for k, v in math.__dict__.items() if not k.startswith("__")}
            def objective_function(x: float) -> float:
                safe_dict['x'] = x
                return eval(func_str, {"__builtins__": {}}, safe_dict)

            problem = OptimizationProblem(
                obj_func=objective_function,
                epsilon=self.eps_input.value(),
                method_name=self.opt_method_combo.currentText(),
                bracketer_name=self.bracketer_combo.currentText(),
                x_0=self.x0_input.value(),
                h=self.h_input.value()
            )
            return problem, True, ""
        except Exception as e:
            return None, False, f"Unexpected error: {str(e)}"