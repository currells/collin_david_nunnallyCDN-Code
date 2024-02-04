NAME_INDEX = 0
GENDER_INDEX = 1
BIRTH_YEAR_INDEX = 2
DEATH_YEAR_INDEX = 3

HUSBAND_KEY_INDEX = 0
WIFE_KEY_INDEX = 1
WEDDING_YEAR_INDEX = 2

gray = "\033[39m"
red = "\033[0;31m"
green = "\003[0;32m"
white = "\033[0;37m"
blue = "\033[0;34m"


def main():
    people_dict = {
        "P143": ["Lola Park", "F", 1663, 1706],
        "P338": ["Savanna Foster", "F", 1674, 1723],
        "P201": ["Tiffany Hughes", "F", 1689, 1747],
        "P203": ["Ignacio Torres", "M", 1693, 1758],
        "P128": ["Yasmin Li", "F", 1701, 1716],
        "P342": ["Trent Ross", "M", 1705, 1757],
        "P202": ["Samyukta Nguyen", "M", 1717, 1774],
        "P132": ["Joel Johnson", "M", 1724, 1800],
        "P445": ["Whitney Nelson", "F", 1757, 1823],
        "P318": ["Khalid Ali", "M", 1759, 1814],
        "P317": ["Davina Patel", "F", 1775, 1860],
        "P313": ["Enzo Ruiz", "M", 1782, 1782],
        "P475": ["Lauren Smith", "F", 1800, 1802],
        "P455": ["Lucas Ross", "M", 1800, 1853],
        "P435": ["Jamal Gray", "M", 1810, 1831],
        "P204": ["Fatima Soares", "F", 1812, 1898],
        "P206": ["Ephraim Foster", "M", 1831, 1885],
        "P500": ["Peter Price", "M", 1832, 1878],
        "P207": ["Rosalina Jimenez", "F", 1875, 1956],
        "P425": ["Rachel Johnson", "F", 1876, 1940],
        "P121": ["Vanessa Bennet", "F", 1880, 1960],
        "P152": ["Jose Castillo", "M", 1884, 1931],
        "P205": ["Liam Myers", "M", 1902, 1950],
        "P465": ["Isabella Lopez", "F", 1907, 1959],
        "P168": ["Megan Anderson", "F", 1909, 1945]
    }

    marriages_dict = {
        "M48": ["P203", "P201", 1711],
        "M45": ["P342", "P338", 1722],
        "M36": ["P203", "P201", 1724],
        "M47": ["P202", "P445", 1774],
        "M21": ["P132", "P445", 1775],
        "M59": ["P132", "P317", 1792],
        "M63": ["P318", "P445", 1804],
        "M12": ["P318", "P317", 1808],
        "M54": ["P435", "P204", 1830],
        "M34": ["P455", "P204", 1853],
        "M55": ["P500", "P317", 1859],
        "M52": ["P206", "P204", 1875],
        "M78": ["P152", "P121", 1905],
        "M50": ["P152", "P425", 1917],
        "M64": ["P205", "P465", 1925],
        "M62": ["P152", "P207", 1925],
        "M70": ["P152", "P168", 1928]
    }

    print_death_age(people_dict)
    print(f"{red}Ages at Death{gray}")
    for person_key, details in people_dict.items():
        name = details[NAME_INDEX]
        birth_year = details[BIRTH_YEAR_INDEX]
        death_year = details[DEATH_YEAR_INDEX]

        age_at_death = death_year - birth_year
        print(f'{name} {age_at_death}')

    print()

    count_genders(people_dict)
    male_count = 0
    female_count = 0

    for details in people_dict.values():
        gender = details[GENDER_INDEX]

        if gender == "F":
            female_count += 1
        elif gender == "M":
            male_count += 1

    print(f"{blue}Genders{gray}")
    print(f"Number of males: {male_count}")
    print(f"Number of females: {female_count}")

    print()

    print_marriages(marriages_dict, people_dict)
    print(f"{white}Marriages{gray}")
    for marraige_key, details in marriages_dict.items():
        husband = details[HUSBAND_KEY_INDEX]
        wife = details[WIFE_KEY_INDEX]
        marriage = details[WEDDING_YEAR_INDEX]

        if husband in people_dict and wife in people_dict:
            husband_details = people_dict[husband]
            husband_name = husband_details[NAME_INDEX]
            husband_birth_year = husband_details[BIRTH_YEAR_INDEX]

            wife_details = people_dict[wife]
            wife_name = wife_details[NAME_INDEX]
            wife_birth_year = wife_details[BIRTH_YEAR_INDEX]

            wife_age_at_marriage = marriage - wife_birth_year
            husband_age_at_marriage = marriage - husband_birth_year
            print(f'{husband_name} {husband_age_at_marriage} > {marriage} < {wife_name} {wife_age_at_marriage} ')

def print_death_age(people_dict):
    """For each person in the people dictionary,
    print the person's name and age at death.

    Parameter
        people_dict: a dictionary that contains data about people
            Each item in the dictionary is in this format:
            person_key: [name, gender, birth_year, death_year]
    Return: nothing
    """
    pass


def count_genders(people_dict):
    """Count and print the number of males
    and females in the people dictionary.

    Parameter
        people_dict: a dictionary that contains data about people
            Each item in the dictionary is in this format:
            person_key: [name, gender, birth_year, death_year]
    Return: nothing
    """
    pass


def print_marriages(marriages_dict, people_dict):
    """For each marriage in the marriages dictionary, print
    the husband's name, his age at wedding, the wedding year,
    the wife's name, and her age at wedding.

    Parameters
        marriages_dict: a dictionary that contains data about
            marriages. Each item in the dictionary is in this format:
            marriage_key: [husband_key, wife_key, wedding_year]
        people_dict: a dictionary that contains data about people
            Each item in the dictionary is in this format:
            person_key: [name, gender, birth_year, death_year]
    Return: nothing
    """
    pass
  
if __name__ == "__main__":
    main()
