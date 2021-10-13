def greater_than_prev(your_list, your_elem):
    if your_elem > your_list[your_list.index(your_elem) - 1]:
        return True
    else:
        return False


users_list = []
elem_quantity = int(input('Give a number of elements your list will consist of: '))
for i in range(elem_quantity):
    elem = int(input('Give a number, please: '))
    users_list.append(elem)




new_users_list = [elem for elem in users_list[1:(len(users_list))] if greater_than_prev(users_list, elem)]

print(new_users_list)

