import sys
from PyQt6.QtWidgets import QApplication

from core import optimizers, bracketers
from gui.app_window import OneDimOptApp
from gui import InputSection, ResultSection


def main():
    app = QApplication(sys.argv)
    window = OneDimOptApp(
        input_section=InputSection(
            optimizers.keys(), 
            bracketers.keys()
        ),
        results_section=ResultSection(),
        optimizers=optimizers,
        bracketers=bracketers
    )
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()