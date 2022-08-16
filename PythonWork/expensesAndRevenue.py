#Practice file to learn python

finances = {}

def initialize_finances():
    finances['cost'] = 0
    finances['revenue'] = 0

    
def add_costs():
    get_input = input()
    
    while get_input != 'done':
        cost = float(get_input)

        finances['cost'] += cost

        print(finances['cost'])

        get_input = input()

    return finances['cost']


def add_revenues():
    get_input = input()
    
    while get_input != 'done':
        revenue = float(get_input)

        finances['revenue'] += revenue

        print(finances['revenue'])

        get_input = input()

    return finances['revenue']

initialize_finances()
add_costs()
add_revenues()

print(finances['cost'], finances['revenue'])

net_cost = (finances['cost'] - finances['revenue'] ) 

print('Money needed to pay off rest of costs: $%.2f' % net_cost)
