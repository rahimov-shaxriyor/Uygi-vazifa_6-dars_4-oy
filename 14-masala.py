list1 = [('item1', '12.20'), ('item2', '15.10'), ('item3', '24.5')]

list2 = sorted(list1, key=lambda n: float(n[1]), reverse=True)

print(list2)