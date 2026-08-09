Parabolic_Curves_Computation_For_Vertical_Alignment_on_Highways.py:

1. This program computes key parameters of a parabolic vertical curve used in highway alignment design, given the coordinates and grades at the two tangent points.
2. The user enters the coordinates of tangent points T1 and T2, along with the signed grade in percent at each point.
3. The user then selects from a menu of computations:
   a. The K value of the curve, representing the horizontal distance required for a 1 percent change in grade.
   b. The coordinates of any point on the curve, given its x coordinate.
   c. The vertical offset at the point of intersection of the two tangents.
   d. The vertical offset at a specific point on the curve, given its x coordinate.
   e. The horizontal and vertical offsets at the highest or lowest point on the curve.
4. The user can repeat this selection for multiple computations in the same session before exiting. All computations use standard parabolic vertical curve formulas, with distances measured in meters.

Super_Elevation_Estimation_for_Highway_Curve.py:

1. This program estimates the required superelevation and checks the safety of a highway curve, based on the model prescribed by IRC:73-2023.
2. The user enters the design speed and radius of curvature, along with the desired superelevation, either the common default value of 0.07 or a custom value, which is checked against a practical upper limit.
3. The program computes the theoretically required superelevation and compares it against the desired value, capping it at the desired value if the theoretical requirement is lower, or stopping with an estimate if the theoretical requirement is lower than what can be practically achieved.
4. Using the resulting superelevation, the program computes the required coefficient of side friction and compares it against a chosen value, either the common default value of 0.15 or a custom value, declaring the design safe if within limits, or otherwise computing the maximum safe speed for the curve and reporting whether the original design speed is adequate or should be limited.
