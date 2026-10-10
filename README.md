<div align="center">

# 🏎️ Speed Studies

**A branch of [Traffic Engineering Problems](https://github.com/shreyanspeaking-arch/Traffic-Engineering-Problems), a collection of Python programs for traffic and transportation engineering.**

![Python](https://img.shields.io/badge/Python-3-3776AB?logo=python&logoColor=white) ![Programs](https://img.shields.io/badge/programs-2-2ea44f) ![Interactive](https://img.shields.io/badge/run%20in-terminal-lightgrey)

</div>

Speed studies measure how fast vehicles actually travel on a road. They are used to set speed limits, check designs and judge safety.

## 📂 Programs in this branch

| # | Program | What it does |
|:-:|---|---|
| 1 | [**Spot Speed Data Collection and Analysis**](#1-spot-speed-data-collection-and-analysis) | Speed distribution, percentiles and a chi square normality test |
| 2 | [**Space Mean Speed and Time Mean Speed**](#2-space-mean-speed-and-time-mean-speed) | Reusable functions for the two mean speeds |

## ⚙️ Getting started

```bash
git clone -b Speed-Studies --single-branch https://github.com/shreyanspeaking-arch/Traffic-Engineering-Problems.git
cd Traffic-Engineering-Problems
pip install pandas numpy scipy matplotlib openpyxl
python Spot_Speed_Data_Collection_and_Analysis.py
```

Every program is interactive: it asks for its inputs one at a time in the terminal, then prints (and, where noted, saves or plots) the results.

---

## 1. Spot Speed Data Collection and Analysis

📄 **File:** [`Spot_Speed_Data_Collection_and_Analysis.py`](./Spot_Speed_Data_Collection_and_Analysis.py)

Collects and statistically analyzes spot speed data for a stretch of road, allowing entry either vehicle by vehicle, as pre-grouped speed intervals, or by importing a CSV or Excel file.

**How it works**

1. The program computes the frequency distribution of speeds, fits smooth interpolated curves to the frequency and cumulative frequency data, and derives the mean, variance, standard deviation, median, and modal speed from this distribution.
2. The program fits a normal distribution to the observed data using the computed mean and standard deviation, performs a chi square goodness of fit test after combining bins with insufficient frequency, and reports whether the speed data significantly deviates from a normal distribution.
3. The program plots the frequency and cumulative frequency curves against speed, and allows the user to look up the speed corresponding to any desired percentile, before exporting the full analysis to an Excel file.

**🧪 Sample input and output**

| Input | Output |
|---|---|
| [`speed_observation_data_Disclaimer_This_is_AI_Generated.csv`](./speed_observation_data_Disclaimer_This_is_AI_Generated.csv) | [`output2.xlsx`](./output2.xlsx)<br>[`%_Frequency_vs_Middle_Speed_Graph_and_Cumulative_%_Frequency_vs_Upper_Speed_Limit_1.png`](./%25_Frequency_vs_Middle_Speed_Graph_and_Cumulative_%25_Frequency_vs_Upper_Speed_Limit_1.png) |
| Manual input (see the commit history of the output files) | [`output3.xlsx`](./output3.xlsx)<br>[`%_Frequency_vs_Middle_Speed_Graph_and_Cumulative_%_Frequency_vs_Upper_Speed_Limit_2.png`](./%25_Frequency_vs_Middle_Speed_Graph_and_Cumulative_%25_Frequency_vs_Upper_Speed_Limit_2.png) |
| Manual input (see the commit history of the output files) | [`output4.xlsx`](./output4.xlsx)<br>[`%_Frequency_vs_Middle_Speed_Graph_and_Cumulative_%_Frequency_vs_Upper_Speed_Limit_3.png`](./%25_Frequency_vs_Middle_Speed_Graph_and_Cumulative_%25_Frequency_vs_Upper_Speed_Limit_3.png) |

**📊 Sample graphs**

<p align="center">
  <img src="./%25_Frequency_vs_Middle_Speed_Graph_and_Cumulative_%25_Frequency_vs_Upper_Speed_Limit_1.png" alt="%_Frequency_vs_Middle_Speed_Graph_and_Cumulative_%_Frequency_vs_Upper_Speed_Limit_1" width="720">
</p>

<p align="center">
  <img src="./%25_Frequency_vs_Middle_Speed_Graph_and_Cumulative_%25_Frequency_vs_Upper_Speed_Limit_2.png" alt="%_Frequency_vs_Middle_Speed_Graph_and_Cumulative_%_Frequency_vs_Upper_Speed_Limit_2" width="720">
</p>

<p align="center">
  <img src="./%25_Frequency_vs_Middle_Speed_Graph_and_Cumulative_%25_Frequency_vs_Upper_Speed_Limit_3.png" alt="%_Frequency_vs_Middle_Speed_Graph_and_Cumulative_%_Frequency_vs_Upper_Speed_Limit_3" width="720">
</p>

---

## 2. Space Mean Speed and Time Mean Speed

📄 **File:** [`Space_and_Time_Mean_Speed.py`](./Space_and_Time_Mean_Speed.py)

Contains two functions, `space_mean_speed` and `time_mean_speed`, meant to be imported and used within other traffic analysis programs. Speeds are in m/s.

**How it works**

1. The `space_mean_speed` function asks for the length of a road segment and the time taken by each vehicle to travel across it, then works out the average speed as the total distance divided by the average travel time.
2. The `time_mean_speed` function asks for the speed of each vehicle as it passes a fixed point, then works out the simple average of these speeds.
3. Each function takes a `verbose` argument. When it is `True` the result is also printed to the screen; in both cases the result is returned for further use.

---

<div align="center"><sub>📚 <a href="https://github.com/shreyanspeaking-arch/Traffic-Engineering-Problems">Back to all topics</a></sub></div>
