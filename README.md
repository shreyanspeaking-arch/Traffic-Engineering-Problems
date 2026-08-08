LOS_Estimation_Under_Ideal_Conditions_using_the_method_prescribed_by_Transportation_Research_Board_for_Multilane_Highways.py:

1. This program estimates the Level of Service of a multilane highway under ideal conditions, using capacity and volume to capacity ratio tables prescribed by the Transportation Research Board.
2. The program reads Table1.csv, containing the capacity of a standard highway lane in vehicles per hour for design speeds of 50, 60 and 70 mi/h, and Table2.csv, containing the volume to capacity ratio thresholds for each Level of Service at these design speeds.
3. The user enters the total number of lanes, peak hour volume, peak hour factor, and design speed, from which the directional service flow rate and applicable lane capacity, read from Table1, are determined.
4. The program computes the volume to capacity ratio for the highway and compares it against the standard thresholds for each Level of Service, read from Table2, at the given design speed.
5. The program reports the resulting Level of Service, ranging from A through F, based on where the computed ratio falls among these thresholds.

LOS_Estimation_Under_Non_Ideal_Conditions_using_the_method_prescribed_by_Transportation_Research_Board_for_Multilane_Highways.py:

1. This program estimates the Level of Service of a multilane highway under non ideal conditions, applying correction factors from several reference tables to the standard capacity and volume to capacity ratio tables prescribed by the Transportation Research Board.
2. The program reads Table1.csv for lane capacity at each design speed and Table2.csv for the volume to capacity ratio thresholds for each Level of Service, the same base tables used in the ideal conditions program.
3. The program also reads Table_5_3_Correction_Factors.csv, giving correction factors for lane width and obstruction clearance from the travelled edge, Table_5_4_PCE_Heavy_Vehicles.csv, giving passenger car equivalents for trucks, buses and recreational vehicles across level, rolling and mountainous terrain, and Table_5_5_Highway_Environment_Correction_Factors.csv, giving correction factors based on highway classification as rural or urban and divided or undivided.
4. The user enters the total number of lanes, peak hour volume, peak hour factor, design speed, lane width, obstruction clearance, terrain type, percentage of heavy vehicles, driver population, and highway classification.
5. The program derives correction factors from Table_5_3, Table_5_4 and Table_5_5, along with a heavy vehicle adjustment factor computed from the entered percentages, and applies them together to adjust the highway's effective capacity, read from Table1.
6. The program computes the corrected volume to capacity ratio and reports the resulting Level of Service, ranging from A through F, based on where this ratio falls among the standard thresholds from Table2 for the given design speed.
