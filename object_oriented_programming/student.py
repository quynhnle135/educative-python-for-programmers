class Student:
    def __init__(self, name, phy, chem, bio):
        self.name = name
        self.phy = phy
        self.chem = chem
        self.bio = bio

    def totalObtained(self):
        return self.phy + self.chem + self.bio

    def percentage(self):
        return (self.totalObtained() / 300) * 100


mark = Student("Mark", 80, 90, 40)
print(mark.totalObtained())
print(mark.percentage())