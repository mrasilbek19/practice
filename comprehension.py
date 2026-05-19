''' Comprehension
    (1) What is comprehension & list comprehension
    (2) set and Dictionary comprehension
'''

print("===== What is comprehension & list comprehension =====")
# Comprehenson act like spread operator!

''' Comprehension general syntax
    a) *iterable
    b) <expression> for item in iterable
    c) <expression> for item in iterable <condition>
'''

numbers = [1, 2, 3, 5, 8, 9]
list_numbers = [*numbers]  # a version

print("list_numbers:", list_numbers)
print(numbers is list_numbers)
print(id(numbers), id(list_numbers))


print("----------")
people = [("Robert", 20), ("Bob", 24), ("Alex", 22)]
list_people = [person[0] for person in people]
print(list_people)

print("----------")

cars = [
    ("Ferrari", 78),
    ("Tayota", 87),
    ("Audi", 116),
    ("BMw", 109),
    ("Pagani", 33)
]

list_cars = [car[0] for car in cars if car[1] > 80]
print(list_cars)


print("===== set and Dictionary comprehension =====")

nums = [1, 2, 3, 5, 8, 9, 3, 5]
set_nums = {*nums}
print("set_numbers:", set_nums)


dict_people = {person[0]: person[1] for person in people}
print("dict_people 1:", dict_people)

dict_people = {person[0]: person[1] for person in people if person[1] > 21}
print("dict_people 2:", dict_people)


# Genericlar ham bor
