# -*- coding: utf-8 -*-
##
# @package biomedical_signal_processing
# @brief Contain the application and interfaces related to biological signal processing field
# @author Gabriel H Riqueti
# @email gabrielhriqueti@gmail.com
# @date 20/04/2021
#

from .info import PATH_GOLDMAN_EQUATION_INFO, PATH_NERNST_EQUATION_INFO

from .lib.constant import ABSOLUTE_TEMPERATURE_CELSIUS, FARADAYS_CONSTANT, GAS_CONSTANT

from .lib.goldman_equation import goldman_equation
from .lib.nernst_equation import nernst_equation

from .tools.pretty_equation_widget import PrettyEquationWidget
from .tools.laplace_transform_app import LaplaceTransformWidget
from .tools.z_transform_app import ZTransformWidget
from .tools.func_plot_app import FunctionPlotWidget
from .tools.discrete_convolution import DiscreteConvWidget

from .tools.goldman_app import GoldmanEquationWidget
from .tools.nernst_app import NernstEquationWidget
