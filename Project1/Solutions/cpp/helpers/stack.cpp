#include "stack.h"


void Stack::push(Node* node) {
    theStack.push_back(node);
}

Node* Stack::pop() {
    Node* retVal = theStack.back();
    theStack.pop_back();
    return retVal;
}

bool Stack::empty() {
    return theStack.empty();
}

int Stack::size() {
    return theStack.size();
}


void Stack::print() {
    std::cout << "(";
    for (std::list<Node*>::iterator it=theStack.begin(); it != theStack.end();
                                                                    ++it) {
        std::cout << (*it)->f << ", ";
    }
    std::cout << ")";
}




