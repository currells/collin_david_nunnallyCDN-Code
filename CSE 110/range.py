# Author: Brother Keers

cart   = ["Eggs", "Milk", "Bread", "Bananas", "Cheese"]
prices = [4.99, 3.85, 5.99, 7.15, 13.00]

print("[EXAMPLE 1]")

# We can always iterate (loop) through a list by its indexes.
for i in range(len(cart)):
    item = cart[i] # We can pull items out if the list to use them foe something.
    print(f"{i + 1}. {item}")

print(f"\n{'-' * 30}\n\n[EXAMPLE 2]")

# When you know that you need the index number and its value enumerate can help.
for i, item in enumerate(cart):
    print(f"{i + 1}. {item}")

print(f"\n{'-' * 30}\n\n[EXAMPLE 3]")

"""
There is no real difference between range(len()) and enumerate() in most cases.
When you know that you are going to iterate (loop) through multiple lists at the
same time using index numbers and directly access them is slightly more efficient.
"""
for i in range(len(cart)): # Both (or all) lists must have the same length...
    # ...if both (or all) list do not we can run into an index error.
    item = cart[i]
    cost = prices[i]
    print(f"{i + 1}. {item:<10} ${cost:.2f}")
