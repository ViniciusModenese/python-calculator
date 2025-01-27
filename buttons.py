from PySide6.QtWidgets import QPushButton, QGridLayout
from PySide6.QtCore import Slot
from variables import MEDIUM_FONT_SIZE
from utils import isNumOrDot, isEmpty, isValidNumber
from display import Display


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
                buttonSlot = self._makeButtonDisplaySlot(
                    self._insertButtonTextOnDisplay,
                    button
                    )
                button.clicked.connect(buttonSlot)

    def _makeButtonDisplaySlot(self, func, *args, **kwargs):
        @Slot(bool)
        def realSlot(checked):
            func(*args, **kwargs)
        return realSlot

    def _insertButtonTextOnDisplay(self, button: QPushButton):
        button_text = button.text()
        newDisplayValue = self.display.text() + button_text
        if not isValidNumber(newDisplayValue):
            return
        self.display.insert(button_text)
