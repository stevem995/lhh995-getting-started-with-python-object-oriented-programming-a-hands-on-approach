"""
Animal sub classes: Getting started with python object oriented programming LHH.
Class Polymorphism challenge.
"""

from animal_polly import Animal

class Dog(Animal):
    def __init__(self, name, sound):
        super().__init__()
        self.name = name
        self.sound = sound

    def wag_tail(self):
        print(f"{self.name} wags tail")

    def make_sound(self):
        print("Woof")



class Cat(Animal):
    def __init__(self, name, sound):
        super().__init__()
        self.name = name
        self.sound = sound

    def purrs(self):
        print(f"{self.name} purrs")

    def make_sound(self):
        print("Meow!")



my_dog = Dog("Dusty", "Woof")
my_cat = Cat("Suki", "Meow")

my_dog.make_sound()
my_cat.make_sound()


my_dog.wag_tail()
my_cat.purrs()
