One_Day_Network_Study_Plan.py:
1. This program estimates the total n-hour volume and peak-hour volume at each of m stations in a network, using the control-count/coverage-count expansion method.
2. A control station's volume is recorded for each of n consecutive time slots.
3. Each of the remaining m-1 (coverage) stations is recorded for only one time slot each, corresponding to the first m-1 slots of the control period (m-1 must be less than n).
4. The control data yields the proportion of daily volume in each slot; each coverage count is divided by its corresponding slot's proportion to estimate that station's n-hour volume, then scaled by the control station's peak-slot proportion to estimate peak-hour volume. Results are exported to an Excel file.

