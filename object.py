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
