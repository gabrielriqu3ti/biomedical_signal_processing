# -*- coding: utf-8 -*-
##
# @file discrete_convolution.py
# @brief Contain a GUI for plotting functions
# @author Gabriel H Riqueti
# @email gabrielhriqueti@gmail.com
# @date 29/04/2021
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


class DiscreteConvWidget(QtWidgets.QWidget):
    ##
    # @class DiscreteConvWidget
    # @brief provides GUI to all the functionalities of the library

    def __init__(self, screen=None, *args, **kwrds):
        """
        Initialize instance
        """
        super().__init__(*args, **kwrds)

        self.label_var = QtWidgets.QLabel('n = [')
        self.label_func_x = QtWidgets.QLabel('x[n] =')
        self.label_func_h = QtWidgets.QLabel('h[n] =')
        self.label_func_y = QtWidgets.QLabel('y[n] =')

        self.line_var_min = QtWidgets.QLineEdit()
        self.line_var_max = QtWidgets.QLineEdit()

        self.line_func_x = QtWidgets.QLineEdit()
        self.line_func_h = QtWidgets.QLineEdit()
        self.line_func_y = QtWidgets.QLineEdit()

        self.mpl_canvas = MPLCanvas(width=5, heigth=4, dpi=100)

        self.button_clear = QtWidgets.QPushButton()
        self.button_plot_convolution = QtWidgets.QPushButton()
        self.button_legend = QtWidgets.QPushButton()
        self.button_plot_x = QtWidgets.QPushButton()
        self.button_plot_h = QtWidgets.QPushButton()
        self.button_plot_y = QtWidgets.QPushButton()

        self.grid = QtWidgets.QGridLayout()

        self.screen = screen

        self.UI()

    def _clear(self):
        self.mpl_canvas.axes.cla()

        self.mpl_canvas.axes.set_xlabel('n')
        self.mpl_canvas.axes.set_ylabel('f[n]')
        self.button_legend.setText('Legend on')

        self.mpl_canvas.draw()

    def _legend(self):
        legend = self.mpl_canvas.axes.get_legend()
        if legend is not None:
            visibility = self.mpl_canvas.axes.get_legend().get_visible()
            self.button_legend.setText('Legend ' + ('on' if visibility else 'off'))
            self.mpl_canvas.axes.get_legend().set_visible(not visibility)

        self.mpl_canvas.draw()

    def _plot(self, var):
        n = sympy.symbols('n')
        line_func = {'x' : self.line_func_x, 'h' : self.line_func_h, 'y' : self.line_func_y}
        marker_color = {'x' : 'C0o', 'h' : 'C1o', 'y' : 'C2o'}

        try:
            n_min = float(self.line_var_min.text())
            n_max = float(self.line_var_max.text())
            if n_min >= n_max:
                raise ValueError
        except ValueError:
            error_msg = 'ValueError: the interval must be constituted of float numbers with the left one being ' \
                        'smaller than the right one '
            # print(error_msg)
            QtWidgets.QMessageBox.about(self, 'Error message', error_msg)
            return -1
        try:
            f = sympy.parsing.sympy_parser.parse_expr(line_func[var].text())
        except (ValueError, TypeError, SyntaxError):
            error_msg = f'ValueError: invalid expression'
            # print(error_msg)
            QtWidgets.QMessageBox.about(self, 'Error message', error_msg)
            return -1

        n_np = np.arange(- 10 * np.max([np.abs(n_min), np.abs(n_max)]), 10 * np.max([np.abs(n_min), np.abs(n_max)]) + 1)
        f_py = sympy.lambdify(n, f, "numpy")
        f_np = f_py(n_np)
        if isinstance(f_np, (int, float)):
            f_np *= np.ones(shape=n_np.shape)

        self.mpl_canvas.axes.stem(n_np[(n_np >= n_min) & (n_np <= n_max)], f_np[(n_np >= n_min) & (n_np <= n_max)], label=sympy.pretty(f), markerfmt=marker_color[var])

        legend = self.mpl_canvas.axes.get_legend()
        if legend is not None:
            visibility = self.mpl_canvas.axes.get_legend().get_visible()
        else:
            visibility = False

        self.mpl_canvas.axes.legend().set_visible(visibility)

        self.mpl_canvas.draw()

    def _plot_convolution(self):
        n = sympy.symbols('n')
        try:
            n_min = float(self.line_var_min.text())
            n_max = float(self.line_var_max.text())
            if n_min >= n_max:
                raise ValueError
        except ValueError:
            error_msg = 'ValueError: the interval must be constituted of float numbers with the left one being ' \
                        'smaller than the right one '
            # print(error_msg)
            QtWidgets.QMessageBox.about(self, 'Error message', error_msg)
            return -1
        try:
            x = sympy.parsing.sympy_parser.parse_expr(self.line_func_x.text())
            h = sympy.parsing.sympy_parser.parse_expr(self.line_func_h.text())
        except (ValueError, TypeError, SyntaxError):
            error_msg = f'ValueError: invalid expression'
            # print(error_msg)
            QtWidgets.QMessageBox.about(self, 'Error message', error_msg)
            return -1

        n_np = np.arange(- 10 * np.max([np.abs(n_min), np.abs(n_max)]), 10 * np.max([np.abs(n_min), np.abs(n_max)]) + 1)

        x_py = sympy.lambdify(n, x, "numpy")
        x_np = x_py(n_np)
        h_py = sympy.lambdify(n, h, "numpy")
        h_np = h_py(n_np)

        if isinstance(x_np, (int, float)):
            x_np *= np.ones(shape=n_np.shape)
        if isinstance(h_np, (int, float)):
            h_np *= np.ones(shape=n_np.shape)
            
        y_np = np.convolve(x_np, h_np, 'same')

        self.mpl_canvas.axes.stem(n_np[(n_np >= n_min) & (n_np <= n_max)], y_np[(n_np >= n_min) & (n_np <= n_max)], label='(h*x)[n]', markerfmt='C3o')

        legend = self.mpl_canvas.axes.get_legend()
        if legend is not None:
            visibility = self.mpl_canvas.axes.get_legend().get_visible()
        else:
            visibility = False

        self.mpl_canvas.axes.legend().set_visible(visibility)

        self.mpl_canvas.draw()

    def _plot_x(self):
        self._plot('x')

    def _plot_h(self):
        self._plot('h')

    def _plot_y(self):
        self._plot('y')

    def UI(self):
        """
        Set the user interface
        """
        self.button_clear.setText('Clear')
        self.button_clear.clicked.connect(self._clear)
        self.button_legend.setText('Legend on')
        self.button_legend.clicked.connect(self._legend)
        self.button_plot_convolution.setText('Plot convolution (h * x)[n]')
        self.button_plot_convolution.clicked.connect(self._plot_convolution)
        self.button_plot_x.setText('Plot x')
        self.button_plot_x.clicked.connect(self._plot_x)
        self.button_plot_h.setText('Plot h')
        self.button_plot_h.clicked.connect(self._plot_h)
        self.button_plot_y.setText('Plot y')
        self.button_plot_y.clicked.connect(self._plot_y)

        self.mpl_canvas.axes.set_xlabel('n')
        self.mpl_canvas.axes.set_ylabel('f[n]')

        self.grid.addWidget(self.label_var, 0, 0)
        self.grid.addWidget(self.line_var_min, 0, 1)
        self.grid.addWidget(QtWidgets.QLabel(','), 0, 2)
        self.grid.addWidget(self.line_var_max, 0, 3)
        self.grid.addWidget(QtWidgets.QLabel(']'), 0, 4)

        self.grid.addWidget(self.label_func_x, 1, 0)
        self.grid.addWidget(self.line_func_x, 1, 1, 1, 3)
        self.grid.addWidget(self.button_plot_x, 1, 4)

        self.grid.addWidget(self.label_func_h, 2, 0)
        self.grid.addWidget(self.line_func_h, 2, 1, 1, 3)
        self.grid.addWidget(self.button_plot_h, 2, 4)

        self.grid.addWidget(self.label_func_y, 3, 0)
        self.grid.addWidget(self.line_func_y, 3, 1, 1, 3)
        self.grid.addWidget(self.button_plot_y, 3, 4)

        self.grid.addWidget(self.button_clear, 4, 1)
        self.grid.addWidget(self.button_plot_convolution, 4, 3)
        self.grid.addWidget(self.button_legend, 4, 4)

        self.grid.addWidget(self.mpl_canvas, 5, 0, 1, 5)

        self.setLayout(self.grid)

        if self.screen is None:
            self.setGeometry(400, 300, 1600, 900)
        else:
            self.setGeometry(1, 1, 1600, 900)
            self.move((self.screen.size().width() - self.width()) // 2,
                      (self.screen.size().height() - self.height()) // 2)

        self.setWindowTitle('Discrete Convolution of Signals')

        self.show()


def main():
    app = QApplication(sys.argv)
    screen = app.primaryScreen()

    win = DiscreteConvWidget(screen)

    win.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
