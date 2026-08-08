Gravity_Model.py:
1. This program estimates the distribution of trips from a single origin zone to all other zones in a network, using a singly constrained gravity model with a power function cost deterrence factor, based on generalised travel cost expressed in time.
2. The user enters the number of zones, the origin zone, and a modal deterrence parameter (alpha) governing the sensitivity of trips to travel cost.
3. For every zone other than the origin, the user enters the generalised cost of travel from the origin to that zone, along with the productions and attractions for each zone.
4. The program computes each zone's travel impedance as its generalised cost raised to the power of negative alpha, and distributes the origin zone's productions to all other zones in proportion to their attractions weighted by this impedance, relative to the total weighted attractiveness of all zones. Results are exported to an Excel file.

Greenberg_Model.py:
1. This program models a highway traffic stream using the Greenberg speed density model, computing capacity and plotting the corresponding speed density and speed volume relationships.
2. The user enters the model's speed as a function of density, in the form of a natural logarithm expression involving traffic density K.
3. The program solves this expression for the jam density, and evaluates the model at the density corresponding to maximum flow to obtain the optimum speed.
4. The program computes and reports the roadway's capacity as the product of the optimum density and optimum speed, and plots speed against density and speed against volume over the full range of densities from just above zero up to jam density.
For sample output containing the graphs it can generate, check Speed-Density and Speed-Volume Relationships Using Greenberg Model.png

Greenshields_Model.py:
1. This program models a highway traffic stream using the Greenshields speed density model, computing capacity and plotting the corresponding speed density and speed volume relationships.
2. The user enters the model's speed as a linear function of density, in the form of a straight line expression involving traffic density K.
3. The program solves this expression for the free flow speed and the jam density, then derives the flow density relationship and finds the optimum speed at which flow is maximised.
4. The program computes and reports the roadway's capacity as the product of the optimum density and optimum speed, and plots speed against density and speed against volume over the full range of densities from zero up to jam density.
