'''Array & set
    (1) Array
    (2) Set
    (3) specific operators with set
'''

from array import array

print("===== Array =====")

numbers = array("i", [1, 2, 4, 5, 22, 8])  # only for large amount of numbers
print("numbers(1):", numbers)

numbers.append(100)
numbers.insert(0, 9)
print("numbers(2):", numbers)

numbers.remove(9)
numbers.pop()
print("numbers(3):", numbers)

del numbers[0:2]
print("numbers(4):", numbers)
