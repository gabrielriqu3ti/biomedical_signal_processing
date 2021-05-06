# -*- coding: utf-8 -*-
##
# @file nernst_app.py
# @brief Contain a gui for the Nernst equation
# @author Gabriel H Riqueti
# @email gabrielhriqueti@gmail.com
# @date 20/04/2021
#

from PySide2 import QtWidgets
from PySide2.QtWidgets import QApplication
import sys

from biomedical_signal_processing import ABSOLUTE_TEMPERATURE_CELSIUS as T0
from biomedical_signal_processing import nernst_equation


class NernstEquationWidget(QtWidgets.QWidget):
    ##
    # @class NernstEquationWidget
    # @brief provides GUI to Nernst equation

    def __init__(self, screen=None, *args, **kwrds):
        """
        Initialize instance
        """
        super().__init__(*args, **kwrds)

        self.label_ion_in = QtWidgets.QLabel('[Íon]in (mM):')
        self.label_ion_out = QtWidgets.QLabel('[Íon]out (mM):')
        self.label_valence = QtWidgets.QLabel('Valence:')
        self.label_temperature = QtWidgets.QLabel('Temperature (Celsius):')
        self.label_potential = QtWidgets.QLabel('Equilibrium potential:')
        self.label_potential_value = QtWidgets.QLabel()

        self.line_ion_in = QtWidgets.QLineEdit()
        self.line_ion_out = QtWidgets.QLineEdit()
        self.line_valence = QtWidgets.QLineEdit()
        self.line_temperature = QtWidgets.QLineEdit()

        self.button_calculate = QtWidgets.QPushButton()
        self.button_about = QtWidgets.QPushButton()

        self.grid = QtWidgets.QGridLayout()

        self.screen = screen

        self.UI()
        
    def _show_info(self):
        message = '''Nernst Equation
        
The Nernst Equation allows us to calculate the equilibrium potential for a given ion separated by a phospholipid membrane with ion channels selectively permeable to that ion and is given by:

E_ion = (RT/(zF)) ln([ion]out / [ion]in)

where:

- E_ion = ionic equilibrium potential
- R = gas constant
- T = absolute temperature
- z = charge of that ion
- F = Faraday's constant
- ln = natural logarithm
- [ion]out = concentration of the ion outside the cell
- [ion]in = concentration of the ion inside the cell

The equilibrium potential is the electrical potential difference that exactly balances an ionic concentration gradient.
        '''

        QtWidgets.QMessageBox.about(self, 'Information', message)

    def _calculate_equilibrium_potential(self):
        try:
            ion_in = float(self.line_ion_in.text())
            if ion_in <= 0:
                raise ValueError
        except ValueError:
            error_msg = 'ValueError: the ionic concentration inside the cell must be a positive float number'
            # print(error_msg)
            QtWidgets.QMessageBox.about(self, 'Error Message', error_msg)
            return -1
        try:
            ion_out = float(self.line_ion_out.text())
            if ion_out <= 0:
                raise ValueError
        except ValueError:
            error_msg = 'ValueError: the ionic concentration outside the cell must be a positive float number'
            # print(error_msg)
            QtWidgets.QMessageBox.about(self, 'Error Message', error_msg)
            return -1
        try:
            temperature = float(self.line_temperature.text())
            if temperature - T0 <= 0:
                raise ValueError
        except ValueError:
            error_msg = f'ValueError: the temperature must be a float number higher than the absolute zero ({T0} Celsius)'
            # print(error_msg)
            QtWidgets.QMessageBox.about(self, 'Error Message', error_msg)
            return -1
        try:
            valence = int(self.line_valence.text())
        except ValueError:
            error_msg = 'ValueError: the ionic valence must be an integer number'
            # print(error_msg)
            QtWidgets.QMessageBox.about(self, 'Error Message', error_msg)
            return -1

        equilibrium_potential = 1000 * nernst_equation(temperature - T0, valence, ion_in, ion_out)

        self.label_potential_value.setText(str(equilibrium_potential) + ' mV')

    def UI(self):
        """
        Set the user interface
        """
        self.button_about.setText('About')
        self.button_about.clicked.connect(self._show_info)

        self.button_calculate.setText('Calculate')
        self.button_calculate.clicked.connect(self._calculate_equilibrium_potential)

        self.grid.addWidget(self.label_ion_in, 0, 0)
        self.grid.addWidget(self.line_ion_in, 1, 0)
        self.grid.addWidget(self.label_ion_out, 2, 0)
        self.grid.addWidget(self.line_ion_out, 3, 0)
        self.grid.addWidget(self.label_temperature, 0, 1)
        self.grid.addWidget(self.line_temperature, 1, 1)
        self.grid.addWidget(self.label_valence, 2, 1)
        self.grid.addWidget(self.line_valence, 3, 1)
        self.grid.addWidget(QtWidgets.QLabel(''), 4, 0)
        self.grid.addWidget(self.button_about, 5, 0)
        self.grid.addWidget(self.button_calculate, 5, 1)
        self.grid.addWidget(QtWidgets.QLabel(''), 6, 0)
        self.grid.addWidget(self.label_potential, 7, 0)
        self.grid.addWidget(self.label_potential_value, 7, 1)

        self.setLayout(self.grid)

        if self.screen is None:
            self.setGeometry(400, 300, 350, 200)
        else:
            self.setGeometry(1, 1, 350, 200)
            self.move((self.screen.size().width() - self.width()) // 2,
                      (self.screen.size().height() - self.height()) // 2)

        self.setWindowTitle('Nernst Equation')

        self.show()


def main():
    app = QApplication(sys.argv)
    screen = app.primaryScreen()

    win = NernstEquationWidget(screen)

    win.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
