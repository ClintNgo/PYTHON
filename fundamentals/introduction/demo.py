# def add(a,b):
#     x = a + b
#     return x

# print(add(2))

# countdown = 10
# while countdown > 0:
#     print(countdown)
#     countdown -= 1
# print("Happy New Year!")

# for i in range(10,-1,-1):
#     print(i)
# for i in "why hello there":
#     print(i)

# ironman = {
#     "name":"Tony Stark",
#     "bday":"5/29/1970",
#     "weight":160,
#     "powers":{
#         "power1":"Genius",
#         "power2":"Master Engineer"
#     }
# }


# ironman.append[3]("power3":"money")
# for i in ironman:
#     print(i,ironman[i])
# print(ironman["powers"]["power1"])
# print(ironman)
# print(ironman["name"])
# ironman["age"] = 51
# print(ironman)
# value = ironman.pop("bday")
# print(value)
# del ironman["weight"]
# print(ironman)

heroes= ("Iron Man", "Hulk", "Wonder Woman", "Thor")
villians= ["Thanos","Joker", "Ultron", ["Marvel","DC"]]
empty = []

def say_hi(list):
    for i in list:
        if (type(i)==str):
            print(f"Hi {i}")

say_hi(heroes)
say_hi(villians)

# for i in range(0,len(heroes)):
#     print(i,heroes[i])

# for i in heroes:
#     print(i)

# for i in villians:
#     print(i)

# for i in villians[3]:
#     print(i)
# heroes[0] = "Old man captain america"
# heroes.append("Spiderman")
# empty.append("Hi")
# print(empty)
# heroes.append("Spiderman")
# heroes[0] = "Old Man Captain America"
# print(heroes)
# villians[3][1] = "DC Comics"
# print(villians)
# print(heroes)
# print(villians)
# combined = heroes + villians
# print(combined)
# lot_of_villians = 2 * villians
# print(lot_of_villians)
# print(heroes[1])
# print(heroes[0])
# print(villians[3][1])


# from random import randint
# print("you rolled a",randint(1,6))

# likes_bbq = True
# # print(type(likes_bbq))
# likes_fruits = False
# weight = 185
# print(type(weight))
# iq = 9000
# # print(len(iq))
# name = "Clint"
# print(type(name))
# age =   "28"
# print(len(age))

# if likes_bbq and weight > 100:
#     weight += 10
#     age = int(age) + 5
#     print(name + " weighs " + str(weight) + " lbs and is " + str(age) + " years old.")
#     print(f"{name} weighs {weight} lbs and is {age} years old.")
#     print("{} weighs {} lbs and is {} years old.".format(name,weight,age))
# elif likes_fruits or iq > 80:
#     weight -= 10
#     print(weight)
# else:
#     print(weight)


# my_money = 5
# print(type(my_money))

# if my_money > 10:
#     print("I am happy")
# else:
#     print("I am broke and sad")
#     #pass -- allow code to continue on



