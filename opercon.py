'''OPERATORS AND CONDITIONS 
   (1) Operators
   (2) Conditions 
   (3) Logical Operators
'''

print("======= Operators ========")
# + - < > >= <=  == is * /   // % += **

a = 26
b = 5

print(a > b)
print(a / b)
print(a * b)


result = a // b
left = a % b
print(result)
print(left)


print("b^2 =", b**2)
print("b^3 =", b**3)

print("*"*7)


c = dict(name="Alex", age=22)
d = dict(name="Alex", age=22)
e = c

print("c==d", c == d)  # only value is compares
print(id(c), id(d))

# == faqat value
# is > referenceni tekshiradi

print(c is d)
print(c is e)
