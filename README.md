<div align="center">

# 🔀 Trip Distribution

**A branch of [Traffic Engineering Problems](https://github.com/shreyanspeaking-arch/Traffic-Engineering-Problems), a collection of Python programs for traffic and transportation engineering.**

![Python](https://img.shields.io/badge/Python-3-3776AB?logo=python&logoColor=white) ![Programs](https://img.shields.io/badge/programs-1-2ea44f) ![Interactive](https://img.shields.io/badge/run%20in-terminal-lightgrey)

</div>

Trip distribution is the step of travel demand forecasting that decides **where** trips go: given how many trips each zone produces and attracts, it estimates how many travel between each pair of zones.

## 📂 Programs in this branch

| # | Program | What it does |
|:-:|---|---|
| 1 | [**Gravity Model**](#1-gravity-model) | Trips from one origin to every other zone |

## ⚙️ Getting started

```bash
git clone -b Trip-Distribution --single-branch https://github.com/shreyanspeaking-arch/Traffic-Engineering-Problems.git
cd Traffic-Engineering-Problems
pip install pandas numpy openpyxl
python Gravity_Model.py
```

Every program is interactive: it asks for its inputs one at a time in the terminal, then prints (and, where noted, saves or plots) the results.

---

## 1. Gravity Model

📄 **File:** [`Gravity_Model.py`](./Gravity_Model.py)

Estimates the distribution of trips from a single origin zone to all other zones in a network, using a singly constrained gravity model with a power function cost deterrence factor, based on generalised travel cost expressed in time.

**How it works**

1. The user enters the number of zones, the origin zone, and a modal deterrence parameter (alpha) governing the sensitivity of trips to travel cost.
2. For every zone other than the origin, the user enters the generalised cost of travel from the origin to that zone, along with the productions and attractions for each zone.
3. The program computes each zone's travel impedance as its generalised cost raised to the power of negative alpha, and distributes the origin zone's productions to all other zones in proportion to their attractions weighted by this impedance, relative to the total weighted attractiveness of all zones. Results are exported to an Excel file.

---

<div align="center"><sub>📚 <a href="https://github.com/shreyanspeaking-arch/Traffic-Engineering-Problems">Back to all topics</a></sub></div>
