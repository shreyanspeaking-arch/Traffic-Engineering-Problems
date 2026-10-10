<div align="center">

# 📈 Traffic Volume Studies

**A branch of [Traffic Engineering Problems](https://github.com/shreyanspeaking-arch/Traffic-Engineering-Problems), a collection of Python programs for traffic and transportation engineering.**

![Python](https://img.shields.io/badge/Python-3-3776AB?logo=python&logoColor=white) ![Programs](https://img.shields.io/badge/programs-1-2ea44f) ![Interactive](https://img.shields.io/badge/run%20in-terminal-lightgrey)

</div>

Volume studies count how many vehicles use a road, and summarise the counts into standard measures such as Average Daily Traffic (ADT) and Average Annual Daily Traffic (AADT).

## 📂 Programs in this branch

| # | Program | What it does |
|:-:|---|---|
| 1 | [**Daily Volume Parameters**](#1-daily-volume-parameters) | Monthly ADT and AWDT, annual AADT, with plots |

## ⚙️ Getting started

```bash
git clone -b Traffic-Volume-Studies --single-branch https://github.com/shreyanspeaking-arch/Traffic-Engineering-Problems.git
cd Traffic-Engineering-Problems
pip install pandas numpy matplotlib openpyxl
python Illustration_of_Daily_Volume_Parameters.py
```

Every program is interactive: it asks for its inputs one at a time in the terminal, then prints (and, where noted, saves or plots) the results.

---

## 1. Daily Volume Parameters

📄 **File:** [`Illustration_of_Daily_Volume_Parameters.py`](./Illustration_of_Daily_Volume_Parameters.py)

Computes and visualizes monthly and annual traffic volume parameters from a dataset of daily vehicle volumes, either read from a CSV or Excel file or entered manually.

**How it works**

1. For each month present in the data, the program computes the total volume across all days, the total volume across weekdays only, and the corresponding day counts, then derives the Average Daily Traffic and Average Weekday Traffic for each month.
2. The program aggregates these monthly figures into annual measures, including Average Annual Daily Traffic, Average Annual Weekday Traffic, Average Annual Weekend Traffic, and total annual traffic split across all days, weekdays, and weekends, and exports the monthly results to an Excel file.
3. The program plots monthly total and weekday volumes, plots average daily traffic across all days, weekdays, and weekends by month, and plots the raw daily traffic volume over the full recorded period.

**🧪 Sample input and output**

| Input | Output |
|---|---|
| [`daily_traffic_2024_this_file_is_AI_generated.csv`](./daily_traffic_2024_this_file_is_AI_generated.csv) | [`output5.xlsx`](./output5.xlsx)<br>[`Daily Variation of Vehicle Volumes.png`](./Daily%20Variation%20of%20Vehicle%20Volumes.png)<br>[`Variation of Total Monthly and Total Weekday Volume per Month.png`](./Variation%20of%20Total%20Monthly%20and%20Total%20Weekday%20Volume%20per%20Month.png)<br>[`Variation of Average Daily Traffic on all days, weekdays and weekends based on months.png`](./Variation%20of%20Average%20Daily%20Traffic%20on%20all%20days%2C%20weekdays%20and%20weekends%20based%20on%20months.png) |

**📊 Sample graphs**

<p align="center">
  <img src="./Daily%20Variation%20of%20Vehicle%20Volumes.png" alt="Daily Variation of Vehicle Volumes" width="720">
</p>

<p align="center">
  <img src="./Variation%20of%20Total%20Monthly%20and%20Total%20Weekday%20Volume%20per%20Month.png" alt="Variation of Total Monthly and Total Weekday Volume per Month" width="720">
</p>

<p align="center">
  <img src="./Variation%20of%20Average%20Daily%20Traffic%20on%20all%20days%2C%20weekdays%20and%20weekends%20based%20on%20months.png" alt="Variation of Average Daily Traffic on all days, weekdays and weekends based on months" width="720">
</p>

---

<div align="center"><sub>📚 <a href="https://github.com/shreyanspeaking-arch/Traffic-Engineering-Problems">Back to all topics</a></sub></div>
