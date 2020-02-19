#!/usr/bin/python3
import sys
import random
import numpy as np
import csv
import math

def generate_rand_x(s):
    random.seed(s)
    random_idx_x = []
    for i in range(5):
        idx = math.floor(9 * random.random())
        random_idx_x.append(idx)
    # print(random_idx_x)
    return random_idx_x

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

def x_move(random_idx_x, board):
    for i in range(len(random_idx_x)):
        if board[random_idx_x[i]] == '-':
            board[random_idx_x[i]] = 'x'
            return random_idx_x[i]
    return 0

def evaluate(board):
    if wins(board, 'o'):
        score = +1
    elif wins(board, 'x'):
        score = -1
    else:
        score = 0
    return score

def wins(board, choice):
    # print(choice)
    # print(board[7])
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

def game_over(board):
    return wins(board, 'x') or wins(board, 'o')

def empty_cells(board):
    cells = []
    for i, cell in enumerate(board):
        if cell == '-':
            cells.append(i)
    return cells

def valid_move(i, board):
    if i in empty_cells(board):
        return True
    else:
        return False

def set_move(i, player, board):
    if valid_move(i, board):
        board[i] = player
        return True
    else:
        return False

# def minimax(board, depth):
#     # print(board)
#     if depth == 0 or game_over(board): #check for game termination
#         score = evaluate(board)
#         return [-1, score] #return utility if terminating (and a bogus position)
#     best = [-1, -np.inf] #return best move (idx pos) and score
#     for i in empty_cells(board): #action here is the index of the empty cell
#         board[i] = 'o'
#         score = minimax(board, depth - 1)
#         board[i] = '-'
#         # print(score)
#         score[0] = i
#         if score[1] > best[1]: #pick max(current and best score) -> save this to best score
#             best = score  #max score
#         # print(best)
#     return best

def max_val(board, depth):
    print("in max")
    # print(board)
    maxv = -2
    p_i = None
    if depth == 0 or game_over(board): #check for game termination
        score = evaluate(board)
        return (score, 0) #return utility if terminating
    for i in empty_cells(board): #action here is the index of the empty cell
        board[i] = 'o'
        (m, min_i) = min_val(board, len(empty_cells(board)))
        if m > maxv:
            maxv = m
            p_i = i
        board[i] = '-'
    return (maxv, p_i)

def min_val(board, depth):
    # print(board)
    minv = 2
    q_i = None
    if depth == 0 or game_over(board): #check for game termination
        score = evaluate(board)
        return (score, 0) #return utility if terminating
    for i in empty_cells(board): #action here is the index of the empty cell
        board[i] = 'x'
        (m, max_i) = max_val(board, len(empty_cells(board)))
        if m < minv:
            minv = m
            q_i = i
        board[i] = '-'
    return (minv, q_i)

def ai_turn(board, c_choice, h_choice):
    # print(board)
    depth = len(empty_cells(board))
    if depth == 0 or game_over(board):
        return
    if depth < 9:
        move = minimax(board, depth)
        i = move[0]
        print(move)
        # print(i)
    set_move(i, 'o', board)

def rand_turn(board, c_choice, h_choice, player_turn):
    depth = len(empty_cells(board))
    if depth == 0 or game_over(board):
        return
    random_idx_x = generate_rand_x(int(sys.argv[1]))
    valid_idx = x_move(random_idx_x, board)
    set_move(valid_idx, 'x', board)
    player_turn = 'o'
