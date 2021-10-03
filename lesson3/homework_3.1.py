def division(num_1, num_2):
    try:
        num_1 = float(num_1)
        num_2 = float(num_2)
        num_1 / num_2
    except ZeroDivisionError:
        print('The second number should not be zero!')
        exit(-1)
    except ValueError:
        print('Some of your inputs is/are not number/-s!')
        exit(-1)
    
    return num_1 / num_2


num1 = input('Give any number here: ')
num2 = input('Give any number here: ')
    
print(division(num1, num2))
