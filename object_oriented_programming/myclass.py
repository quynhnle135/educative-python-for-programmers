class MyClass:
    classVariable = "educative"

    @classmethod
    def demo(cls):
        return cls.classVariable


new_class = MyClass()
print(new_class.classVariable)
print(MyClass.demo())