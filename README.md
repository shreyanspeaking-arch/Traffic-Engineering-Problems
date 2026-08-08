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

For sample output containing the graphs it can generate, check Speed-Density and Speed-Volume Relationships Using Greenshield' s Model.png

Modal_Split_based_on_Travel_expenses_and_Time_in_and_out_of_vehicle.py:
1. This program estimates the modal split among competing modes of transport using a multinomial logit model based on user defined utility functions of in vehicle time, out of vehicle time, and travel expenses.
2. For each mode, the user enters a utility function with numeric coefficients for in vehicle time, out of vehicle time, and travel cost, along with the actual time and cost components that make up each variable.
3. The program computes each mode's utility, converts it to a probability share using the logit formula, and normalizes these shares across all modes.
4. The user then chooses to either estimate ridership on each mode from a known total number of commuters, or to estimate ridership and vehicle counts on each mode from a known vehicle capacity, headway, and percentage of capacity filled for one reference mode, combined with a given modal split ratio and the average occupancy of each other mode.

Predicting_Change_in_Modal_Split_due_to_a_new_contribution.py:
1. This program predicts the change in modal split and ridership between an origin and destination due to an infrastructure change, using a multinomial logit model based on user defined utility functions of cost and travel time for each mode.
2. The user specifies whether any mode of transport was added or removed by the change, and enters the number of commuters, along with a utility function, cost, and travel time for each mode before the change.
3. The program computes each mode's probability share and estimated ridership before the change, using the logit formula.
4. The user then enters the modes remaining after the change, along with updated cost and travel time for each surviving mode, and provides a name and utility function for any newly added mode, or removes any discontinued mode by name. Only one newly added mode is currently supported per run, since the program does not yet accumulate more than one new mode's name and utility function when multiple modes are added at once.
5. The program recomputes probability shares and ridership after the change, and reports the increase or decrease in the number of commuters using each mode common to both periods.
