"""
Author: Collin Nunnally
File: prove.py

Creating a shopping cart where user can add / remove items, see contents, and see total of items.
"""
import math
menu =["Add item", "Remove item", "See contents", "See total", "Quit"]
cart = []
prices = []
total = 0


while True:
# Printing the available items
    for i, menu_item in enumerate(menu):
        print(f"[{i + 1}] {menu_item}")
    print(menu_item)
    option = input("What would you like to do? ").strip()
    if option == "1":
        add = input("What item would you like to add? ")
        cart.append(add.capitalize())
        cost = float(input(f"What is the cost of <{add.capitalize()}>? Ex.[3.23] "))
        prices.append(cost)
    elif option == "2":
        take_out = input.capitalize("What item would you like to take out? ")
        if take_out in cart:
            cart.remove(take_out)
        else:
            print("Item is not in cart. ")
    elif option == "3":
        print("Your current cart:")
        for i, ind_item in enumerate(cart):
            ind_item = cart[i]
            ind_price = prices[i]
            print(f"{i + 1}. {ind_item} - ${ind_price}")
    elif option == "4":
            total = math.fsum(prices)
            print(f"\nTotal: {total}\n")
    elif option == "5": # Sets running to false, not making the while loop run
        break
    else:
        print("Please choose a valid option.😡")

print("Have a great day! 😉")


"""
for i, s_letter in enumerate(secret_word):
guess_letter = guess[i]
secret_letter = secret_word[i]
print(f"{secret_letter} <> {guess_letter}")
"""

'''
single_item = cart[i]
single_price = prices[i]
'''