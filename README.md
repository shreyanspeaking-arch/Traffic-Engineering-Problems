Space_and_Time_Mean_Speed.py:
1. This program contains two functions, space_mean_speed and time_mean_speed, meant to be imported and used within other traffic analysis programs.
2. The space_mean_speed function asks for the length of a road segment and the time taken by each vehicle to travel across it, then works out the average speed as the total distance divided by the average travel time.
3. The time_mean_speed function asks for the speed of each vehicle as it passes a fixed point, then works out the simple average of these speeds.
4. Each function takes a verbose argument, which when entered as True prints the result to the screen, and when entered as False returns the result instead for further use.

Spot_Speed_Data_Collection_and_Analysis.py:

1. This program collects and statistically analyzes spot speed data for a stretch of road, allowing entry either vehicle by vehicle, as pre-grouped speed intervals, or by importing a CSV or Excel file.
2. The program computes the frequency distribution of speeds, fits smooth interpolated curves to the frequency and cumulative frequency data, and derives the mean, variance, standard deviation, median, and modal speed from this distribution.
3. The program fits a normal distribution to the observed data using the computed mean and standard deviation, performs a chi square goodness of fit test after combining bins with insufficient frequency, and reports whether the speed data significantly deviates from a normal distribution.
4. The program plots the frequency and cumulative frequency curves against speed, and allows the user to look up the speed corresponding to any desired percentile, before exporting the full analysis to an Excel file.
