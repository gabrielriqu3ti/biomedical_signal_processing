# -*- coding: utf-8 -*-
"""
Created on Tue Apr 20 15:01:58 2021

@author: gabri
"""

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys

from nernst_equation import Nernst_equation
from constant import ABSOLUTE_TEMPERATURE_CELSIUS as T0


class NerstEquationWidget(QtWidgets.QWidget):

    def __init__(self):
        super().__init__()

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

        self.button = QtWidgets.QPushButton()

        self.grid = QtWidgets.QGridLayout()

        self.UI()

    def calculate_resting_potential(self):
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

        equilibrium_potential = 1000 * Nernst_equation(temperature - T0, valence, ion_in, ion_out)

        self.label_potential_value.setText(str(equilibrium_potential) + ' mV')

    def UI(self):
        self.button.setText('Calculate')
        self.button.clicked.connect(self.calculate_resting_potential)

        self.grid.addWidget(self.label_ion_in, 0, 0)
        self.grid.addWidget(self.line_ion_in, 1, 0)
        self.grid.addWidget(self.label_ion_out, 2, 0)
        self.grid.addWidget(self.line_ion_out, 3, 0)
        self.grid.addWidget(self.label_temperature, 0, 1)
        self.grid.addWidget(self.line_temperature, 1, 1)
        self.grid.addWidget(self.label_valence, 2, 1)
        self.grid.addWidget(self.line_valence, 3, 1)
        self.grid.addWidget(self.button, 4, 0)
        self.grid.addWidget(self.label_potential, 5, 0)
        self.grid.addWidget(self.label_potential_value, 5, 1)

        self.setLayout(self.grid)
        self.setGeometry(400, 300, 350, 200)
        self.setWindowTitle('Nerst Equation')

        self.show()


def main():
    app = QApplication(sys.argv)
    win = NerstEquationWidget()

    win.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
