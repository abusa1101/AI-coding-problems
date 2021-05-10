#include "enumeration.h"

int main(int argc, char** argv) {
    Enumeration myEnum;

    // 1) Read in the Bayes Net and Query
    if (myEnum.read()) return 1;

    // 2) Perform Exact Inference on the Bayes Net
    myEnum.inference();

    // 3) Print Answer to Terminal
    myEnum.print();

    return 0;
}
