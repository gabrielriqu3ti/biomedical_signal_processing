# -*- coding: utf-8 -*-
"""
Created on Tue Apr 21 14:09:51 2021

@author: Gabriel H Riqueti
"""

from constant import ABSOLUTE_TEMPERATURE_CELSIUS as T0
from nernst_equation import Nernst_equation

import pandas as pd


def main():
    T = 37  # Celsius

    K_in = 100  # mM
    K_out = 5  # mM

    Na_in = 15  # mM
    Na_out = 150  # mM

    Ca_in = 0.0002  # mM
    Ca_out = 2  # mM

    Cl_in = 13  # mM
    Cl_out = 150  # mM

    z_K = 1
    z_Na = 1
    z_Ca = 2
    z_Cl = -1

    ions = pd.Series(['K+', 'Na+', 'Ca++', 'Cl-'])
    ions_in = pd.Series([K_in, Na_in, Ca_in, Cl_in], index=ions)
    ions_out = pd.Series([K_out, Na_out, Ca_out, Cl_out], index=ions)
    z_ions = pd.Series([z_K, z_Na, z_Ca, z_Cl], index=ions)

    df = pd.DataFrame({'[Ion]in (mM)': ions_in, '[Ion]out (mM)': ions_out, 'Valence': z_ions})
    df['E_r (mV)'] = 1000 * Nernst_equation(T - T0, df['Valence'], df['[Ion]in (mM)'], df['[Ion]out (mM)'])

    print(f'Approximate concentrations and ionic equilibrium potentials for a human neuron (at {T} Celsius):')
    print()
    print(df)


if __name__ == '__main__':
    main()
