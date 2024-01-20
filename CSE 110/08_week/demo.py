# Prepare demo 1:
items = ["crayon", "scissors", "paper", "glitter glue", "markers", "pens"]
for item in items:
    print(f"The item is: {item}")
# Prepare demo 2 & 3:
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# numbers = range(10)
# numbers = range(1,10,2)
for number in numbers:
    print(number)
# Prepare demo 4:
"""
A loop will blindly repeat any code that is in its body. That code could include if statement, mathematics, new variable definitions, or anything else—including other loops!
"""
for i in range(5):
    print(i)
    for j in range(10, 13):
        print(f"--{j}")