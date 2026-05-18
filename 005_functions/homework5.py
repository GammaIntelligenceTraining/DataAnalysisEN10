# Write a function that accepts a list of numbers as an argument
# And returns list with squares for each number
def square_list(numbers_lst: list) -> list:
    result = []
    for num in numbers_lst:
        result.append(num ** 2)
    return result


print(square_list([1, 2, 3, 4, 5, 6, 7]))


# Write a function that accepts a list of numbers
# And returns a tuple with two numbers, amount of odd and even numbers
# Example: input -> [1, 2, 3, 4, 5] output (3, 2)
# Where 3 is amount of Odds and 2 is amount of evens
def count_odd_and_even(numbers_lst: list) -> tuple:
    odds, evens = 0, 0

    for num in numbers_lst:
        if num % 2 == 0:
            evens += 1
        else:
            odds += 1
    
    return (odds, evens)

print(count_odd_and_even([1, 2, 3, 4, 5, 6, 7, 8]))


# Write a function that accepts a list of numbers
# and returns largest number
def find_largest_number(numbers_lst: list) -> int|float:

    max_val = 0
    for num in numbers_lst:
        if max_val < num:
            max_val = num
    
    return max_val

print(find_largest_number([1, 2, 3, 4, 5, 6, 7, 8, 9]))


# Write a function that accepts a start number and end number
# Create a FizzBuzz for given range
# (If number divided by 3 has no remainder, print number + FIZZ
# If number divided by 5 has no remainder, print number + BUZZ
# If number divided by 5 and 3 has no remainder, print number + FIZZBUZZ)

def fizz_buzz(start: int, end: int) -> None:

    for num in range(start, end + 1):
        if num % 3 == 0 and num % 5 == 0:
            print(num, 'FIZZBUZZ')
        elif num % 3 == 0:
            print(num, 'FIZZ')
        elif num % 5 == 0:
            print(num, 'BUZZ')
        

fizz_buzz(1, 100)
