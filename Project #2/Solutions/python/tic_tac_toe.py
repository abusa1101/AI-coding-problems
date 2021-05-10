""" Part II - Problem 1 (Tic-Tac-Toe) """

import sys
import random
import math
import copy



class TicTacToe:
    """ Tic-Tac-Toe Game Class """
    def __init__(self):
        self.board = [0] * 9
        self.xs_turn = True
        self.output_str = None

    def play(self):
        """ High level function call that starts the game """
        while not self.terminal_test(self.board):
            self.move()
            self.add_to_output_string()
        self.print_boards_to_file()

    def move(self):
        """ high level move function, selects which player to move """
        if self.xs_turn:
            self.move_x()
        else:
            self.move_o()
        self.xs_turn = not self.xs_turn

    def move_x(self):
        """ move x randomly """
        space = self.rand_space()
        while self.board[space] is not 0:
            space = self.rand_space()
        self.board[space] = 1

    def move_o(self):
        """ move o using minimax algorithm """
        action = self.minimax_decision(self.board)
        self.board[action[0]] = action[1]

    def minimax_decision(self, board, player=2):
        """ minimax decision algorithm """
        action_set = self.get_action_set(board, player)

        max_index = 0
        max_util = -math.inf
        for idx, action in enumerate(action_set):
            curr_util = self.min_value(self.result(board, action))
            if curr_util > max_util:
                max_util = curr_util
                max_index = idx

        return action_set[max_index]

    def max_value(self, board):
        """ max_value function from minimax algorithm """
        if self.terminal_test(board):
            return self.utility(board)

        max_util = -math.inf
        action_set = self.get_action_set(board, 2)

        for action in action_set:
            new_util = self.min_value(self.result(board, action))
            max_util = max(max_util, new_util)

        return max_util

    def min_value(self, board):
        """ min_value function from minimax algorithm """
        if self.terminal_test(board):
            return self.utility(board)

        min_util = math.inf
        action_set = self.get_action_set(board, 1)

        for action in action_set:
            new_util = self.max_value(self.result(board, action))
            min_util = min(min_util, new_util)

        return min_util

    def result(self, board, action):
        """ obtains new copy of board with action taken """
        new_board = copy.deepcopy(board)
        new_board[action[0]] = action[1]
        return new_board

    def terminal_test(self, board):
        """ Returns false if someone has won OR if there are no moves to play, true otherwise """
        return self.win_check(board, 1) or self.win_check(board, 2) or self.no_moves_left(board)

    def no_moves_left(self, board):
        """ Returns True if there are no moves left to play """
        ret_val = all(space != 0 for space in board)
        # print("No moves left = ",ret_val)
        return ret_val

    def win_check(self, board, p):
        """ Returns True if player p has won, false otherwise """
        # Column wins
        col1 = (board[6] == p) and (board[3] == p) and (board[0] == p)
        col2 = (board[7] == p) and (board[4] == p) and (board[1] == p)
        col3 = (board[8] == p) and (board[5] == p) and (board[2] == p)

        # Row wins
        row1 = (board[6] == p) and (board[7] == p) and (board[8] == p)
        row2 = (board[3] == p) and (board[4] == p) and (board[5] == p)
        row3 = (board[0] == p) and (board[1] == p) and (board[2] == p)

        # Diagonal wins
        diag1 = (board[0] == p) and (board[4] == p) and (board[8] == p)
        diag2 = (board[2] == p) and (board[4] == p) and (board[6] == p)

        ret_val = (col1 or col2 or col3 or row1 or row2 or row3 or diag1 or diag2)
        # print("Win check = ",ret_val)
        return ret_val


    def utility(self, board):
        """ Returns the utility value of the board """
        if self.win_check(board, 2):
            return 1.0
        if self.win_check(board, 1):
            return 0.0
        return 0.5

    def get_action_set(self, board, player):
        """ Obtain a list of the available actions """
        action_set = []
        for i in range(0, 9):
            if board[i] == 0:
                new_action = (i, player)
                action_set.append(new_action)
        return action_set

    def rand_space(self):
        """ Generate a random integer in [0,8] """
        return math.floor(9 * random.random())

    def add_to_output_string(self):
        """Add current board to output string """
        # 1) Pre-process values to characters
        chars = ['-'] * 9
        for idx, val in enumerate(self.board):
            chars[idx] = self.val_to_char(val)

        # 2) Add the characters to the output string
        if self.output_str is None:
            self.output_str = ""
        else:
            self.output_str += "\n\n"
        self.output_str += chars[6] + "," + chars[7] + "," + chars[8] + "\n"
        self.output_str += chars[3] + "," + chars[4] + "," + chars[5] + "\n"
        self.output_str += chars[0] + "," + chars[1] + "," + chars[2]


    def print_boards_to_file(self):
        """ Print the output string to the file """
        f = open("tic_tac_toe.txt", "w")
        f.write(self.output_str)
        f.close()

    def val_to_char(self, val):
        """ convenience function for printing """
        if val == 0:
            return '-'
        if val == 1:
            return 'x'
        return 'o'


def main(prng_seed=42):
    """ main function to call tic_tac_toe code """

    # 1) Seed the PRNG
    random.seed(prng_seed)

    # 2) Init the Tic-Tac-Toe Game
    my_tic_tac_toe = TicTacToe()

    # 3) Play the game
    my_tic_tac_toe.play()




def cli_help():
    """ Command Line Interface Help Function """
    print("Please call tic_tac_toe.py as follows: python tic_tac_toe.py <seed> ")
    print("<seed> = (any number to initialize the PRNG)),")
    print()
    print("Example - : python tic_tac_toe.py 42")


if __name__ == "__main__":
    if len(sys.argv) is not 2:
        cli_help()
    else:
        main(sys.argv[1])
