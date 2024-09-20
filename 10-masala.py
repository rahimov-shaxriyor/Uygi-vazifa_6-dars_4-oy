n = 5

son = 0
yigindi = 0

for i in range(1, n+1):

    son = son*10+2
    yigindi+=son

    if i<n:
        print(son,end='+')
    else:
        print(son, end="=")

print(yigindi)