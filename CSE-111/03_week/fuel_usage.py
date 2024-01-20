"""
Name: Collin Nunnally
Class: CSE-111
Comments:
Write a Python program that asks the user for three numbers:

1. A starting odometer value in miles
2. An ending odometer value in miles
3. An amount of fuel in gallons

Your program must calculate and print fuel efficiency in both miles per gallon and liters per 100 kilometers. Your program must have three functions named as follows:

1. main
2. miles_per_gallon
3. lp100k_from_mpg

mpg = end − start / gallons
lp100k = 235.215 / mpg

Ex. Output:
> python fuel_usage.py
Enter the first odometer reading (miles): 30462
Enter the second odometer reading (miles): 30810
Enter the amount of fuel used (gallons): 11.2
31.1 miles per gallon
7.57 liters per 100 kilometers
"""
def cdn_get_inputs():
    start = float(input("Enter the first odometer reading (miles): "))
    end = float(input("Enter the second odometer reading (miles): "))
    gallons = float(input("Enter the amount of fuel used (gallons): "))
    return start, end, gallons
def cdn_miles_per_gallon(start, end, gallons):
    mpg = (end - start) / gallons
    print(f"{mpg:.1f} miles per gallon")
    return mpg
def cdn_lp100k_from_mpg(mpg):
    lp100k_from_mpg = (235.215 / mpg)
    print(f"{lp100k_from_mpg:.1f} liters per 100 kilometers")
    return lp100k_from_mpg

def main():
    start, end, gallons = cdn_get_inputs()
    mpg = cdn_miles_per_gallon(start, end, gallons)
    cdn_lp100k_from_mpg(mpg)

main()