# -*- coding: utf-8 -*-
##
# @file ex_nernst_equation.py
# @author Gabriel H Riqueti
# @email gabrielhriqueti@gmail.com
# @date 20/04/2021
# @brief Calculates the equilibrium potential for a given set of concentrations
#
# @details The equilibrium potentials are calculated for an excitable membrane at 25 Celsius with concentrations of
#          potassium inside the cell of 400 mM, potassium outside the cell of 20 mM, sodium inside the cell of 50 mM,
#          sodium outside the cell of 440 mM, cloride inside the cell of 52 mM and cloride outside the cell of 560 mM.
#

from biomedical_signal_processing import ABSOLUTE_TEMPERATURE_CELSIUS as T0
from biomedical_signal_processing import nernst_equation

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
    df['E_r (mV)'] = 1000 * nernst_equation(T - T0, df['Valence'], df['[Ion]in (mM)'], df['[Ion]out (mM)'])
    
    print(f'Ionic Equilibrium Potentials at {T} Celsius')
    print()
    print(df)
    

if __name__ == '__main__':
    main()
