D_D_1_Queuing_Model.py:
  1. This program analyzes a deterministic D/D/1 queue at a single service point, using Kendall's notation where the first D denotes deterministic (fixed, non random) arrivals, the second D denotes deterministic departures or service times, and 1 denotes a single server or service channel. It computes queue dissipation time, maximum queue length, total vehicles served, average delay per vehicle, and average queue length, and plots cumulative arrivals and departures against time.
  2. The user enters the number of instances at which the departure rate and the arrival rate change, along with the time, and either the average headway or the rate itself, at each change point, plus any vehicles already queued at the start of the study.
  3. The program constructs piecewise linear cumulative arrival and departure curves from these rates, with the initial queue reflected as a starting offset in the arrival curve, solves for the time at which the two curves meet to determine when the queue dissipates, and evaluates the queue length at each rate change to find the maximum.
  4. The program computes total delay as the area between the arrival and departure curves, derives average delay per vehicle and average queue length from it, and plots both cumulative curves over the full study period.

A sample graph created by this program of No. of Vehicles vs Time has been shown in the file Cumulative_No_of_vehicles_stuck_in_a_queue_vs_Time_Graph_for_D_D_1_Queuing_Analysis.png. Check the commit history for the sample input.

Deterministic_Queuing_Analysis.py:
1. This program analyzes deterministic queue buildup and dissipation over a series of time intervals with varying arrival and departure rates, either entered manually or read from a CSV or Excel file.
2. For each interval, the user provides the arrival and departure rates, either as totals or per lane, along with the number of lanes if applicable, and the program computes the number of vehicles arriving and departing, and the resulting queue size at the end of each interval.
3. If the queue is found to clear before the final recorded interval, the program truncates the analysis at that point. Otherwise, assuming constant rates continue beyond the last recorded interval, the program extrapolates forward to estimate the exact time the queue fully dissipates.
4. The program reports the queue clearance time, exports the interval by interval results to an Excel file, and plots the size of the queue over time from the start of the study through to its dissipation.

There are 3 sample inputs/outputs of this program which are:
1. scenario_1_same_day_veh_h_ln.csv → output6.xlsx + Size of Queue vs End Time 1.png
2. scenario_2_multiday_arr_veh_h.csv → output7.xlsx + Size of Queue vs End Time 2.png
3. scenario_3_sameday_both_veh_h.csv → output8.xlsx + Size of Queue vs End Time 3.png

