sentence = input("Enter a sentence: ")

mylist = sentence.split(' ')

mylist.sort()

x = len(mylist)

if (sentence.strip() == ""):
    print("empty sentence! ")

else:
    dict1 = {mylist[0]: 1}

    y = 0
    while (y < x-1):
        if (mylist[y] == mylist[y+1]):
            y += 1
            dict1[mylist[y]] += 1

        else:
            dict1[mylist[y+1]] = 1
            y += 1

    for key, value in dict1.items():
        print(key + ' ->', value)
