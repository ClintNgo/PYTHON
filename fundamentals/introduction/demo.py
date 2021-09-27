likes_bbq = True
# print(type(likes_bbq))
likes_fruits = False
weight = 185
print(type(weight))
iq = 9000
# print(len(iq))
name = "Clint"
print(type(name))
age =   "28"
print(len(age))

if likes_bbq and weight > 100:
    weight += 10
    age = int(age) + 5
    print(name + " weighs " + str(weight) + " lbs and is " + str(age) + " years old.")
elif likes_fruits or iq > 80:
    weight -= 10
    print(weight)
else:
    print(weight)


# my_money = 5
# print(type(my_money))

# if my_money > 10:
#     print("I am happy")
# else:
#     print("I am broke and sad")
#     #pass -- allow code to continue on



