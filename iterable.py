print("===== Iterable objects & RANGE =====")

# Iterable objects > string, dict, tuple, list, range, map, filter

range_obj = range(5)  # [0, 5)
print("range_obj:", range_obj)

text = "MIT"
for letter in text:
    print(f"the letter: {letter}")

for ele in range_obj:
    print(f"the element: {ele}")  # [0, 1, 2, 3, 4]


print("===== DICTIONARY =====")

# Dictionary is JSON object!
person = {"name": "Alex", "age": 22, "single": True}
person_obj = dict(name="Alex", age=22, single=True)

print(f"the person: {person}")
print(f"the person_obj: {person_obj}")

name = person_obj["name"]
print("name:", name)

# st1 = person_obj["hobby"]
# print("hobby", st1) ----> Errorga sabab buladi error bulmasligi uchun get() method kerak

hobby = person_obj.get("hobby")

# default value berish kerak bulsa yonidan yozib qoysa buladi
balance = person_obj.get("balace", 0)

print(f"name - {name}, hobby - {hobby}, balance - {balance}")


# dictionaryni iterable ekanligini test qilish

# del --> delete qiladi
del person_obj["single"]

for key in person_obj:
    print(f"keys: {key} => value {person_obj.get(key)}")
