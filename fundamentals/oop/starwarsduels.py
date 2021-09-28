from random import randint

class Trooper:
    game_name = "Star Wars Dojo Duel"
    def __init__(self,name,attack):
        self.name = name
        self.weapon = "Blaster"
        self.attack = attack
        self.health = 100

    def fight(self,foe):
        rand_attack = randint(0,self.attack)
        foe.health -= rand_attack
        if(foe.health > 0):
            print(f"{self.name} damages {foe.name} with a {self.weapon} by {rand_attack}")
            print(f"{foe.name} Health: {foe.health}")
        else:
            print(f"{self.name} obliterated {foe.name} with an attack of {rand_attack} using their {self.weapon}")


rex = Trooper("Rex",50)
cody= Trooper("Cody",12)

rex.fight(cody)
cody.fight(rex)
rex.fight(cody)
cody.fight(rex)
rex.fight(cody)
cody.fight(rex)
rex.fight(cody)

print("---------------------------------------")
print(f"Welcome to {Trooper.game_name}")
print(f"{rex.name} vs {cody.name}")
print(f"{rex.name}: Attack - {rex.attack} | Health: {rex.health}")
print(f"{cody.name}: Attack - {cody.attack} | Health: {cody.health}")



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