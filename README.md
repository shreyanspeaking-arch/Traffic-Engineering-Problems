<div align="center">

# 🚗 Traffic Flow Parameters

**A branch of [Traffic Engineering Problems](https://github.com/shreyanspeaking-arch/Traffic-Engineering-Problems), a collection of Python programs for traffic and transportation engineering.**

![Python](https://img.shields.io/badge/Python-3-3776AB?logo=python&logoColor=white) ![Programs](https://img.shields.io/badge/programs-4-2ea44f) ![Interactive](https://img.shields.io/badge/run%20in-terminal-lightgrey)

</div>

The three basic descriptors of a traffic stream are **flow** (vehicles per hour), **density** (vehicles per km) and **speed**, linked by *q = k × v*. These programs calibrate how volume varies through the year, and model the speed density relationship to find a road's capacity.

## 📂 Programs in this branch

| # | Program | What it does |
|:-:|---|---|
| 1 | [**Daily and Monthly Variation Factors**](#1-daily-and-monthly-variation-factors) | Daily and monthly factors, AADT and annual VKT |
| 2 | [**Greenshields' Model (linear)**](#2-greenshields-model-linear) | Linear speed density model and capacity |
| 3 | [**Greenberg's Model (logarithmic)**](#3-greenbergs-model-logarithmic) | Logarithmic speed density model and capacity |
| 4 | [**Underwood's Model (exponential)**](#4-underwoods-model-exponential) | Exponential speed density model and capacity |

## ⚙️ Getting started

```bash
git clone -b Traffic-Flow-Parameters --single-branch https://github.com/shreyanspeaking-arch/Traffic-Engineering-Problems.git
cd Traffic-Engineering-Problems
pip install pandas numpy sympy matplotlib openpyxl
python Calibration_and_graph_of_Daily_and_Monthly_Variation_Factors.py
```

Every program is interactive: it asks for its inputs one at a time in the terminal, then prints (and, where noted, saves or plots) the results.

---

## 1. Daily and Monthly Variation Factors

📄 **File:** [`Calibration_and_graph_of_Daily_and_Monthly_Variation_Factors.py`](./Calibration_and_graph_of_Daily_and_Monthly_Variation_Factors.py)

Calibrates daily and monthly traffic variation factors from a dataset of daily vehicle volumes, and uses them to estimate Average Annual Daily Traffic and Annual Vehicle Kilometers Travelled for a road segment.

**How it works**

1. The program reads a CSV or Excel file of dates and vehicle volumes, computes the average volume for each day of the week and each month of the year, and derives a Daily Adjustment Factor and a Monthly Adjustment Factor for each, based on their ratio to the overall average.
2. The user can optionally estimate Average Annual Daily Traffic from the observed volume on one or more specific dates, by applying the corresponding daily and monthly adjustment factors to each date's raw count, and can optionally use this estimate along with a given segment length to compute Annual Vehicle Kilometers Travelled.
3. The program plots the variation of the daily and monthly adjustment factors, and exports the calibrated daily and monthly factor tables to separate Excel files.

**🧪 Sample input and output**

| Input | Output |
|---|---|
| [`vehicle_volume_2026_Disclaimer_This_Document_is_AI_generated_Not_from_a_genuine_Source.csv`](./vehicle_volume_2026_Disclaimer_This_Document_is_AI_generated_Not_from_a_genuine_Source.csv) | [`Daily_Variation_Factors_Data_Output.xlsx`](./Daily_Variation_Factors_Data_Output.xlsx)<br>[`Monthly_Variation_Factors_Data_Output.xlsx`](./Monthly_Variation_Factors_Data_Output.xlsx)<br>[`Graphs of Daily and Monthly Variation Factors.png`](./Graphs%20of%20Daily%20and%20Monthly%20Variation%20Factors.png) |

**📊 Sample graph**

<p align="center">
  <img src="./Graphs%20of%20Daily%20and%20Monthly%20Variation%20Factors.png" alt="Graphs of Daily and Monthly Variation Factors" width="720">
</p>

---

## 2. Greenshields' Model (linear)

📄 **File:** [`Greenshields_Model.py`](./Greenshields_Model.py)

Models a highway traffic stream using the Greenshields speed density model, computing capacity and plotting the corresponding speed density and speed volume relationships.

**How it works**

1. The user enters the model's speed as a linear function of density, in the form of a straight line expression involving traffic density K.
2. The program solves this expression for the free flow speed and the jam density, then derives the flow density relationship and finds the optimum speed at which flow is maximised.
3. The program computes and reports the roadway's capacity as the product of the optimum density and optimum speed, and plots speed against density and speed against volume over the full range of densities from zero up to jam density.

**📊 Sample graph**

<p align="center">
  <img src="./Speed-Density%20and%20Speed-Volume%20Relationships%20Using%20Greenshield%27%20s%20Model.png" alt="Speed-Density and Speed-Volume Relationships Using Greenshield' s Model" width="720">
</p>

---

## 3. Greenberg's Model (logarithmic)

📄 **File:** [`Greenberg_Model.py`](./Greenberg_Model.py)

Models a highway traffic stream using the Greenberg speed density model, computing capacity and plotting the corresponding speed density and speed volume relationships.

**How it works**

1. The user enters the model's speed as a function of density, in the form of a natural logarithm expression involving traffic density K.
2. The program solves this expression for the jam density, and evaluates the model at the density corresponding to maximum flow to obtain the optimum speed.
3. The program computes and reports the roadway's capacity as the product of the optimum density and optimum speed, and plots speed against density and speed against volume over the full range of densities from just above zero up to jam density.

**📊 Sample graph**

<p align="center">
  <img src="./Speed-Density%20and%20Speed-Volume%20Relationships%20using%20Greenberg%20Model.png" alt="Speed-Density and Speed-Volume Relationships using Greenberg Model" width="720">
</p>

---

## 4. Underwood's Model (exponential)

📄 **File:** [`Underwood_Model.py`](./Underwood_Model.py)

Models a highway traffic stream using the Underwood exponential speed density model, computing capacity and plotting the corresponding speed density and speed volume relationships.

**How it works**

1. The user enters the model's speed as an exponential function of density, in the form of an exponential decay expression involving traffic density K, along with a maximum density value used only to set the plotting range, since this model has no finite jam density.
2. The program evaluates the free flow speed from this expression, computes the optimum speed at which flow is maximised, then solves the expression for the corresponding optimum density.
3. The program computes and reports the roadway's capacity as the product of the optimum density and optimum speed, and plots speed against density and speed against volume over the chosen range of densities.

**📊 Sample graph**

<p align="center">
  <img src="./Speed-Density%20and%20Speed-Volume%20Relationships%20using%20Underwood%20Model.png" alt="Speed-Density and Speed-Volume Relationships using Underwood Model" width="720">
</p>

---

<div align="center"><sub>📚 <a href="https://github.com/shreyanspeaking-arch/Traffic-Engineering-Problems">Back to all topics</a></sub></div>
