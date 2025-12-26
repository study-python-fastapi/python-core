class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
    def display_info(self):
        print(f"This Vehicle made by {self.make}. Model is  {self.model}. Made in {self.year}.")
class Car(Vehicle):
    def __init__(self, make, model, year, all_riding_distance):
        Vehicle.__init__(self, make, model, year)
        self.all_riding_distance = all_riding_distance
    def distance(self):
        Vehicle.display_info(self)
        print(f"You ride {self.all_riding_distance}")
class Bicycle(Vehicle):
    def __init__(self, make, model, year, is_sport_bike):
        Vehicle.__init__(self, make, model, year)
        self.is_sport_bike = is_sport_bike
    def sport(self):
        Vehicle.display_info(self)
        print(f"It is {self.is_sport_bike}")
class Motorcycle(Vehicle):
    def __init__(self, make, model, year, max_fuel):
        Vehicle.__init__(self, make, model, year)
        self.max_fuel = max_fuel
    def fuel(self):
        Vehicle.display_info(self)
        print(f"Max fuel is {self.max_fuel} litres")

car1 = Car("Volvo","XC70",2015, "543 km")
car1.distance()
print("----------------")
bike1 = Bicycle("Trek","Marlin 7",2023,"sport")
bike1.sport()
print("----------------")
moto1 = Motorcycle("Yamaha","MT-07",2022,14)
moto1.fuel()
print("----------------")


