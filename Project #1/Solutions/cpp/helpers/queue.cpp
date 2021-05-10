#include "queue.h"


void Queue::push(Node* node) {
    theQueue.push_back(node);
}

Node* Queue::pop() {
    Node* retVal = theQueue.front();
    theQueue.pop_front();
    return retVal;
}

bool Queue::empty() {
    return theQueue.empty();
}

int Queue::size() {
    return theQueue.size();
}

void Queue::print() {
    std::cout << "(";
    for (std::list<Node*>::iterator it=theQueue.begin(); it != theQueue.end();
                                                                    ++it) {
        std::cout << (*it)->f << ", ";
    }
    std::cout << ")";
}




