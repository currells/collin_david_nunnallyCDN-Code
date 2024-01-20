"""
Author: Collin Nunnally
File: prove.py
Description:
Taking "life-expectancy.csv" and interpreting the data set
"""
# ['Entity', 'Code', 'Year', 'Life expectancy (years)']

import statistics

NAME_INDEX = 0
CODE_INDEX = 1
YEAR_INDEX = 2
EXP_INDEX  = 3

lowest_country = ""
lowest_abbreviation = ""
lowest_year = 99999
lowest_expectancy = 99999

highest_country = ""
highest_abbreviation = ""
highest_year = 0
highest_expectancy = 0

input_lowest_country = ""
input_lowest_abbreviation = ""
input_lowest_expectancy = 99999

input_highest_country = ""
input_highest_abbreviation = ""
input_highest_expectancy = 0

country_highest_expectancy = 0
country_lowest_expectancy = 99999
country_expectancy_list = []
country_expectancy_average = 0


year_input = int(input("\nEnter a year of interest: "))
country_input = input("\nEnter a country of interest: ")

with open("life-expectancy.csv", "r") as expectancy_file:
    next(expectancy_file) # Skips first line in .csv file

    for row in expectancy_file: # Defines variables in data set, makes columns from data
        columns = row.strip().split(",")
        country = columns[NAME_INDEX]
        abbreviation = columns[CODE_INDEX]
        year = int(columns[YEAR_INDEX])
        expectancy = float(columns[EXP_INDEX])

        if expectancy < lowest_expectancy: # Grabs data for lowest life expectancy in dataset
            lowest_country = country
            lowest_abbreviation = abbreviation
            lowest_year = year
            lowest_expectancy = expectancy
        if expectancy > highest_expectancy: # Grabs data for highest life expectancy in dataset
            highest_country = country
            highest_abbreviation = abbreviation
            highest_year = year
            highest_expectancy = expectancy

        if year == year_input:
            if expectancy < input_lowest_expectancy: # Grabs data for lowest data for user input
                input_lowest_country = country
                input_lowest_abbreviation = abbreviation
                input_lowest_expectancy = expectancy
            if expectancy > input_highest_expectancy: # Grabs data for highest data for user input
                input_highest_country = country
                input_highest_abbreviation = abbreviation
                input_highest_expectancy = expectancy

        if country == country_input: # Allow the user to type in a country, then show the minimum, maximum, and average life expectancy for that country.
            country_expectancy_list.append(expectancy)
            country_expectancy_average = statistics.mean(country_expectancy_list)

            if expectancy < country_lowest_expectancy:
                country_lowest_expectancy = expectancy
            if expectancy > country_highest_expectancy:
                country_highest_expectancy = expectancy

if lowest_expectancy != 99999 or highest_expectancy != 0 or input_lowest_expectancy != 99999 or input_highest_expectancy != 0:
    # What is the year and country that has the lowest life expectancy in the dataset?
    print(f"\nThe overall minimum life expectancy is in {lowest_country} [{lowest_abbreviation}], in {lowest_year} with {lowest_expectancy}(years)")
    # What is the year and country that has the highest life expectancy in the dataset?
    print(f"The overall maximum life expectancy is in {highest_country} [{highest_abbreviation}], in {highest_year} with {highest_expectancy}(years)\n")

    # Allow the user to type in a year, then, find the average life expectancy for that year. Then find the country with the minimum and the one with the maximum life expectancies for that year.
    print(f"For {year_input}, minimum life expectancy is in {input_lowest_country} [{input_lowest_abbreviation}], with {input_lowest_expectancy}(years)")
    print(f"For {year_input}, maximum life expectancy is in {input_highest_country} [{input_highest_abbreviation}], with {input_highest_expectancy}(years)\n")

    print(f"For the country you input, {country_input}, the minimum expectancy is {country_lowest_expectancy}, the maximun expectancy is {country_highest_expectancy}, and the average is {country_expectancy_average}")
else:
    print(f"There is no data for {year_input}. Try another year!")