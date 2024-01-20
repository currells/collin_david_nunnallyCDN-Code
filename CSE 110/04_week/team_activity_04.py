"""
Author: Unathletic Avengers 
File: team_activity_04.py

Convert v(t) = sqrt(mg/c) * (1 - exp((-sqrt(mgc)/m)t)) into code
Compute c with c = (1 / 2) * p * A * C [c is 3 decimals]
Display overall velocity
"""
import math
# White is to distinguish TIPs shown as white
# Blue is to show the answers at the end of the output as blue
# Gray reverts the terminal color back to gray after color is used
white = "\033[0;37m"
gray = "\033[39m"
blue = "\033[0;34m"

print("\nVelocity Calculator:\n")

m = float(input("What is the mass (kg)? "))
print(f"{white}TIP: In m/s^2, Earth is 9.8, Jupiter is 24.{gray}")
g = float(input("What is the gravity acceleration (m/s^2)? "))
t = float(input("What is time (sec)? "))
print(f"{white}TIP: In kg/m^3, air is 1.3 and water is 1000.{gray}")
p = float(input("What is the Density of the fluid (kg/m^3)? "))
a = float(input("What is the Cross sectional Area (m^2)? " ))
print(f"{white}TIP: A Sphere is 0.5, and a Cylinder is 1.1.{gray}")
upp_c = float(input("What is the Drag Constant? "))

# Equations for Lower c, velocity, and Terminal Velocity
low_c = (1/2) * p * a * upp_c
v = math.sqrt(m * g / low_c) * (1 - math.exp((-math.sqrt(m * g * low_c) / m) * t))
v_term = math.sqrt(m * g / low_c)

# Rounding answers after the calculations for the user
v = round(v, 3)
low_c = round(low_c, 3)
v_term = round(v_term, 3)

# Final statements printed into blue
print(f"\n{blue}Inner c value: {low_c}.")
print(f"Velocity after {t} seconds is: {v}.")
print(f"The Terminal Velocity is: {v_term}.{gray}\n")