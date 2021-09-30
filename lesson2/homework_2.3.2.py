# decision using list
seasons = [[1, 2, 12], [3, 4, 5], [6, 7, 8], [9, 10, 11]]

month_num = input('Give an int number in range from 1 to 12 inclusively: ')

try:
    month_num = int(month_num)
except ValueError:
    print('You have given an incorrect input data!')
    exit(-1)

if 0 < month_num < 13:
    if month_num in seasons[0]:
        print('winter')
    elif month_num in seasons[1]:
        print('spring')
    if month_num in seasons[2]:
        print('summer')
    if month_num in seasons[3]:
        print('fall')
else:
    print('This number does not correspond to any month!')
