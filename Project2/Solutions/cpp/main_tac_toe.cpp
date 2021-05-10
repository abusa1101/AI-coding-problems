#include "tic_tac_toe.h"
using std::cout;
using std::endl;
using std::vector;


int main(int argc, char** argv) {
    ticTacToe myTicTacToe;

    if (argc != 2) {
        myTicTacToe.help();
        return 1;
    }

    int seed = std::stoi(argv[1]);
    srand(seed);

    myTicTacToe.play();

    return 0;
}
