'''Packages & Debugging
    (1) Python PACKAGES and Core Package
    (2) Package Manager & External Package
    (3) Debugging
'''


import turtle
print("===== Python Packages and Core Package =====")

# core
t = turtle.Turtle()
t.shape("turtle")
t.speed(5)
t.circle(100)

turtle.done


print("---------")

my_file = open("material/message.txt", "r")
try:
    content = my_file.read()
    print(content)
finally:
    my_file.close()


# with - Context Manager
with open("material/message.txt", "r") as your_file:
    your_content = your_file.read()
    print("your_content:", your_content)

print("Done")
