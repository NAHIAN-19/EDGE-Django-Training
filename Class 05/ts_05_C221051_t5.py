# SOLID Principles - Open Closed principle

# Encapsulation Examples
from math import pi

# Base class set to implement calculate area method that has no need for modification
class Shape:
    def calculate_area(self):
        raise NotImplementedError("Subclass must implement this base method!!!!")
    
# Derived class extended from base class without modifying base class
class Circle(Shape):
    # constructor to set attributes 
    def __init__(self, radius):
        self.radius = radius
        
    # abstruction method to calculate area
    def calculate_area(self):
        print(f"Area of Circle is {pi * self.radius ** 2}\n")
        
# Derived class extended from base class without modifying base class
class Rectangle(Shape):
    # constructor to set attributes
    def __init__(self, height, width):
        self.height = height
        self.width = width
    # Abstruction method to calculate area
    def calculate_area(self):
        print(f"Area of Rectangle is {0.5 * self.height * self.width}\n")

# Derived class extended from base class without modifying base class
class Square(Shape):
    def __init__(self, side_length):
        self.side_length = side_length
        
    def calculate_area(self):
        print(f"Area of this Square is {self.side_length ** 2}\n")

# Create objects of derived classs
shape_type_circle = Circle(8)
shape_type_rectangle = Rectangle(4,5)
shape_type_square = Square(4)

# call the abstructed method
shape_type_circle.calculate_area()
shape_type_rectangle.calculate_area()
shape_type_square.calculate_area()