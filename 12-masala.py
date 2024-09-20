list1 =  [(10, 20, 40), (40, 50, 60), (70, 80, 90)]

list2 = []

for i in list1:

    i = list(i)

    i[-1] = 100

    list2.append(tuple(i))

print(list2)

