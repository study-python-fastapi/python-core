from abc import ABC,abstractclassmethod
class Shape(ABC):
    @abstractclassmethod
    def find_area(self):
        pass
class Circle(Shape):
    def __init__(self,radius):
        self.radius = radius
    def find_area(self):
        area = self.radius * 3.14 ** 2
        print(area)
class Rectangle(Shape):
    def __init__(self,length,width):
        self.length = length
        self.width = width
    def find_area(self):
        area = self.length * self.width
        print(area)
class Triangle(Shape):
    def __init__(self,side1,height):
        self.side1 = side1
        self.height = height
    def find_area(self):
        area = self.side1 * self.height / 2
        print(area)

circle = Circle(5)
circle.find_area()
rectangle = Rectangle(5,5)
rectangle.find_area()
triangle = Triangle(5,3)
triangle.find_area()