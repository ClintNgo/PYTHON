x = [ [5,2,3], [10,8,9] ] 
students = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'}
]
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]

x[1][0] = "15"
students[0]['last_name'] = "Bryant"
sports_directory['soccer'][0] = "Andres"
z[0]['y'] = 30

print(x)
print(students)
print(sports_directory)
print(z)

students = [
        {'first_name':  'Michael', 'last_name' : 'Jordan'},
        {'first_name' : 'John', 'last_name' : 'Rosales'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]

def iterateDictionary(students):
    for i in range(0,len(students)):
        print (f" first_name - {students[i]['first_name']}, last_name - {students[i]['last_name']}")
iterateDictionary(students)

students = [
        {'first_name':  'Michael', 'last_name' : 'Jordan'},
        {'first_name' : 'John', 'last_name' : 'Rosales'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]

def iterateDictionary2(key, students):
    for i in range(0,len(students)):
        print(f"{students[i][key]}")
iterateDictionary2('first_name', students)
iterateDictionary2('last_name', students)

dojo = {
    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

def printInfo(dojo):
    for i,j in dojo.items():
        print(f"{len(j)} {i.upper()}")
        for k in j:
            print(k)
printInfo(dojo)

# def printInfo(dojo):
#     print("")
# print (f"{len(dojo['locations'])} LOCATIONS" )
# for i in range (0,len(dojo['locations'])):
#     print(f"{dojo['locations'][i]}")
# print("--------------------------------------------")
# print (f"{len(dojo['instructors'])} INSTRUCTORS")
# for i in range (0,len(dojo['instructors'])):
#         print (f"{dojo['instructors'][i]}" )
# printInfo(dojo)
