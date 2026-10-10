## [Modal_Split_based_on_Travel_expenses_and_Time_in_and_out_of_vehicle.py](https://github.com/shreyanspeaking-arch/Traffic-Engineering-Problems/blob/Modal-Split-Analysis/Modal_Split_based_on_Travel_expenses_and_Time_in_and_out_of_vehicle.py)
1. This program estimates the modal split among competing modes of transport using a multinomial logit model based on user defined utility functions of in vehicle time, out of vehicle time, and travel expenses.
2. For each mode, the user enters a utility function with numeric coefficients for in vehicle time, out of vehicle time, and travel cost, along with the actual time and cost components that make up each variable.
3. The program computes each mode's utility, converts it to a probability share using the logit formula, and normalizes these shares across all modes.
4. The user then chooses to either estimate ridership on each mode from a known total number of commuters, or to estimate ridership and vehicle counts on each mode from a known vehicle capacity, headway, and percentage of capacity filled for one reference mode, combined with a given modal split ratio and the average occupancy of each other mode.

## [Predicting_Change_in_Modal_Split_due_to_a_new_contribution.py](https://github.com/shreyanspeaking-arch/Traffic-Engineering-Problems/blob/Modal-Split-Analysis/Predicting_Change_in_Modal_Split_due_to_a_new_contribution.py)
1. This program predicts the change in modal split and ridership between an origin and destination due to an infrastructure change, using a multinomial logit model based on user defined utility functions of cost and travel time for each mode.
2. The user specifies whether any mode of transport was added or removed by the change, and enters the number of commuters, along with a utility function, cost, and travel time for each mode before the change.
3. The program computes each mode's probability share and estimated ridership before the change, using the logit formula.
4. The user then enters the modes remaining after the change, along with updated cost and travel time for each surviving mode, and provides a name and utility function for any newly added mode, or removes any discontinued mode by name. Only one newly added mode is currently supported per run, since the program does not yet accumulate more than one new mode's name and utility function when multiple modes are added at once.
5. The program recomputes probability shares and ridership after the change, and reports the increase or decrease in the number of commuters using each mode common to both periods.

## [Use_of_Multinomial_Logit_Model_for_the_Estimation_of_Modal_Split.py](https://github.com/shreyanspeaking-arch/Traffic-Engineering-Problems/blob/Modal-Split-Analysis/Use_of_Multinomial_Logit_Model_for_the_Estimation_of_Modal_Split.py)
1. This program estimates the modal split between an origin and destination using a multinomial logit model based on user defined utility functions of cost and travel time for each mode of transport.
2. The user enters the number of commuters, the number of available modes, and for each mode, a name and a utility function expressed in terms of cost and travel time.
3. The user then enters the actual cost and travel time for each mode, and the program evaluates each mode's utility and converts it into a probability share using the logit formula, normalized across all modes.
4. The program reports the probability of commuters choosing each mode and the corresponding estimated number of commuters using that mode between the given origin and destination.
