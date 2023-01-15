class Rectangle:
    def __init__(self, length, width):
        self.__length = length
        self.__width = width

    def find_area(self):
        return self.__length * self.__width

    def find_perimeter(self):
        return 2 * (self.__width + self.__length)


my_rectangle = Rectangle(4, 5)
print(my_rectangle.find_area())
print(my_rectangle.find_perimeter())
