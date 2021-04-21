# Nernst Equation

The **Nernst Equation** allows us to calculate the equilibrium potential for a given ion separated by a phospholipid membrane with ion channels selectively permeable to that ion and is given by:

<img src="https://render.githubusercontent.com/render/math?math=E_{ion} = \frac{RT}{zF} \ln{\frac{[ion]_{out}}{[ion]_{in}}}">

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
python app.py
```

#### The ionic equilibrium for an exercise of the course PTC3456

The equilibrium potential and the ionic concentration of ions in the exercise are displayed by running the following code:

```
python ex_nernst_equation.py
```