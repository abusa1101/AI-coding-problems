#ifndef NODE_H
#define NODE_H

#ifdef USING_ROUTE
    #include "../route.h"
#else
    #include "../tsp.h"
#endif


class Node {
 public:
  Node() : parent(nullptr), depth(0), f(0), g(0) {}

  explicit Node(State s) : state(s), parent(nullptr), depth(0), f(0), g(0) {}

  Node(State s, Node* p) : state(s), parent(p), depth(p->depth+1), f(0), g(0) {}

  Node(State s, Node* p, float F) : state(s), parent(p), depth(p->depth+1),
        f(F), g(0) {}

  Node(State s, Node* p, float F, float G) : state(s), parent(p),
        depth(p->depth+1), f(F), g(G) {}


  State state;
  Node* parent;
  int depth;

  float f;  // cost from Start to this node
  float g;
};

#endif  // NODE_H
