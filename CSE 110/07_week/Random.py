import random

number = random.randint(1, 100)

guess = -1

while guess != number:
    # Get the users guess.
    guess = int(input("Please guess the number: "))

    if guess < 1 or guess > 100:
        print("You guessed outside the range!")
        # Stop here! Restart the loop because the number is outside the range.
        continue

    if guess == number:
        print("You guessed it!")
        break

    if guess < number:
        ...
    else:
        ...
