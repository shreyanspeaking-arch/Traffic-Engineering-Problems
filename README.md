<div align="center">

# 💰 Highway Economics

**A branch of [Traffic Engineering Problems](https://github.com/shreyanspeaking-arch/Traffic-Engineering-Problems), a collection of Python programs for traffic and transportation engineering.**

![Python](https://img.shields.io/badge/Python-3-3776AB?logo=python&logoColor=white) ![Programs](https://img.shields.io/badge/programs-1-2ea44f) ![Interactive](https://img.shields.io/badge/run%20in-terminal-lightgrey)

</div>

Is a highway project worth building? These programs weigh the money a project costs against the savings it brings road users, discounted to today's value.

## 📂 Programs in this branch

| Program | What it does |
|---|---|
| [**Cost Benefit Analysis of a Highway Project**](#cost-benefit-analysis-of-a-highway-project) | NPV from accident, operating cost and travel time savings |

## ⚙️ Getting started

```bash
git clone -b Highway-Economics --single-branch https://github.com/shreyanspeaking-arch/Traffic-Engineering-Problems.git
cd Traffic-Engineering-Problems
pip install pandas numpy sympy openpyxl
python Economic_Appraisal_of_Highway_Project_using_Cost_Benefit_Analysis.py
```

Every program is interactive: it asks for its inputs one at a time in the terminal, then prints (and, where noted, saves or plots) the results.

---

## Cost Benefit Analysis of a Highway Project

📄 **File:** [`Economic_Appraisal_of_Highway_Project_using_Cost_Benefit_Analysis.py`](./Economic_Appraisal_of_Highway_Project_using_Cost_Benefit_Analysis.py)

Performs an economic appraisal of a highway project using cost benefit analysis, estimating user benefits from reduced accidents, reduced vehicle operating costs, and reduced travel time, and comparing their discounted value against discounted project costs to compute Net Present Value.

**How it works**

1. The user enters the project's economic life, the number of years required for initial construction, accident rates and average accident cost, average vehicle speeds before and after the upgrade, the discount rate, and a formula for average vehicle operating cost as a function of speed.
2. For each year of the project, the user enters either the annual construction cost, for years before inauguration, or the predicted traffic flow and annual operating cost, for years after inauguration.
3. The program computes annual savings in accidents, vehicle operating costs, and travel time based on the difference between existing and upgraded road conditions, discounts these benefits and the annual costs to present value using the given discount rate, and reports whether the project is economically acceptable based on its Net Present Value. Results are exported to an Excel file.

**🧪 Sample input and output**

| Input | Output |
|---|---|
| Manual input (see the commit history of output1.xlsx in [Original-Branch-Disorganized](https://github.com/shreyanspeaking-arch/Traffic-Engineering-Problems/tree/Original-Branch-Disorganized)) | [`output1.xlsx`](./output1.xlsx) |

<!-- preview:start -->
**📋 First five rows**

<details open>
<summary><code>output1.xlsx</code></summary>

| Predicted flow per million vehicle km | Construction Cost | Operating Cost | Accident Savings | Operating Cost Savings | Travel Time Savings | Total User Benefits | Discounted Benefits | Construction and Maintenance Cost | Discounted Costs |
|---|---|---|---|---|---|---|---|---|---|
|  | 15000000 |  |  |  |  |  |  | 15000000 | 14150943.396 |
|  | 10000000 |  |  |  |  |  |  | 10000000 | 8899964.4 |
| 250 |  | 500000 | 1500000 | 454963.235 | 6617647.059 | 8572610.294 | 7197728.909 | 500000 | 419809.642 |
| 260 |  | 500000 | 1560000 | 473161.765 | 6882352.941 | 8915514.706 | 7061922.703 | 500000 | 396046.832 |
| 270 |  | 500000 | 1620000 | 491360.294 | 7147058.824 | 9258419.118 | 6918429.353 | 500000 | 373629.086 |

<sub>12 rows in total.</sub>

</details>
<!-- preview:end -->

---

<div align="center"><sub>📚 <a href="https://github.com/shreyanspeaking-arch/Traffic-Engineering-Problems">Back to all topics</a></sub></div>
