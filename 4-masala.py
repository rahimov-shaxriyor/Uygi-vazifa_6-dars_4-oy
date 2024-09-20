list1 = [1, 2, 33, 5, 6, 7, 7]
son = 8

list2 = []

for i in range(len(list1)):

    for j in range(i + 1, len(list1)):

        if list1[i] + list1[j] == son:

            print(f"{i}, {j}")




