# Abstruction Examples
from abc import ABC,abstractmethod
from math import pi

# Base class to apply abstruction method from
class Shape(ABC):
    @abstractmethod
    def calculate_area(self):
        pass
    
# Derived class to apply abstruction method 
class Circle(Shape):
    # constructor to set attributes 
    def __init__(self, radius):
        self.radius = radius
        
    # abstruction method to calculate area
    def calculate_area(self):
        print(f"Area of Circle is {pi * self.radius ** 2}\n")
        
# Derived class to apply abstruction method 
class Rectangle(Shape):
    # constructor to set attributes
    def __init__(self, height, width):
        self.height = height
        self.width = width
    # Abstruction method to calculate area
    def calculate_area(self):
        print(f"Area of Rectangle is {0.5 * self.height * self.width}\n")

# Create objects of derived classs
shape_type_1 = Circle(8)
shape_type_2 = Rectangle(4,5)

# call the abstructed method
shape_type_1.calculate_area()
shape_type_2.calculate_area()