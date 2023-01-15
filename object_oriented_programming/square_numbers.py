class Point:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def sqSum(self):
        a = self.x ** 2
        b = self.y ** 2
        c = self.z ** 2
        return a + b + c


my_point = Point(1, 3, 5)
print(my_point.sqSum())


