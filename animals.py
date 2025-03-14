"""
Animal sub class Dog: Getting started with python object oriented programming LHH.
Class Inheritance challenge.
"""

import animal

class Dog(animal.Animal):
    def __init__(self, name, sound):
        super().__init__(name, sound)
        self.name = name
        self.sound = sound

    def wag_tail(self):
        print(f"{self.name} wags tail")


class Cat(animal.Animal):
    def __init__(self, name, sound):
        super().__init__(name, sound)
        self.name = name
        self.sound = sound

    def purrs(self):
        print(f"{self.name} purrs")


my_dog = Dog("Dusty", "Woof")
my_cat = Cat("Suki", "Meow")

my_dog.make_sound()
my_cat.make_sound()


my_dog.wag_tail()
my_cat.purrs()
