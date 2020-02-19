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

def write_file(file_name, updated_board):
    with open(file_name, 'w') as sorted_f:
        file = csv.writer(sorted_f, delimiter=',')
        file.writerow(updated_board[0:3])
        file.writerow(updated_board[3:6])
        file.writerow(updated_board[6:9])
        file.writerow('')

# Player X random ply
def x_move(random_idx_x, board):
    for i in range(len(random_idx_x)):
        if board[random_idx_x[i]] == '-':
            board[random_idx_x[i]] = 'x'
            return random_idx_x[i]
    return 0

def check_win(board, symbol):
    #Check rows
    if board[0] == board[1] and board[1] == board[2] and board[2] == symbol:
        return True
    if board[3] == board[4] and board[4] == board[5] and board[5] == symbol:
        return True
    if board[6] == board[7] and board[7] == board[8] and board[8] == symbol:
        return True
    #Check columns
    if board[0] == board[3] and board[3] == board[6] and board[6] == symbol:
        return True
    if board[1] == board[4] and board[4] == board[7] and board[7] == symbol:
        return True
    if board[2] == board[5] and board[5] == board[8] and board[8] == symbol:
        return True
    #Check diagonals
    if board[2] == board[4] and board[4] == board[6] and board[6] == symbol:
        return True
    if board[0] == board[4] and board[4] == board[8] and board[8] == symbol:
        return True
    return False
#
# def utility_test(board):
#     utility = 0
#     if check_win(board, 'x'):
#         utility = -10
#     if check_win(board, 'o'):
#         utility = 10
#     return utility

# def terminal_test(board):
#     #Check for no more blanks
#     if '-' not in board:
#         print('no more blank spaces')
#         return True
#     #Check for win
#     if utility_test(board) == 10:
#         print('o won!')
#         return True
#     if utility_test(board) == -10:
#         print('x won!')
#         return True
#     return False
#
# def max_value(board):
#     if terminal_test(board):
#         best_utility = utility_test(board, player)
#         return best_utility
#     v = -np.inf
#     for a in actions(board):
#         v = max(v, min_value(board))
#     return v
#
# def min_value(board):
#     if terminal_test(board):
#         best_utility = utility_test(board, player)
#         return best_utility
#     v = np.inf
#     for a in actions(state):
#         v = min(v, max_value(board))
#     return v
#
# def minmax_decision(state, best_utility):
#     player = game.to_move(state)
#     utility = max(best_utility, key=lambda a: min_value(game.result(state, a)))
#     return utility
#

def max_value(board, scores):
    result = check_win(board, 'o')
    if result:
        return scores['o']
    bestScore = -np.inf
    for i in range(9):
        if board[i] == '-':
            board[i] = 'o'
            score = minimax(board, depth + 1, True)
            board[i] = '-'
            bestScore = max(score, bestScore)
    print(bestScore)
    return bestScore

def min_value(board, scores):
    result = check_win(board, 'x')
    if result:
        return scores['x']
    bestScore = np.inf
    for i in range(9):
        if board[i] == '-':
            board[i] = 'x'
            score = minimax(board, depth + 1, false)
            board[i] = '-'
            bestScore = min(score, bestScore)
    print(bestScore)
    return bestScore

def bestMove(board):
  bestScore = -np.inf
  move = {}
  for i in range(9):
      if board[i] == '-':
          board[i] = 'o'
          score = minimax(board, 0, True)
          board[i] = '-'
          if score > bestScore:
              bestScore = score
              move[bestScore] = i
  board[move[bestScore]] = 'o'
  # currentPlayer = 'x'
  print(bestScore)
  print(board[move[bestScore]])
  return bestScore, board[move[bestScore]]

def minimax(board, depth, is_Max, ):
    print(board)
    if '-' not in board:
        print('no more blank spaces')
        return 0
    scores = {}
    scores['x'] = 10
    scores['o'] = -10
    scores['draw'] = 0

    if is_Max:
        score = max_value(board, scores)
        return score
    else:
        score = min_value(board, scores)
        return score
    return scores['draw']
