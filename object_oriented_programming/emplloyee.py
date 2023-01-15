class Employee:
    # ID = 3789
    # salary = 2500
    # department = "Human Resource"

    def __init__(self, ID=None, salary=0, department=None):
        self.ID = ID
        self.salary = salary
        self.department = department


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
