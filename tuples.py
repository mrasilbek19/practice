'''Tuples
(1) What is tuple: tuple vs list
(2) Unpacking arguments
(3) zip
'''

print("===== What is tuple: tuple vs list ======")
# Java, Php, NodeJs array => Python list

# literal
nums = [2, 5, 6, 7]
# car_dict = {"brand": "Ferrari", "year": 2025}
print(nums)

# constructor
letters = list("Hello World!")
# person_dict = dict(name="Alex", age=22)
print(letters)


fruits = ["apple", "lemon", "banana", "kiwi"]
print("before fruits: ", fruits)

fruits[2] = "melon"
print("after fruits: ", fruits)  # listda uzgartirish mumkin


# tuple 1  martta qurildimi kiginchalik uzgartirib bulaydi
animals = ("dog", "cat", "fish", "lion")
tuple_obj = ("MIT", 100, True)
print(animals)

# animals[0] = "tiger"  # --> TypeError buladi
# print(animals)


# tupleni shunaqa yozsaham bular ekanu lekin yozmagan maqul--> Avoid this
people = "Alex", "Bob"
animal = "dog",

print("===== Unpacking arguments ======")
groups = ["MIT", "FLEXY", "DEVEX", "MG"]
(x, y, z, a) = groups  # har bir element varibalelarga yoyib qoydik
(x, y, *z) = groups
# yoyib berish bu yerda 2 ta oldingini uzini olib va qolgan boshqalarni bitta variablega quy dedik

print(f"the x is {x} and y is {y}")
print(z)  # list

# *args > tuple


def calculate(*args):
    print("args >", args)
    total = 1
    for x in args:
        total *= x
    print(f"the type(args) value: {type(args)}")
    print(f"the total value: {total}")


# CALL
calculate(1, 7, 2, 9)
print("--------------")
calculate(0, 9, 4)
print("--------------")
calculate(2, 9)

# **kwargs > dictionary


def introduce(**kwargs):
    print(f"Type of **kwargs {type(kwargs)}")
    print(f"Hi, I am {kwargs["name"]} and I am {kwargs["age"]} years old!")


introduce(name="Alex", age=22)


def greeting(*args, **kwargs):
    print("*args >", args)
    print("**kwargs >", kwargs)


greeting("hi", True,  10, name="Alex", age=22)


print("===== zip ======")
tuple1 = (1, 2, 3, 4, 5)
tuple2 = ('a', 'b', 'c', 'd')

zipped = zip(tuple1, tuple2)
print("zipped", zipped)

'''list bir hil indexdagi valuelarni olib tuple qilib arrayga joylab 
berar ekan agar indexlar soni farq qilsa kickkna indexligigacha ishlaydi'''
result = list(zipped)
print(result)
