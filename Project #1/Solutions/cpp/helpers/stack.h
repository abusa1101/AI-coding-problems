#ifndef STACK_H
#define STACK_H

#include <list>
#include "node.h"
using std::list;


/*
*	Stack
*
*	A stack using vector
*/
class Stack {
 public:
  void push(Node* node);
  Node* pop();
  bool empty();
  int size();
  void print();

  list<Node*> theStack;
};


#endif  // STACK_H

