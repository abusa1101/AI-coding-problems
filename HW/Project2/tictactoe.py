#!/usr/bin/python3
import sys
import tictactoe_functions as t


if len(sys.argv) != 2:
    sys.stderr.write("Please enter a seed value for Player x, as a command line argument\n")
    sys.exit()

# LIST_TTT = t.read_file("ttt_input.csv")
BOARD = t.setup_board()

t.play_game(BOARD)

t.declare_winner(BOARD)
