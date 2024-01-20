cart   = ["Eggs", "Milk", "Bread", "Bananas", "Cheddar"]

while True:
    # Show the cart to the use with 0 based index numbers:
    for i, item in enumerate(cart):
        print(f"[{i}] {item}")

    # Ask the user if the would like to edit the cart
    answer = input("Would you like to edit the cart?[Yes/No] ").lower()

    # If no, break loop
    if answer == "no":
        break

    # Ask the user what they would like to edit
    index = int(input("What item would you like to change? (number) "))

    # Ask user for the new item
    new_item = input("What is the new item? ")

    # Update the cart
    cart[index] = new_item
