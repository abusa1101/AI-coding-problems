#!/usr/bin/python3
import sys
import other_funcs as func
import search_funcs as search
import bts_funcs as bts

######### VERSION 1: BASED ON R&N ALGORITHM WITH MRV, LCV, FC AND CP #####################
## A. PRE-PROCESSING
# Pre-processing with AC-3 first, before trying BTS
VARIABLES, VALUES, NEIGHBORS, CONSTRAINTS = func.init_game()
search.ac_3(CONSTRAINTS, VALUES, NEIGHBORS)
IS_SOLVED_AC3 = func.solved(VALUES)
# Write solution (completely or partially solved depending on Sudoku difficulty) to output csv file
func.write_file(VALUES, 0)

## B. SEARCH (If necessary)
# If AC-3 didn't completely solve the sudoku problem,
# implement backtracking search with reduced domain values (from AC3)
if not IS_SOLVED_AC3:
    RESULT = search.bt_search(VARIABLES, VALUES, NEIGHBORS)
    GAME = {}
    for key in sorted(RESULT.keys()):
        GAME[key] = RESULT[key]

## C. WRITE OUTPUT (To csv file)
# Write completely solved solution or failure to output csv file
if not RESULT:
    func.write_file(GAME, 1)
    sys.stderr.write("Failed to solve Sudoku :(\n")
    sys.exit()
else:
    func.write_file(GAME, 0)


########## VERSION 2: BASED ON MY OWN BTS ALGORITHM WITH VERY MINIMAL HEURISTICS #########
########## Comment V1 & uncomment below to run V2

# ## A. PRE-PROCESSING
# # Pre-processing with AC-3 first, before trying BTS
# VARIABLES, VALUES, NEIGHBORS, CONSTRAINTS = func.init_game()
# search.AC3(CONSTRAINTS, VALUES, NEIGHBORS)
# IS_SOLVED_AC3 = func.solved(VALUES)
# # Write solution (completely or partially solved- depends on Sudoku difficulty) to output csv file
# func.write_file(VALUES, 0)
#
# ## B. SEARCH (If necessary)
# # If AC-3 didn't completely solve the sudoku problem, implement backtracking search
# if not IS_SOLVED_AC3:
#     GAME = bts.init_bts()
#     IS_SOLVED_BTS = bts.backtracking_search(GAME)
#
# ## C. WRITE OUTPUT (To csv file)
# # Write completely solved solution or failure to output csv file
# if not IS_SOLVED_BTS:
#     func.write_file(GAME, 1)
#     sys.stderr.write("Failed to solve Sudoku :(\n")
#     sys.exit()
# else:
#     func.write_file(GAME, 2)
