n = 6

yigindi = 0

for i in range(1, n+1):

    for j in range(1, i+1):

        if j==1:
            print(j, end='')
        else:
            print(f'+{j}', end='')

    yigindi+=i
    print(f'={yigindi}')

