Gravity_Model.py:
1. This program estimates the distribution of trips from a single origin zone to all other zones in a network, using a singly constrained gravity model with a power function cost deterrence factor, based on generalised travel cost expressed in time.
2. The user enters the number of zones, the origin zone, and a modal deterrence parameter (alpha) governing the sensitivity of trips to travel cost.
3. For every zone other than the origin, the user enters the generalised cost of travel from the origin to that zone, along with the productions and attractions for each zone.
4. The program computes each zone's travel impedance as its generalised cost raised to the power of negative alpha, and distributes the origin zone's productions to all other zones in proportion to their attractions weighted by this impedance, relative to the total weighted attractiveness of all zones. Results are exported to an Excel file.

