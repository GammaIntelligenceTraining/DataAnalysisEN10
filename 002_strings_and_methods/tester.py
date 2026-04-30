"""
asdas
dsa
das
asd
das
asd
asd
asd
das
"""

string_sample1 = "Hello world world"
                 #0123456789....
                          #-4-3-2-1
string_sample2 = "first letteR is lowErcase. New sentence"
string_sample3 = " *  extra whitespace string * "
german_sample = "der Fluß"

# print(len(string_sample1))

# # [START:STOP:STEP]
# print(string_sample1[0])
# print(string_sample1[len(string_sample1) - 1])
# print(string_sample1[-1])
# print(string_sample1[6:11])
# # string_sample1 = string_sample1[6:11]
# # print(string_sample1)
# print(string_sample1[0:17:2])
# print(string_sample1[::-1])

# print(str(12312312312)[0])
# # print(string_sample1[17])

# print(string_sample1[6:11][0:3])
# print(len(string_sample1) ** 2)

print(string_sample2.upper())

print(german_sample.lower())
print(german_sample.casefold())

# print(ord('a'))
# print(chr(97))

# print('aaa' > 'aaaa')

# print('001' < '342')

# print(string_sample2.title())
# print(string_sample2.capitalize())

# print(string_sample3.strip(' *'))
# print(string_sample3.lstrip(' *'))
# print(string_sample3.rstrip(' *'))

# print(string_sample1.replace('world', 'planet', 1))
# print(string_sample1.replace(' ', '').upper())

# print(string_sample1.count('w', 7, 12))
# print(string_sample1.find('World'))

# a = "that's"
# b = 'I favourite book is "Metro 2033"'
# c = 'That\'s "Metro \2033"'

# print(c)

# print('Hello\nWorld')
# d = """sdas
# dsa
# das
# das
# das         sdadas
#             dsadasd
#                 asddasd"""

# print(d)


# print('=' * 100)

# print('Hello', end="*")
# print('World', 123, False, sep=" - ")


salary = 2000
name = 'Jack'
sample_str = '{0}s salary is {1}$. {0} is hardworking!'
print(sample_str.format(name, salary))


product = 'computer'
price = 1300
sample_str = '{product} costs {price:.2f}$.'
print(sample_str.format(product=product, price=price))

# Formated string used in Python 2
x = 12231.3456789
y = 131.1314
print('The value of x is %.4f' % x)
print('The value of y is %.2f' % y)

emp_name = 'john'
emp_age = 30
emp_salary = 1500

emp_string = 'Hi, my name is %(name)s! I am %(age)s old. My salary is %(salary).2f' % {'name': emp_name, 'salary': emp_salary, 'age': emp_age}
print(emp_string)

print(f'This is {emp_name.title()}. He is {emp_age} years old. His salary is {emp_salary:.2f}$')

# byte_sting = b'\xcf\x84o\xcf\x81\xce\xbdo\xcf\x82'
# print(byte_sting.decode('utf-16'))

# text = 'Hello world'
# print(text.encode('utf-16'))

user_input = input("Say your name: ")
print('Hello', user_input)
