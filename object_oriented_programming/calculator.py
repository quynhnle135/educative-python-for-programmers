class Calculator:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def add(self):
        return self.num1 + self.num2

    def subtract(self):
        return self.num2 - self.num1

    def multiply(self):
        return self.num1 * self.num2

    def divide(self):
        return self.num2 // self.num1


demo1 = Calculator(10, 94)
print("addition: ", demo1.add())
print("subtraction: ", demo1.subtract())
print("multiplication: ", demo1.multiply())
print("division: ", demo1.divide())