import json

list_of_firms = []
list_of_revenue = []

with open('test5.7.1.txt') as file:
    sum_revenue = 0
    num_of_firms = len(file.readlines())
    file.seek(0)
    for firm in file.readlines():
        data = (firm.replace('\n', '')).split(' ')
        print(data)
        revenue = int(data[2]) - int(data[3])
        list_of_revenue.append(revenue)
        list_of_firms.append(data[0])
        print(revenue)
        if revenue > 0:
            sum_revenue += revenue
        else:
            num_of_firms -= 1

dict_of_firms_revenue = dict(zip(list_of_firms, list_of_revenue))
dict_of_average_revenue = {'average_profit': sum_revenue / num_of_firms}
result_list = [dict_of_firms_revenue, dict_of_average_revenue]
print(result_list)
with open('test5.7.2.txt', 'w') as file:
    json.dump(result_list, file)
