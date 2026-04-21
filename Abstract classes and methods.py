import abc
class Shape(abc.ABC):
    @abc.abstractmethod
    def area(self): pass # площадь фигуры

# Классы-наследники должны реализовать все абстрактные методы абстрактного класса. 
# Oпределим класс прямоугольника:
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    def area(self): return self.width * self.height

# класс круга 
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    def area (self): return self.radius * self.radius * 3.14
     
 
def print_area(shape):
    print("Area:", shape.area())
     
 
rect = Rectangle(30, 50)
circle = Circle(30)
print_area(rect)        # Area: 1500
print_area(circle)      # Area: 2826.0

