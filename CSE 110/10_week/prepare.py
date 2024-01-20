"""
Author: Collin Nunnally
File: prepare.py

Looping through a list; being able to update a list
"""
cart = []
# Loop through the items in the regular way (for example, for thing in the_list) and display each one to make sure you have the initial list built correctly.
print("Please enter the items of the shopping list. Type [Quit] to finish.\n")
while True:
    addition = input("Item: ").capitalize()
    if addition == "Quit":
        break
    cart.append(addition)

while True:
    print("\nThe shopping list is:")
    for i in range(len(cart)):
        ind_item = cart[i]
        print(f"{ind_item}")

    print("\nThe shopping cart with indexes is:")
    for i in range(len(cart)):
        ind_item = cart[i]
        print(f"{i}. {ind_item}")

    update = input("\nWould you like to update the cart? [Yes / No] ").capitalize()

    if update == "No":
        break

    index = int(input("\nWhat item number would you like to update? "))

    new_item = input("\nWhat is the new item? ")

    cart[index] = new_item

