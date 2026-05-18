# Task 1: The Stubborn Door
# Write a program that asks the user to enter a password.
# Keep asking them for the password while their input does not match "open sesame".
# Once they type the correct password, print "Access granted!" 
# and end the program.

# Hint: You will need a variable to store the user's input before the loop starts,
# and you will need to update that same variable inside the loop.

# password = 'open sesame'

# while True:
#     user_pass = input('Enter password: ')
#     if user_pass.lower() == password.lower():
#         print('Access granted!')
#         break
#     print('Wrong password, try again!')


# Task 2: The Safe Divider
# Write a program that asks the user for two numbers.
# Divide the first number by the second number and print the result.
# Wrap your code in a try...except block to catch the ZeroDivisionError that
# happens if the user enters 0 for the second number.

# Sample Output (Success): "10 divided by 2 is 5.0"
# Sample Output (Error handled): "Error: You cannot divide a number by zero!"

# try:
#     number1 = int(input('Enter first number: '))
#     number2 = int(input('Enter second number: '))
#     print(number1 / number2)
# except ValueError:
#     print('One of the values you entered is not numeric.')
# except ZeroDivisionError:
#     print('Second value can not be 0, ZeroDivision is not alowed.')



# Task 3: The Vowel Counter
# Create a variable with the string text = "python programming is fun".
# Create a vowel_count variable and set it to 0.
# Loop through every letter in the text using a for loop.
# If the letter is a vowel (a, e, i, o, u), add 1 to your counter. 
# Print the final count at the very end.
some_text = "python programming is fun"
vowel_count = 0
for letter in some_text:
    if letter in ('a', 'e', 'i', 'o', 'u', 'y'):
        vowel_count += 1

print(vowel_count)

# Task 4: The VIP Bouncer
# You have a list of guests: guests = ["Alice", "Bob", "VIP_Charlie", "Dave", "VIP_Eve"].
# Loop through the list. If the guest's name starts with "VIP_", print "Welcome to the lounge, [Name]!".
# Otherwise, print "Enjoy the main floor, [Name].".

# Hint: You can check if a string starts with a specific word by
# using slicing or the .startswith() string method.

guests = ["Alice", "Bob", "VIP_Charlie", "Dave", "VIP_Eve"]
for name in guests:
    if name.startswith('VIP_'):
        print(f"Welcome to the lounge {name.replace("VIP_", "")}")
    else:
        print(f'Enjoy the main floor {name}')


# Task 5 *: Find the Champion (Without shortcuts)
# You have a list of scores: scores = [45, 88, 72, 95, 33, 81].
# Without using Python's built-in max() function, find the highest score.
scores = [45, 88, 72, 95, 33, 81]

max_val = 0
for score in scores:
    if max_val < score:
        max_val = score

print(max_val)