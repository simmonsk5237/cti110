# Kimberly Simmons
# Date: 03/09/2025
# Assignment: P2LAB1
# This program calculates and displays the diameter, circumference, and area of a circle.

import math

radius = float(input("What is the radius of the circle? "))

diameter = 2 * radius
circumference = 2 * math.pi * radius
area = math.pi * radius ** 2

print(f"\nThe diameter of the circle is {diameter:.1f}")
print(f"The circumference of the circle is {circumference:.2f}")
print(f"The area of the circle is {area:.3f}")
