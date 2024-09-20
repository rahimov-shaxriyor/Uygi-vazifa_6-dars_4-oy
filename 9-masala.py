text = 'salomlar'

harf = 'a'

for i in text:

    if harf in i:

        print(i.replace('a', 'A'), end='')

    else:

        print(i, end='')