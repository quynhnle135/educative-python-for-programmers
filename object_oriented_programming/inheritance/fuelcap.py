class Vehicle:
    fuelcap = 90
    def display(self):
        print("I am from parent class")


class Car(Vehicle):
    fuelcap = 50

    def display(self):
        super().display()
        print("I am from children class")
        # print("Fuel cap of Vehicle is: ", super().fuelcap)
        # print("Fuel cap of Car is: ", self.fuelcap)


my_car = Car()
my_car.display()
print("------")
my_vehicle = Vehicle()
my_vehicle.display()