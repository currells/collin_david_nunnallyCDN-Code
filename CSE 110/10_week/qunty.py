cart   = ["Eggs", "Milk", "Bread", "Bananas", "Cheddar"]
prices = [4.99, 3.85, 5.99, 7.15, 1333.00]
qty = [2, 2, 3, 1, 5]

for i in range(len(cart)):
    smile = qty[i]
    item = cart[i]
    cost = prices[i] * smile
    print(f"[{i + 1}] {item:.<10}x {smile:<3}${cost:,.2f}")