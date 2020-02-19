#!/usr/bin/python3
import sys
import tictactoe_functions as t
import csv

x_choice = 'x'
o_choice = 'o'

list_ttt = t.read_file("ttt_input.csv")
board = t.setup_board(list_ttt)

player_turn = x_choice #set which player goes first
file = csv.writer(open("tictactoe.csv", 'w'), delimiter=',')
while len(t.valid_action(board)) > 0 and not t.terminate_game(board):
    if player_turn == x_choice:
        t.min_value(board, len(t.valid_action(board)))
        t.rand_turn(board, o_choice, x_choice)
        player_turn = o_choice
    else:
        # print("in else"), player_turn
        (score, a) = t.max_value(board, len(t.valid_action(board)))
        board[a] = 'o'
        player_turn = x_choice
    t.write_file(file, board)

if t.check_win(board, x_choice):
    print('AI LOSES :(')
elif t.check_win(board, o_choice):
    print('AI WINS!')
else:
    print('DRAW..')
