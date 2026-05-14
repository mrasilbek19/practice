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

print("======= Conditions ========")

x = 15

if x > 50:
    print("case A")
elif x > 10:
    print("case B")
else:
    print("case C")


print("======= Logical. Operators ========")
age = 22
# person = None

# if age > 16:
#     person = "adult"
# else:
#     person = "child"

# print("person:", person)

# Ternary

person = "adult" if age > 18 else "minor"
print("person:", person)

is_student = True
is_admin = False
is_guest = True
is_parent = True
# is_parent = False

# if is_student:
#     print("Excuted")

if not is_student:
    print("Excuted")
elif is_admin:
    print("Please go to Office")
elif is_guest or is_parent:
    print("Go to waiting room")
# elif is_guest and is_parent:
#     print("Go to waiting room")
else:
    print("other cases")
