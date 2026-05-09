print("================= NUBMERS ===================")

# in JAVA, variable is a name of storage location
# in Python, variable is named reference because all of them are objects

count = 100
count_type = type(count)

# Pythondagi format bu  jsdagi superstring
print(f"the count: {count} and type: {count_type}")

result1 = count.bit_count()  # methodi bor
result2 = count.numerator  # state

print(result1, result2)

print("=============== STRING =================")

# METHODS: upper(), lower(), title(), find(), replace()

course = "Mern AI fullStack"

result = type(course)
print(f"the type of course is: {result}")

result = course.title()
print(f"result 2 is: {result}")

result = course.upper()
print(f"result 3 is: {result}")

result = course.replace("Mern", "Python")
print(f"result 4 is: {result}")

# print(course)

print("=============== BOOLEAN =================")

# functions > type(), input(), bool(), int(), str()

y = input("Input value of y: ")
print(f"Value of y: {y}")


result = y.isnumeric()
print(f"Input number is numeric: {result}")

# TRUTHY: True, 100, -1, "nimadir"
# FALSY: False, 0, "", None


test_falsy = "" or False or None or 0
print("test_falsy:", bool(test_falsy))

test_truthy = "100"
print("test_truthy", bool(test_truthy))
