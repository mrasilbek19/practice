print("=======================================")

# in JAVA, variable is a name of storage location
# in Python, variable is named reference because all of them are objects

count = 100
count_type = type(count)

# Pythondagi format bu  jsdagi superstring
print(f"the count: {count} and type: {count_type}")

result1 = count.bit_count()  # methodi bor
result2 = count.numerator  # state

print(result1, result2)
