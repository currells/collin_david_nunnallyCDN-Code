"""
Author:
File:
Description:
What is the temperature? 8
Fahrenheit or Celsius (F/C)? F
At temperature 8.0F, and wind speed 5 mph, the windchill is: -1.11F
"""

def cel_to_far(cel):
    return cel * 1.8 + 32

def wind_chill(temp, speed):
    return 35.74 + 0.6215 * temp - 35.75 * (speed * 0.16) + 0.4275 * temp * (speed ** 0.16)

temp = float(input("What is the temperature: "))
symbol = input("Fahrenheit or Celsius?[F / C] ").strip().upper()

if symbol == "C":
    temp = cel_to_far(temp)

for wind_speed in range(5, 61, 5):
    wc = wind_chill(temp, wind_speed)

    print(f"at temperature {temp}F, and wind speed is {wind_speed} mph, the windchill is: {wc:.2f}F")


# wind chill:35.74 + 0.6215T - 35.75(V0.16) + 0.4275T(V0.16)

#01. Write a function to calculate and return the wind chill based on a given temperature and wind speed.

#02. Write a function to convert from Celsius to Fahrenheit. The formula for this conversion is to multiply the Celsius temperature by (9/5) and then add 32.

#03. Allow the user to enter the temperature in Celsius of Fahrenheit. If they provide it in Celsius, first convert it to Fahrenheit before using the formula above.

#04. Loop through wind speeds from 5 to 60 miles per hour, incrementing by 5, and calculate and display the wind chill for each of these wind speeds.

#05. Display the wind chill value to 2 decimals of precision.