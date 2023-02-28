import random

class Car:
    def __init__(self, mileage, fuel, condition):
        self.mileage = mileage
        self.fuel = fuel
        self.condition = condition

    def refuel(self, amount):
        self.fuel += amount

    def repair(self):
        self.condition = "new"

    def __str__(self):
        return f"Car with mileage {self.mileage} km, {self.fuel} l of fuel and condition {self.condition}"

    def generate_random_car():
        mileage = random.randint(0, 1000000)
        fuel = random.randint(0, 70)
        conditions = ["new", "used", "old", "dead"]
        condition = random.choice(conditions)

        return Car(mileage, fuel, condition)
car = Car.generate_random_car()
print(car)