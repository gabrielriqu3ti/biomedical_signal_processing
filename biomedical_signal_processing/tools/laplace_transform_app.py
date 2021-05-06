# -*- coding: utf-8 -*-
##
# @file laplace_transform_app.py
# @brief Contain a gui calculating the Laplace Transform
# @author Gabriel H Riqueti
# @email gabrielhriqueti@gmail.com
# @date 27/04/2021
#

from PySide2 import QtWidgets
from PySide2.QtWidgets import QApplication
import sys
import sympy

from biomedical_signal_processing import PrettyEquationWidget


class LaplaceTransformWidget(QtWidgets.QWidget):
    ##
    # @class LaplaceTransformWidget
    # @brief provides GUI to the Laplace Transform

    def __init__(self, screen=None, *args, **kwrds):
        """
        Initialize instance
        """
        super().__init__(*args, **kwrds)

        self.label_exp_time = QtWidgets.QLabel('f(t) = ')
        self.label_exp_state = QtWidgets.QLabel('F(s) = ')

        self.line_exp_time = QtWidgets.QLineEdit()
        self.line_exp_state = QtWidgets.QLineEdit()

        self.button_calculate_laplace_transform = QtWidgets.QPushButton()
        self.button_calculate_inverse_laplace_transform = QtWidgets.QPushButton()
        self.button_about = QtWidgets.QPushButton()

        self.grid = QtWidgets.QGridLayout()

        self.screen = screen

        self.UI()

    def _show_info(self):
        t, s = sympy.symbols('t, s')
        f = sympy.symbols('f', cls=sympy.Function)

        expr = sympy.integrate(f(t) * sympy.exp(-s * t), (t, 0, sympy.oo))

        self._msg = PrettyEquationWidget(title='Information', message='Laplace Transform',
                                         var='L{f(t)} = ', func=expr)
        self._msg.show()

        # message = 'Laplace Transform \n\n L{f(t)} = \n\n' + sympy.pretty(expr, use_unicode=True)
        # QtWidgets.QMessageBox.about(self, 'Information', message)

    def _calculate_laplace_transform(self):
        t, s = sympy.symbols('t, s')

        try:
            f = sympy.parsing.sympy_parser.parse_expr(self.line_exp_time.text())
            F = sympy.laplace_transform(f, t, s, noconds=True)
        except (ValueError, TypeError, SyntaxError):
            error_msg = f'ValueError: invalid expression'
            # print(error_msg)
            QtWidgets.QMessageBox.about(self, 'Error message', error_msg)
            return -1

        self.line_exp_state.setText(str(F))

    def _calculate_inverse_laplace_transform(self):
        t, s = sympy.symbols('t, s')

        try:
            F = sympy.parsing.sympy_parser.parse_expr(self.line_exp_state.text())
            f = sympy.inverse_laplace_transform(F, s, t, noconds=True)
        except (ValueError, TypeError, SyntaxError):
            error_msg = f'ValueError: invalid expression'
            # print(error_msg)
            QtWidgets.QMessageBox.about(self, 'Error message', error_msg)
            return -1

        self.line_exp_time.setText(str(f))

    def UI(self):
        """
        Set the user interface
        """
        self.button_about.setText('About')
        self.button_about.clicked.connect(self._show_info)

        self.button_calculate_laplace_transform.setText('Laplace Transform')
        self.button_calculate_laplace_transform.clicked.connect(self._calculate_laplace_transform)
        self.button_calculate_inverse_laplace_transform.setText('Inverse Laplace Transform')
        self.button_calculate_inverse_laplace_transform.clicked.connect(self._calculate_inverse_laplace_transform)

        self.grid.addWidget(self.label_exp_time, 0, 0)
        self.grid.addWidget(self.line_exp_time, 0, 1, 1, 4)
        self.grid.addWidget(self.label_exp_state, 1, 0)
        self.grid.addWidget(self.line_exp_state, 1, 1, 1, 4)
        self.grid.addWidget(self.button_about, 2, 0)
        self.grid.addWidget(self.button_calculate_laplace_transform, 2, 1, 1, 2)
        self.grid.addWidget(self.button_calculate_inverse_laplace_transform, 2, 3, 1, 2)

        self.setLayout(self.grid)
        if self.screen is None:
            self.setGeometry(400, 300, 500, 150)
        else:
            self.setGeometry(1, 1, 500, 150)
            self.move((self.screen.size().width() - self.width()) // 2,
                      (self.screen.size().height() - self.height()) // 2)
        self.setWindowTitle('Laplace Transform')

        self.show()


def main():
    app = QApplication(sys.argv)
    screen = app.primaryScreen()

    win = LaplaceTransformWidget(screen)

    win.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
