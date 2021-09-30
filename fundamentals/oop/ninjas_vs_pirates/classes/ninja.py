from random import randint
class Ninja:

    def __init__( self , name, strength):
        self.name = name
        self.strength = strength
        self.speed = 5
        self.health = 100
    
    def show_stats( self,):
        print(f"Name: {self.name}\nStrength: {self.strength}\nSpeed: {self.speed}\nHealth: {self.health}\n")

    def attack ( self , pirate,):
        rand_strength  = randint(0,self.strength )
        pirate.health -= rand_strength 
        if(pirate.health > 0):
            print(f"{self.name} damages {pirate.name} for {rand_strength}")
            print(f"{pirate.name} Health: {pirate.health}")
        else:
            print(f"{self.name} defeats {pirate.name}!")
        return self

    def heal(self):
        rand_health = randint(1,10)
        future_health = self.health + rand_health
        if Ninja.can_heal(future_health):
            self.health += rand_health
            print(f"{self.name} healed {rand_health} | Current Health {self.health}")
        else:
            self.health = 100
            print(f"{self.name} health cannot be healed above 100 | Current Health: {self.health}")
        return self

    @staticmethod
    def can_heal(future_health):
        if future_health > 100:
            return False
        else:
            return True