from itertools import cycle

my_list = [1, 2, 3, 4, 5]
iterator = cycle(my_list)
iterations = 0

for i in iterator:
    if iterations < 100:  # I will break the cycle if number of iterations > 100
        print(i)
        iterations += 1
    else:
        print('Too much iterations')
        exit(0)
