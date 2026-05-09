'''FUNCTIONS
(1) DEFINE vs CALL
(2) Parametr vs Argument
(3) Keyword & deafult arguments
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
