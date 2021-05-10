#ifndef QUEUE_H
#define QUEUE_H

#include <list>
#include "node.h"
using std::list;


/*
*	Queue
*
*	A queue using list
*/
class Queue {
 public:
  void push(Node* node);
  Node* pop();
  bool empty();
  int size();
  void print();

  list<Node*> theQueue;
};


#endif  // QUEUE_H

