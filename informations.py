from PySide6.QtWidgets import QLabel
from PySide6.QtCore import Qt
from variables import MIN_FONT_SIZE


class Info(QLabel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.cfgStyle()

    def cfgStyle(self):
        self.setAlignment(Qt.AlignmentFlag.AlignRight)
        self.setStyleSheet(f'font-size: {MIN_FONT_SIZE}px')
