'''FUNCTIONS
(1) DEFINE vs CALL
(2) Parametr vs Argument
(3) Keyword & default arguments
(4) Scope
'''

print("=========DEFINE vs CALL===========")

# build in functions > print(), type()
# Function - reusable block of code!
#  Block urniga {} (JS JAVA C), Pythonda indentation!


# DEFINE - build
def greet(a):  # parametr define vaqtida beriladi
    # pass  # bush bulsa ishlamaydi shuning uchun hech bulmasa pass deb yozib ketish kerak
    print(f"How are you: {a}")


def greeting(b):
    print("functions is executed")
    return f"Hello {b}"


# CALL - execute
result1 = greet("Tony")  # call vaqtida argument beriladi
print("result1: ", result1)


result2 = greeting("Bob")
print("result2: ", result2)


print("=========Keyword & default arguments===========")


def give_greet(name, age=22):  # define vaqtida default value bersak buladi
    print("give_great is executed")
    return f"Hello {name}, your age is {age}"


# result3 = give_greet("ALEX", 22)
# print("result3: ", result3)


# kod yanada tushunarli bulishi uchun keyword berish kk bu yerda name bilan age keywoardlar
result3 = give_greet(name="ALEX", age=22)
print("result3: ", result3)

result4 = give_greet(name="ALEX",)
print("result3: ", result4)

print("========= Scope ===========")

b = 100  # 3


def calculate(a, b):  # 2
    c = a + b  # 1
    print(f"c value is: {c}")


calculate(5, 55)
calculate(5, b)
