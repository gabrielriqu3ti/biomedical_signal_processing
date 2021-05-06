# -*- coding: utf-8 -*-
##
# @file func_plot_app.py
# @brief Contain a GUI for plotting functions
# @author Gabriel H Riqueti
# @email gabrielhriqueti@gmail.com
# @date 28/04/2021
#

from PySide2 import QtWidgets
from PySide2.QtWidgets import QApplication
import sys
import numpy as np
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from matplotlib.figure import Figure
import sympy


class MPLCanvas(FigureCanvasQTAgg):
    ##
    # @class FigureCanvasQTAgg
    # @brief provides GUI to all the functionalities of the library

    def __init__(self, parent=None, width=5, height=4, dpi=100, *args, **kwrds):
        """
        Initialize instance
        """
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)
        super(MPLCanvas, self).__init__(fig)


class FunctionPlotWidget(QtWidgets.QWidget):
    ##
    # @class FunctionPlotWidget
    # @brief provides GUI to all the functionalities of the library

    def __init__(self, screen=None, *args, **kwrds):
        """
        Initialize instance
        """
        super().__init__(*args, **kwrds)

        self.label_var = QtWidgets.QLabel('t = [')
        self.label_func = QtWidgets.QLabel('f(t) =')

        self.line_var_min = QtWidgets.QLineEdit()
        self.line_var_max = QtWidgets.QLineEdit()
        self.line_func = QtWidgets.QLineEdit()

        self.mpl_canvas = MPLCanvas(width=5, heigth=4, dpi=100)

        self.button_clear = QtWidgets.QPushButton()
        self.button_legend = QtWidgets.QPushButton()
        self.button_plot = QtWidgets.QPushButton()

        self.grid = QtWidgets.QGridLayout()

        self.screen = screen

        self.UI()

    def _clear(self):
        self.mpl_canvas.axes.cla()

        self.mpl_canvas.axes.set_xlabel('t')
        self.mpl_canvas.axes.set_ylabel('f(t)')
        self.button_legend.setText('Legend on')

        self.mpl_canvas.draw()

    def _legend(self):
        legend = self.mpl_canvas.axes.get_legend()
        if legend is not None:
            visibility = self.mpl_canvas.axes.get_legend().get_visible()
            self.button_legend.setText('Legend ' + ('on' if visibility else 'off'))
            self.mpl_canvas.axes.get_legend().set_visible(not visibility)

        self.mpl_canvas.draw()

    def _plot(self):
        t = sympy.symbols('t')

        try:
            t_min = float(self.line_var_min.text())
            t_max = float(self.line_var_max.text())
            if t_min >= t_max:
                raise ValueError
        except ValueError:
            error_msg = 'ValueError: the interval must be constituted of float numbers with the left one being ' \
                        'smaller than the right one '
            # print(error_msg)
            QtWidgets.QMessageBox.about(self, 'Error message', error_msg)
            return -1
        try:
            f = sympy.parsing.sympy_parser.parse_expr(self.line_func.text())
        except (ValueError, TypeError, SyntaxError):
            error_msg = f'ValueError: invalid expression'
            # print(error_msg)
            QtWidgets.QMessageBox.about(self, 'Error message', error_msg)
            return -1

        t_np = np.linspace(t_min, t_max, 1000)
        f_py = sympy.lambdify(t, f, "numpy")
        f_np = f_py(t_np)
        if isinstance(f_np, (int, float)):
            f_np *= np.ones(shape=t_np.shape)

        self.mpl_canvas.axes.plot(t_np, f_np, label=sympy.pretty(f))

        legend = self.mpl_canvas.axes.get_legend()
        if legend is not None:
            visibility = self.mpl_canvas.axes.get_legend().get_visible()
        else:
            visibility = False

        self.mpl_canvas.axes.legend().set_visible(visibility)

        self.mpl_canvas.draw()

    def UI(self):
        """
        Set the user interface
        """
        self.button_clear.setText('Clear')
        self.button_clear.clicked.connect(self._clear)
        self.button_legend.setText('Legend on')
        self.button_legend.clicked.connect(self._legend)
        self.button_plot.setText('Plot')
        self.button_plot.clicked.connect(self._plot)

        self.mpl_canvas.axes.set_xlabel('t')
        self.mpl_canvas.axes.set_ylabel('f(t)')

        self.grid.addWidget(self.label_var, 0, 0)
        self.grid.addWidget(self.line_var_min, 0, 1)
        self.grid.addWidget(QtWidgets.QLabel(','), 0, 2)
        self.grid.addWidget(self.line_var_max, 0, 3)
        self.grid.addWidget(QtWidgets.QLabel(']'), 0, 4)

        self.grid.addWidget(self.label_func, 1, 0)
        self.grid.addWidget(self.line_func, 1, 1, 1, 3)

        self.grid.addWidget(self.button_clear, 2, 1)
        self.grid.addWidget(self.button_plot, 2, 3)
        self.grid.addWidget(self.button_legend, 3, 3)

        self.grid.addWidget(self.mpl_canvas, 4, 0, 1, 4)

        self.setLayout(self.grid)

        if self.screen is None:
            self.setGeometry(400, 300, 800, 700)
        else:
            self.setGeometry(1, 1, 800, 700)
            self.move((self.screen.size().width() - self.width()) // 2,
                      (self.screen.size().height() - self.height()) // 2)

        self.setWindowTitle('Function display')

        self.show()


def main():
    app = QApplication(sys.argv)
    screen = app.primaryScreen()

    win = FunctionPlotWidget(screen)

    win.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
