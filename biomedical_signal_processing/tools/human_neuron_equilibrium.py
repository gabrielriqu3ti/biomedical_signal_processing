# -*- coding: utf-8 -*-
"""
Created on Tue Apr 21 14:09:51 2021

@author: Gabriel H Riqueti
"""

from biomedical_signal_processing import ABSOLUTE_TEMPERATURE_CELSIUS as T0
from biomedical_signal_processing import Nernst_equation, Goldman_equation

import numpy as np
import pandas as pd


def main():
    T = 37  # Celsius

    K_in = 100  # mM
    K_out = 5  # mM

    Na_in = 15  # mM
    Na_out = 150  # mM

    Cl_in = 13  # mM
    Cl_out = 150  # mM

    z_K = 1
    z_Na = 1
    z_Cl = -1

    K_perm = 1
    Na_perm = 0.025
    Cl_perm = 0.45

    ions = pd.Series(['K+', 'Na+', 'Cl-'])
    ions_in = pd.Series([K_in, Na_in, Cl_in], index=ions)
    ions_out = pd.Series([K_out, Na_out, Cl_out], index=ions)
    z_ions = pd.Series([z_K, z_Na, z_Cl], index=ions)
    perm_ions = pd.Series([K_perm, Na_perm, Cl_perm], index=ions)

    df = pd.DataFrame({'[Ion]in (mM)': ions_in, '[Ion]out (mM)': ions_out, 'Valence': z_ions, 'Relative Permeability to K+' : perm_ions})
    df['E_r (mV)'] = 1000 * Nernst_equation(T - T0, df['Valence'], df['[Ion]in (mM)'], df['[Ion]out (mM)'])

    mono_cations_in = np.array([K_in, Na_in], dtype=np.float32)
    mono_cations_out = np.array([K_out, Na_out], dtype=np.float32)
    mono_cations_perm = np.array([K_perm, Na_perm], dtype=np.float32)
    mono_anions_in = np.array([Cl_in], dtype=np.float32)
    mono_anions_out = np.array([Cl_out], dtype=np.float32)
    mono_anions_perm = np.array([Cl_perm], dtype=np.float32)

    E_r = Goldman_equation(T - T0, mono_cations_in, mono_cations_out, mono_cations_perm, mono_anions_in, mono_anions_out, mono_anions_perm)

    print(f'Approximate concentrations and ionic equilibrium potentials for a human neuron (at {T} Celsius):')
    print()
    print(df)
    print()
    print(f'Resting membrane potential = {1000 * E_r} mV')


if __name__ == '__main__':
    main()
