#ifndef PRIORITY_QUEUE_H
#define PRIORITY_QUEUE_H


#include <list>
#include <iostream>
#include "node.h"
using std::list;

/*
*	priorityQueue
*
*	A priorityQueue using list
*/
class priorityQueue {
 public:
  void push(Node* node);
  Node* pop();
  bool empty();
  int size();
  void print();

  list<Node*> theQueue;
};


#endif  // PRIORITY_QUEUE_H

