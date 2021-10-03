def users_numbers_sum():
    while True:
        str_of_numbers = input('Give a string of numbers, divided by whitespaces: ')
        str_of_numbers = str_of_numbers.split(' ')
        for i in range(len(str_of_numbers)):
            try:
                float(str_of_numbers[i])
            except ValueError:
                print('Finished')
                exit(0)
            if 'sum' in locals():
                if type(str_of_numbers[i]) == float or int:
                    sum += float(str_of_numbers[i])
                else:
                    break
            else:
                sum = float(str_of_numbers[i])
        print(sum)
    
users_numbers_sum()
