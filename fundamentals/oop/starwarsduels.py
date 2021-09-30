from random import randint

class Trooper:
    game_name = "Star Wars Dojo Duel"
    everyone = []
    def __init__(self,name,attack):
        self.name = name
        self.weapon = "Blaster"
        self.attack = attack
        self.health = 100
        Trooper.everyone.append(self)

    def fight(self,foe):
        rand_attack = randint(0,self.attack)
        foe.health -= rand_attack
        if(foe.health > 0):
            print(f"{self.name} damages {foe.name} with a {self.weapon} by {rand_attack}")
            print(f"{foe.name} Health: {foe.health}")
        else:
            print(f"{self.name} obliterated {foe.name} with an attack of {rand_attack} using their {self.weapon}")
        return self

    def heal(self):
        rand_health = randint(1,10)
        future_health = self.health + rand_health
        if Trooper.can_heal(future_health):
            self.health += rand_health
            print(f"{self.name} healed {rand_health} | Current Health {self.health}")
        else:
            self.health = 100
            print(f"{self.name} health cannot be healed above 100 | Current Health: {self.health}")
        return self

    @classmethod
    def all_fighters(cls):
        print("Fighters:")
        for fighter in Trooper.everyone:
            print(fighter.name, fighter.weapon, fighter.attack, fighter.health)

    @staticmethod
    def can_heal(future_health):
        if future_health > 100:
            return False
        else:
            return True

class Jedi(Trooper):
    def __init__(self, name, attack):
        super().__init__(name,attack)
        self.health = 200
        self.weapon = "Light Saber"
        self.force_push_attack = 50
        self.trooper = Trooper("Finn", 25)

    def force_push(self,foe):
        foe.health -= self.force_push_attack
        if(foe.health > 0):
            print(f"{self.name} damages {foe.name} with a force push by {self.force_push_attack}")
            print(f"{foe.name} Health: {foe.health}")
        else:
            print(f"{self.name} obliterated {foe.name} with an attack of Force Push")
        return self

    def heal(self):
        rand_health = randint(1,20)
        future_health = self.health + rand_health
        if Jedi.can_heal(future_health):
            self.health += rand_health
            print(f"{self.name} healed {rand_health} | Current Health {self.health}")
        else:
            self.health = 200
            print(f"{self.name} health cannot be healed above 200 | Current Health: {self.health}")
        return self

    @staticmethod
    def can_heal(future_health):
        if future_health > 200:
            return False
        else:
            return True

class Sith(Jedi):
    def __init__(self,name,attack):
        super().__init__(name,attack)
        self.force_lighting_attack = 90

    
    def force_lighting(self,foe):
        foe.health -= self.force_lighting_attack
        if(foe.health > 0):
            print(f"{self.name} damages {foe.name} with a Force Lighting by {self.force_lighting_attack}")
            print(f"{foe.name} Health: {foe.health}")
        else:
            print(f"{self.name} obliterated {foe.name} with an attack of Force Lighting")
        return self

vader = Sith("Darth Vader", 75)

obi = Jedi("Obi Wan", 75)
rex = Trooper("Rex",50)

# print(vader.name)
# print(vader.health)
# print(vader.attack)
# print(vader.weapon)


vader.force_lighting(obi)
obi.force_push(vader)
obi.heal()
vader.heal()
vader.fight(obi)
obi.fight(vader)
vader.force_lighting(obi)
obi.force_push(vader)
obi.heal()
vader.heal()
vader.fight(obi)
obi.fight(vader)


# rex.fight(obi)
# obi.force_push(rex)
# obi.heal()
# rex.heal()
# rex.fight(obi)
# obi.force_push(rex)
# obi.heal()
# rex.heal()
# rex.fight(obi)
# obi.force_push(rex)

# print(obi.name)
# print(obi.weapon)
# print(obi.health)
# print(obi.attack)

# cody= Trooper("Cody",12)
# clint= Trooper("Clint", 90)

# Trooper.all_fighters()

# rex.fight(cody)
# cody.heal()
# cody.fight(rex)
# rex.fight(cody)
# cody.fight(rex)
# cody.heal()
# rex.fight(cody)
# cody.fight(rex)
# rex.fight(cody)
# clint.fight(rex)
# rex.fight(clint)
# clint.fight(rex)

# print("---------------------------------------")
# print(f"Welcome to {Trooper.game_name}")
# print(f"{rex.name} vs {cody.name}")
# print(f"{rex.name}: Attack - {rex.attack} | Health: {rex.health}")
# print(f"{cody.name}: Attack - {cody.attack} | Health: {cody.health}")



# rex = {
#     "name":"Rex",
#     "attack":15,
#     "weapon":"Blaster",
#     "health":100,
# }
# cody ={
#     "name":"Cody",
#     "attack":15,
#     "weapon":"Blaster",
#     "health":100,
# }

# print(rex["name"])
# print(rex["attack"])
# print(rex["weapon"])
# print(rex["health"])
# print(cody["name"])
# print(cody["attack"])
# print(cody["weapon"])
# print(cody["health"])