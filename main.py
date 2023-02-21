class cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.hunger = 70
        self.energy = 60
    def __str__(self):
        return f"Cat {self.name}, age {self.age}"

    def sleep(self):
        if self.energy < 30:
           print("I`m sleep")
           self.energy += 50
           self.hunger += 10
        else:
            print("I want new toys!")
    def eat(self):
        if self.hunger < 30:
            print("I`m eat")
            self.hunger -= 30
            self.energy += 10

    def play(self):
        if self.energy >= 20 and self.hunger < 80:
            print("I`m play")
            self.energy -= 20
            self.hunger += 10
        else:
            print("I want sleep or eat")

barsik = cat("Barsik", 6)

print(barsik)

barsik.play()

barsik.eat()

barsik.sleep()
