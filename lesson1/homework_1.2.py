time_in_sec = input('Give here a number of seconds: ')


def is_zero_needed(time_unit):
    if time_unit < 10:
        time_unit = '0' + str(time_unit)
        return time_unit
    else:
        return str(time_unit)


try:
    time_in_sec = float(time_in_sec)
except ValueError:
    print('This is not a number!')
    exit(-1)

hours = is_zero_needed(int(time_in_sec // 3600))
minutes = is_zero_needed(int(time_in_sec % 3600 // 60))
seconds = is_zero_needed(int(time_in_sec % 3600 % 60))

print(f'Time is: {hours}:{minutes}:{seconds}')
