with open('test5.5.txt', 'w+') as file:
    nums = input('Give some numbers here, divide them by whitespace, please: ')
    file.write(nums)
    file.seek(0)
    new_nums_list = (file.readline()).split(' ')
    sum = 0
    for i in new_nums_list:
        try:
            i = float(i)
        except ValueError:
            print('Some of given items are not numbers! I will sum only nums')
            continue
        sum += i
    print('Sum of given numbers is: ', sum)
