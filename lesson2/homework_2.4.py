users_str = input('Please, give a string here: ')

users_list = users_str.split(' ')

for i, elem in enumerate(users_list, start=1):
    print(f'№ {i}: {elem[:10]}')
