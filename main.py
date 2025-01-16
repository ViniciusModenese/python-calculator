from PySide6.QtWidgets import QApplication
import sys
from main_window import MainWindow

if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = MainWindow()

    window.adjustFixedSize(302, 510)

    window.show()

    app.exec()
