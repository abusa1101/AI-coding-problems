#include "dtree.h"

int main(int argc, char** argv) {
    Dtree myDtree;

    if (myDtree.readInput()) {
        std::cout << "Error Reading Input File" << std::endl;
    }

    myDtree.run();

    if (myDtree.writeOutput()) {
        std::cout << "Error Writing Output File" << std::endl;
    }

    return 0;
}
