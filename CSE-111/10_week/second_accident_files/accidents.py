"""
Name: Maidens of Mayhem (BC, CN, PT, JH, ZM)
Class: CSE-111
Comments:
Outline from team activity page.
"""
import csv

YEAR_COLUMN = 0
FATALITIES_COLUMN = 1
INJURIES_COLUMN = 2
CRASHES_COLUMN = 3
FATAL_CRASHES_COLUMN = 4
DISTRACT_COLUMN = 5
PHONE_COLUMN = 6
SPEED_COLUMN = 7
DUI_COLUMN = 8
FATIGUE_COLUMN = 9

def main():
    filename = input("Name of file that contains NHTSA data: ")
    try: # This big try statement will check for a FileNotFoundError and ValueError.
        with open(filename, "rt") as text_file:
            perc_reduc = float(input("Percent reduction of texting while driving [0, 100]: "))
            if perc_reduc <= 0: # Checks for values that are less than 0
                print(f"Error: {perc_reduc} is too low. Please enter a different number.")
            elif perc_reduc >= 100: # Checks for values that are greater than 100
                print(f"Error: {perc_reduc} is too high. Please enter a different number.")
            else:
                print()
                print(f"With a {perc_reduc}% reduction in using a cell",
                      "phone while driving, approximately the",
                      "following number of injuries and deaths",
                      "would have been prevented in the USA.", sep="\n")
                print()
                print("Year, Injuries, Deaths")
                reader = csv.reader(text_file)
                next(reader)
                for row in reader:
                    year = row[YEAR_COLUMN]
                    injur, fatal = estimate_reduction(row, PHONE_COLUMN, perc_reduc)
                    print(year, injur, fatal, sep=", ")
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        print("Please choose a different file.")
    except ValueError:
        print(f"Error: could not convert string to float.")

def estimate_reduction(row, behavior_key, perc_reduc):
    behavior = int(row[behavior_key])
    fatal_crashes = int(row[FATAL_CRASHES_COLUMN])
    if fatal_crashes == 0:
        ratio = 0
    else:
        ratio = perc_reduc / 100 * behavior / fatal_crashes

    fatalities = int(row[FATALITIES_COLUMN])
    injuries = int(row[INJURIES_COLUMN])

    reduc_fatal = int(round(fatalities * ratio, 0))
    reduc_injur = int(round(injuries * ratio, 0))
    return reduc_injur, reduc_fatal

if __name__ == "__main__":
    main()
