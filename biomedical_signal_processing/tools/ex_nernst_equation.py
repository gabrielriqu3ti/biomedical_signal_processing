# -*- coding: utf-8 -*-
"""
Created on Tue Apr 20 14:09:51 2021

@author: Gabriel H Riqueti
"""

from constant import ABSOLUTE_TEMPERATURE_CELSIUS as T0
from nernst_equation import Nernst_equation

import pandas as pd


def main():
    
    T = 25  # Celsius
    
    K_in = 400  # mM
    K_out = 20  # mM
    
    Na_in = 50  # mM
    Na_out = 440    # mM
    
    Cl_in = 52  # mM
    Cl_out = 560    # mM
    
    z_K = 1
    z_Na = 1
    z_Cl = -1
    
    ions = pd.Series(['K+', 'Na+', 'Cl-'])
    ions_in = pd.Series([K_in, Na_in, Cl_in], index=ions)
    ions_out = pd.Series([K_out, Na_out, Cl_out], index=ions)
    z_ions = pd.Series([z_K, z_Na, z_Cl], index=ions)
    
    df = pd.DataFrame({'[Ion]in (mM)' : ions_in, '[Ion]out (mM)' : ions_out, 'Valence' : z_ions})
    df['E_r (mV)'] = 1000 * Nernst_equation(T - T0, df['Valence'], df['[Ion]in (mM)'], df['[Ion]out (mM)'])
    
    print(f'Ionic Equilibrium Potentials at {T} Celsius')
    print()
    print(df)
    

if __name__ == '__main__':
    main()
