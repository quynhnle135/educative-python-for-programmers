class Employee:
    # ID = 3789
    # salary = 2500
    # department = "Human Resource"

    def __init__(self, ID=None, salary=0, department=None):
        self.ID = ID
        self.salary = salary
        self.department = department

    def demo(self, a, b, c, d=5, e=None):
        print("a=", a)
        print("b=", b)
        print("c=", c)
        print('d=', d)
        print("e=", e)

    def tax(self):
        return self.salary * 0.2

    def salary_per_day(self):
        return self.salary / 30


Steve = Employee(3789, 2500, "Human Resources")
print("ID = ", Steve.ID)
print("Salary: ", Steve.salary)
print("Department: ", Steve.department)
print("Tax paid by Steve: ", Steve.tax())
print("Salary per day of Steve: ", Steve.salary_per_day())

print("Demo 1")
Steve.demo(1, 2, 3)
print("Demo 2")
Steve.demo(1, 2, 3, 4)
print("Demo 3")
Steve.demo(1, 2, 3, 4, 5)


print("-------")
quinn = Employee()
print("ID:", quinn.ID)
print("Salary: ", quinn.salary)
print("Department: ", quinn.department)
# quinn.ID = 1234
# quinn.salary = 50000
# quinn.department = "IT"

john = Employee(4321, 45000, "Finance")
# print(john.ID)
# print(john.department)
# print(john.salary)
# john.ID = 4321
# john.department = "Finance"
# john.salary = 40000
print("ID: ", john.ID)
print("Department: ", john.department)
print("Salary: ", john.salary)


john.title = "Manager"
print("Title: ", john.title)
