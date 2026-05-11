'''CLASS
    (1) WHAT is CLASS
    (2) ordinary vs static properties
    (3) special methods
'''

print("===== WHAT is CLASS =======")
# class -- blueprint for object creation
# structure --> state constructor method


class Person():
    # state
    message = "static state property"

    # constructor
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # methods
    def introduce(self):
        print(f"{self.name} says: How are you?")

    def say_age(self):
        print(f"{self.name} says: I am {self.age}")

    @classmethod
    def explain(cls):
        print("Static method property is executed!")


person1 = Person("Alex", 22)
person2 = Person("Justin", 25)
person3 = Person("Bob", 35)

# ordinary state property
name = person1.name
print(name)

# ordinary method

person1.introduce()
person2.say_age()


print("===== ordinary vs static properties =======")
new_message = Person.message
print(new_message)

# static methods
Person.explain()
