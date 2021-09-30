quantity = int(input('Give a number of elements you want to put in the list: '))
users_list = []
for j in range(0, quantity):
    elem = input('Give an element for your list: ')
    users_list.append(elem)

print(users_list)


def change_nums(first, last, step):
    for i in range(first, last, step):
        users_list[i], users_list[i+1] = users_list[i+1], users_list[i]


if len(users_list) % 2 == 0:
    change_nums(0, quantity-1, 2)
else:
    change_nums(0, quantity-2, 2)

print(users_list)
