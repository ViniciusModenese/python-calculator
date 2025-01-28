from PySide6.QtWidgets import QLineEdit
from variables import MAX_FONT_SIZE, TEXT_MARGIN
from PySide6.QtCore import Qt


class Display(QLineEdit):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.cfgStyle()

    def cfgStyle(self):
        self.setStyleSheet(f'font-size: {MAX_FONT_SIZE}px')
        self.setMinimumHeight(MAX_FONT_SIZE * 2)
        self.setAlignment(Qt.AlignmentFlag.AlignRight)
        self.setTextMargins(TEXT_MARGIN,
                            TEXT_MARGIN,
                            TEXT_MARGIN,
                            TEXT_MARGIN)
