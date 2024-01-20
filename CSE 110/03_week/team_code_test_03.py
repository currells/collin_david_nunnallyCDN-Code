"""
Author: Unathletic Avengers
File: random_03.py
Square—The area is the length of a side squared.

Rectangle—The area is the length multiplied by the width.

Circle—The area is Pi (you can use 3.14) multiplied by the radius squared.
"""

# win + . to insert emojis, gifs, etc.
import math
print("\nArea of a square: (⓿_⓿)")
side = float(input("What is the length of the side? "))
a_square = (side ** 2)
print(f"\nThe area of the square is: {a_square}.\n")

print("Area of a rectangle: (●__●)")
length = float(input("What is the length? "))
width = float(input("What is the width? "))
a_rectangle = (length * width)
print(f"\nThe area of the square is : {a_rectangle}.\n")

print("Area of a circle: (┬┬﹏┬┬)")
radius = float(input("What is the radius? "))
a_circle = (math.pi) * (radius ** 2)
print(f"\nThe area of the circle is: {a_circle}.\n")

print("Compute single length value:✍️ (◔ ◡ ◔)")
value = float(input("What is the value? "))
a1_square = (value ** 2)
a1_circle = (math.pi) * (value ** 2 )
v_cube = (value ** 3)
v_sphere = 4 * (math.pi) * (value ** 2)
print(f"\nThe area of the square is: {a1_square}.\n")
print(f"The area of the circle is: {a1_circle}.\n")
print(f"The volume of the cube is: {v_cube}.\n")
print(f"The volume of the sphere is: {v_cube}.\n")


