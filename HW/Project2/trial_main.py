#!/usr/bin/python3
import sys
import trial_funcs as t
import csv

x_choice = 'x'
o_choice = 'o'
RAND = -1
AI = +1
list_ttt = t.read_file("ttt_in.csv")
board = t.setup_board(list_ttt)

file = csv.writer(open("ttt_out.csv", 'w'), delimiter=',')
# while len(t.empty_cells(board)) > 0 and not t.game_over(board):
#     # print(len(t.empty_cells(board)))
#     # print(board)
#     t.rand_turn(board, o_choice, x_choice)
#     t.ai_turn(board, o_choice, x_choice)
#     t.write_file(file, board)
player_turn = x_choice
while len(t.empty_cells(board)) > 0 and not t.game_over(board):
    if player_turn == x_choice:
        (m, q_i) = t.min_val(board, len(t.empty_cells(board)))
        t.rand_turn(board, o_choice, x_choice, player_turn)

    else:
        (m, p_i) = t.max_val(board, len(t.empty_cells(board)))
        board[p_i] = 'o'
        player_turn = x_choice
    t.write_file(file, board)

if t.wins(board, x_choice):
    print('RANDOM WINS!')
elif t.wins(board, o_choice):
    print('AI WINS!')
else:
    print('DRAW!')
