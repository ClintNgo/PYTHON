class Ninja:
    Ninja = []
    def __init__(self, first_name , last_name , treats , pet_food):
        self.first_name = first_name 
        self.last_name = last_name 
        self.treats = treats
        self.pet_food= 2

    def walk(self,pet):
        pet.play()
        print(f" {self.first_name} {self.last_name} walks {pet.name}, it increases 5 health. Nikey now has {pet.health} health.")
        return self

    def feed(self,pet):
        pet.eat()
        print(f" {self.first_name} {self.last_name} feeds {pet.name}, it increases 5 energy and 10 health. Nikey now has {pet.energy} energy and {pet.health} health.")
        return self

    def bathe(self,pet):
        print(f" {self.first_name} {self.last_name} bathes {pet.name}")
        pet.noise()
        return self
