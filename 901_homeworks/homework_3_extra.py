# Convert this string to all uppercase
# Then, replace 'PYTHON' with 'CODING'
text = "learning python is fun"

text = text.upper().replace('PYTHON', 'CODING')
print(text)


# Given this messy string, extract only the numbers using slicing
# Hint: You want '12345'
serial_number = "ID-12345-X"
print(serial_number[3:-2])


# Create a single string that looks like a 3x3 grid of 'X' using only one variable and line breaks
# X X X
# X X X
# X X X

grid = 'X X X\n' * 3
print(grid)


# 1. Sort this list alphabetically
# 2. Print the very last name in the sorted list
# 3. Count how many times 'Apple' appears in the list
fruits = ['Orange', 'Apple', 'Banana', 'Apple', 'Kiwi']
fruits.sort()
print(fruits[-1])
print(fruits.count('Apple'))


# Remove 'Bread' from the list using a method
# Add 'Eggs' to the beginning of the list
grocery_list = ['Milk', 'Bread', 'Butter']
grocery_list.remove('Bread')
grocery_list.insert(0, 'Eggs')
print(grocery_list)


# Find elements that are in group_a OR group_b, but NOT in both.
group_a = {"Admin", "Editor", "Viewer"}
group_b = {"Admin", "SuperUser", "Guest"}

print(group_a.symmetric_difference(group_b))


# Find the highest and lowest number in this tuple
# Calculate the average of these numbers (sum divided by length)
scores = (88, 92, 78, 95, 84)
print('lowest', min(scores))
print('highest', max(scores))
print('average', sum(scores) / len(scores))

# You have a list with duplicates. 
# Convert it to a type that removes duplicates, then back to a list.
# Sort the final list.
points = [10, 20, 10, 30, 40, 20, 50]
points = list(set(points))
points.sort()
print(points)


# EXTRA
# Given a tuple of test scores, use a loop to find how many students scored above 80.
# Print the final count.
# Print average score for those students
scores = (75, 92, 85, 60, 45, 99, 81)
great_score = 0
total_great_score = 0

for score in scores:
    if score > 80:
        great_score += 1
        total_great_score += score

print(great_score)
print(total_great_score / great_score)

# EXTRA
# You have two sets of items. Loop through set_a. For every item,
# check if it also exists in set_b. If it does, print "Match found: [item]".
set_a = {"apple", "banana", "cherry", "date"}
set_b = {"cherry", "elderberry", "date", "fig"}

for item in set_a:
    if item in set_b:
        print(f'Match found: [{item}]')


# EXTRA
# Take the following list of hobbies and print them out as a numbered list
# (e.g., "1. Coding", "2. Reading").
hobbies = ["Coding", "Reading", "Running", "Gaming"]

for i in range(len(hobbies)):
    print(i + 1, hobbies[i])