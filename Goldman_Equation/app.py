# -*- coding: utf-8 -*-
"""
Created on Tue Apr 20 15:01:58 2021

@author: Gabriel H Riqueti
"""

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys
import numpy as np

from constant import ABSOLUTE_TEMPERATURE_CELSIUS as T0
from goldman_equation import Goldman_equation


class GoldmanEquationWidget(QtWidgets.QWidget):

    def __init__(self):
        super().__init__()

        self.label_potassium_in = QtWidgets.QLabel('[K+]in (mM):')
        self.label_potassium_out = QtWidgets.QLabel('[K+]out (mM):')
        self.label_potassium_relative_permeability = QtWidgets.QLabel('P_K+:')
        self.label_potassium_relative_permeability_value = QtWidgets.QLabel('1')
        self.label_sodium_in = QtWidgets.QLabel('[Na+]in (mM):')
        self.label_sodium_out = QtWidgets.QLabel('[Na+]out (mM):')
        self.label_sodium_relative_permeability = QtWidgets.QLabel('P_Na+:')
        self.label_cloride_in = QtWidgets.QLabel('[Cl-]in (mM):')
        self.label_cloride_out = QtWidgets.QLabel('[Cl-]out (mM):')
        self.label_cloride_relative_permeability = QtWidgets.QLabel('P_Cl-:')
        self.label_temperature = QtWidgets.QLabel('Temperature (Celsius):')
        self.label_potential = QtWidgets.QLabel('Equilibrium potential:')
        self.label_potential_value = QtWidgets.QLabel()

        self.line_potassium_in = QtWidgets.QLineEdit()
        self.line_potassium_out = QtWidgets.QLineEdit()
        self.line_valence = QtWidgets.QLineEdit()
        self.line_sodium_in = QtWidgets.QLineEdit()
        self.line_sodium_out = QtWidgets.QLineEdit()
        self.line_sodium_relative_permeability = QtWidgets.QLineEdit()
        self.line_cloride_in = QtWidgets.QLineEdit()
        self.line_cloride_out = QtWidgets.QLineEdit()
        self.line_cloride_relative_permeability = QtWidgets.QLineEdit()
        self.line_temperature = QtWidgets.QLineEdit()

        self.button = QtWidgets.QPushButton()

        self.grid = QtWidgets.QGridLayout()

        self.UI()

    def calculate_resting_potential(self):
        try:
            K_in = float(self.line_potassium_in.text())
            if K_in <= 0:
                raise ValueError
            Na_in = float(self.line_sodium_in.text())
            if Na_in <= 0:
                raise ValueError
            Cl_in = float(self.line_cloride_in.text())
            if Cl_in <= 0:
                raise ValueError
            K_out = float(self.line_potassium_out.text())
            if K_out <= 0:
                raise ValueError
            Na_out = float(self.line_sodium_out.text())
            if Na_out <= 0:
                raise ValueError
            Cl_out = float(self.line_cloride_out.text())
            if Cl_out <= 0:
                raise ValueError
        except ValueError:
            error_msg = 'ValueError: the ionic concentrations must be positive float numbers'
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

        K_perm = 1
        try:
            Na_perm = float(self.line_sodium_relative_permeability.text())
            if Na_perm <= 0:
                raise ValueError
            Cl_perm = float(self.line_cloride_relative_permeability.text())
            if Cl_perm <= 0:
                raise ValueError
        except ValueError:
            error_msg = 'ValueError: the relative permeabilities must be positive float numbers'
            # print(error_msg)
            QtWidgets.QMessageBox.about(self, 'Error Message', error_msg)
            return -1

        cations_in = np.array([K_in, Na_in], dtype=np.float32)
        cations_out = np.array([K_out, Na_out], dtype=np.float32)
        cations_perm = np.array([K_perm, Na_perm], dtype=np.float32)
        anions_in = np.array([Cl_in], dtype=np.float32)
        anions_out = np.array([Cl_out], dtype=np.float32)
        anions_perm = np.array([Cl_perm], dtype=np.float32)

        resting_potential = 1000 * Goldman_equation(temperature - T0, cations_in, cations_out, cations_perm, anions_in, anions_out, anions_perm)

        self.label_potential_value.setText(str(resting_potential) + ' mV')

    def UI(self):
        self.button.setText('Calculate')
        self.button.clicked.connect(self.calculate_resting_potential)

        self.grid.addWidget(self.label_potassium_in, 0, 0)
        self.grid.addWidget(self.line_potassium_in, 1, 0)
        self.grid.addWidget(self.label_potassium_out, 2, 0)
        self.grid.addWidget(self.line_potassium_out, 3, 0)
        self.grid.addWidget(self.label_potassium_relative_permeability, 4, 0)
        self.grid.addWidget(self.label_potassium_relative_permeability_value, 5, 0)

        self.grid.addWidget(self.label_sodium_in, 0, 1)
        self.grid.addWidget(self.line_sodium_in, 1, 1)
        self.grid.addWidget(self.label_sodium_out, 2, 1)
        self.grid.addWidget(self.line_sodium_out, 3, 1)
        self.grid.addWidget(self.label_sodium_relative_permeability, 4, 1)
        self.grid.addWidget(self.line_sodium_relative_permeability, 5, 1)

        self.grid.addWidget(self.label_cloride_in, 0, 2)
        self.grid.addWidget(self.line_cloride_in, 1, 2)
        self.grid.addWidget(self.label_cloride_out, 2, 2)
        self.grid.addWidget(self.line_cloride_out, 3, 2)
        self.grid.addWidget(self.label_cloride_relative_permeability, 4, 2)
        self.grid.addWidget(self.line_cloride_relative_permeability, 5, 2)

        self.grid.addWidget(self.label_temperature, 0, 3)
        self.grid.addWidget(self.line_temperature, 1, 3)
        self.grid.addWidget(self.button, 6, 3)
        self.grid.addWidget(self.label_potential, 7, 1)
        self.grid.addWidget(self.label_potential_value, 7, 2)

        self.setLayout(self.grid)
        self.setGeometry(400, 300, 350, 200)
        self.setWindowTitle('Goldman Equation')

        self.show()


def main():
    app = QApplication(sys.argv)
    win = GoldmanEquationWidget()

    win.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
