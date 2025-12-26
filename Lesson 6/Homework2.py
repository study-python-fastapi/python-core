class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    def calculate_area(self):
        print(self.width * self.height)

Rectangle1 = Rectangle(40, 2)
Rectangle2 = Rectangle(7, 15)
Rectangle1.calculate_area()
Rectangle2.calculate_area()