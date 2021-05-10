#ifndef ROUTE_H
#define ROUTE_H

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

  const int getHash() {
      return vertex_index;
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

  void printState(State state);

  char method;

 private:
  int readGraphFile();
  int readCoordFile();
  int readProbFile();

  int start;
  int goal;

  Graph myGraph;  // Underlying Graph
  State goalState;
};

#endif  // ROUTE_H








