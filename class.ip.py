'''CLASS deep diving
     (1) ENCAPSULATION
     (2) INHERITANCE
     (3) POLIMORPHISM
'''

print("========== INHERITANCE =============")
# meros berish public va protected state va methodlarni bera oladi


class Animal():

    description = "Class for creating animals"

    def __init__(self, voice):
        self.voice = voice
        self._status = "alive"

    def make_voice(self):
        print(f"the animal can make voice: {self.voice}")


class Dog(Animal):

    def __init__(self, name, sound, voice):
        super().__init__(voice)
        self.name = name
        self.sound = sound

    def introduce(self):
        print(f"{self.name} says: {self.sound}-{self.sound}")

    def protect(self):
        print("Yes, I can protect you!")


class Cat(Animal):

    def __init__(self, name, sound, voice):
        super().__init__(voice)
        self.name = name
        self.sound = sound

    def introduce(self):
        print(f"{self.name} says: {self.sound}-{self.sound}")

    def play(self):
        print("Cat plays")


class Fish(Animal):

    def __init__(self, name, sound, voice):
        super().__init__(voice)
        self.name = name
        self.sound = sound

    def introduce(self):
        print(f"{self.name} says: {self.sound}-{self.sound}")

    def swim(self):
        print("Fish swim")


dog = Dog("Rex", "wow", True)
cat = Cat("Tom", "myoew", True)
fish = Fish("Nemo", "zzzz", False)

dog.introduce()
cat.introduce()
fish.introduce()

fish.make_voice()

print(Dog.description)

print(cat._status)
