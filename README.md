Calibration_and_graph_of_Daily_and_Monthly_Variation_Factors.py:

1. This program calibrates daily and monthly traffic variation factors from a dataset of daily vehicle volumes, and uses them to estimate Average Annual Daily Traffic and Annual Vehicle Miles Travelled for a road segment.
2. The program reads a CSV or Excel file of dates and vehicle volumes, computes the average volume for each day of the week and each month of the year, and derives a Daily Adjustment Factor and a Monthly Adjustment Factor for each, based on their ratio to the overall average.
3. The user can optionally estimate Average Annual Daily Traffic from the observed volume on one or more specific dates, by applying the corresponding daily and monthly adjustment factors to each date's raw count, and can optionally use this estimate along with a given segment length to compute Annual Vehicle Kilometers Travelled.
4. The program plots the variation of the daily and monthly adjustment factors, and exports the calibrated daily and monthly factor tables to separate Excel files.

Sample Input/Output:
vehicle_volume_2026_Disclaimer_This_Document_is_AI_generated_Not_from_a_genuine_Source.csv → Daily_Variation_Factors_Data_Output.xlsx + Graphs of Daily and Monthly Variation Factors.png + Monthly_Variation_Factors_Data_Output.xlsx
