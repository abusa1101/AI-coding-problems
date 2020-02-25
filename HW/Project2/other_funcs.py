#!/usr/bin/python3
import csv

Y_KEYS = 'ABCDEFGHI'
X_KEYS = '123456789'

def set_keys(x_values, y_values):
    return [x + y for x in x_values for y in y_values]

def set_variables():
    variables = set_keys(Y_KEYS, X_KEYS)
    return variables

# def set_domain(game, variables):
#     domain = {}
#     for i, val in enumerate(variables):
#         if game[i] == '0':
#             domain.update([(val, list(range(1, 10)))])
#         else:
#             domain.update([(val, [int(game[i])])])
#     return domain

def set_constraints(variables):
    keys_list_row = [set_keys(Y_KEYS, x) for x in X_KEYS]
    keys_list_col = [set_keys(y, X_KEYS) for y in Y_KEYS]
    keys_list_sq = [set_keys(y, x) for y in ('ABC', 'DEF', 'GHI') for x in ('123', '456', '789')]

    units = {}
    neighbors = {}
    constraints = set()
    for var in variables:
        for unit in keys_list_row:
            if var in unit:
                units1 = unit
        for unit in keys_list_col:
            if var in unit:
                units2 = unit
        for unit in keys_list_sq:
            if var in unit:
                units3 = unit
        units[var] = [units1, units2, units3]
        neighbor_set = set([item for elem in units[var] for item in elem])
        neighbors[var] = neighbor_set - set([var])
        for neighbor in neighbors[var]:
            constraints.add((var, neighbor))
    return neighbors, constraints

def set_domain(variables, board):
    i = 0
    domain = {}
    for var in variables:
        if board[i] == '0':
            values[var] = X_KEYS
        else:
            values[var] = board[i]
        i += 1
    return domain

def init_game():
    board = read_file()
    _game = list(board)

    variables = set_variables()
    domain = set_domain(variables, board)
    neighbors, constraints = set_constraints(variables)
    return variables, domain, neighbors, constraints

def read_file():
    file = csv.reader(open("suinput.csv", 'r'), skipinitialspace='True')
    values = list(file)
    board = ''
    for value in values:
        for val in value:
            board = board + val
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
    with open("suoutput.csv", 'w') as file_s:
        file = csv.writer(file_s, delimiter=',')
        file.writerows(values)

def solved(values):
    for variable in values:
        if len(values[variable]) > 1:
            return False
    return True
