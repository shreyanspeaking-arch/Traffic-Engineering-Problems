One_Day_Network_Study_Plan.py:

1. This program estimates the total n-hour volume and peak-hour volume at each of m stations in a network, using the control-count/coverage-count expansion method.
2. A control station's volume is recorded for each of n consecutive time slots.
3. Each of the remaining m-1 (coverage) stations is recorded for only one time slot each, corresponding to the first m-1 slots of the control period (m-1 must be less than n).
4. The control data yields the proportion of daily volume in each slot; each coverage count is divided by its corresponding slot's proportion to estimate that station's n-hour volume, then scaled by the control station's peak-slot proportion to estimate peak-hour volume. Results are exported to an Excel file.

Multiday_Network_Study_Plan.py:

1. This program estimates adjusted volumes at each of n coverage count locations in a network, using the day to day adjustment factor method.
2. A control station's volume is recorded for the same fixed number of hours on each of n separate days.
3. Each of the n coverage locations is recorded for that same number of hours on one day, paired in order with the control station's n days. The first coverage location entered is paired with the first control day entered, and so on.
4. The control data yields an Adjustment Factor per day, calculated as the average control volume divided by that day's volume. Each coverage count is multiplied by its corresponding day's factor to estimate its adjusted volume. Results are exported to an Excel file.

Multiple_Slots_in_Multiple_Days_Network_Study_Plan.py:

1. This program estimates expanded and adjusted volumes at coverage count locations in a network, combining a within day slot expansion method with a day to day adjustment factor method.
2. A control station's volume is recorded across s time slots on each of d days, using the same slot start and end times on every day.
3. The control data yields two things for each day, the percentage of that day's total volume falling in each slot, and a daily Adjustment Factor, calculated as the average total volume across all days divided by that particular day's total volume.
4. A coverage count is recorded for every slot on every day at a given station. Each entry is expanded to a full day volume using that day's slot percentage, then multiplied by that day's Adjustment Factor to estimate its final adjusted volume. Results are exported to an Excel file.
