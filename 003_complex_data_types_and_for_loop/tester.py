# empty = []
# empty = list()

# print(type(empty))
# print(bool(empty))

filled_list = [123, 0.3223, False, [1, 2, [30, 20, 40, 50], 4, 5, 6], 'hello world', None]

# print(len(filled_list))
# print(filled_list[3][2][2])
# print(filled_list[1])
# print(filled_list[1:4])


# courses = ['Math', 'Economics', 'Geography', 'History', 'Literature']

# var1, var2, *var3 = [1, 2, 3, 4, 5]
# print(var1, var2, var3)

# print(*courses)
# print('Math', 'Economics', 'Geography', 'History', 'Literature')
# print([1, 2, 3, *courses, 4, 5, 6])

# courses[1] = 'Art'
# print(courses)

# courses[1:4] = ['Art']
# print(courses)

# courses.append('Art')

# print(courses[3])
# courses.insert(0, 'English')
# print(courses[3])

# courses.extend(['English', 'Art', 'Estonian'])
# courses.extend('English')

# courses.remove('Math')

# deleted = courses.pop(0)

# print(courses)
# print(deleted)

# print([1, 2, 3] + [4, 5, 6])
# print([1, 2, 3] * 3)


# courses = ['Math', 'Economics', 'Geography', 'History', 'Literature']
# print(courses)

# courses.reverse()
# courses.sort(reverse=True)

# print(courses)

# x = [[2, 6], [1, 3], [8, 4], [3, 5], [1, 1]]
# x.sort()
# print(x)

# print(courses.index('Geography'))
# print(courses.count('Math'))

# courses_str = ', '.join(courses)
# print(courses_str)

# new_lst = courses_str.split(', ')
# print(new_lst)

# sentence = 'Hello people of planet Earth. Are you ok?'
# print(sentence.split('. '))

# courses.clear()
# print(courses)

# courses = []


# a = [1, 2, 3]
# b = a.copy()
# a.append(4)
# b.append(5)

# print(a)
# print(b)

# x = [1, 2, 3, 4, 5]
# print(min(x))
# print(max(x))
# print(sum(x))


# empty = ()
# empty = tuple()
# empty = ('asdasd',)

# print(type(empty))
# courses = (
#     'Math',
#     'Economics',
#     'Geography',
#     'History',
#     'Literature',
# )

# print((1, 2, 3) + (4, 5, 6))
# print((1, 2, 3) * 3)


courses = {
    'Math',
    'Economics',
    'Geography',
    'History',
    'Literature',
    'Math',
    'Math',
}

# empty = set()
# print(type(empty))

print(type(courses))

# courses.add('Art')
# courses.remove('Math')  # WILL RAISE ERROR IF ELEMENT DOES NOT EXIST
# courses.discard('Math')

# d = courses.pop()
# print(d)
# courses.update({'Art', 'English'})

# print(courses)

set1 = {'Math', 'English', 'Art', 'Physics'}
set2 = {'Art', 'Geography', 'English', 'Estonian'}

print(set1.difference(set2))
print(set2.difference(set1))

print(set1.intersection(set2))

print(set1.symmetric_difference(set2))

print(set1.union(set2))
print(set1 | set2)

set3 = {'Math', 'English'}
print(set3.issubset(set1))
print(set1.issuperset(set3))