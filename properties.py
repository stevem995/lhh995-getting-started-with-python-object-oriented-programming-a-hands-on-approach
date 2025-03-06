"""
Python class properties LHH getting started obeject oriented python
"""

class Rectangle: 
    def __init__(self, base, height): 
        self.base = base
        self.height = height

    def __repr__(self):
        return f"Rectangle Properties: base: {self.base} height: {self.height}"

    def display_area(self):
        print("Area of rectangle: {} square units".format(self.base * self.height))

new_rectangle = Rectangle(12, 10)
print("new_rectangle.base: {}".format(new_rectangle.base))
print("new_rectangle.height: {}".format(new_rectangle.height))

new_rectangle.base = 5

print("\nnew_rectangle: {}".format(new_rectangle))
new_rectangle.display_area()