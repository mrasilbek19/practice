'''OBJECTS
(1) What is object
(2) Iterably objects and Range
(3) DICTIONARY
(4) Error handling systems
'''


import array   # package/module
import math

# packagedan faqat kerakli bulganini chaqirib olish va shundagina line 30 ishlaydi
from math import ceil

print("===== (1) What is object =====")

# An object has state and method properties.
# Everything is object in Python

print(type("Hello World"))
print(type(123))
print(type(True))
print(type(array))
print(type(math))

# Paradigm --> Functional Programming and OOP
# OOP 4 CONCEPTS > Abstraction | Encapsulation | Inheritance | Polymorphism

result1 = math.ceil(17.6)
print("result1:", result1)

result2 = ceil(34.3)
print("result2:", result2)


print("===== (4) Error handling systems =====")
car_obj = dict(name="Toyota", year=2026, electric=True)

try:
    print("Passed here")
    # x = car_obj.speed
    result = car_obj["origin"]
    # result = car_obj["name"]
    print(result)
# except KeyError as err:
#     print("origin state didn't found: ", err)
# except AttributeError as err:
#     print("speed state not found", err)
# except (KeyError, AttributeError) as err:
#     print("Error: ", err)
except Exception as err:  # error type qiziq bolmasa
    print("General Error: ", err)
else:
    print("Executed succesfully without any errors")
finally:
    print("Finally block is executed")
