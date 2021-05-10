#include "mdp.h"

using std::cout;
using std::endl;

int main(int argc, char** argv) {
    MDP myMDP;

    // 1) Read Input
    if (myMDP.readInput()) {
        cout << "Failed to read Input File" << endl;
        return 1;
    }

    // 2) Compute Optimal Policy
    myMDP.run();

    // 3) Write Output
    if (myMDP.writeOutput()) {
        cout << "Failed to Write Output File" << endl;
        return 1;
    }

    return 0;
}
