from itertools import count

start = input('Give a small number less than 10 from which I should start counting: ')

try:
    start = int(start)
except ValueError:
    print('You have given not a number/-s!')
    exit(-1)

if start < 10:
    iter_count = count(start, step=1)
    for elem in iter_count:
        if elem == 10:
            break
        print(elem)
else:
    print('I asked you to give a number less than 10 !')
    exit(-1)

