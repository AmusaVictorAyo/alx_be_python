import math


class Shape:
    # Base class defining the area contract
    def area(self):
        # Forces subclasses to implement their own area logic
        raise NotImplementedError("Subclasses must implement area().")


class Rectangle(Shape):
    # Rectangle shape with length and width
    def __init__(self, length, width):
        # Store rectangle dimensions
        self.length = length
        self.width = width

    def area(self):
        # Area formula: length × width
        return self.length * self.width


class Circle(Shape):
    # Circle shape with radius
    def __init__(self, radius):
        # Store circle radius
        self.radius = radius

    def area(self):
        # Area formula: π × r²
        return math.pi * (self.radius ** 2)