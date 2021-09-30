from random import randint
class Pirate:

    def __init__( self , name, strength):
        self.name = name
        self.strength = strength
        self.speed = 3
        self.health = 100

    def show_stats( self ):
        print(f"Name: {self.name}\nStrength: {self.strength}\nSpeed: {self.speed}\nHealth: {self.health}\n")

    def attack ( self , ninja ):
        rand_strength = randint(0,self.strength)
        ninja.health -= rand_strength
        if(ninja.health > 0):
            print(f"{self.name} damages {ninja.name} for {rand_strength}")
            print(f"{ninja.name} Health: {ninja.health}")
        else:
            print(f"{self.name} defeats {ninja.name}")
        return self

    def heal(self):
        rand_health = randint(1,10)
        future_health = self.health + rand_health
        if Pirate.can_heal(future_health):
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

class Captain(Pirate):
    def __init__(self, name, strength):
        super().__init__(name, strength)
        self.health = 300
        self.cannon_shot_attack = 50
        self.pirate = Pirate("Cap", 60)

def cannon_shot(self,ninja):
    ninja.health -= self.cannon_shot_attack
    if(ninja.health > 0):
        print(f"{self.name} damages {ninja.name} for {rand_strength}")
        (f"{ninja.name} Health: {ninja.health}")
    else:
        print(f"{self.name} defeats {ninja.name}")
    return self