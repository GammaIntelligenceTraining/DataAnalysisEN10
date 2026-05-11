# Create two empty lists (long_names, short_names)
# Iterate through names list and add names that are longer than 5 characters
# to long_names, and others to short names
names = ['Sarah', 'Jessica', 'Anthony', 'Jack', 'Simon', 'Arthur', 'Maria', 'Samantha']

long_names, short_names = [], []

for name in names:
    if len(name) > 5:
        long_names.append(name)
    else:
        short_names.append(name)

print('Long', long_names)
print('Short', short_names)


# Given a list where each element is a year. Determine whether the given year is a leap year. 
# If the year is a leap year,
# print YES, otherwise print NO. According to the Gregorian calendar, 
# a year is a leap year if its number is a multiple of 4,
# but not a multiple of 100 OR if it is a multiple of 400.
years_list = [2012, 2011, 1492, 1861, 1600, 1700, 1800, 1900, 2000]

for year in years_list:
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        print(year, 'is a leap year')
    else:
        print(year, 'is not a leap year')



# Write a program that prompts the user for a string and checks if the string contains only unique characters.
user_input = input('Enter something: ')
if len(user_input) == len(set(user_input)):
    print("\"" + user_input + "\" contains unique characters only")
else:
    print("\"" + user_input + "\" non unique characters")

# Write a program that checks gender for each person.
# If person is a male, print "This is NAME SURNAME. He is AGE years old"
# If person is a female, print "This is NAME SURNAME. She is AGE years old"
people = [
    ('Jane', 'Smith', 26, 'Female'),
    ('Jack', 'Green', 30, 'male'),
    ('Maria', 'Gold', 29, 'female'),
    ('Simon', 'Bloom', 35, 'Male'),
]
for name, surname, age, gender in people:
    # pronoun = ''
    # if gender.lower() == 'male':
    #     pronoun = 'He'
    # else:
    #     pronoun = 'She'
    # print(f'This is {name} {surname}. {pronoun} is {age} years old.')
    print(f'This is {name} {surname}. {'He' if gender.lower() == 'male' else 'She'} is {age} years old.')


# For each student print a message
# Example:
#   "Students name: Bob Green. Students courses: physics, geography, math."

students = [
    {
        "name": "Jack",
        "surname": "Smith",
        "courses": [
            "Math",
            "Physics",
            "Chemistry",
        ],
    },
    {
        "name": "Sarah",
        "surname": "Brown",
        "courses": [
            "Art",
            "Spanish",
            "Geography",
        ],
    },
    {
        "name": "Maria",
        "surname": "Gold",
        "courses": [
            "English",
            "Literature",
            "History",
        ],
    },
]

for student in students:
    print(f'Student name: {student['name']}' \
          f' {student['surname']}. Student courses: {', '.join(student['courses']).lower()}.')