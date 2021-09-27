number = input('Give any int number, please: ')

try:
    int(number)
except ValueError:
    print('This is not int number!')
    exit(-1)

i = 0
max_digit = number[0]
while i < len(number):
    if number[i] > max_digit:
        max_digit = number[i]
    i += 1
print(max_digit)
