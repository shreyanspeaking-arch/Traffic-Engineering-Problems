<div align="center">

# 🛣️ Curve Fitting for Highways

**A branch of [Traffic Engineering Problems](https://github.com/shreyanspeaking-arch/Traffic-Engineering-Problems), a collection of Python programs for traffic and transportation engineering.**

![Python](https://img.shields.io/badge/Python-3-3776AB?logo=python&logoColor=white) ![Programs](https://img.shields.io/badge/programs-2-2ea44f) ![Interactive](https://img.shields.io/badge/run%20in-terminal-lightgrey)

</div>

Geometric design of highway curves: parabolic vertical curves that join two grades smoothly, and superelevation (banking) that keeps vehicles safely on horizontal curves.

## 📂 Programs in this branch

| # | Program | What it does |
|:-:|---|---|
| 1 | [**Parabolic Vertical Curves**](#1-parabolic-vertical-curves) | K value, offsets and the high or low point of a vertical curve |
| 2 | [**Superelevation for a Highway Curve (IRC:73-2023)**](#2-superelevation-for-a-highway-curve-irc73-2023) | Required superelevation, side friction check and safe speed |

## ⚙️ Getting started

```bash
git clone -b Curve-Fitting-for-Highways --single-branch https://github.com/shreyanspeaking-arch/Traffic-Engineering-Problems.git
cd Traffic-Engineering-Problems
# no extra packages needed, only the Python standard library
python Parabolic_Curves_Computation_For_Vertical_Alignment_on_Highways.py
```

Every program is interactive: it asks for its inputs one at a time in the terminal, then prints (and, where noted, saves or plots) the results.

---

## 1. Parabolic Vertical Curves

📄 **File:** [`Parabolic_Curves_Computation_For_Vertical_Alignment_on_Highways.py`](./Parabolic_Curves_Computation_For_Vertical_Alignment_on_Highways.py)

Computes key parameters of a parabolic vertical curve used in highway alignment design, given the coordinates and grades at the two tangent points.

**How it works**

1. The user enters the coordinates of tangent points T1 and T2, along with the signed grade in percent at each point.
2. The user then selects from a menu of computations:
   - The K value of the curve, representing the horizontal distance required for a 1 percent change in grade.
   - The coordinates of any point on the curve, given its x coordinate.
   - The vertical offset at the point of intersection of the two tangents.
   - The vertical offset at a specific point on the curve, given its x coordinate.
   - The horizontal and vertical offsets at the highest or lowest point on the curve.
3. The user can repeat this selection for multiple computations in the same session before exiting. All computations use standard parabolic vertical curve formulas, with distances measured in meters.

---

## 2. Superelevation for a Highway Curve (IRC:73-2023)

📄 **File:** [`Super_Elevation_Estimation_for_Highway_Curve.py`](./Super_Elevation_Estimation_for_Highway_Curve.py)

Estimates the required superelevation and checks the safety of a highway curve, based on the model prescribed by IRC:73-2023.

**How it works**

1. The user enters the design speed and radius of curvature, along with the desired superelevation, either the common default value of 0.07 or a custom value, which is checked against a practical upper limit.
2. The program computes the theoretically required superelevation and compares it against the desired value, capping it at the desired value if the theoretical requirement is lower, or stopping with an estimate if the theoretical requirement is lower than what can be practically achieved.
3. Using the resulting superelevation, the program computes the required coefficient of side friction and compares it against a chosen value, either the common default value of 0.15 or a custom value, declaring the design safe if within limits, or otherwise computing the maximum safe speed for the curve and reporting whether the original design speed is adequate or should be limited.

---

<div align="center"><sub>📚 <a href="https://github.com/shreyanspeaking-arch/Traffic-Engineering-Problems">Back to all topics</a></sub></div>
