"""
Author: Collin Nunnally
File: testing.py


"""
# TYPE_A = "electric"
# TYPE_B = "rock"

# ATK_A1 = "thunderbolt"
# ATK_B1 = "boulder"

# ATK_TYPE = "damage"

# DOG_A = "flash"
# DOG_B = "side eyes"

# CON_A = True
# CON_B = False

# if ATK_TYPE == "damage" and CON_A == False:
#     pass # Damage
# else:
#     pass # Defense


# if not CON_A == False:
#     pass # Not confused
# else:
#     pass

red = "\033[0;31m"
green = "\033[0;32m"
gray = "\033[39m"


yes = ("You passed! 😄")
no = ("You did not pass. 🥺")
yes = (f"{green}{yes}{gray}") 
no = (f"{red}{no}{gray}")

print(f"{yes}")
print(f"{no}")