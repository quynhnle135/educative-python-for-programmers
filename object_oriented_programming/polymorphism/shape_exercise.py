class Shape:
    sname = "Shape"

    def getName(self):
        return self.sname


class XShape(Shape):
    def __init__(self, name):
        self.xsname = name

    def getName(self):
        print(f"{super().getName()}, {self.xsname}")

circle = XShape("Circle")
circle.getName()