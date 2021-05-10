""" Part II - Problem 2 (Sudoku) """

import csv
from collections import deque

def revise(csp, arc):
    """ Revise function from AC-3 Algorithm """
    revised = False
    row_i, col_i = index_to_rc(arc[0])
    row_j, col_j = index_to_rc(arc[1])
    for x in csp.domains[row_i][col_i]:
        sat = False
        for y in csp.domains[row_j][col_j]:
            if x != y:
                sat = True
                break
        if not sat:
            csp.domains[row_i][col_i].remove(x)
            revised = True
    return revised


def ac_3(csp):
    """ AC-3 Algorithm - Return false if inconsistency found, true otherwise """
    # 1) Grab all of the constraint arcs
    arc_queue = deque()
    for i in range(0, 9):
        for j in range(0, 9):
            for arc in csp.constraints[i][j]:
                arc_queue.append(arc)

    # 2) Check each arc for consistency
    while len(arc_queue) > 0:
        next_arc = arc_queue.popleft()
        if revise(csp, next_arc):
            row, col = index_to_rc(next_arc[0])
            if len(csp.domains[row][col]) == 0:
                return False
            neighbor_idxs = neighbors(row, col)
            for neighbor_idx in neighbor_idxs:
                arc = (neighbor_idx, next_arc[0])
                arc_queue.append(arc)

    return True


def rc_to_index(i, j):
    """ Returns the linear index from the row and column """
    return i*9 + j

def index_to_rc(idx):
    """ Returns the row and column from the linear index """
    row = int(idx / 9)
    col = int(idx) % 9
    return row, col

def neighbors(row, col):
    """ Returns the constraint graph neighbors for index idx """
    neighbor_idxs = []

    # Add row neighbors
    for j in range(0, 9):
        if j != col:
            neighbor_idxs.append(rc_to_index(row, j))

    # Add col neighbors
    for i in range(0, 9):
        if i != row:
            neighbor_idxs.append(rc_to_index(i, col))

    # Add box neighbors
    box_row = int(row / 3) * 3
    box_col = int(col / 3) * 3
    for i in range(box_row, box_row + 3):
        for j in range(box_col, box_col + 3):
            if i != row and j != col:
                neighbor_idxs.append(rc_to_index(i, j))

    return  neighbor_idxs


def arc_constraints(row, col):
    """ Generate Arc Constraints for this row and col """
    arcs = []
    neighbor_idxs = neighbors(row, col)
    for neighbor_idx in neighbor_idxs:
        arc = (rc_to_index(row, col), neighbor_idx)
        arcs.append(arc)
    return arcs


class CSP:
    """ Constraint Satisfaction Problem """
    def __init__(self, board):
        self.domains = []
        self.constraints = []
        self.sudoku_init_domains(board)
        self.sudoku_init_constraints()

    def sudoku_init_domains(self, board):
        """ Initialize domains to 1-9 for every cell """
        for i in range(0, 9):
            row_domains = []
            for j in range(0, 9):
                domain = []
                if board[i][j] == 0:
                    for k in range(1, 10):
                        domain.append(k)
                else:
                    domain.append(board[i][j])
                row_domains.append(domain)
            self.domains.append(row_domains)

    def sudoku_init_constraints(self):
        """ Initialize constraints for the sudoku board """
        for i in range(0, 9):
            row_constraints = []
            for j in range(0, 9):
                arcs = arc_constraints(i, j)
                row_constraints.append(arcs)
            self.constraints.append(row_constraints)


class Sudoku:
    """ Sudoku Puzzle Class """
    def __init__(self):
        self.board = []
        self.read_input_file()
        self.csp = CSP(self.board)

    def read_input_file(self, fname="suinput.csv"):
        """ Read sudoku board puzzle from input file """
        with open(fname, 'r') as infile:
            csvreader = csv.reader(infile)
            lines = []
            for line in csvreader:
                lines.append(line)
            for i in range(0, 9):
                row_list = []
                for j in range(0, 9):
                    row_list.append(int(lines[i][j]))
                self.board.append(row_list)

    def write_output_file(self, fname="suoutput.csv"):
        """ Write Sudoku Board solution to output file """
        # 1) Open the file for writing
        f = open(fname, "w")

        # 2) Construct the output string
        out_str = ""
        for i in range(0, 9):
            out_str += str(self.board[i][0])
            for j in range(1, 9):
                out_str += "," + str(self.board[i][j])
            if i < 8:
                out_str += "\n"

        # 3) Write to the output file and then close it
        f.write(out_str)
        f.close()

    def write_output_file_fail(self, fname="suoutput.csv"):
        """ Write Failure Sudoku Board to output file """
        # 1) Open the file for writing
        f = open(fname, "w")

        # 2) Construct the output string
        out_str = ""
        for i in range(0, 9):
            out_str += str(0)
            for j in range(1, 9):
                out_str += "," + str(0)
            if i < 8:
                out_str += "\n"

        # 3) Write to the output file and then close it
        f.write(out_str)
        f.close()

    def solve(self):
        """ Solve the Sudoku Puzzle """
        # 1) Run AC-3
        if not ac_3(self.csp):
            print("AC-3 returned Inconsistent!")
            return False

        # 2) Assign Values we're sure of
        for i in range(0, 9):
            for j in range(0, 9):
                if len(self.csp.domains[i][j]) == 1:
                    self.board[i][j] = self.csp.domains[i][j][0]

        # 3) Solve the rest using search on the limited domains
        return self.search(0)


    def search(self, idx):
        """ Backtracking search """
        # Loop over every space that hasn't been filled yet
        row, col = index_to_rc(idx)
        for i in range(row, 9):
            for j in range(col, 9):
                if self.board[i][j] != 0:
                    continue

                # Try every value in its domain
                curr_idx = rc_to_index(i, j)
                for val in self.csp.domains[i][j]:
                    self.board[i][j] = val
                    if not self.valid_placement(i, j):
                        continue

                    if self.search(curr_idx+1):
                        return True

                # And if none of them work, set back to 0 and return failure
                self.board[i][j] = 0
                return False


        return self.valid_board()

    def valid_board(self):
        """ Constraint checker on whole board """
        # 1) Check Row Constraints
        for i in range(0, 9):
            if not self.valid_row(i):
                return False

        # 2) Check Col Constraints
        for j in range(0, 9):
            if not self.valid_col(j):
                return False

        # 3) Check Box Constraints
        for i in range(0, 3):
            for j in range(0, 3):
                if not self.valid_box(i*3, j*3):
                    return False

        # Otherwise return true
        return True

    def valid_placement(self, row, col):
        """ Constraint checker for a specific cell """
        return self.valid_row(row) and \
               self.valid_col(col) and \
               self.valid_box(int(row/3)*3, int(col/3)*3)


    def valid_row(self, row):
        """ Constraint checker on a specific row """
        for j in range(0, 8):
            if self.board[row][j] == 0:
                continue
            for k in range(j+1, 9):
                if self.board[row][j] == self.board[row][k]:
                    return False
        return True

    def valid_col(self, col):
        """ Constraint checker on a specific col """
        for i in range(0, 8):
            if self.board[i][col] == 0:
                continue
            for k in range(i+1, 9):
                if self.board[i][col] == self.board[k][col]:
                    return False
        return True

    def valid_box(self, row, col):
        """ Constraint checker on a specific box """
        values = []
        for i in range(row, row + 3):
            for j in range(col, col + 3):
                values.append(self.board[i][j])
        for k in range(1, 10):
            if values.count(k) > 1:
                return False
        return True


def main():
    """ main function to call sudoku code """
    # 1) Read in the sudoku board
    my_sudoku = Sudoku()

    # 2) Solve the sudoku board
    valid_solution = my_sudoku.solve()

    # 3) Write the solution
    if valid_solution:
        print("Success!")
        my_sudoku.write_output_file()
    else:
        print("Failure!")
        my_sudoku.write_output_file_fail()


def test_input_output():
    """ Test Code for input output """
    my_sudoku = Sudoku()
    my_sudoku.write_output_file()


if __name__ == "__main__":
    main()
    # test_input_output()
