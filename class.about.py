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


# web sitedan keraklisini topib ishlatsa buladi
print("===== special/magic methods =======")

# most used special methods:
# __init__, __new__, __str__, __call__, __getitem__, __eq__, __len__ .....


class Car():
    # state
    description = "This class makes cars"

    # constructor
    def __new__(cls, *args):
        print("------__new__ -----")
        return super().__new__(cls)

    def __init__(self, name, year):
        self.name = name
        self.year = year

    # method
    def start_engine(self):
        print(f"{self.name} started Engine")

    def stop_engine(self):
        print(f"{self.name} stoped Engine")

    def __str__(self):
        return f"{self.name} was produced in {self.year}"

    def __call__(self):
        print("Object called as function")
        return True


car1 = Car("Bmw", 2022)
car1.start_engine()
car1.stop_engine()


print("------------------------")
car2 = Car("KIA", 2024)
print(car2)
responce = car2()
print(responce)
