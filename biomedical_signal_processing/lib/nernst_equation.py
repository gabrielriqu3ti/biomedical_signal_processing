# -*- coding: utf-8 -*-
##
# @file nernst_equation.py
# @brief Contain a function that calculates the equilibrium potential using the Goldman equation
# @author Gabriel H Riqueti
# @email gabrielhriqueti@gmail.com
# @date 20/04/2021
#

from biomedical_signal_processing import FARADAYS_CONSTANT as F
from biomedical_signal_processing import GAS_CONSTANT as R

import math
import numpy as np


@np.vectorize
def nernst_equation(temperature, valence, ion_in, ion_out):
    """
    Calculate the equilibrium potential for a specific ion

    Parameters
    ----------
    temperature  : float
                   Temperature (Kelvin)
    valence      : int
                   Valence
    ion_in       : positive float
                   Ionic concentration inside the cell
    ion_out      : positive float
                   Ionic concentration outside the cell

    Returns
    -------
    e_ion        : float
                   Ionic equilibrium potential

    """

    if ion_in <= 0 or ion_out <= 0:
        raise ValueError('ion_in and ion_out must have positive values')
    if valence == 0:
        return 0 * valence * temperature * ion_in * ion_out

    return (R * temperature / (valence * F)) * math.log(ion_out / ion_in)

