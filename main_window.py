from PySide6.QtWidgets import QMainWindow, QWidget, QVBoxLayout
from PySide6.QtGui import QIcon
from variables import WINDOW_ICON_PATH
import sys


class MainWindow(QMainWindow):
    def __init__(self, parent: QWidget | None = None, *args, **kwargs) -> None:
        super().__init__(parent, *args, **kwargs)

        # Setting the basic layout
        self.central_widget = QWidget()

        WINDOW_ICON = QIcon(str(WINDOW_ICON_PATH))
        self.setWindowIcon(WINDOW_ICON)

        # Setting AUMID
        if sys.platform.startswith('win'):
            import ctypes
            ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(
                u'CompanyName.ProductName.SubProduct.VersionInformation')

        # Layout
        self.vertical_layout = QVBoxLayout()
        self.central_widget.setLayout(self.vertical_layout)

        self.setCentralWidget(self.central_widget)

        # Main window title
        self.setWindowTitle('Calculator')

    # Setting the size
    def adjustFixedSize(self, width, height):
        self.adjustSize()
        self.setFixedSize(width, height)

    def addWidgetToVLayout(self, widget: QWidget):
        self.vertical_layout.addWidget(widget)
