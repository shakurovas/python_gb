# decision using dict

months = {'winter': [1, 2, 12],
          'spring': [3, 4, 5],
          'summer': [6, 7, 8],
          'fall': [9, 10, 11]}

month_num = input('Give an int number in range from 1 to 12 inclusively: ')

try:
    month_num = int(month_num)
except ValueError:
    print('You have given not a correct input data!')
    exit(-1)

if 0 < month_num < 13:
    for season, numbers in months.items():
        for number in numbers:
            if number == month_num:
               print(season)
else:
    print('This number does not correspond to any month!')
