number = input('Give any int number, please: ')
try:
    float(number)

except ValueError:
    print('This is not a number!')
    exit(-1)

double_number = int(number * 2)
thrice_number = int(number * 3)

print(int(number) + double_number + thrice_number)