list1 = [1, 2, 5, 6, 7, 8, 54, 646, 4, 7, 3, 66, 654, 6, 46, 6, 64, 7]

list2 = list1[::-1]

print(list1)
print(list2)

x = max(list1)
y = min(list1)
z = sum(list1)

print(x, y, z)

set1 = set(list1)
print(set1)

list3 = []
for n in set1:
    list3.append(n)

print(list3)
