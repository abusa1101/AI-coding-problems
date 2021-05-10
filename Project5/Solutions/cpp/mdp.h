#ifndef MDP_H_
#define MDP_H_

// C Includes
#include <math.h>

// C++ includes
#include <iostream>
#include <vector>
#include <string>
#include <fstream>        // ifstream / ofstream
#include <unordered_map>  // unordered_map
#include <iomanip>        // std::setprecision


using std::vector;
using std::string;


class MDP {
 public:
  MDP();

  // User Functions
  int readInput();
  void run();
  int writeOutput();

  // Value Iteration Functions
  vector<double> valueIteration();

  // Helper Functions
  double P(int s_, int s, int a) { return P_[a][s][s_]; }
  double R(int s, int a) { return R_[s][a]; }

 private:
  // MDP Variables and Parameters
  vector<string> states;    // <S1, S2, S3>
  std::unordered_map<string, int> nameToState;
  int numStates = 0;        // (e.g. 3)

  vector<string> actions;   // <a1, a2>
  std::unordered_map<string, int> nameToAction;
  int numActions = 0;       // (e.g. 2)

  vector<vector<vector<double>>> P_;    // [a][s][s'] (prob s->s' by a)
  vector<vector<double>> R_;   // R[s][a] (reward of doing a in s)

  double gamma;             // discount factor
  double eps;               // tolerance

  vector<double> U_final;   // final Utilities
  vector<int>    policy;    // final policy

  double negInf = -1000000000;  // large negative #

  // File I/O
  string inFilename = "mdpinput.txt";
  string outFilename = "policy.txt";
};

#endif  // MDP_H_

