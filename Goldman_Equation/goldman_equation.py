# -*- coding: utf-8 -*-
"""
Created on Tue Apr 22 14:17:16 2021

@author: Gabriel H Riqueti
"""

from constant import FARADAYS_CONSTANT as F
from constant import GAS_CONSTANT as R

import numpy as np


def Goldman_equation(temperature, mono_cations_in, mono_cations_out, mono_cations_perm, mono_anions_in, mono_anions_out, mono_anions_perm,):
    """
    Calculate the resting membrane potential for a specific ion
    
    Parameters
    ----------
    temperature         : Temperature (Kelvin)
    mono_cations_in     : Concentration of monovalent cations inside the cell
    mono_cations_out    : Concentration of monovalent cations outside the cell
    mono_cations_perm   : Relative permeability of monovalent cations outside the cell
    mono_anions_in      : Concentration of monovalent anions inside the cell
    mono_anions_out     : Concentration of monovalent anions outside the cell
    mono_anions_perm    : Relative permeability of monovalent anions outside the cell

    Returns
    -------
    e_r                 : Resting membrane potential
        
    """

    if (mono_cations_in <= 0).any() or (mono_cations_out <= 0).any() or (mono_anions_in <= 0).any() or (mono_anions_out <= 0).any():
        raise ValueError('The ionic concentrations must have positive values')

    return (R * temperature / F) * np.log(
        (np.sum(mono_cations_out * mono_cations_perm) + np.sum(mono_anions_in * mono_anions_perm)) /
        (np.sum(mono_cations_in * mono_cations_perm) + np.sum(mono_anions_out * mono_anions_perm))
    )

