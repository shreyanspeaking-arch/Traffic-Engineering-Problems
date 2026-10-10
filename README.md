## [Calibration_and_graph_of_Daily_and_Monthly_Variation_Factors.py](https://github.com/shreyanspeaking-arch/Traffic-Engineering-Problems/blob/Traffic-Flow-Parameters/Calibration_and_graph_of_Daily_and_Monthly_Variation_Factors.py)

1. This program calibrates daily and monthly traffic variation factors from a dataset of daily vehicle volumes, and uses them to estimate Average Annual Daily Traffic and Annual Vehicle Miles Travelled for a road segment.
2. The program reads a CSV or Excel file of dates and vehicle volumes, computes the average volume for each day of the week and each month of the year, and derives a Daily Adjustment Factor and a Monthly Adjustment Factor for each, based on their ratio to the overall average.
3. The user can optionally estimate Average Annual Daily Traffic from the observed volume on one or more specific dates, by applying the corresponding daily and monthly adjustment factors to each date's raw count, and can optionally use this estimate along with a given segment length to compute Annual Vehicle Kilometers Travelled.
4. The program plots the variation of the daily and monthly adjustment factors, and exports the calibrated daily and monthly factor tables to separate Excel files.

Sample Input/Output:

vehicle_volume_2026_Disclaimer_This_Document_is_AI_generated_Not_from_a_genuine_Source.csv → Daily_Variation_Factors_Data_Output.xlsx + Graphs of Daily and Monthly Variation Factors.png + Monthly_Variation_Factors_Data_Output.xlsx

## [Greenberg_Model.py](https://github.com/shreyanspeaking-arch/Traffic-Engineering-Problems/blob/Traffic-Flow-Parameters/Greenberg_Model.py)
1. This program models a highway traffic stream using the Greenberg speed density model, computing capacity and plotting the corresponding speed density and speed volume relationships.
2. The user enters the model's speed as a function of density, in the form of a natural logarithm expression involving traffic density K.
3. The program solves this expression for the jam density, and evaluates the model at the density corresponding to maximum flow to obtain the optimum speed.
4. The program computes and reports the roadway's capacity as the product of the optimum density and optimum speed, and plots speed against density and speed against volume over the full range of densities from just above zero up to jam density.

For sample output containing the graphs it can generate, check Speed-Density and Speed-Volume Relationships Using Greenberg Model.png

## [Greenshields_Model.py](https://github.com/shreyanspeaking-arch/Traffic-Engineering-Problems/blob/Traffic-Flow-Parameters/Greenshields_Model.py)
1. This program models a highway traffic stream using the Greenshields speed density model, computing capacity and plotting the corresponding speed density and speed volume relationships.
2. The user enters the model's speed as a linear function of density, in the form of a straight line expression involving traffic density K.
3. The program solves this expression for the free flow speed and the jam density, then derives the flow density relationship and finds the optimum speed at which flow is maximised.
4. The program computes and reports the roadway's capacity as the product of the optimum density and optimum speed, and plots speed against density and speed against volume over the full range of densities from zero up to jam density.

For sample output containing the graphs it can generate, check Speed-Density and Speed-Volume Relationships Using Greenshield' s Model.png

## [Underwood_Model.py](https://github.com/shreyanspeaking-arch/Traffic-Engineering-Problems/blob/Traffic-Flow-Parameters/Underwood_Model.py)
1. This program models a highway traffic stream using the Underwood exponential speed density model, computing capacity and plotting the corresponding speed density and speed volume relationships.
2. The user enters the model's speed as an exponential function of density, in the form of an exponential decay expression involving traffic density K, along with a maximum density value used only to set the plotting range, since this model has no finite jam density.
3. The program evaluates the free flow speed from this expression, computes the optimum speed at which flow is maximised, then solves the expression for the corresponding optimum density.
4. The program computes and reports the roadway's capacity as the product of the optimum density and optimum speed, and plots speed against density and speed against volume over the chosen range of densities.

For sample output containing the graphs it can generate, check Speed-Density and Speed-Volume Relationships using Underwood Model.png
