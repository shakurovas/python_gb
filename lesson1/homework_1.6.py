result = input('Give the first result of a sportsman: ')
min_needed_result = input('Give the number of km, the first day with result bigger than this I should find: ')

try:
    result = float(result)
    min_needed_result = float(min_needed_result)

except ValueError:
    print('You have given not number/numbers!')
    exit(-1)

counter_of_days = 1
while result <= min_needed_result:
    result = result * 1.1
    counter_of_days += 1

print('Number of first day with needed result: ', counter_of_days)
