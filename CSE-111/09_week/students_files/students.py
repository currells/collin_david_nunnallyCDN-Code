"""
Name:
Class:
Comments:
Goes through a .csv file

1. Open the students.csv file for reading, skip the first line of text in the file because it contains only headings, and read the other lines of the file into a dictionary. The program must store each student I-Number as a key and each I-Number name pair or each name as a value in the dictionary.
2. Get an I-Number from the user, use the I-Number to find the corresponding student name in the dictionary, and print the name.
3. If a user enters an I-Number that doesn’t exist in the dictionary, your program must print the message, "No such student" (without the quotes).
"""

I_NUMBER_INDEX = 0
NAME_INDEX = 1

def read_dictionary(filename):
    dict_students = {}
    with open("students.csv", "r") as students_file:
        next(students_file) # Skips first line in students.csv
    
        for row in students_file:
            columns = row.strip().split(",") 
            i_number = columns[I_NUMBER_INDEX]
            name = columns[NAME_INDEX] # Defines the columns with a name
            dict_students[i_number] = name 
    return dict_students # Groups the i-number with the name and returns the created dictionary

def main():
    get_i_num = input("I-Number: ")

    dict_students = read_dictionary("students.csv") # Able to use the created dictionary

    if get_i_num in dict_students:
        print(f"Your name is {dict_students[get_i_num]}.") # Checks to see if the i-number is in the dict, and if it is, returns the name with it
    else:
        print("No such student")

main()