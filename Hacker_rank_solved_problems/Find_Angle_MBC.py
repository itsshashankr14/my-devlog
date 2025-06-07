# Given two sides AB and BC of a right triangle with right angle at B,
# find the angle MBC in degrees, where M is the midpoint of hypotenuse AC.
# Output the angle rounded to the nearest integer, followed by the degree symbol.

import math

ab = int(input())
bc = int(input())

angle_rad = math.atan2(ab, bc)
angle_deg = math.degrees(angle_rad)

print(f"{round(angle_deg)}\u00B0")