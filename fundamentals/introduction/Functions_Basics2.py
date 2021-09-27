# 1
def countdown(number):
    for i in range(number,-1,-1):
        print(i)

# 2
def print_and_return(list):
    print(list[0])
    return list[1]

# 3
def first_plus_length(list):
    list = list[0] + len(list)
    return list

#  4
def values_greater_than_second(list):
    if len(list) < 2:
        return False
    list1 = []
    for i in list:
        if i>list[1]:
            list1.append(i)
            print(len(list1))
            return(list1)

# 5
def length_and_value(size,value):
    List = []
    for i in range(size):
        if i <= size:
            List.append(value)
    return List


