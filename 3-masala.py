list1 = ['salom', 123, True, 'Hayr', 'world', 3.14, '7214']

text = [i for i in list1 if isinstance(i, str)]

text.sort()

other = [i for i in list1 if not isinstance(i, str)]

print(text)
print(other)



