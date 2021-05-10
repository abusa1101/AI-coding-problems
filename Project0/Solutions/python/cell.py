""" cell.py - Problem #1

    Matthew Romano
    eecs592
"""

from random import random
import copy

def update_cells(cell_auto):
    """ updates cell_auto according to update rule """
    cell_auto_last = copy.deepcopy(cell_auto)
    for j in range(1, len(cell_auto_last)-1):
        if (cell_auto_last[j] == 0) and (cell_auto_last[j-1] ^ cell_auto_last[j+1]):
            cell_auto[j] = True
        else:
            cell_auto[j] = False


def print_cells(cell_auto):
    """ prints out a cell_auto to the terminal with .s & *s"""
    str_out = ''
    for cell in cell_auto:
        if cell == 1:
            str_out += '*'
        else:
            str_out += '.'
    print(str_out)


def main():
    """ main function implementing a 1d cellular automaton """

    # 1) Ask user for # of cells and generations
    num_cells = int(input("# of cells in 1dCA: "))
    num_gens = int(input("# of generations to compute: "))

    # 2) Initialize Cellular Automaton
    cell_auto = [False] * num_cells
    for i in range(1, num_cells - 1):
        cell_auto[i] = random() < 0.5

    # 3) Print initial generation to terminal
    print_cells(cell_auto)

    # 4) Update the cells for each new generation and print
    for i in range(1, num_gens):
        update_cells(cell_auto)
        print_cells(cell_auto)


if __name__ == "__main__":
    main()
