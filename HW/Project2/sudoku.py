#!/usr/bin/python3
import sys
import other_funcs as func
import csp_funcs as csp
import bts_funcs as bts

#Check validity of input data

#Pre-processing with AC-3 first, before trying BTS
VARIABLES, VALUES, PEERS, CONSTRAINTS = func.init_game()
csp.AC3(CONSTRAINTS, VALUES, PEERS)
IS_SOLVED_AC3 = func.solved(VALUES)

#Write solution (completely or partially solved- depends on Sudoku difficulty) to output csv file
func.write_file(VALUES, 0)

#If AC-3 didn't completely solve the sudoku problem, implement backtracking search
if not IS_SOLVED_AC3:
    GAME = bts.init_bts()
    IS_SOLVED_BTS = bts.backtracking_search(GAME)

#Write completely solved solution or failure to output csv file
if not IS_SOLVED_BTS:
    func.write_file(GAME, 1)
    sys.stderr.write("Failed to solve Sudoku :(\n")
    sys.exit()
else:
    func.write_file(GAME, 2)
