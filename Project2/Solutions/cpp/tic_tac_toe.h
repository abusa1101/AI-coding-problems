#ifndef TIC_TAC_TOE_H_
#define TIC_TAC_TOE_H_

// C Headers
#include <stdlib.h>     /* srand, rand */
#include <math.h>

// C++ Headers
#include <string>     // std::string, std::stoi
#include <vector>
#include <fstream>   // ofstream
#include <iostream>

using std::vector;

typedef vector<int> State;

struct Action {
    int player;
    int space;
};

class ticTacToe {
 public:
  // Gameplay Functions
  void play();
  void move(vector<int>* board);
  void moveX(vector<int>* board);
  void moveO(vector<int>* board);

  // Minimax Functions
  Action minimaxDecision(State state, int player);
  float maxValue(State state);
  float minValue(State state);
  vector<Action> getActionSet(State state, int player);
  bool terminalTest(State state);
  float utility(State state);

  // Helper Functions
  int randSpace();
  void help();
  void printBoardToTerminal(vector<int> board);
  void printBoardToFile(vector<int> board);
  char v2C(int val);
  bool boardValid(vector<int> board);
  bool noMovesLeft(vector<int> board);
  bool winCheck(vector<int> board, int p);
  vector<int> result(vector<int> board, Action act);

 private:
  std::ofstream myfile;
  bool Xs_Turn = true;

  // Definition of pos and neg inf
  float posInf =  10000;
  float negInf = -10000;

  bool first_board_printed = false;
};

#endif  // TIC_TAC_TOE_H_




