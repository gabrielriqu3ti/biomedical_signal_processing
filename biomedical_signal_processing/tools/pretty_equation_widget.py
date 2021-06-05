# -*- coding: utf-8 -*-
##
# @file pretty_equation_app.py
# @brief Contain a GUI for displaying pretty equations
# @author Gabriel H Riqueti
# @email gabrielhriqueti@gmail.com
# @date 25/04/2021
#

from PySide2 import QtWidgets
from PySide2.QtWidgets import QApplication
import sys
import sympy


class PrettyEquationWidget(QtWidgets.QWidget):
    ##
    # @class PrettyEquationWidget
    # @brief provides GUI to all the functionalities of the library

    def __init__(self, title='Information', message='Equation:', var='', func='', *args, **kwrds):
        """
        Initialize instance
        """
        super().__init__(*args, **kwrds)

        self.var = var
        self.func = func

        self.label_details = QtWidgets.QLabel(message)
        self.label_var = QtWidgets.QLabel('')
        self.label_func = QtWidgets.QLabel('')

        self.button_okay = QtWidgets.QPushButton()

        self.grid = QtWidgets.QGridLayout()

        self.title = title

        self.UI()

    def UI(self):
        """
        Set the user interface
        """
        self.button_okay.setText('Okay')
        self.button_okay.clicked.connect(self.close)

        self.label_var.setText(sympy.pretty(self.var, use_unicode=True))
        self.label_func.setText(sympy.pretty(self.func, use_unicode=True))

        self.grid.addWidget(self.label_details, 0, 0)
        self.grid.addWidget(self.label_var, 1, 0)
        self.grid.addWidget(self.label_func, 1, 1, 1, 2)
        self.grid.addWidget(QtWidgets.QLabel(''), 2, 0)
        self.grid.addWidget(QtWidgets.QLabel(''), 3, 0, 1, 2)
        self.grid.addWidget(self.button_okay, 3, 2)

        self.setLayout(self.grid)
        self.setGeometry(400, 300, 400, 60)
        self.setWindowTitle(self.title)

        self.show()


def main():
    app = QApplication(sys.argv)
    win = PrettyEquationWidget()

    screen = app.primaryScreen()
    win.move((screen.size().width() - win.width()) // 2, (screen.size().height() - win.height()) // 2)

    win.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
