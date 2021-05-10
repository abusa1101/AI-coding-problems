#include "sudoku.h"


using std::cout;
using std::endl;
using std::queue;


/*
*   Sudoku Constructor
*/
Sudoku::Sudoku() {
    board.assign(81, 0);
}


/*
*   solve: High Level Function that calls both AC-3 and the solver
*/
bool Sudoku::solve() {
    CSP csp;

    // 1) Initialize the CSP problem for sudoku
    initCSP(&csp);

    // 2) Run AC-3 to reduce the domains for each variable
    if (!AC_3(&csp)) {
        cout << "Not consistent!" << endl;
        return false;
    }

    // 3) Solve the rest using search (assigning values we're sure of first)
    for (unsigned i = 0; i < 81; i++) {
        if (csp.D[i].size() == 1) {
            board[i] = csp.D[i][0];
        }
    }
    return search(&csp, 0);
}

void Sudoku::initCSP(CSP* csp) {
    // D (Domain)
    for (int i=0; i < 81; i++) {
        vector<int> domain;
        if (board[i] == 0) {
            for (int j = 1; j < 10; j++) {
                domain.push_back(j);
            }
        } else {
            domain.push_back(board[i]);
        }
        csp->D.push_back(domain);
    }

    // C (Constraints)
    for (int i=0; i < 81; i++) {
        vector<Arc> arcVec = arcConstraints(i);
        csp->C.push_back(arcVec);
    }
}


/*
*   AC_3 Algorithm
*
*   Returns false if an inconsistency is found, true otherwise
*/
bool Sudoku::AC_3(CSP* csp) {
    // generate all of the arcs in the csp
    queue<Arc> arcQ;
    for (unsigned i = 0; i < (csp->C).size(); i++) {
        for (unsigned j = 0; j < (csp->C)[i].size(); j++) {
            arcQ.push((csp->C)[i][j]);
        }
    }

    while (!arcQ.empty()) {
        Arc nextArc = arcQ.front(); arcQ.pop();
        if (revise(csp, nextArc)) {
            if ((csp->D)[nextArc.i].empty()) {
                return false;
            }
            vector<int> neighVec = neighbors(nextArc.i);
            for (unsigned i = 0; i < neighVec.size(); i++) {
                Arc arc(neighVec[i], nextArc.i);
                arcQ.push(arc);
            }
        }
    }

    return true;
}


/*
*   revise
*
*   Returns true IFF we revise the domain of arc.i
*/
bool Sudoku::revise(CSP* csp, Arc arc) {
    bool revised = false;
    unsigned maxI = (csp->D)[arc.i].size();

    for (unsigned i = 0; i < maxI; i++) {
        int x = (csp->D)[arc.i][i];
        bool sat = false;
        for (unsigned j = 0; j < (csp->D)[arc.j].size(); j++) {
            int y = (csp->D)[arc.j][j];
            if (constrSat(csp, x, y, arc.i, arc.j)) {
                sat = true;
                break;
            }
        }
        if (sat == false) {
            (csp->D)[arc.i].erase ( (csp->D)[arc.i].begin() + i );
            maxI--;
            revised = true;
        }
    }

    return revised;
}


/*
*   constrSat
*
*   Returns true if location i == x, location j == y satisfies constraints
*/
bool Sudoku::constrSat(CSP* csp, int x, int y, int i, int j) {
    if (x != y) return true;

    vector<Arc> constraints = (csp->C)[i];

    for (unsigned i = 0; i < constraints.size(); i++) {
        if (constraints[i].j == j) {
            return false;
        }
    }

    return true;
}

/*
*   Arc Constraints
*/
vector<Arc> Sudoku::arcConstraints(int ind) {
    vector<Arc> arcVec;
    vector<int> neighVec = neighbors(ind);

    for (unsigned i = 0; i < neighVec.size(); i++) {
        Arc arc(ind, neighVec[i]);
        arcVec.push_back(arc);
    }

    return arcVec;
}


/*
*   neighbors
*/
vector<int> Sudoku::neighbors(int ind) {
    vector<int> neighVec;

    int row, col;
    ind2rc(ind, &row, &col);

    // Add row neighbors
    int rInd = index(row, 0);
    for (int i = rInd; i < (rInd+9); i++) {
        if (i != ind) {
            neighVec.push_back(i);
        }
    }

    // Add col neighbors
    int cInd = index(0, col);
    for (int i = cInd; i < (cInd + 81); i = i + 9) {
        if (i != ind) {
            neighVec.push_back(i);
        }
    }

    // Add box neighbors (using bInd as our accessor)
    int bInd = index(row - (row % 3), col - (col % 3) );
    for (int i = 0; i < 9; i++) {
        if ( (i == 3) || (i == 6) ) {
            bInd = bInd + 6;
        }
        if (bInd != ind) {
            neighVec.push_back(bInd);
        }
        bInd++;
    }

    return neighVec;
}

/*
*   Backtracking search
*/
bool Sudoku::search(CSP* csp, int ind) {
    for (int i=ind; i < 81; i++) {
        if (board[i] != 0) continue;

        // Try every variable in the domain
        for (unsigned j = 0; j < ( (csp->D)[i].size() - 1); j++) {
            board[i] = (csp->D)[i][j];
            if (!validPlacement(i)) {
                continue;
            }
            if (search(csp, i+1)) {
                return true;
            }
        }
        board[i] = (csp->D)[i].back();
        if (validPlacement(i)) {
            if (search(csp, i+1)) {
                return true;
            }
        }
        board[i] = 0;
        return false;
    }

    return validBoard();
}

//////////////////////////////////////////////////////////////////////////////
//                                                                          //
//                                                                          //
//                         Validity Checkers                                //
//                                                                          //
//                                                                          //
//////////////////////////////////////////////////////////////////////////////


/*
*   Returns true if no constraints are violated
*
*   Checks every constraint
*
*/
bool Sudoku::validBoard() {
    // Check Row Constraints
    for (int i=0; i < 9; i++) {
        if (!validRow(i)) {
            return false;
        }
    }

    // Check Col Constraints
    for (int j=0; j < 9; j++) {
        if (!validCol(j)) {
            return false;
        }
    }

    // Check Box Constraints
    for (int ii = 0; ii < 3; ii++) {
        for (int jj = 0; jj < 3; jj++) {
            if (!validBox(ii, jj)) {
                return false;
            }
        }
    }

    // otherwise return true
    return true;
}

/*
*   validPlacement
*
*   Returns true if value i doesn't violate any binary constraints
*/
bool Sudoku::validPlacement(int i) {
    int row, col;
    ind2rc(i, &row, &col);

    return (validRow(row) &&
            validCol(col) &&
            validBox(row/3, col/3));
}


/*
*   Verifies row is valid
*/
bool Sudoku::validRow(int i) {
    for (int j=0; j < 8; j++) {
        if (board[index(i, j)] == 0) continue;
        for (int k=j+1; k < 9; k++) {
            if (board[index(i, j)] == board[index(i, k)]) {
                return false;
            }
        }
    }
    return true;
}


/*
*   Verifies col is valid
*/
bool Sudoku::validCol(int j) {
    for (int i=0; i < 8; i++) {
        if (board[index(i, j)] == 0) continue;
        for (int k=i+1; k < 9; k++) {
            if (board[index(i, j)] == board[index(k, j)]) {
                return false;
            }
        }
    }
    return true;
}


/*
*   Verifies box is valid
*/
bool Sudoku::validBox(int ii, int jj) {
    for (int i=ii*3; i < (ii*3+3); i++) {
        for (int j=jj*3; j < (jj*3+3); j++) {
            if (board[index(i, j)] == 0) continue;
            for (int ki = i; ki < (ii*3+3); ki++) {
                for (int kj = jj*3; kj < (jj*3+3); kj++) {
                    if ( (ki == i) && (kj == j) ) continue;
                    if (board[index(i, j)] == board[index(ki, kj)]) {
                        return false;
                    }
                }
            }
        }
    }
    return true;
}


//////////////////////////////////////////////////////////////////////////////
//                                                                          //
//                                                                          //
//                         Helper  Functions                                //
//                                                                          //
//                                                                          //
//////////////////////////////////////////////////////////////////////////////


/*
*   converts row i, col j, to vector index
*/
int Sudoku::index(int i, int j) {
    return (i*9 + j);
}


/*
*   converts vector index to row i, col j
*/
void Sudoku::ind2rc(int ind, int* row, int* col) {
    int row_, col_;

    row_ = 0;
    while (ind >= 9) {
        ind = ind - 9;
        row_++;
    }
    col_ = ind;

    (*row) = row_;
    (*col) = col_;
}


/*
*   Reads in "suinput.csv" and populates board
*
*   Returns 0 on success, 1 on failure
*/
int Sudoku::readInputFile() {
    std::ifstream inFile("suinput.csv");
    // std::ifstream inFile("suinput_worlds_hardest.csv");
    std::string line, val;

    // Read in the data
    if (inFile.is_open()) {
        for (int i=0; i < 9; i++) {
            if (getline(inFile, line)) {
                for (int j=0; j < 9; j++) {
                    val = line[j*2];
                    board[index(i, j)] = std::stoi(val);
                }
            } else {
                cout << "error reading suinput.csv" << endl;
                return 1;
            }
        }
        inFile.close();
        return 0;
    } else {
        cout << "Unable to open file" << endl;
        return 1;
    }
}


/*
*   Writes board to "suoutput.csv"
*/
void Sudoku::writeOutputFile() {
    std::ofstream outFile("suoutput.csv");

    for (int i=0; i < 9; i++) {
        for (int j=0; j < 9; j++) {
            outFile << board[index(i, j)];
            if (j != 8) outFile << ",";
        }
        if (i != 8) outFile << endl;
    }
    outFile.close();
}

/*
*   Writes board to "suoutput.csv"
*/
void Sudoku::writeOutputFileFail() {
    std::ofstream outFile("suoutput.csv");

    for (int i=0; i < 9; i++) {
        for (int j=0; j < 9; j++) {
            outFile << 0;
            if (j != 8) outFile << ",";
        }
        if (i != 8) outFile << endl;
    }
    outFile.close();
}

/*
*   writeToTerminal
*
*   Writes board to terminal
*/
void Sudoku::writeToTerminal() {
    for (int i=0; i < 9; i++) {
        for (int j=0; j < 9; j++) {
            cout << board[index(i, j)];
            if (j != 8) cout << ",";
        }
        cout << endl;
    }
    cout << endl;
}


















