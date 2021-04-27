# -*- coding: utf-8 -*-
##
# @file z_transform_app.py
# @brief Contain a gui calculating the Z Transform
# @author Gabriel H Riqueti
# @email gabrielhriqueti@gmail.com
# @date 27/04/2021
#

from PySide2 import QtWidgets
from PySide2.QtWidgets import QApplication
import sys
import sympy


class ZTransformWidget(QtWidgets.QWidget):
    ##
    # @class ZTransformWidget
    # @brief provides GUI to the Z Transform

    def __init__(self):
        """
        Initialize instance
        """
        super().__init__()

        self.label_exp_sample = QtWidgets.QLabel('f[n] = ')
        self.label_exp_state = QtWidgets.QLabel('F(z) = ')

        self.line_exp_sample = QtWidgets.QLineEdit()
        self.line_exp_state = QtWidgets.QLineEdit()

        self.button_calculate_z_transform = QtWidgets.QPushButton()
#        self.button_calculate_inverse_z_transform = QtWidgets.QPushButton()
        self.button_about = QtWidgets.QPushButton()

        self.grid = QtWidgets.QGridLayout()

        self.UI()

    def _show_info(self):
        z = sympy.symbols('z')
        n = sympy.symbols('n', integer=True)
        f = sympy.symbols('f', cls=sympy.Function)

        expr = sympy.Sum(f(n) * sympy.exp(-z * n), (n, 0, sympy.oo))

        message = 'Z Transform \n\n Z{f[n]} = \n\n' + str(sympy.pretty(expr, use_unicode=True))

        QtWidgets.QMessageBox.about(self, 'Information', message)

    def _calculate_z_transform(self):
        z = sympy.symbols('z')
        n = sympy.Symbol('n', integer=True)

        try:
            f = sympy.parsing.sympy_parser.parse_expr(self.line_exp_sample.text())
            F = sympy.Sum(f * z**(-n), (n, 0, sympy.oo)).doit(noconds=True).args[0][0]
        except  (ValueError, TypeError, SyntaxError):
            error_msg = f'ValueError: invalid expression'
            # print(error_msg)
            QtWidgets.QMessageBox.about(self, 'Error message', error_msg)

        self.line_exp_state.setText(str(F))


    """ Not implemented
        def _calculate_inverse_z_transform(self):
            z = sympy.symbols('z')
            n = sympy.Symbol('n', integer=True)
    
            try:
                F = sympy.parsing.sympy_parser.parse_expr(self.line_exp_state.text())
                f = sympy.Sum(F * z**(-n), (n, -sympy.oo, sympy.oo)).doit(noconds=True)
            except ValueError:
                error_msg = f'ValueError: invalid expression'
                # print(error_msg)
                QtWidgets.QMessageBox.about(self, 'Error message', error_msg)
    
            self.line_exp_sample.setText(str(f))
    """

    def UI(self):
        """
        Set the user interface
        """
        self.button_about.setText('About')
        self.button_about.clicked.connect(self._show_info)

        self.button_calculate_z_transform.setText('Z Transform')
        self.button_calculate_z_transform.clicked.connect(self._calculate_z_transform)
#        self.button_calculate_inverse_z_transform.setText('Inverse Z Transform')
#        self.button_calculate_inverse_z_transform.clicked.connect(self._calculate_inverse_z_transform)

        self.grid.addWidget(self.label_exp_sample, 0, 0)
        self.grid.addWidget(self.line_exp_sample, 0, 1, 1, 2)
        self.grid.addWidget(self.label_exp_state, 1, 0)
        self.grid.addWidget(self.line_exp_state, 1, 1, 1, 2)
        self.grid.addWidget(self.button_about, 2, 0)
        self.grid.addWidget(self.button_calculate_z_transform, 2, 1)
#        self.grid.addWidget(self.button_calculate_inverse_z_transform, 2, 2)

        self.setLayout(self.grid)
        self.setGeometry(400, 300, 400, 150)
        self.setWindowTitle('Z Transform')

        self.show()


def main():
    app = QApplication(sys.argv)
    win = ZTransformWidget()

    screen = app.primaryScreen()
    win.move((screen.size().width() - win.width()) // 2, (screen.size().height() - win.height()) // 2)

    win.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
