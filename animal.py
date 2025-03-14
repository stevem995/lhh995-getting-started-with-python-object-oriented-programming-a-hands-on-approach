"""
Animal base class: Getting started with python object oriented programming LHH.
Class Inheritance challenge.
"""

class Animal:
    def __init__(self, name, sound):
        self.name = name
        self.sound = sound

    def make_sound(self):
        print(f"{self.name} says {self.sound}")
