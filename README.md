<div align="center">

# 🚌 Modal Split Analysis

**A branch of [Traffic Engineering Problems](https://github.com/shreyanspeaking-arch/Traffic-Engineering-Problems), a collection of Python programs for traffic and transportation engineering.**

![Python](https://img.shields.io/badge/Python-3-3776AB?logo=python&logoColor=white) ![Programs](https://img.shields.io/badge/programs-3-2ea44f) ![Interactive](https://img.shields.io/badge/run%20in-terminal-lightgrey)

</div>

Modal split estimates how travellers divide themselves between competing modes, such as car, bus and rail. These programs use the multinomial logit model, where each mode's share depends on its utility (built from cost and travel time).

## 📂 Programs in this branch

| # | Program | What it does |
|:-:|---|---|
| 1 | [**Modal Split using the Multinomial Logit Model**](#1-modal-split-using-the-multinomial-logit-model) | Mode shares and commuters per mode from cost and time |
| 2 | [**Modal Split from Travel Cost and In / Out of Vehicle Time**](#2-modal-split-from-travel-cost-and-in--out-of-vehicle-time) | Mode shares, ridership and vehicle counts from in and out of vehicle time |
| 3 | [**Change in Modal Split after an Infrastructure Change**](#3-change-in-modal-split-after-an-infrastructure-change) | Ridership before and after a mode is added or removed |

## ⚙️ Getting started

```bash
git clone -b Modal-Split-Analysis --single-branch https://github.com/shreyanspeaking-arch/Traffic-Engineering-Problems.git
cd Traffic-Engineering-Problems
pip install numpy sympy
python Use_of_Multinomial_Logit_Model_for_the_Estimation_of_Modal_Split.py
```

Every program is interactive: it asks for its inputs one at a time in the terminal, then prints (and, where noted, saves or plots) the results.

---

## 1. Modal Split using the Multinomial Logit Model

📄 **File:** [`Use_of_Multinomial_Logit_Model_for_the_Estimation_of_Modal_Split.py`](./Use_of_Multinomial_Logit_Model_for_the_Estimation_of_Modal_Split.py)

Estimates the modal split between an origin and destination using a multinomial logit model based on user defined utility functions of cost and travel time for each mode of transport.

**How it works**

1. The user enters the number of commuters, the number of available modes, and for each mode, a name and a utility function expressed in terms of cost and travel time.
2. The user then enters the actual cost and travel time for each mode, and the program evaluates each mode's utility and converts it into a probability share using the logit formula, normalized across all modes.
3. The program reports the probability of commuters choosing each mode and the corresponding estimated number of commuters using that mode between the given origin and destination.

---

## 2. Modal Split from Travel Cost and In / Out of Vehicle Time

📄 **File:** [`Modal_Split_based_on_Travel_expenses_and_Time_in_and_out_of_vehicle.py`](./Modal_Split_based_on_Travel_expenses_and_Time_in_and_out_of_vehicle.py)

Estimates the modal split among competing modes of transport using a multinomial logit model based on user defined utility functions of in vehicle time, out of vehicle time, and travel expenses.

**How it works**

1. For each mode, the user enters a utility function with numeric coefficients for in vehicle time, out of vehicle time, and travel cost, along with the actual time and cost components that make up each variable.
2. The program computes each mode's utility, converts it to a probability share using the logit formula, and normalizes these shares across all modes.
3. The user then chooses to either estimate ridership on each mode from a known total number of commuters, or to estimate ridership and vehicle counts on each mode from a known vehicle capacity, headway, and percentage of capacity filled for one reference mode, combined with a given modal split ratio and the average occupancy of each other mode.

---

## 3. Change in Modal Split after an Infrastructure Change

📄 **File:** [`Predicting_Change_in_Modal_Split_due_to_a_new_contribution.py`](./Predicting_Change_in_Modal_Split_due_to_a_new_contribution.py)

Predicts the change in modal split and ridership between an origin and destination due to an infrastructure change, using a multinomial logit model based on user defined utility functions of cost and travel time for each mode.

**How it works**

1. The user specifies whether any mode of transport was added or removed by the change, and enters the number of commuters, along with a utility function, cost, and travel time for each mode before the change.
2. The program computes each mode's probability share and estimated ridership before the change, using the logit formula.
3. The user then enters the modes remaining after the change, along with updated cost and travel time for each surviving mode, and provides a name and utility function for any newly added mode, or removes any discontinued mode by name.
4. The program recomputes probability shares and ridership after the change, and reports the increase or decrease in the number of commuters using each mode common to both periods.

> [!NOTE]
> Only one newly added mode is currently supported per run, since the program does not yet accumulate more than one new mode's name and utility function when multiple modes are added at once.

---

<div align="center"><sub>📚 <a href="https://github.com/shreyanspeaking-arch/Traffic-Engineering-Problems">Back to all topics</a></sub></div>
