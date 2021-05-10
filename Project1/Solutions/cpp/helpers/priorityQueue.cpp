#include "priorityQueue.h"


bool compare_nodes(const Node* first, const Node* second) {
    return first->f < second->f;
}


void priorityQueue::push(Node* node) {
    theQueue.push_back(node);
    theQueue.sort(compare_nodes);
}

Node* priorityQueue::pop() {
    Node* retVal = theQueue.front();
    theQueue.pop_front();
    return retVal;
}

bool priorityQueue::empty() {
    return theQueue.empty();
}

int priorityQueue::size() {
    return theQueue.size();
}

void priorityQueue::print() {
    std::cout << "(";
    for (std::list<Node*>::iterator it=theQueue.begin(); it != theQueue.end();
                                                                    ++it) {
        std::cout << (*it)->f << ", ";
    }
    std::cout << ")";
}


