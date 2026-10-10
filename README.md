<div align="center">

# 📊 LOS Estimation of Multilane Highways

**A branch of [Traffic Engineering Problems](https://github.com/shreyanspeaking-arch/Traffic-Engineering-Problems), a collection of Python programs for traffic and transportation engineering.**

![Python](https://img.shields.io/badge/Python-3-3776AB?logo=python&logoColor=white) ![Programs](https://img.shields.io/badge/programs-2-2ea44f) ![Interactive](https://img.shields.io/badge/run%20in-terminal-lightgrey)

</div>

Level of Service (LOS) grades how well a highway is operating, from **A** (free flow) to **F** (breakdown). These programs follow the Highway Capacity Manual, 1994 method from the Transportation Research Board.

## 📂 Programs in this branch

| # | Program | What it does |
|:-:|---|---|
| 1 | [**LOS Under Ideal Conditions**](#1-los-under-ideal-conditions) | LOS from the volume to capacity ratio |
| 2 | [**LOS Under Non Ideal Conditions**](#2-los-under-non-ideal-conditions) | LOS with lane width, clearance, heavy vehicle and environment corrections |

## ⚙️ Getting started

```bash
git clone -b LOS-Estimation-of-Multilane-Highways --single-branch https://github.com/shreyanspeaking-arch/Traffic-Engineering-Problems.git
cd Traffic-Engineering-Problems
pip install pandas
python LOS_Estimation_Under_Ideal_Conditions_using_the_method_prescribed_by_Transportation_Research_Board_for_Multilane_Highways.py
```

Every program is interactive: it asks for its inputs one at a time in the terminal, then prints (and, where noted, saves or plots) the results.

---

## 1. LOS Under Ideal Conditions

📄 **File:** [`LOS_Estimation_Under_Ideal_Conditions_using_the_method_prescribed_by_Transportation_Research_Board_for_Multilane_Highways.py`](./LOS_Estimation_Under_Ideal_Conditions_using_the_method_prescribed_by_Transportation_Research_Board_for_Multilane_Highways.py)

Estimates the Level of Service of a multilane highway under ideal conditions, using capacity and volume to capacity ratio tables prescribed by the Highway Capacity Manual, 1994.

**How it works**

1. The user enters the total number of lanes, peak hour volume, peak hour factor, and design speed, from which the directional service flow rate and applicable lane capacity, read from Table1, are determined.
2. The program computes the volume to capacity ratio for the highway and compares it against the standard thresholds for each Level of Service, read from Table2, at the given design speed.
3. The program reports the resulting Level of Service, ranging from A through F, based on where the computed ratio falls among these thresholds.

**📥 Data files it reads**

| File | Contents |
|---|---|
| [`Table1.csv`](./Table1.csv) | Capacity of a standard highway lane (veh/h) for design speeds of 50, 60 and 70 mi/h |
| [`Table2.csv`](./Table2.csv) | Volume to capacity ratio thresholds for each Level of Service at these design speeds |

---

## 2. LOS Under Non Ideal Conditions

📄 **File:** [`LOS_Estimation_Under_Non_Ideal_Conditions_using_the_method_prescribed_by_Transportation_Research_Board_for_Multilane_Highways.py`](./LOS_Estimation_Under_Non_Ideal_Conditions_using_the_method_prescribed_by_Transportation_Research_Board_for_Multilane_Highways.py)

Estimates the Level of Service of a multilane highway under non ideal conditions, applying correction factors from several reference tables to the standard capacity and volume to capacity ratio tables prescribed by the Highway Capacity Manual, 1994.

**How it works**

1. The user enters the total number of lanes, peak hour volume, peak hour factor, design speed, lane width, obstruction clearance, terrain type, percentage of heavy vehicles, driver population, and highway classification.
2. The program derives correction factors from Table_5_3, Table_5_4 and Table_5_5, along with a heavy vehicle adjustment factor computed from the entered percentages, and applies them together to adjust the highway's effective capacity, read from Table1.
3. The program computes the corrected volume to capacity ratio and reports the resulting Level of Service, ranging from A through F, based on where this ratio falls among the standard thresholds from Table2 for the given design speed.

**📥 Data files it reads**

| File | Contents |
|---|---|
| [`Table1.csv`](./Table1.csv) | Lane capacity at each design speed (same as the ideal conditions program) |
| [`Table2.csv`](./Table2.csv) | Volume to capacity ratio thresholds for each Level of Service |
| [`Table_5_3_Correction_Factors.csv`](./Table_5_3_Correction_Factors.csv) | Correction factors for lane width and obstruction clearance from the travelled edge |
| [`Table_5_4_PCE_Heavy_Vehicles.csv`](./Table_5_4_PCE_Heavy_Vehicles.csv) | Passenger car equivalents for trucks, buses and recreational vehicles across level, rolling and mountainous terrain |
| [`Table_5_5_Highway_Environment_Correction_Factors.csv`](./Table_5_5_Highway_Environment_Correction_Factors.csv) | Correction factors for rural or urban, divided or undivided highways |

---

<div align="center"><sub>📚 <a href="https://github.com/shreyanspeaking-arch/Traffic-Engineering-Problems">Back to all topics</a></sub></div>
