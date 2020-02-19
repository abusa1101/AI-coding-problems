#!/usr/bin/python3
import sys
import random
import numpy as np
import csv
import math

def setup_board(list_name):
    board = [0] * 9
    for i in range(3):
        board[i] = list_name[0][i]
    for i in range(3,6):
        board[i] = list_name[1][i - 3]
    for i in range(6,9):
        board[i] = list_name[2][i - 6]
    return board

def read_file(file_name):
    file = csv.reader(open(file_name, 'r'), skipinitialspace='True')
    f_list = list(file)
    return f_list

def write_file(file, updated_board):
    file.writerow(updated_board[6:9])
    file.writerow(updated_board[3:6])
    file.writerow(updated_board[0:3])
    file.writerow('')

def check_win(board, choice):
    #Check rows
    if board[0] == board[1] and board[1] == board[2] and board[2] == choice:
        return True
    if board[3] == board[4] and board[4] == board[5] and board[5] == choice:
        return True
    if board[6] == board[7] and board[7] == board[8] and board[8] == choice:
        return True
    #Check columns
    if board[0] == board[3] and board[3] == board[6] and board[6] == choice:
        return True
    if board[1] == board[4] and board[4] == board[7] and board[7] == choice:
        return True
    if board[2] == board[5] and board[5] == board[8] and board[8] == choice:
        return True
    #Check diagonals
    if board[2] == board[4] and board[4] == board[6] and board[6] == choice:
        return True
    if board[0] == board[4] and board[4] == board[8] and board[8] == choice:
        return True
    return False

def return_utility(board):
    if check_win(board, 'o'):
        score = +1
    elif check_win(board, 'x'):
        score = -1
    else:
        score = 0
    return score

def terminate_game(board):
    return check_win(board, 'x') or check_win(board, 'o')

def valid_action(board):
    actions = []
    for i, action in enumerate(board):
        if action == '-':
            actions.append(i)
    return actions

def make_move(i, player, board):
    if i in valid_action(board):
        board[i] = player
        return True
    else:
        return False

def max_value(board, depth):
    max_v = -10
    max_i = None
    if depth == 0 or terminate_game(board): #check for game termination
        score = return_utility(board)
        return (score, 0) #return utility if terminating
    for i in valid_action(board): #action here is the index of the empty cell
        board[i] = 'o'
        (v, min_i) = min_value(board, len(valid_action(board)))
        if v > max_v:
            max_v = v
            max_i = i
        board[i] = '-'
    return (max_v, max_i)

def min_value(board, depth):
    min_v = 10
    min_i = None
    if depth == 0 or terminate_game(board): #check for game termination
        score = return_utility(board)
        return (score, 0) #return utility if terminating
    for i in valid_action(board): #action here is the index of the empty cell
        board[i] = 'x'
        (v, max_i) = max_value(board, len(valid_action(board)))
        if v < min_v:
            min_v = v
            min_i = i
        board[i] = '-'
    return (min_v, min_i)

def generate_random(s):
    random.seed(s)
    random_idx = []
    for i in range(0,5):
        idx = math.floor(9 * random.random())
        random_idx.append(idx)
    return random_idx

def move_x(random_idx_x, board):
    for i in range(len(random_idx_x)):
        if board[random_idx_x[i]] == '-':
            board[random_idx_x[i]] = 'x'
            return random_idx_x[i]
    return 0

def rand_turn(board, c_choice, h_choice):
    depth = len(valid_action(board))
    if depth == 0 or terminate_game(board):
        return
    random_idx_x = generate_random(int(sys.argv[1]))
    valid_idx = move_x(random_idx_x, board)
    # print(valid_idx)
    make_move(valid_idx, 'x', board)
