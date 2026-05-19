'''Array & set
    (1) Array
    (2) Set
    (3) Specific operators with set
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

print("===== Set =====")
# { set } of unique collection without keeping order!
new_numbers = array("i", [1, 2, 4, 5, 22, 8, 5, 2, 8, 10, 22])
numbs_set = set(new_numbers)

print(f"the numbs_set: {numbs_set} and type:{type(numbs_set)}")

numbs_set.add(200)
print("numbs_sest(1):", numbs_set)

numbs_set.add(5)
print("numbs_sest(2):", numbs_set)


print("===== specific operators with set =====")

# | & - ^

a = {10, 20, 50}
b = {20, 40}

result1 = a | b  # union
result2 = a & b  # intersection
result3 = a - b  # defference
result4 = a ^ b  # symmetric difference

print(result1)
print(result2)
print(result3)
print(result4)
