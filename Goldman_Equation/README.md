# Goldman Equation

The **Goldman Equation** allows us to calculate the resting membrane potential for a given set of monovalent ions separated by a phospholipid membrane with ion channels selectively permeable to these ions and is given by:

<img src="https://render.githubusercontent.com/render/math?math=E_{ion} = \frac{RT}{F} \ln{\frac{\sum{P_{cation_i} [cation]_{out_i}} + \sum{P_{anion_i} [anion]_{in_i}}}{\sum{P_{cation_i} [cation]_{in_i}} + \sum{P_{anion_i} [anion]_{out_i}}}}">

where:

- E_ion     = ionic equilibrium potential
- R         = gas constant
- T         = absolute temperature
- z         = charge of that ion
- F         = Faraday's constant
- ln        = natural logarithm
- [cation]out  = concentration of the monovalent cation outside the cell
- [cation]in   = concentration of the monovalent cation inside the cell
- P_cation   = relative permeability of the cell membrane to the monovalent cation in relation to an ion
- [anion]out  = concentration of the monovalent anion outside the cell
- [anion]in   = concentration of the monovalent anion inside the cell
- P_anion   = relative permeability of the cell membrane to the monovalent anion in relation to an ion

The **resting membrane potential** is the electrical potential difference across an membrane not conducting **action potentials**.

## Tools

#### The resting potential for a human neuron

The resting potential and the ionic concentration of ions in a human neuron are displayed by running the following code:

```
python human_neuron_equilibrium.py
```

#### App

To calculate the equilibrium potential of an ion for a specific setting, run:

```
python app.py
```
