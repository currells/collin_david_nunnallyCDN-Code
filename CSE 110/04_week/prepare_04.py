"""
Author: Collin Nunnally
File: prepare_04.py
Going over 04 Prepare: Preparation Material
"""

import math as math #Have the imports at the top

#Examples of math

# math.sqrt(x)

# math.exp(x) or num ** 2


fahrenheit = float(input("What is the temperature today in °F? "))

celsius = (fahrenheit - 32) * 5 / 9
celsius = round(celsius, 1)
# Calculated the °F to °C, then made it only have 2 decimals

print(f"Temperature in Celsius: {celsius}") #Can put the round at the end print statement

# # v(t) = sqrt(mg/c) * (1-exp((-sqrt(mgc)/m)t))
# v = math.sqrt(m * g / c) * (1 - math.exp((-math.sqrt(m * g * c)) / m) * t)
