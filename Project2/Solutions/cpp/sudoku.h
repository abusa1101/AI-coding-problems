#ifndef SUDOKU_H_
#define SUDOKU_H_

// C++ includes
#include <iostream>
#include <vector>
#include <string>
#include <fstream>   // ifstream / ofstream
#include <queue>

using std::vector;


class Arc {
 public:
  Arc(int ii, int jj) : i(ii), j(jj) {}

  int i;
  int j;
};

class CSP {
 public:
  vector<int> X;
  vector<vector<int>> D;
  vector<vector<Arc>> C;
};

class Sudoku {
 public:
  Sudoku();

  // High Level Function Call
  bool solve();

  // AC-3 & Search
  void initCSP(CSP* csp);
  bool AC_3(CSP* csp);
  bool search(CSP* csp, int ind);
  bool revise(CSP* csp, Arc arc);
  bool constrSat(CSP* csp, int x, int y, int i, int j);
  vector<Arc> arcConstraints(int ind);
  vector<int> neighbors(int ind);

  // Validity Checkers
  bool validBoard();
  bool validPlacement(int i);
  bool validRow(int i);
  bool validCol(int j);
  bool validBox(int ii, int jj);

  // Helper Functions
  int index(int i, int j);
  void ind2rc(int ind, int* row, int* col);
  int readInputFile();
  void writeOutputFile();
  void writeOutputFileFail();
  void writeToTerminal();

 private:
  vector<int> board;
};

#endif  // SUDOKU_H_

