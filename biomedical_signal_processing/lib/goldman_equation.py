# -*- coding: utf-8 -*-
##
# @file goldman_equation.py
# @brief Contain a function that calculates the equilibrium potential using the Goldman equation
# @author Gabriel H Riqueti
# @email gabrielhriqueti@gmail.com
# @date 22/04/2021
#

from biomedical_signal_processing import FARADAYS_CONSTANT as F
from biomedical_signal_processing import GAS_CONSTANT as R

import numpy as np


def goldman_equation(temperature, mono_cations_in, mono_cations_out, mono_cations_perm, mono_anions_in, mono_anions_out, mono_anions_perm,):
    """
    Calculate the resting membrane potential for a specific ion

    Parameters
    ----------
    temperature         : float
                          Temperature (Kelvin)
    mono_cations_in     : positive float
                          Concentration of monovalent cations inside the cell
    mono_cations_out    : positive float
                          Concentration of monovalent cations outside the cell
    mono_cations_perm   : positive float
                          Relative permeability of monovalent cations outside the cell
    mono_anions_in      : positive float
                          Concentration of monovalent anions inside the cell
    mono_anions_out     : positive float
                          Concentration of monovalent anions outside the cell
    mono_anions_perm    : positive float
                          Relative permeability of monovalent anions outside the cell

    Returns
    -------
    e_r                 : float
                          Resting membrane potential

    """

    if (mono_cations_in <= 0).any() or (mono_cations_out <= 0).any() or (mono_anions_in <= 0).any() or (mono_anions_out <= 0).any():
        raise ValueError('The ionic concentrations must have positive values')
    if temperature < 0:
        raise ValueError('temperature must have non-negative values')

    if (np.sum(mono_cations_in * mono_cations_perm) + np.sum(mono_anions_out * mono_anions_perm) == 0
            and (np.sum(mono_cations_out * mono_cations_perm) + np.sum(mono_anions_in * mono_anions_perm)) == 0):
        return 0 * (R * temperature / F) * (
                (np.sum(mono_cations_out * mono_cations_perm) + np.sum(mono_anions_in * mono_anions_perm)) *
                (np.sum(mono_cations_in * mono_cations_perm) + np.sum(mono_anions_out * mono_anions_perm))
        )

    return (R * temperature / F) * np.log(
        (np.sum(mono_cations_out * mono_cations_perm) + np.sum(mono_anions_in * mono_anions_perm)) /
        (np.sum(mono_cations_in * mono_cations_perm) + np.sum(mono_anions_out * mono_anions_perm))
    )

