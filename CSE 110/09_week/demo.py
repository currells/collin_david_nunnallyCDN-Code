letters = ["A", "B", "C", "D", "E", "F", "G"]

letters.remove("C")
# Removes "C" from the list letters

value = letters.pop(2)
# Pop will take the first 2 values and store the values into the variable

vayed = letters.pop(len(letters) - 1)
# Takes the last number and stores the value to "vayed"

count = letters.pop(-3) # Takes the 3rd to last number and stores the value to "count"

del letters[1] # Deletes 2nd value
del letters[-3] # Deletes 3rd to last value in the "letters" list

del letters[1:-1] # Deletes every value besides 1st and last value in "letters"

del letters[1:] # Every value besides 1st

try:
    ...
except:
    ...
# Try will run and if there is an error, it will run except line.

