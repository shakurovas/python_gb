def sum_of_max_two(num_1, num_2, num_3):

    try:
        num_1 = float(num_1)
        num_2 = float(num_2)
        num_3 = float(num_3)

    except TypeError:
        print('Some of given numbers is/are not number/-s!')
        exit(-1)

    max_nums = [num_1, num_2, num_3]
    max_nums.remove(min(num_1, num_2, num_3))
    result = max_nums[0] + max_nums[1]
    if num_1 == num_2 == num_3:
        return f'All 3 numbers are equal, sum of two of them is {result}'
    elif num_1 == num_2 or num_1 == num_3 or num_2 == num_3:
        return f'Some of 2 numbers are equal, sum of one of them and the greatest is {result}'
    else:
        return f'Sum of two greatest of them is {result}'


num1 = input('Give any number, please: ')
num2 = input('Give any number, please: ')
num3 = input('Give any number, please: ')

print(sum_of_max_two(num1, num2, num3))
