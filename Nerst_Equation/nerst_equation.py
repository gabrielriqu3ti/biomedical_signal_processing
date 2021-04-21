# -*- coding: utf-8 -*-
"""
Created on Tue Apr 20 14:17:16 2021

@author: gabri
"""

from constant import FARADAYS_CONSTANT as F
from constant import GAS_CONSTANT as R

import math
import numpy as np


@np.vectorize
def Nerst_equation(temperature, valence, ion_in, ion_out):
    """
    Calculate the equilibrium potential for a specific ion
    
    Parameters
    ----------
    temperature  : Temperature (Kelvin)
    valence      : Valence
    ion_in       : Ionic concentration inside the cell
    ion_out      : Ionic concentration outside the cell
    
    Returns
    -------
    e_ion        : Ionic equilibrium potential
        
    """
    
    if ion_in <= 0 or ion_out <= 0:
        raise ValueError('I_in and I_out must have positive values')
    if valence == 0:
        return 0 * temperature * math.log(ion_in / ion_out)

    return (R * temperature / (valence * F)) * math.log(ion_in / ion_out)

