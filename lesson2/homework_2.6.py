# [
# (1, {“название”: “компьютер”, “цена”: 20000, “количество”: 5, “eд”: “шт.”}),
# (2, {“название”: “принтер”, “цена”: 6000, “количество”: 2, “eд”: “шт.”}),
# (3, {“название”: “сканер”, “цена”: 2000, “количество”: 7, “eд”: “шт.”})
# ]

goods = list()
good = tuple()
properties = dict()
i = 1


def update_database(goods_array, name, price, quantity, units):
    new_dict = {'item': name,
                'price': price,
                'quantity': quantity,
                'units': units}
    new_tuple = (i, new_dict)
    goods_array.append(new_tuple)


while True:
    new_name = input('Please, enter the name of your good (for exit print 0): ')
    if new_name == '0':
        break
    new_price = input('Please, enter the price of your good: ')
    new_quantity = input('Please, enter the quantity of your good: ')
    new_units = input('Please, enter the name of unit of your good: ')

    update_database(goods, new_name, new_price, new_quantity, new_units)
    i += 1

print(goods)

print('Analytics:')

# {
# “название”: [“компьютер”, “принтер”, “сканер”],
# “цена”: [20000, 6000, 2000],
# “количество”: [5, 2, 7],
# “ед”: [“шт.”]
# }


def get_analytics(all_goods):
    data = {'items': [],
            'prices': [],
            'quantities': [],
            'units': []}
    for one_good in all_goods:
        data['items'].append(one_good[1]['item'])
        data['prices'].append(one_good[1]['price'])
        data['quantities'].append(one_good[1]['quantity'])
        data['units'].append(one_good[1]['units'])
    data['units'] = list(set(data['units']))
    print(data)


get_analytics(goods)
