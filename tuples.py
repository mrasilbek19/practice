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
