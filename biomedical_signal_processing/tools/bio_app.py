# -*- coding: utf-8 -*-
##
# @file bio_app.py
# @brief Contain a GUI for the entire biological signals project
# @author Gabriel H Riqueti
# @email gabrielhriqueti@gmail.com
# @date 25/04/2021
#

from PySide2 import QtWidgets
from PySide2.QtWidgets import QApplication
import sys

from biomedical_signal_processing import NernstEquationWidget, GoldmanEquationWidget


class BioWidget(QtWidgets.QWidget):
    ##
    # @class BioWidget
    # @brief provides GUI to all the functionalities of the library

    def __init__(self, screen=None, *args, **kwrds):
        """
        Initialize instance
        """
        super().__init__(*args, **kwrds)

        self._app_dict = {'Nernst equation' : NernstEquationWidget, 'Goldman equation' : GoldmanEquationWidget}

        self.label_choose_app = QtWidgets.QLabel('Choose an application:')

        self.box_choose_app = QtWidgets.QComboBox()

        self.button_enter = QtWidgets.QPushButton()

        self.grid = QtWidgets.QGridLayout()

        self.screen =screen

        self.UI()

    def _enter_app(self):
        self.app = self._app_dict[self.box_choose_app.currentText()](screen=self.screen)

        self.app.show()

    def UI(self):
        """
        Set the user interface
        """
        self.box_choose_app.addItems(list(self._app_dict.keys()))

        self.button_enter.setText('Enter')
        self.button_enter.clicked.connect(self._enter_app)

        self.grid.addWidget(self.label_choose_app, 0, 0)
        self.grid.addWidget(self.box_choose_app, 1, 0, 1, 2)
        self.grid.addWidget(self.button_enter, 1, 2)

        self.setLayout(self.grid)

        if self.screen is None:
            self.setGeometry(400, 300, 400, 60)
        else:
            self.setGeometry(1, 1, 400, 60)
            self.move((self.screen.size().width() - self.width()) // 2,
                      (self.screen.size().height() - self.height()) // 2)

        self.setWindowTitle('Biological App')

        self.show()


def main():
    app = QApplication(sys.argv)
    screen = app.primaryScreen()

    win = BioWidget(screen)

    win.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
