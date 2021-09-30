from random import randint
class Captain(Pirate):
    def __init__(self, name, strength):
        super().__init__(name, strength)
        self.health = 300
        self.cannon_shot_attack = 50
        self.pirate =Pirate("Cap", 60)

def cannon_shot(self,ninja):
    ninja.health -= self.cannon_shot_attack
    if(ninja.health > 0):
        print(f"{self.name} damages {ninja.name}")
        (f"{ninja.name} Health: {ninja.health}")
    else:
            print(f"{self.name} defeats {ninja.name}")
    return self