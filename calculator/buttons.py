from PySide6.QtWidgets import QPushButton, QGridLayout
from PySide6.QtCore import Slot
from variables import MEDIUM_FONT_SIZE
from utils import isNumOrDot, isEmpty, isValidNumber
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from display import Display
    from informations import Info


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
    def __init__(self, display: 'Display', info: 'Info', *args, **kwargs):
        super().__init__(*args, **kwargs)

        self._grid_mask = [
            ['C', '◀', '^', '/'],
            ['7', '8', '9', '*'],
            ['4', '5', '6', '-'],
            ['1', '2', '3', '+'],
            ['',  '0', '.', '='],
        ]
        self.display = display
        self.info = info
        self._equation = ''
        self._leftnum = None
        self._rightnum = None
        self._mathop = None
        self._makeGrid()

    @property
    def equation(self):
        return self._equation

    @equation.setter
    def equation(self, value):
        self._equation = value
        self.info.setText(value)

    def _makeGrid(self):
        for index, row in enumerate(self._grid_mask):
            for index2, item in enumerate(row):
                button = Button(item)
                if not isNumOrDot(item) and not isEmpty(item):
                    button.setProperty('cssClass', 'specialButton')
                    button.font().setBold(True)
                    self._configSpecialButton(button)

                self.addWidget(button, index, index2)
                slot = self._makeSlot(self._insertButtonTextOnDisplay, button)
                self._connectButtonClicked(button, slot)

    def _connectButtonClicked(self, button: QPushButton, slot):
        button.clicked.connect(slot)

    def _configSpecialButton(self, button: QPushButton):
        text = button.text()

        if text == 'C':
            self._connectButtonClicked(button, self._clear)

        if text in '+-/*^':
            self._connectButtonClicked(
                button,
                self._makeSlot(self._operatorClicked, button)
            )

        if text == '=':
            self._connectButtonClicked(button, self._equal)

        if text == '◀':
            self._connectButtonClicked(button, self.display.backspace)

    def _makeSlot(self, func, *args, **kwargs):
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

    def _clear(self):
        self._leftnum = None
        self._rightnum = None
        self._mathop = None
        self.equation = ''
        self.display.clear()
        self.info.clear()

    def _operatorClicked(self, button: QPushButton):
        button_text = button.text()
        display_text = self.display.text()
        self.display.clear()

        if not isValidNumber(display_text) and self._leftnum is None:
            print('Left number is None')
            return

        if self._leftnum is None:
            self._leftnum = float(display_text)

        self._mathop = button_text
        self.equation = f'{self._leftnum} {self._mathop} ?'

    def _equal(self):
        display_text = self.display.text()

        if not isValidNumber(display_text) or (
            self._leftnum or self._mathop
        ) is None:
            print('Right number is None')
            return

        self._rightnum = float(display_text)
        self.equation = f'{self._leftnum} {self._mathop} {self._rightnum}'
        result = 'error'

        try:
            if '^' in self.equation:
                result = eval(self.equation.replace('^', '**'))
            else:
                result = eval(self.equation)
            self.display.setText(str(result))
        except ZeroDivisionError:
            print('Zero Division Error')
        except OverflowError:
            print('Result too large')

        self.display.clear()
        self.info.setText(f'{self.equation} = {result}')
        self._leftnum = result
        self._rightnum = None

        if result == 'error':
            self._leftnum = None
