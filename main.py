from PySide6.QtWidgets import QApplication
import sys
from main_window import MainWindow
from display import Display

if __name__ == '__main__':
    # Initialize app
    app = QApplication(sys.argv)
    window = MainWindow()

    # Display
    display = Display()
    display.setPlaceholderText('0')
    window.addWidgetToVLayout(display)

    # Run and adjust app
    window.adjustFixedSize(302, 510)
    window.show()
    app.exec()
