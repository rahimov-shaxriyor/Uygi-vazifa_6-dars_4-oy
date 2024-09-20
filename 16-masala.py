list1 = [1, 2, 3]
list2 = [4, 5, 6]
list3 = [10, 11, 12]
list4 = [7, 8, 9]

list5 = [list1, list2, list3, list4]

result = max(list5, key=sum)

print(result)