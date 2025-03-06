"""
A class for representing a circle
LHH python object oriented Challenge object properties and methods
"""


class Circle:
    pi = 3.14

    def __init__(self, radius):
        self.radius = radius


    def __repr__(self):
        return f"Circle Properties: radius: {self.radius} area: {pi*self.radius**2} Circumference: {2*self.pi*self.radius}"

    def display_area(self):
        print("Area of circle: {} square units".format(self.pi*self.radius**2))

    def display_circumference(self):
        print("Circumference of circle: {0:.2f}".format(2*self.pi*self.radius))


new_circle = Circle(5)

print("Circle Radius: {}".format(new_circle.radius))
print("Circle Pi: {}".format(new_circle.pi))

new_circle.display_area()
new_circle.display_circumference()



