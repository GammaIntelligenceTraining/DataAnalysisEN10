# Fizz Buzz Bang
# Create a function that accespts two numbers
# start and end
# Inside function run a cycle for numeric row between theese numbers
# If number is divisible by 3 without a remainder print number and FIZZ
# If number is divisible by 5 without a remainder print number and BUZZ
# If number is divisible by 7 without a remainder print number and BANG
# If divisible by combination, in example by 3 and 7 -> print combination FIZZBANG
# or divisible by 5 and 7 -> print number and combination BUZZBANG
# or divisible by 3, 5 and 7 -> print number and combination FIZZBUZZBANG
# Otherwise skip to next number
# All combinations must be covered

def fizz_buzz_bang(start, end):

    for num in range(start, end + 1):
        word = ''
        if num % 3 == 0:
            word += 'FIZZ'
        if num % 5 == 0:
            word += 'BUZZ'
        if num % 7 == 0:
            word += 'BANG'
        if word:
            print(num, word)

fizz_buzz_bang(1, 200)