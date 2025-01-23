from PySide6.QtWidgets import QPushButton, QGridLayout
from variables import MEDIUM_FONT_SIZE
from utils import isNumOrDot, isEmpty
from display import Display
from typing import cast


class Button(QPushButton):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.cfg_style()

    def cfg_style(self):
        font = self.font()
        font.setPixelSize(MEDIUM_FONT_SIZE)
        font.setBold(False)
        self.setFont(font)
        self.setMinimumSize(75, 75)


class ButtonsGrid(QGridLayout):
    def __init__(self, display: Display, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self._grid_mask = [
            ['C', '◀', '^', '/'],
            ['7', '8', '9', '*'],
            ['4', '5', '6', '-'],
            ['1', '2', '3', '+'],
            ['',  '0', '.', '='],
        ]
        self.display = display
        self._makeGrid()

    def _makeGrid(self):
        for index, row in enumerate(self._grid_mask):
            for index2, item in enumerate(row):
                button = Button(item)
                if not isNumOrDot(item) and not isEmpty(item):
                    button.setProperty('cssClass', 'specialButton')
                    button.font().setBold(True)

                self.addWidget(button, index, index2)
                button.clicked.connect(self._insertButtonTextOnDisplay)

    def _insertButtonTextOnDisplay(self):
        Button = cast(QPushButton, self.sender())
        self.display.setText(Button.text())
