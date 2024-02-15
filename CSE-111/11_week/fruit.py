"""
Name: Collin Nunnally
Class: CSE-111
Comments:
Some code copied from 12 Checkpoint page on Canvas
"""
def main():
    # Create and print a list named fruit.
    fruit_list = ["pear", "banana", "apple", "mango"]
    print(f"original: {fruit_list}")
    fruit_list.reverse() # Reverse the order of the list
    print(f"Reverse fruit_list: {fruit_list}")
    fruit_list.append("orange") # Adding "orange" at the end of the list
    print(f"Orange added: {fruit_list}")
    find_apple = fruit_list.index("apple") # Inserting "cherry" after apple
    fruit_list = fruit_list[:find_apple] + ["cherry"] + fruit_list[find_apple:]
    print(f"Cherry added: {fruit_list}")
    fruit_list.remove("banana") # Removing "banana" from the list
    print(f"Banana removed: {fruit_list}")
    popped_fruit = fruit_list.pop() # Printing the last fruit in the list 
    print(f"Popped fruit: {popped_fruit}")
    fruit_list.sort() # Sorting the list alphabetically
    print(f"Sorted fruit_list: {fruit_list}")
    fruit_list.clear() # Clearing the list 
    print(f"Cleared fruit_list: {fruit_list}")

main()