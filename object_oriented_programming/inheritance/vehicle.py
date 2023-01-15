class Vehicle:
    def __init__(self, make, color, model):
        self.make = make
        self.color = color
        self.model = model

    def print_details(self):
        print("Manufacturer: ", self.make)
        print("Color: ", self.color)
        print("Model: ", self.model)

    def set_top_speed(self, speed):
        self.speed = speed
        print(f"Top speed is {self.speed}")


class Car(Vehicle):
    def __init__(self, make, color, model, doors):
        Vehicle.__init__(self, make, color, model)
        self.doors = doors

    def print_car_details(self):
        self.print_details()
        print("Doors: ", self.doors)

    def open_trunk(self):
        print("Trunk is opened now!!!")


class Hybrid(Car):
    def turn_on_hybrid(self):
        print("Hybrid is turned on!!!")

    def display(self):
        super().print_car_details()
        print("This is a hybrid!!")

my_car = Car("Toyota", "White", "Corolla", 4)
my_car.print_car_details()
my_car.open_trunk()
my_car.set_top_speed(220)

print("------")
my_vehicle = Vehicle("Honda", "Black", "Civic")
my_vehicle.print_details()

print("------")
my_hybrid = Hybrid("Toyota", "White", "Corolla", 4)
my_hybrid.turn_on_hybrid()
my_hybrid.display()



