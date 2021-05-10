#ifndef TSP_H
#define TSP_H


#include <iostream>
#include <fstream>      // file input/output
#include <string>       // string
#include <vector>       // vector

#include "helpers/graph.h"

using std::cout;
using std::endl;
using std::string;


class State {
 public:
  int vertex_index = -1;
  int visited_indices = 0;

  const int getHash() {
      return (visited_indices << 8) | (0xFF & vertex_index);
  }
};



struct Action {
    State state;
    float cost;
};


class Domain {
 public:
  Domain();

  State startState;
  std::vector<Action> getActions(State state);
  bool goalTest(State state);
  float heuristic(State state);
  float heuristicNN(State state);
  float heuristicFN(State state);

  void printState(State state);

  char method;

 private:
  int readGraphFile();
  int readCoordFile();
  int readProbFile();

  int start;

  Graph myGraph;  // Underlying Graph

  int goal_visits = 0;
};

#endif  // TSP_H
