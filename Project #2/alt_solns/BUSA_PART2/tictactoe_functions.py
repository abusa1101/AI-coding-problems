#!/usr/bin/python3
import sys
import csv
import math
import random

X_CHOICE = 'x'
O_CHOICE = 'o'
BLANK_CELL = '-'

def setup_board():
    board = [BLANK_CELL] * 9
    # board = [0] * 9
    # for i in range(3):
    #     board[i] = list_name[0][i]
    # for i in range(3, 6):
    #     board[i] = list_name[1][i - 3]
    # for i in range(6, 9):
    #     board[i] = list_name[2][i - 6]
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
    if check_win(board, O_CHOICE):
        score = 1
    elif check_win(board, X_CHOICE):
        score = -1
    else:
        score = 0
    return score

def terminate_game(board):
    if check_win(board, X_CHOICE) or check_win(board, O_CHOICE):
        return True
    return False

def valid_action(board):
    actions = []
    for i, action in enumerate(board):
        if action == BLANK_CELL:
            actions.append(i)
    return actions

def generate_random(seed):
    random.seed(seed)
    random_idx = []
    for _i in range(0, 15):
        idx = math.floor(9 * random.random())
        random_idx.append(idx)
    return random_idx

def move_x(random_idx_x, board):
    for i, _item in enumerate(random_idx_x):
        if board[random_idx_x[i]] == BLANK_CELL:
            return random_idx_x[i]
    return None

def max_value(board, depth):
    max_score = -100
    max_i = None
    if depth == 0 or terminate_game(board): #check for game termination
        score = return_utility(board)
        return score, 0 #return utility if terminating
    for i in valid_action(board): #action here is the index of the empty cell
        board[i] = O_CHOICE #set blank cell to player choice
        #second argumet used to check # of empty cells left i.e. termination state
        min_score, _min_i = min_value(board, len(valid_action(board)))
        if min_score > max_score: #reset score and index as needed
            max_score = min_score
            max_i = i
        board[i] = BLANK_CELL #reset cell back to empty
    return max_score, max_i

def min_value(board, depth):
    min_score = 100
    min_i = None
    if depth == 0 or terminate_game(board): #check for game termination
        score = return_utility(board)
        return score, 0 #return utility if terminating
    for i in valid_action(board): #action here is the index of the empty cell
        board[i] = X_CHOICE #set blank cell to player choice
        max_score, _max_i = max_value(board, len(valid_action(board)))
        if max_score < min_score: #reset score and index as needed
            min_score = max_score
            min_i = i
        board[i] = BLANK_CELL  #reset cell back to empty
    return min_score, min_i

# def get_score(board, score, is_max):
#     for i in valid_action(board): #action here is the index of the empty cell
#         if not is_max:
#             board[i] = X_CHOICE
#             (final_score, final_idx) = max_value(board, len(valid_action(board)))
#             if final_score < score:
#                 score = final_score
#                 final_idx = i
#         else:
#             board[i] = O_CHOICE
#             (final_score, final_idx) = min_value(board, len(valid_action(board)))
#             if final_score > score:
#                 score = final_score
#                 final_idx = i
#         board[i] = BLANK_CELL
#     return (final_score, final_idx)


def rand_turn(board):
    depth = len(valid_action(board))
    if depth == 0 or terminate_game(board):
        return
    random_idx_x = generate_random(int(sys.argv[1]))
    valid_idx = move_x(random_idx_x, board)
    if valid_idx in valid_action(board):
        board[valid_idx] = X_CHOICE

def run_game(board):
    return len(valid_action(board)) > 0 and not terminate_game(board)

def play_game(board):
    player = X_CHOICE #set which player goes first
    file = csv.writer(open("tictactoe.csv", 'w'), delimiter=',')
    while run_game(board):
        if player == X_CHOICE:
            min_value(board, len(valid_action(board)))
            rand_turn(board)
            player = O_CHOICE
        else:
            _score, idx = max_value(board, len(valid_action(board)))
            board[idx] = O_CHOICE
            player = X_CHOICE
        write_file(file, board)

def declare_winner(board):
    if check_win(board, X_CHOICE):
        print('AI LOSES :(')
    elif check_win(board, O_CHOICE):
        print('AI WINS!')
    else:
        print('DRAW..')
