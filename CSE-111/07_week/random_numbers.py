import random


def append_random_numbers(numbers, quantity=1):


    for x in range(quantity):

        number = random.uniform(0.0, 100.0) 
        numbers.append(round(number, 1))

    return numbers

def main():
    numbers = []
    print(numbers)

    append_random_numbers(numbers)
    print(numbers)

    append_random_numbers(numbers, 3)
    print(numbers)
    return numbers


main()