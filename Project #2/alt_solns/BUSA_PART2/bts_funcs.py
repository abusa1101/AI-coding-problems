import math
import csv

DIM = 9

def select_unassigned_value(game):
    for i in range(DIM):
        for j in range(DIM):
            if game[i][j] == 0:
                return i, j
    return -1, -1

def row_consistent(game, val, row):
    for i in range(DIM):
        if game[row][i] == val:
            return False
    return True

def col_consistent(game, val, col):
    for i in range(DIM):
        if game[i][col] == val:
            return False
    return True

def sq_range(i):
    i_adjusted = (math.floor(i / 3) * 3)
    return i_adjusted

def sq_consistent(game, val, row, col):
    for i in range(sq_range(row), sq_range(row) + 3):
        for j in range(sq_range(col), sq_range(col) + 3):
            if game[i][j] == val:
                return False
    return True

def consistent(game, val, row, col):
    if not row_consistent(game, val, row) or \
    not col_consistent(game, val, col) or \
    not sq_consistent(game, val, row, col):
        return False
    return True

def backtracking_search(game):
    row, col = select_unassigned_value(game)
    if row == -1 or col == -1:
        return True
    for i in range(1, DIM + 1):
        if consistent(game, i, row, col):
            game[row][col] = i
            if backtracking_search(game):
                return True
    game[row][col] = 0
    return False

def make_int(game):
    for i in range(DIM):
        for j in range(DIM):
            game[i][j] = int(game[i][j])
    return game

def init_bts():
    file = csv.reader(open("suinput.csv", 'r'), skipinitialspace='True')
    values = list(file)
    game = make_int(values)
    return game
