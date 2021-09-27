try:
    revenue = float(input('How much is your company`s revenue? '))
    costs = float(input('How much are your company`s costs? '))
except ValueError:
    print('This is not a number!')
    exit(-1)

currency = input('What is your currency? ')

if revenue > costs:
    print('Your company works with a good profit!:)')
    print('Profitability is ', (revenue - costs) / revenue)
    employees = int(input('Give a number of employees in your company, please: '))
    print('Profit per one employee is: ', (revenue - costs) / employees, currency, '/ person')
elif revenue == costs:
    print('Your company is breaking even:|')
else:
    print('Your company works at a loss:(')
