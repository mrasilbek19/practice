'''Loops
(1) Working with lists
(2) List methods
(3) Lubmda functions
(4) enumerate, map and filter
'''

print("===== Working with lists ======")
# Java, Php, NodeJs array => Python list

# literal
person = {"name": "Alex", "age": 25}  # dictionary
people = ("Andrew", "Justin")  # tuple
gruops = ["MIT", "DEVEX", "MG", "FLEXY"]
for team in gruops:
    print(team)


# constructor
letters = list("Hello World!")

print(f"letters: {letters} and size: {len(letters)}")

print("--------")
fruits = ["apple", "lemon", "banana", "kiwi"]
a = fruits[0]
b = fruits[0:2]  # [0, 2)

c = fruits[::3]
# nechi qadam sakrashini aytamiz bu yerda 1 chidan ohirigacha 3 qadam tashab olib be dedik

d = fruits[::-1]
# orqa tomonga yur


print("a:", a)
print("b:", b)
print("c:", c)
print("d:", d)

print("===== List methods ======")
# methods > append() insert() pop() remove() clear() sort() => mutable
# sorted() index() => immutable

letters = ["a", "b", "c"]

letters.append("toEnd")
print(f"Append result is: {letters} ")

# hohlagan index position berib usha joyga bersak buladi
# index argumenti arraydan katta bulsa ohiriga quyib beradi
letters.insert(0, "toStart")
print(f"Insert result is: {letters} ")

size = len(letters) - 1
result1 = letters.pop(size)  # ohiridagini udalit qilib ushani return qiladi
print(f"Insert pop result is: {result1} and letter: {letters}")

result2 = letters.pop(0)  # Boshidagini udalit qilib ushani return qiladi
print(f"Insert pop result is: {result2} and letter: {letters}")


print("--------")
animals = ["dog", "cat", "fish", "lion", "fox"]
print("animals:", animals)

animals.remove("lion")
print("animals remove:", animals)

del animals[2:4]
print("animals delete:", animals)

exist = animals.index("cat")
print("cat exist in index:", exist)

animals.clear()
print("animals clear:", animals)

# exist1 = animals.index("cat")
# print("cat exist in index:", exist1)  # pythonda topilmasa error buladi

if "cat" in animals:
    print(f"cat exist in index: {animals.index("cat")}", )
else:
    print("cat does not exist")


print("--------")
x = [2, 55, 4, 3, 8, 90]

x.sort()
print("sorted list (default)", x)

x.sort(reverse=True)
print("sorted list (reversed)", x)

# immutable sort => sorted()
y = [25, 4, 3, 18, 77]
new_y = sorted(y)
print(f"original array: {y} sorted array: {new_y}")

print("===== Lubmda functions ======")
# labmda is small anonymous functions
def calculate(x, y): return x * y


result = calculate(3, 6)
print(result)

people = [
    ("Robert", 20),
    ("Nick", 33),
    ("Bob", 26),
    ("Alex", 22)
]
people.sort()
print("People(1):", people)

# sort via labmda
people.sort(key=lambda person: person[1])
print("People(2):", people)

print("===== enumerate, map and filter ======")
animals = ["dog", "cat", "fish"]
for element in enumerate(animals):
    print("element", element)

print("--------")
for (index, value) in enumerate(animals):
    print(f"the index: {index} and value: {value}")


# similar in dictionary
car_obj = dict(brand="BMW", year=2022)
result = car_obj.items()
print("result:", result)
for (key, value) in result:
    print(f"the key: {key} and value: {value}")


print("--------")
cars = [
    ("Ferrari", 78),
    ("Tayota", 87),
    ("Audi", 116),
    ("BMw", 109),
    ("Pagani", 33)
]

# ananaviy method
new_cars = []
for car in cars:
    new_cars.append(car[0])
print("new_car(1):", new_cars)

# map
result_map = map(lambda car: car[0], cars)
print(f"the result: {result_map} and type: {type(result_map)}")
new_cars = list(result_map)
print("new_cars(2)", new_cars)

print("--------")
# filter
result_filter = filter(lambda car: car[1] > 80, cars)
print(f"the result_filter:{result_filter} and type: {type(result_filter)}")
print(list(result_filter))
