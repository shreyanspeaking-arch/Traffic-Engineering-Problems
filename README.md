Accumulation_Computations_for_an_Illustrative_Cordon_Study.py:
1. This program computes and plots the accumulation of vehicles within a cordon area over time, based on vehicles entering and leaving at the cordon boundary.
2. The user first enters a known starting accumulation value, observed over an initial time interval.
3. For each subsequent time interval, either at a fixed interval length matching the first, or with individually specified start and end times, the user enters the number of vehicles entering and leaving the cordon.
4. The accumulation for each interval is computed as the previous interval's accumulation plus vehicles entering minus vehicles leaving in the current interval. The resulting accumulation data is printed as a table and plotted against time.
