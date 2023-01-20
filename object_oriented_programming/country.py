class Country:
    def __init__(self, name=None, population=0):
        self.name = name
        self.population = population

    def printDetails(self):
        print("Country's name: ", self.name)
        print("Country's population: ", self.population)


class Person:
    def __init__(self, name, country):
        self.name = name
        self.country = country

    def printDetails(self):
        print("Person's name: ", self.name)
        self.country.printDetails()


c = Country("Wales", 1500)
c.printDetails()
# p = Person("Joe", c)
# p.printDetails()