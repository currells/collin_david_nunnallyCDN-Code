"""
Author: Unathletic Avengers
File: 13_team.py
Description:
Using functions to calaculate areas square, rectangle, and circle.
"""

print("""
                             .!!!!.               
                            .&@@@@^               
                       ... ^&@@@@@^               
                 ^JG#&&&&&&@@@@@@@:               
              !B@&BJ~:.  J@@@@@@@@#!              
            J&@P^       J@@@@?&@@@#@&J            
          ^&@5.        5@@@&^ &@@@: 5@&^          
         7@@^         G@@@&.  &@@@^  ^@@7         
        ^@@:        .#@@@#.   @@@@^   :@@^        
        #@J        .&@@@G     7G@@^    J@#        
       .@@.       :&@@@@J????JBJ!Y:    .@@.       
       :@@.      ~@@@@@@@@@@@@@@&7     .@@:       
        &@!     7@@@@PJYYYYYY5#Y!J.    !@&        
        ?@&    J@@@@!         !P&@^    &@?        
         P@B  5@@@&^          @@@@^   B@P         
          57 G@@@&:           &@@@: ~&@Y          
            B@@@#.               .!#@#^           
          .&@@@B ~?:          :7G&@G^             
         .B&&&P  Y#&&&#BGGB#&&&#5~                
                    .^~!77!~^.     

                 Avengers Assemble                          
                                                            """)

import math

# Computes the area of a square using the side variable. Stretch 01. using the rectange definition to compute the square definition
def compute_area_square(side):
  return compute_area_rectangle(side, side)

# Computes the area of a rectangle using two perameters
def compute_area_rectangle(length, width):
  return length * width

# Computes the area of a circle using the user given radius
def compute_area_circle(radius):
  return math.pi * radius**2

# Determine if the user is computing a square or circle and call the appropriate function
def compute_area(shape, measurement, measurement_2):
  if shape == 'circle':
    return compute_area_circle(measurement)
  elif shape == 'rectangle':
    return compute_area_rectangle(measurement, measurement_2)
  else:
    return compute_area_square(measurement)
  

# Sets shape so while loop will run
shape_category = ""

# Until the user types "quit" continue to compute the shape they give
while shape_category != "quit":
  shape_category = input("What kind of shape are you wanting to compute? ").lower()
  # Asks for the radius of the circle and calls the circle function to complete the math
  if shape_category == "circle":
    radius = int(input("What is the radius of the circle? "))
    circle_area = compute_area(shape_category, radius, 1)
    print(circle_area)
  # Asks for the side of the square then calls the rectangle function to complete the square math
  elif shape_category == "square":
    side = int(input("What is the side? "))
    square_area = compute_area(shape_category, side, 1)
    print(square_area)
  # Asks user for the length and width then calls the rectangle function to complete the math
  elif shape_category == "rectangle":
    length = int(input("What is the length? "))
    width = int(input("What is the width? "))
    rectangle_area = compute_area(shape_category, length, width)
    print(rectangle_area)
  elif shape_category == "quit":
    break
  # If the user gives a shape that isn't sqaure, rectangle, or circle, ask them for the shape again
  else:
    print("Please return a circle, square, or rectangle.")
    continue
print("Have a great day, Avenger! 😆")