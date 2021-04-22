# Biomedical Signal Processing

This project encapsulates some small projects developed in the course [PTC3456 - Biomedical Signals Processing](https://uspdigital.usp.br/jupiterweb/obterDisciplina?nomdis=&sgldis=PTC3456). Each on aims to give some elucidation and simulate the human body and its signals.

The available projects are:

- [Nernst Equation](https://github.com/gabrielriqu3ti/biomedical_signal_processing/#nernst_equation)
- [Goldman Equation](https://github.com/gabrielriqu3ti/biomedical_signal_processing/#goldman_equation)

## Nernst Equation

The **Nernst Equation** allows us to calculate the equilibrium potential for a given ion separated by a phospholipid membrane with ion channels selectively permeable to that ion and is given by:

<img src="https://latex.codecogs.com/svg.latex?\Large&space;E_{ion} = \frac{RT}{zF} \ln{\frac{[ion]_{out}}{[ion]_{in}}}" title="\Large E_{ion} = \frac{RT}{zF} \ln{\frac{[ion]_{out}}{[ion]_{in}}}" />

<img src="https://latex.codecogs.com/svg.image?\inline&space;E_{ion}&space;=&space;\frac{RT}{zF}&space;\ln{\frac{[ion]_{out}}{[ion]_{in}}}" title="\inline E_{ion} = \frac{RT}{zF} \ln{\frac{[ion]_{out}}{[ion]_{in}}}" />

where:

- E_ion     = ionic equilibrium potential
- R         = gas constant
- T         = absolute temperature
- z         = charge of that ion
- F         = Faraday's constant
- ln        = natural logarithm
- [ion]out  = concentration of the ion outside the cell
- [ion]in   = concentration of the ion inside the cell

The **equilibrium potential** is the electrical potential difference that exactly balances an **ionic concentration gradient**.

## Tools

#### The ionic equilibrium for a human neuron

The equilibrium potential and the ionic concentration of ions in a human neuron are displayed by running the following code:

```
python human_neuron_equilibrium.py
```

#### App

To calculate the equilibrium potential of an ion for a specific setting, run:

```
python nernst_app.py
```

#### The ionic equilibrium for an exercise of the course PTC3456

The equilibrium potential and the ionic concentration of ions in the exercise are displayed by running the following code:

```
python ex_nernst_equation.py
```

## Goldman Equation

The **Goldman Equation** allows us to calculate the resting membrane potential for a given set of monovalent ions separated by a phospholipid membrane with ion channels selectively permeable to these ions and is given by:

<img src="https://latex.codecogs.com/svg.latex?\Large&space;E_{R} = \frac{RT}{F} \ln{\frac{\sum{P_{cation_i} [cation]_{out_i}} + \sum{P_{anion_i} [anion]_{in_i}}}{\sum{P_{cation_i} [cation]_{in_i}} + \sum{P_{anion_i} [anion]_{out_i}}}}" title="\Large E_{R} = \frac{RT}{F} \ln{\frac{\sum{P_{cation_i} [cation]_{out_i}} + \sum{P_{anion_i} [anion]_{in_i}}}{\sum{P_{cation_i} [cation]_{in_i}} + \sum{P_{anion_i} [anion]_{out_i}}}}" />
![\Large E_{R} = \frac{RT}{F} \ln{\frac{\sum{P_{cation_i} [cation]_{out_i}} + \sum{P_{anion_i} [anion]_{in_i}}}{\sum{P_{cation_i} [cation]_{in_i}} + \sum{P_{anion_i} [anion]_{out_i}}}}](https://latex.codecogs.com/svg.latex?x%3D%5Cfrac%7B-b%5Cpm%5Csqrt%7Bb%5E2-4ac%7D%7D%7B2a%7D)
where:

<img src="https://latex.codecogs.com/svg.image?\inline&space;E_{R}&space;=&space;\frac{RT}{F}&space;\ln{\frac{\sum{P_{cation_i}&space;[cation]_{out_i}}&space;&plus;&space;\sum{P_{anion_i}&space;[anion]_{in_i}}}{\sum{P_{cation_i}&space;[cation]_{in_i}}&space;&plus;&space;\sum{P_{anion_i}&space;[anion]_{out_i}}}}" title="\inline E_{R} = \frac{RT}{F} \ln{\frac{\sum{P_{cation_i} [cation]_{out_i}} + \sum{P_{anion_i} [anion]_{in_i}}}{\sum{P_{cation_i} [cation]_{in_i}} + \sum{P_{anion_i} [anion]_{out_i}}}}" />

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
python goldman_app.py
```
