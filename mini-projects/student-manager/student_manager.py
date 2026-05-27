def input_dict():
    dicto1 = {}

    p = int(input("Number of students: "))

    while (p):
        key1 = input("Enter name: ")
        value1 = int(input("Enter marks: "))

        dicto1[key1] = value1
        p = p - 1

    return dicto1


student = input_dict()


def print_manager(printer):
    print(printer)


def find_average(average):
    sum = 0
    n = 0

    for key in average.keys():
        n = n + 1

    for value in average.values():
        sum = sum + value

    av = sum / n

    return av


print_manager(student)
x = find_average(student)

print(x)


def max_finder(maxer):
    y = max(maxer.values())

    for key, value in maxer.items():
        if maxer[key] == y:
            print(key, value)


max_finder(student)

name = input("Enter a name: ")


def name_finder(dicto, namer):

    count = 0

    for key, value in dicto.items():
        if key == namer:
            print(key, value)
            count += 1

    if count == 0:
        print("Not found!")


name_finder(student, name)
