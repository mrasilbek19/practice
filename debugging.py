'''Packages & Debugging
    (1) Python PACKAGES and Core Package
    (2) Package Manager & External Package
    (3) Debugging
'''


from PIL import Image
import turtle
print("===== Python Packages and Core Package =====")

# core
# t = turtle.Turtle()
# t.shape("turtle")
# t.speed(5)
# t.circle(100)

# turtle.done()


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


print("===== Package Manager & External Package =====")
# External packages list - https://pypi.org
# Python Package manager --> pip pipenv


with Image.open("material/image.png") as img_obj:
    resized_img = img_obj.resize((300, 300))
    resized_img.show()
    resized_img.save("material/newImg.png")


print("===== Debugging =====")


def get_summary(*args):
    total_amount = 0
    for a in args:
        total_amount += a
        return total_amount  # Bug found in  debugging


test = 100
result = get_summary(1, 6, 4, 9, 10)
print(result)
