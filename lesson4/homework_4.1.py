from sys import argv


def salary(rate, hours, premium):
    try:
        rate = float(rate)
        hours = float(hours)
        premium = float(premium)
    except ValueError:
        print('You have given not a number/-s!')
        exit(-1)
    result = rate * hours + premium
    return result


print(salary(argv[1], argv[2], argv[3]))
