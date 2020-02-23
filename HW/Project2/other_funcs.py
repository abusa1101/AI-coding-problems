#!/usr/bin/python3
import csv

y_keys = 'ABCDEFGHI'
x_keys = '123456789'

def combine(x_values, y_values):
    return [x + y for x in x_values for y in y_values]

def set_variables():
    variables = combine(y_keys, x_keys)
    return variables

def set_domain(game, variables):
    domain = {}
    for i, v in enumerate(variables):
        if game[i] == '0':
            domain.update([(v, list(range(1, 10)))])
        else:
            domain.update([(v, [int(game[i])])])
    return domain

def set_constraints(variables):
    squares = combine(y_keys, x_keys)
    constraint_list = (
        [combine(y_keys, x) for x in x_keys] + \
        [combine(y, x_keys) for y in y_keys] + \
        [combine(y, x) for y in ('ABC', 'DEF', 'GHI') for x in ('123', '456', '789')]
    )
    units = dict((s, [u for u in constraint_list if s in u]) \
             for s in squares)
    peers = dict((s, set(sum(units[s],[]))-set([s])) \
             for s in squares)
    constraints = {(variable, peer) for variable in variables for peer in peers[variable]}
    # print(constraints)
    return peers, constraints

def set_domain(variables, grid):
		i = 0
		values = dict()
		for cell in variables:
			if grid[i]!='0':
				values[cell] = grid[i]
			else:
				values[cell] = x_keys
			i = i + 1
		return values

def init_game():
    # board = '000000002100360540000708900040020100060901080002080030004105000058034006200000000'
    # board1 = '900760340428500006070084590043206009600053024290400670009047205762305000004020937'

    board = read_file()
    game = list(board)

    variables = set_variables()
    values = set_domain(variables, board)
    # domain = f.set_domain(game, variables)
    peers, constraints = set_constraints(variables)
    return variables, values, peers, constraints

def read_file():
    file = csv.reader(open("suinput.csv", 'r'), skipinitialspace='True')
    values = list(file)
    board = ''
    for val in values:
        for v in val:
            board = board + v
    return board

def write_file(values, is_failure):
    file = open("suoutput.csv", 'w')
    i = 1
    if is_failure == 0:
        for variable in values:
            file.write(values[variable])
            if i % 9 != 0:
                file.write(",")
            if i % 9 == 0:
                file.write("\n")
            i += 1
    elif is_failure == 1:
        for variable in values:
            file.write('0')
            if i % 9 != 0:
                file.write(",")
            if i % 9 == 0:
                file.write("\n")
            i += 1
    else:
        write_bts(values)

def write_bts(values):
    with open("suoutput.csv", 'w') as f:
        file = csv.writer(f, delimiter=',')
        file.writerows(values)

def solved(values):
    for variable in values:
        if len(values[variable]) > 1:
            # print(values[variable])
            return False
    return True
