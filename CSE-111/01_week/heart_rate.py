"""
Name: Collin Nunnally
Class: CSE-111
Comments:
Asks person's age, compute fastest and slowest heart rate.

When you physically exercise to strengthen your heart, you
should maintain your heart rate within a range for at least 20
minutes. To find that range, subtract your age from 220. This
difference is your maximum heart rate per minute. Your heart
simply will not beat faster than this maximum (220 - age).
When exercising to strengthen your heart, you should keep your
heart rate between 65% and 85% of your heart’s maximum rate.
"""

age = int(input("What is your age?(Ex. 20) "))

max_rate = int(220 - age)
lower_range = int(max_rate * 0.65)
upper_range = int(max_rate * 0.85)

print(f"With your age being {age}, you should maintain a range of {lower_range} and {upper_range}.")