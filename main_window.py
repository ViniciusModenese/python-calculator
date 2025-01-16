from PySide6.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QLabel


class MainWindow(QMainWindow):
    def __init__(self, parent: QWidget | None = None, *args, **kwargs) -> None:
        super().__init__(parent, *args, **kwargs)

        # Setting the basic layout
        self.central_widget = QWidget()

        self.vertical_layout = QVBoxLayout()
        self.central_widget.setLayout(self.vertical_layout)

        self.test_text = QLabel('Test Text')
        self.vertical_layout.addWidget(self.test_text)

        self.setCentralWidget(self.central_widget)

        # Main window title
        self.setWindowTitle('Calculadora')

    # Setting the size
    def adjustFixedSize(self, width, height):
        self.adjustSize()
        self.setFixedSize(width, height)
