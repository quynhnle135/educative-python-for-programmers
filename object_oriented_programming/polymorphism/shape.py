class Shape:
    def __init__(self):
        self.side = 0

    def getArea(self):
        pass

class Rectangle(Shape):
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        self.sides = 4

    def getArea(self):
        return self.width * self.height


class Circle(Shape):
    def __init__(self, radius=0):
        self.radius = radius
        self.sides = 0

    def getArea(self):
        return self.radius * self.radius * 3.14


shapes = [Rectangle(6, 10), Circle(7)]
print("sides of a rectangle are: ", str(shapes[0].sides))
print("area of a rectangle is: ", shapes[0].getArea())

print("side of a circle are: ", str(shapes[1].sides))
print("area of a circle is: ", shapes[1].getArea())