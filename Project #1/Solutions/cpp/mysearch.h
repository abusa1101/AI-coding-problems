#ifndef MYSEARCH_H
#define MYSEARCH_H

#include "helpers/queue.h"
#include "helpers/stack.h"
#include "helpers/priorityQueue.h"
#include "helpers/node.h"

#ifdef USING_ROUTE
    #include "route.h"
#else
    #include "tsp.h"
#endif


#include <math.h>
#include <iostream>
#include <algorithm>    // std::reverse
#include <unordered_map>
#include <set>
#include <utility>      // std::pair,
#include <vector>       // std::vector
#include <string>       // std::string
using std::cout;
using std::endl;
using std::vector;
using std::unordered_map;
using std::string;


class Solution {
 public:
  int totalNodesExpanded;
  vector<State> solPath;
  float totSolCost;
};

class Search {
 public:
  // Constructor
  explicit Search(Domain* myDomain_);

  // Top Level Function Call
  void generalSearch();

  // Search methods
  Solution BFS();
  Solution DFS();
  Solution iterDeep();
  Solution uniCost();
  Solution aStar();

  // work horse function that actually searches
  template <class queueType>
  Solution search(int depthLimit, bool useHeuristic);

  Solution returnSolution(Node* node, int nodesExp);

  void reportSolution();

  int maxDepth = 15;
  char method;

 private:
  Domain* myDomain;
};


#endif  // MYSEARCH_H
