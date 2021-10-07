from math import factorial


def fact(num):
    if num == 0:
        print(1)
    elif num < 0:
        print('You should give a POSITIVE number!')
        exit(-1)
    else:
        for i in range(1, num+1):
            yield factorial(i)


n = input('Give a positive int number, factorials from 1 to which you would like to count: ')

try:
    n = int(n)
except ValueError:
    print('You have given not a correct number!')
    exit(-1)

for elem in fact(n):
    print(elem)
