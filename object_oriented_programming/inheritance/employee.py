class Employee:
    def __init__(self, name, id, department):
        self.name = name
        self.id = id
        self.department = department


    def display(self):
        print(f"My name is {self.name}")
        print(f"My ID is {self.id}")
        print(f"My deparment is {self.department}")


class Engineer(Employee):
    def __init__(self, name, id, department, speciality):
        Employee.__init__(self, name, id, department)
        self.speciality = speciality

    def display(self):
        super().display()
        print(f"My speciality is {self.speciality}")


quinn = Engineer("Quinn", 1234, "IT", "Back-end")
quinn.display()