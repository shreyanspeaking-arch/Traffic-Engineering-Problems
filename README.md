<div align="center">

# 🦺 Traffic Safety Analysis

**A branch of [Traffic Engineering Problems](https://github.com/shreyanspeaking-arch/Traffic-Engineering-Problems), a collection of Python programs for traffic and transportation engineering.**

![Python](https://img.shields.io/badge/Python-3-3776AB?logo=python&logoColor=white) ![Programs](https://img.shields.io/badge/programs-2-2ea44f) ![Interactive](https://img.shields.io/badge/run%20in-terminal-lightgrey)

</div>

Programs for predicting crashes and checking that drivers have enough distance to stop safely.

## 📂 Programs in this branch

| # | Program | What it does |
|:-:|---|---|
| 1 | [**Crash Prediction at a Four Leg Signalized Intersection**](#1-crash-prediction-at-a-four-leg-signalized-intersection) | Predicted crashes per year using the HSM 1st Edition (2010) method |
| 2 | [**Safe Stopping Distance (SSD)**](#2-safe-stopping-distance-ssd) | Stopping distance between two vehicles across many cases |

## ⚙️ Getting started

```bash
git clone -b Traffic-Safety-Analysis --single-branch https://github.com/shreyanspeaking-arch/Traffic-Engineering-Problems.git
cd Traffic-Engineering-Problems
pip install pandas numpy sympy matplotlib openpyxl
python Traffic_Safety_Analysis_at_a_4_signal_intersection.py
```

Every program is interactive: it asks for its inputs one at a time in the terminal, then prints (and, where noted, saves or plots) the results.

---

## 1. Crash Prediction at a Four Leg Signalized Intersection

📄 **File:** [`Traffic_Safety_Analysis_at_a_4_signal_intersection.py`](./Traffic_Safety_Analysis_at_a_4_signal_intersection.py)

Predicts the annual number of crashes at a four leg signalized intersection, using safety performance functions and crash modification factors consistent with the predictive method in Part C, Chapter 12 of the Highway Safety Manual (HSM), 1st Edition (2010).

**🧰 Prerequisites**

- **Software**
  - Python 3
  - `pandas`
  - `sympy`
  - Install the packages with `pip install pandas sympy`
- **Files in the same folder as the program** (included in this branch)
  - [`Table_12_10_CMF_Left_Turn_Phasing.csv`](./Table_12_10_CMF_Left_Turn_Phasing.csv)
  - [`Table_12_11_Formatted.csv`](./Table_12_11_Formatted.csv)
  - [`Table_12_4_Calibration_Coefficients.csv`](./Table_12_4_Calibration_Coefficients.csv)
  - [`Table_12_5_Calibration_Coefficients.csv`](./Table_12_5_Calibration_Coefficients.csv)
  - [`Table_12_6_Calibration_Coefficients.csv`](./Table_12_6_Calibration_Coefficients.csv)
  - [`Table_12_7_Pedestrian_Volume_Default_Values.csv`](./Table_12_7_Pedestrian_Volume_Default_Values.csv)
  - [`Table_12_9_CMF_Turn_Lanes.csv`](./Table_12_9_CMF_Turn_Lanes.csv)
- **Choices you will be asked to make** (type the value shown)
  - Pedestrian volume known: `Yes` to enter the daily count, or `No` to pick an activity level: `high`, `medium - high`, `medium`, `medium - low` or `low`
  - Left turn phasing type: `Permitted`, `Compound` (protected + permitted) or `Protected`
  - Red light camera crash data: `Yes1` to enter crash counts, `Yes2` to enter proportions, `No` if none (use `No` unless the intersection has a red light camera)
- **Data to have ready**
  - AADT on the major and minor streets (veh/day)
  - Daily pedestrian volume, if known
  - Maximum number of lanes a pedestrian crosses
  - Number of approaches (0 to 4) with left turn lanes and with right turn lanes
  - Number of approaches prohibiting right turn on red, and number with exclusive left turn phasing
  - Numbers of schools, bus stops and alcohol selling stores within 1000 ft
  - A local calibration factor (`1` if unknown)

**How it works**

1. Using the major and minor street traffic volumes and the calibration coefficients of Tables 12-4 and 12-5, the program computes base crash frequencies for multi-vehicle and single-vehicle crashes, split into injury and fatal, and property damage only components.
2. Using the pedestrian volume (or a default from Table 12-7), the maximum number of lanes a pedestrian must cross, and the coefficients of Table 12-6, the program computes a base pedestrian crash frequency.
3. The program applies crash modification factors for turn lanes (Table 12-9) and left turn phasing (Table 12-10). The user also enters the number of approaches prohibiting right turn on red, and either the number or proportion of multi-vehicle crashes that are right angle or rear end collisions, from which the program derives further crash modification factors for right turn on red restrictions and red light cameras. A crash modification factor for intersection lighting is also applied.
4. Crash modification factors for nearby schools, bus stops and alcohol selling stores (Table 12-11) are applied to the base pedestrian crash frequency.
5. The program combines the adjusted vehicle, pedestrian, and bicycle crash predictions, applies a user supplied local calibration factor, and reports the total predicted number of crashes per year at the intersection.

> [!NOTE]
> **Assumptions and limitations**
> - The intersection is assumed to be lit: the lighting crash modification factor (1 − 0.38 × 0.235 ≈ 0.91) is always applied, so for an unlit intersection the prediction is about 9% too low.
> - The red light camera crash modification factor is applied whenever right angle and rear end crash data are entered. Enter `<No>` at that prompt unless the intersection has a red light camera.
> - When crash counts are entered, the right angle and rear end proportions are taken relative to the sum of those two crash types, whereas the HSM uses all multi-vehicle crashes.
> - The Empirical Bayes adjustment with observed crash history is not included, so the result is the predicted crash frequency, not the expected crash frequency.
> - The safety performance functions were developed from crash data in the United States. For intersections elsewhere, such as in India, a locally calibrated factor should be used instead of 1.

**📥 Data files it reads**

| File | Contents |
|---|---|
| [`Table_12_4_Calibration_Coefficients.csv`](./Table_12_4_Calibration_Coefficients.csv) | Calibration coefficients for the multi-vehicle base crash frequency model |
| [`Table_12_5_Calibration_Coefficients.csv`](./Table_12_5_Calibration_Coefficients.csv) | Calibration coefficients for the single-vehicle base crash frequency model |
| [`Table_12_6_Calibration_Coefficients.csv`](./Table_12_6_Calibration_Coefficients.csv) | Calibration coefficients for the base pedestrian crash frequency model |
| [`Table_12_7_Pedestrian_Volume_Default_Values.csv`](./Table_12_7_Pedestrian_Volume_Default_Values.csv) | Default pedestrian volumes when an actual count is not available |
| [`Table_12_8_Crash_Modification_Factors.csv`](./Table_12_8_Crash_Modification_Factors.csv) | Reference only (not read by the program): which crash modification factors apply to each crash type |
| [`Table_12_9_CMF_Turn_Lanes.csv`](./Table_12_9_CMF_Turn_Lanes.csv) | Crash modification factors for exclusive left or right turn lanes |
| [`Table_12_10_CMF_Left_Turn_Phasing.csv`](./Table_12_10_CMF_Left_Turn_Phasing.csv) | Crash modification factors for left turn signal phasing |
| [`Table_12_11_Formatted.csv`](./Table_12_11_Formatted.csv) | Crash modification factors for nearby schools, bus stops and alcohol selling stores |

**🧪 Sample input and output**

| Input | Output |
|---|---|
| Manual input | [`Sample_Input_Output.md`](./Sample_Input_Output.md) |

---

## 2. Safe Stopping Distance (SSD)

📄 **File:** [`Safe_Stopping_Distance_SSD.py`](./Safe_Stopping_Distance_SSD.py)

Computes and compares the Safe Stopping Distance (SSD) between two model vehicles, A and B, across multiple user-defined cases, accounting for reaction time, road grade, coefficient of friction, and relative direction of movement.

**🧰 Prerequisites**

- **Software**
  - Python 3
  - `pandas`
  - `numpy`
  - `matplotlib`
  - `openpyxl`
  - Install the packages with `pip install pandas numpy matplotlib openpyxl`
- **Choices you will be asked to make** (type the value shown)
  - Speed unit: `kmph` or `mph`
  - Grade: enter it in degrees as `5o`, or as a percentage as `4%`; press Enter if both vehicles share the same grade
  - Friction: press Enter if both vehicles share the same coefficient, or `No` to enter each
  - Direction of each vehicle: `1` uphill, `2` downhill; and the vehicles' relative direction: `same` or `opposite`
  - After each case: press Enter to compare another case, or `No` to finish
- **Data to have ready**
  - Total reaction plus maneuver time (s)
  - Speeds of vehicles A and B
  - Coefficient of friction between each vehicle's wheels and the pavement
  - Head start distance between the vehicles (m; `0` if unknown)
  - An optional description for each case
  - A name for the output Excel file, typed without `.xlsx`

**How it works**

1. The user enters the unit of speed (kmph or mph), and for each case, the total reaction plus maneuver time, the speeds of both vehicles, the grade of the highway for each (entered either in degrees or as a percentage, with uphill or downhill direction specified), the coefficient of friction between each vehicle's wheels and the pavement surface, and any head start distance between the two vehicles.
2. The program determines whether the vehicles are moving in the same or opposite directions, either from user input or inferred from their uphill/downhill orientation, and applies the corresponding sign convention when combining their individual stopping distances.
3. The individual stopping distance for each vehicle is computed as the sum of the distance travelled during reaction time and the braking distance derived from its speed, friction coefficient, and grade. These are combined according to the direction of travel and reduced by the head start distance to obtain the Safe Stopping Distance for that case.
4. The user can repeat this for multiple cases within a single session, optionally adding a descriptive statement for each. All case parameters and results are tabulated and exported to an Excel file, and the variation of Safe Stopping Distance across cases is plotted.

**🧪 Sample input and output**

| Input | Output |
|---|---|
| Manual input (see the commit history of the output files) | [`Various_Stopping_Sight_Distance_Conditions.xlsx`](./Various_Stopping_Sight_Distance_Conditions.xlsx)<br>[`Various_Stopping_Sight_Distance_Conditions.png`](./Various_Stopping_Sight_Distance_Conditions.png) |

<!-- preview:start -->
**📋 First five rows**

<details open>
<summary><code>Various_Stopping_Sight_Distance_Conditions.xlsx</code></summary>

| Velocity of Vehicle A | Velocity of Vehicle B | Direction of movement wrt each other | Coefficient of Friction between Vehicle A and Pavement Surface | Coefficient of Friction between Vehicle B and Pavement Surface | Total Reaction + Maneuver Time | Head Start Distance | Grade of Slope of road of Vehicle A | Grade of Slope of road of Vehicle B | Safe Stopping Distance | Related Statement |
|---|---|---|---|---|---|---|---|---|---|---|
| 120 | 60 | SAME | 0.5 | 0.5 | 2 | 0 | 0 | 0 | 118.281 |  |
| 120 | 60 | OPPOSITE | 0.5 | 0.5 | 2 | 0 | 0 | 0 | 241.579 |  |
| 60 | 0 | OPPOSITE | 0.5 | 0.5 | 2 | 0 | 0 | 0 | 61.649 |  |
| 120 | 60 | SAME | 0.5 | 0.5 | 2.5 | 0 | 0 | 0 | 126.614 |  |
| 120 | 60 | OPPOSITE | 0.5 | 0.5 | 2.5 | 0 | 0 | 0 | 266.579 |  |

<sub>18 rows in total.</sub>

</details>
<!-- preview:end -->

**📊 Sample graph**

<table align="center"><tr><td align="center">
  <img src="./Various_Stopping_Sight_Distance_Conditions.png" alt="Safe stopping distance across the sample cases" width="720"><br><sub><b>Figure 1.</b> Safe stopping distance across the sample cases<br><a href="./Various_Stopping_Sight_Distance_Conditions.png">Various_Stopping_Sight_Distance_Conditions.png</a></sub>
</td></tr></table>

---

<div align="center"><sub>📚 <a href="https://github.com/shreyanspeaking-arch/Traffic-Engineering-Problems">Back to all topics</a></sub></div>
