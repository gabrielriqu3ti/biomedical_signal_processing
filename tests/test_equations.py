# -*- coding: utf-8 -*-
##
# @file test_equations.py
# @brief Automatically test equations of the biomedical_signal_processing library
# @author Gabriel H Riqueti
# @email gabrielhriqueti@gmail.com
# @date 06/05/2021
#

import numpy as np
from biomedical_signal_processing import nernst_equation, goldman_equation
from biomedical_signal_processing import ABSOLUTE_TEMPERATURE_CELSIUS


class TestNernstEquation:
    def test_nernst_equation_temperature_0K(self):

        temperature = 0
        valence = 1
        ion_in = 10
        ion_out = 1

        assert np.isclose(nernst_equation(temperature, valence, ion_in, ion_out), 0)

    def test_nernst_equation_valence_0(self):

        temperature = - ABSOLUTE_TEMPERATURE_CELSIUS
        valence = 0
        ion_in = 10
        ion_out = 1

        assert np.isclose(nernst_equation(temperature, valence, ion_in, ion_out), 0)

    def test_nernst_equation_ion_in_equal_to_ion_out(self):

        temperature = - ABSOLUTE_TEMPERATURE_CELSIUS
        valence = 1
        ion_in = 1
        ion_out = 1

        assert np.isclose(nernst_equation(temperature, valence, ion_in, ion_out), 0)

    def test_nernst_equation_valence_odd_symmetry(self):

        temperature = - ABSOLUTE_TEMPERATURE_CELSIUS
        valence = 1
        ion_in = 10
        ion_out = 1

        assert np.isclose(nernst_equation(temperature, valence, ion_in, ion_out),
                          - nernst_equation(temperature, - valence, ion_in, ion_out))

    def test_nernst_equation_inversion_ion_in_ion_out_change_signal(self):

        temperature = - ABSOLUTE_TEMPERATURE_CELSIUS
        valence = 1
        ion_in = 10
        ion_out = 1

        assert np.isclose(nernst_equation(temperature, valence, ion_in, ion_out),
                          - nernst_equation(temperature, valence, ion_out, ion_in))

    def test_nernst_equation_human_neuron_potassium_equilibrium_potential(self):

        temperature = 37 - ABSOLUTE_TEMPERATURE_CELSIUS
        valence = 1
        ion_in = 100
        ion_out = 5

        assert np.isclose(nernst_equation(temperature, valence, ion_in, ion_out), - 80 * 1e-3, atol=1e-3)

    def test_nernst_equation_human_neuron_sodium_equilibrium_potential(self):

        temperature = 37 - ABSOLUTE_TEMPERATURE_CELSIUS
        valence = 1
        ion_in = 15
        ion_out = 150

        assert np.isclose(nernst_equation(temperature, valence, ion_in, ion_out), 62 * 1e-3, atol=1e-3)

    def test_nernst_equation_human_neuron_calcium_equilibrium_potential(self):

        temperature = 37 - ABSOLUTE_TEMPERATURE_CELSIUS
        valence = 2
        ion_in = 0.0002
        ion_out = 2

        assert np.isclose(nernst_equation(temperature, valence, ion_in, ion_out), 123 * 1e-3, atol=1e-3)

    def test_nernst_equation_human_neuron_cloride_equilibrium_potential(self):

        temperature = 37 - ABSOLUTE_TEMPERATURE_CELSIUS
        valence = - 1
        ion_in = 13
        ion_out = 150

        assert np.isclose(nernst_equation(temperature, valence, ion_in, ion_out), - 65 * 1e-3, atol=1e-3)

    def test_nernst_equation_human_neuron_equilibrium_potential_numpy_array(self):

        temperature = 37 - ABSOLUTE_TEMPERATURE_CELSIUS
        valence = np.array([1, 1, 2, -1])
        ion_in = np.array([100, 15, 0.0002, 13])
        ion_out = np.array([5, 150, 2, 150])

        assert np.isclose(nernst_equation(temperature, valence, ion_in, ion_out), np.array([-80, 62, 123, -65]) * 1e-3, atol=1e-3).all()

    def test_nernst_equation_human_neuron_equilibrium_potential_numpy_array_temperature_0(self):

        temperature = 0
        valence = np.array([1, 1, 2, -1])
        ion_in = np.array([100, 15, 0.0002, 13])
        ion_out = np.array([5, 150, 2, 150])

        assert np.isclose(nernst_equation(temperature, valence, ion_in, ion_out), np.array([0, 0, 0, 0])).all()

    def test_nernst_equation_human_neuron_equilibrium_potential_numpy_array_valence_0(self):

        temperature = 37 - ABSOLUTE_TEMPERATURE_CELSIUS
        valence = np.array([1, 1, 2, -1, 0])
        ion_in = np.array([100, 15, 0.0002, 13, 10])
        ion_out = np.array([5, 150, 2, 150, 1])

        assert np.isclose(nernst_equation(temperature, valence, ion_in, ion_out), np.array([-80, 62, 123, -65, 0]) * 1e-3, atol=1e-3).all()

    def test_nernst_equation_human_neuron_equilibrium_potential_numpy_array_ion_in_equals_ion_out(self):

        temperature = 37 - ABSOLUTE_TEMPERATURE_CELSIUS
        valence = np.array([1, 1, 2, -1, 1])
        ion_in = np.array([100, 15, 0.0002, 13, 10])
        ion_out = np.array([5, 150, 2, 150, 10])

        assert np.isclose(nernst_equation(temperature, valence, ion_in, ion_out), np.array([-80, 62, 123, -65, 0]) * 1e-3, atol=1e-3).all()

    def test_nernst_equation_negative_temperature_assert_ValueError(self):

        temperature = - 1
        valence = 1
        ion_in = 10
        ion_out = 1

        try:
            _ = nernst_equation(temperature, valence, ion_in, ion_out)
        except ValueError:
            return

        raise ValueError('nernst_equation should have raised ValueError')

    def test_nernst_equation_negative_ion_in_assert_ValueError(self):

        temperature = 37 - ABSOLUTE_TEMPERATURE_CELSIUS
        valence = 1
        ion_in = - 10
        ion_out = 1

        try:
            _ = nernst_equation(temperature, valence, ion_in, ion_out)
        except ValueError:
            return

        raise ValueError('nernst_equation should have raised ValueError')

    def test_nernst_equation_ion_in_0_assert_ValueError(self):

        temperature = 37 - ABSOLUTE_TEMPERATURE_CELSIUS
        valence = 1
        ion_in = 0
        ion_out = 1

        try:
            _ = nernst_equation(temperature, valence, ion_in, ion_out)
        except ValueError:
            return

        raise ValueError('nernst_equation should have raised ValueError')

    def test_nernst_equation_ion_out_0_assert_ValueError(self):

        temperature = 37 - ABSOLUTE_TEMPERATURE_CELSIUS
        valence = 1
        ion_in = 10
        ion_out = - 1

        try:
            _ = nernst_equation(temperature, valence, ion_in, ion_out)
        except ValueError:
            return

        raise ValueError('nernst_equation should have raised ValueError')


class TestGoldmanEquation:
    def test_goldman_equation_temperature_0K(self):

        temperature = 0
        mono_cations_in = np.array([10])
        mono_cations_out = np.array([1])
        mono_cations_perm = np.array([1])
        mono_anions_in = np.array([2])
        mono_anions_out = np.array([10])
        mono_anions_perm = np.array([0.4])

        assert np.isclose(goldman_equation(temperature, mono_cations_in, mono_cations_out, mono_cations_perm,
                                           mono_anions_in, mono_anions_out, mono_anions_perm),
                          0)

    def test_goldman_equation_equilibrium_cations_anions(self):

        temperature = 37 - ABSOLUTE_TEMPERATURE_CELSIUS
        mono_cations_in = np.array([10])
        mono_cations_out = np.array([1])
        mono_cations_perm = np.array([1])
        mono_anions_in = np.array([10])
        mono_anions_out = np.array([1])
        mono_anions_perm = np.array([1])

        assert np.isclose(goldman_equation(temperature, mono_cations_in, mono_cations_out, mono_cations_perm,
                                           mono_anions_in, mono_anions_out, mono_anions_perm),
                          0)

    def test_goldman_equation_equilibrium_2_cations_0_anions(self):

        temperature = 37 - ABSOLUTE_TEMPERATURE_CELSIUS
        mono_cations_in = np.array([10, 1])
        mono_cations_out = np.array([1, 10])
        mono_cations_perm = np.array([1, 1])
        mono_anions_in = np.array([])
        mono_anions_out = np.array([])
        mono_anions_perm = np.array([])

        assert np.isclose(goldman_equation(temperature, mono_cations_in, mono_cations_out, mono_cations_perm,
                                           mono_anions_in, mono_anions_out, mono_anions_perm),
                          0)

    def test_goldman_equation_equilibrium_0_cations_2_anions(self):

        temperature = 37 - ABSOLUTE_TEMPERATURE_CELSIUS
        mono_cations_in = np.array([])
        mono_cations_out = np.array([])
        mono_cations_perm = np.array([])
        mono_anions_in = np.array([10, 1])
        mono_anions_out = np.array([1, 10])
        mono_anions_perm = np.array([1, 1])

        assert np.isclose(goldman_equation(temperature, mono_cations_in, mono_cations_out, mono_cations_perm,
                                           mono_anions_in, mono_anions_out, mono_anions_perm),
                          0)

    def test_goldman_equation_equilibrium_2_cations_1_anions(self):

        temperature = 37 - ABSOLUTE_TEMPERATURE_CELSIUS
        mono_cations_in = np.array([5, 5])
        mono_cations_out = np.array([1, 1])
        mono_cations_perm = np.array([1, 1])
        mono_anions_in = np.array([10])
        mono_anions_out = np.array([2])
        mono_anions_perm = np.array([1])

        assert np.isclose(goldman_equation(temperature, mono_cations_in, mono_cations_out, mono_cations_perm,
                                           mono_anions_in, mono_anions_out, mono_anions_perm),
                          0)

    def test_goldman_equation_equilibrium_1_cations_2_anions(self):

        temperature = 37 - ABSOLUTE_TEMPERATURE_CELSIUS
        mono_cations_in = np.array([10])
        mono_cations_out = np.array([2])
        mono_cations_perm = np.array([1])
        mono_anions_in = np.array([5, 5])
        mono_anions_out = np.array([1, 1])
        mono_anions_perm = np.array([1, 1])

        assert np.isclose(goldman_equation(temperature, mono_cations_in, mono_cations_out, mono_cations_perm,
                                           mono_anions_in, mono_anions_out, mono_anions_perm),
                          0)

    def test_goldman_equation_human_neuron_potassium_equilibrium_potential(self):

        temperature = 37 - ABSOLUTE_TEMPERATURE_CELSIUS
        mono_cations_in = np.array([100])
        mono_cations_out = np.array([5])
        mono_cations_perm = np.array([1])
        mono_anions_in = np.array([])
        mono_anions_out = np.array([])
        mono_anions_perm = np.array([])

        assert np.isclose(goldman_equation(temperature, mono_cations_in, mono_cations_out, mono_cations_perm,
                                           mono_anions_in, mono_anions_out, mono_anions_perm),
                          - 80 * 1e-3, atol=1e-3)

    def test_goldman_equation_human_neuron_sodium_equilibrium_potential(self):

        temperature = 37 - ABSOLUTE_TEMPERATURE_CELSIUS
        mono_cations_in = np.array([15])
        mono_cations_out = np.array([150])
        mono_cations_perm = np.array([1])
        mono_anions_in = np.array([])
        mono_anions_out = np.array([])
        mono_anions_perm = np.array([])

        assert np.isclose(goldman_equation(temperature, mono_cations_in, mono_cations_out, mono_cations_perm,
                                           mono_anions_in, mono_anions_out, mono_anions_perm),
                          62 * 1e-3, atol=1e-3)

    def test_goldman_equation_human_neuron_cloride_equilibrium_potential(self):

        temperature = 37 - ABSOLUTE_TEMPERATURE_CELSIUS
        mono_cations_in = np.array([])
        mono_cations_out = np.array([])
        mono_cations_perm = np.array([])
        mono_anions_in = np.array([13])
        mono_anions_out = np.array([150])
        mono_anions_perm = np.array([1])

        assert np.isclose(goldman_equation(temperature, mono_cations_in, mono_cations_out, mono_cations_perm,
                                           mono_anions_in, mono_anions_out, mono_anions_perm),
                          - 65 * 1e-3, atol=1e-3)

    def test_goldman_equation_human_neuron_potassium_sodium_equilibrium_potential(self):

        temperature = 37 - ABSOLUTE_TEMPERATURE_CELSIUS
        mono_cations_in = np.array([100, 15])
        mono_cations_out = np.array([5, 150])
        mono_cations_perm = np.array([1, 0.025])
        mono_anions_in = np.array([])
        mono_anions_out = np.array([])
        mono_anions_perm = np.array([])

        assert np.isclose(goldman_equation(temperature, mono_cations_in, mono_cations_out, mono_cations_perm,
                                           mono_anions_in, mono_anions_out, mono_anions_perm),
                          - 65 * 1e-3, atol=1e-3)

    def test_goldman_equation_human_neuron_potassium_sodium_cloride_equilibrium_potential(self):

        temperature = 37 - ABSOLUTE_TEMPERATURE_CELSIUS
        mono_cations_in = np.array([100, 15])
        mono_cations_out = np.array([5, 150])
        mono_cations_perm = np.array([1, 0.025])
        mono_anions_in = np.array([13])
        mono_anions_out = np.array([150])
        mono_anions_perm = np.array([0.45])

        assert np.isclose(goldman_equation(temperature, mono_cations_in, mono_cations_out, mono_cations_perm,
                                           mono_anions_in, mono_anions_out, mono_anions_perm),
                          - 65 * 1e-3, atol=1e-3)

    def test_goldman_equation_0_ions(self):

        temperature = 37 - ABSOLUTE_TEMPERATURE_CELSIUS
        mono_cations_in = np.array([])
        mono_cations_out = np.array([])
        mono_cations_perm = np.array([])
        mono_anions_in = np.array([])
        mono_anions_out = np.array([])
        mono_anions_perm = np.array([])

        assert np.isclose(goldman_equation(temperature, mono_cations_in, mono_cations_out, mono_cations_perm,
                                           mono_anions_in, mono_anions_out, mono_anions_perm),
                          0)
