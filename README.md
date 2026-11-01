<div align="center">

# 🗺️ Network Study Plans

**A branch of [Traffic Engineering Problems](https://github.com/shreyanspeaking-arch/Traffic-Engineering-Problems), a collection of Python programs for traffic and transportation engineering.**

![Python](https://img.shields.io/badge/Python-3-3776AB?logo=python&logoColor=white) ![Programs](https://img.shields.io/badge/programs-4-2ea44f) ![Interactive](https://img.shields.io/badge/run%20in-terminal-lightgrey)

</div>

Counting traffic at every point in a network all the time is impractical. A network study counts continuously at a few **control stations** and briefly at many **coverage stations**, then uses the control data to expand the short counts into full estimates.

## 📂 Programs in this branch

| # | Program | What it does |
|:-:|---|---|
| 1 | [**One Day Network Study Plan**](#1-one-day-network-study-plan) | n-hour and peak hour volumes from one day of counts |
| 2 | [**Multiday Network Study Plan**](#2-multiday-network-study-plan) | Day to day adjustment factors across several days |
| 3 | [**Multiple Slots in Multiple Days Network Study Plan**](#3-multiple-slots-in-multiple-days-network-study-plan) | Slot expansion combined with daily adjustment factors |
| 4 | [**Origin Destination Matrix Balancing (Furness Method)**](#4-origin-destination-matrix-balancing-furness-method) | Balances an O-D trip matrix to forecast totals |

## ⚙️ Getting started

```bash
git clone -b Network-Study-Plans --single-branch https://github.com/shreyanspeaking-arch/Traffic-Engineering-Problems.git
cd Traffic-Engineering-Problems
pip install pandas numpy openpyxl
python One_Day_Network_Study_Plan.py
```

Every program is interactive: it asks for its inputs one at a time in the terminal, then prints (and, where noted, saves or plots) the results.

---

## 1. One Day Network Study Plan

📄 **File:** [`One_Day_Network_Study_Plan.py`](./One_Day_Network_Study_Plan.py)

Estimates the total n-hour volume and peak-hour volume at each of m stations in a network, using the control-count/coverage-count expansion method.

**How it works**

1. A control station's volume is recorded for each of n consecutive time slots.
2. Each of the remaining m-1 (coverage) stations is recorded for only one time slot each, corresponding to the first m-1 slots of the control period (m-1 must be less than n).
3. The control data yields the proportion of daily volume in each slot; each coverage count is divided by its corresponding slot's proportion to estimate that station's n-hour volume, then scaled by the control station's peak-slot proportion to estimate peak-hour volume. Results are exported to an Excel file.

---

## 2. Multiday Network Study Plan

📄 **File:** [`Multiday_Network_Study_Plan.py`](./Multiday_Network_Study_Plan.py)

Estimates adjusted volumes at each of n coverage count locations in a network, using the day to day adjustment factor method.

**How it works**

1. A control station's volume is recorded for the same fixed number of hours on each of n separate days.
2. Each of the n coverage locations is recorded for that same number of hours on one day, paired in order with the control station's n days. The first coverage location entered is paired with the first control day entered, and so on.
3. The control data yields an Adjustment Factor per day, calculated as the average control volume divided by that day's volume. Each coverage count is multiplied by its corresponding day's factor to estimate its adjusted volume. Results are exported to an Excel file.

---

## 3. Multiple Slots in Multiple Days Network Study Plan

📄 **File:** [`Multiple_Slots_in_Multiple_Days_Network_Study_Plan.py`](./Multiple_Slots_in_Multiple_Days_Network_Study_Plan.py)

Estimates expanded and adjusted volumes at coverage count locations in a network, combining a within day slot expansion method with a day to day adjustment factor method.

**How it works**

1. A control station's volume is recorded across s time slots on each of d days, using the same slot start and end times on every day.
2. The control data yields two things for each day, the percentage of that day's total volume falling in each slot, and a daily Adjustment Factor, calculated as the average total volume across all days divided by that particular day's total volume.
3. A coverage count is recorded for every slot on every day at a given station. Each entry is expanded to a full day volume using that day's slot percentage, then multiplied by that day's Adjustment Factor to estimate its final adjusted volume. Results are exported to an Excel file.

---

## 4. Origin Destination Matrix Balancing (Furness Method)

📄 **File:** [`Specialized_Intersection_Counting_Studies_Using_Origin_and_Destination_Data.py`](./Specialized_Intersection_Counting_Studies_Using_Origin_and_Destination_Data.py)

Balances an observed origin destination trip matrix to match forecasted zone totals, using the Furness iterative proportional fitting method.

**How it works**

1. The user enters the observed number of trips between every pair of zones, forming a square origin destination matrix.
2. The user also enters the forecasted total number of trip origins and trip destinations for each zone.
3. The program repeatedly scales each row by the ratio of its forecasted origin total to its current row total, and each column by the ratio of its forecasted destination total to its current column total, continuing until these ratios fall within the user specified acceptable error of 1. The final balanced matrix is printed as whole numbers.

---

<div align="center"><sub>📚 <a href="https://github.com/shreyanspeaking-arch/Traffic-Engineering-Problems">Back to all topics</a></sub></div>
