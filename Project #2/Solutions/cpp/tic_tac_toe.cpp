#include "tic_tac_toe.h"
using std::cout;
using std::endl;
using std::vector;


//////////////////////////////////////////////////////////////////////////////
//                                                                          //
//                                                                          //
//                         Gameplay Functions                               //
//                                                                          //
//                                                                          //
//////////////////////////////////////////////////////////////////////////////

/*
*   Plays tic tac toe
*/
void ticTacToe::play() {
     // Init the board
    vector<int> board(9, 0);

    while (boardValid(board)) {
        move(&board);
        // printBoardToTerminal(board);
        printBoardToFile(board);
    }
}

/*
*   moves either x or o depending on who's turn it is
*
*   And then change who's turn it is
*/
void ticTacToe::move(vector<int>* board) {
    if (Xs_Turn) {
        moveX(board);
    } else {
        moveO(board);
    }

    Xs_Turn = !Xs_Turn;
}

/*
*   Randomly sample spaces until a free one is found
*
*   Then, choose that as the move
*/
void ticTacToe::moveX(vector<int>* board) {
    int space = randSpace();
    while ((*board)[space] != 0) {
        space = randSpace();
    }

    (*board)[space] = 1;
}

/*
*   Uses the Minimax algorithm to choose a move
*/
void ticTacToe::moveO(vector<int>* board) {
    Action nextAction = minimaxDecision((*board), 2);
    (*board)[nextAction.space] = nextAction.player;
}




//////////////////////////////////////////////////////////////////////////////
//                                                                          //
//                                                                          //
//                         Minimax Functions                                //
//                                                                          //
//                                                                          //
//////////////////////////////////////////////////////////////////////////////


/*
*   Minimax Algorithm
*
*   Returns an action 
*/
Action ticTacToe::minimaxDecision(State state, int player) {
    // Obtain the action set
    vector<Action> actionSet = getActionSet(state, player);

    // Compute arg max over the action set of minValue of each action
    int maxIndex = 0;
    float maxUtil = negInf;
    for (unsigned int i=0; i < actionSet.size(); i++) {
        float currUtil = minValue(result(state, actionSet[i]));
        if (currUtil > maxUtil) {
            maxUtil = currUtil;
            maxIndex = i;
        }
    }

    return actionSet[maxIndex];
}


/*
*   maxValue
*
*   Returns a utility value
*/
float ticTacToe::maxValue(State state) {
    if (terminalTest(state)) {
        float util = utility(state);
        return util;
    }

    float v = negInf;
    vector<Action> actionSet = getActionSet(state, 2);

    // Compute the max utility of the min value from the action set
    for (unsigned int i=0; i < actionSet.size(); i++) {
        float newV = minValue(result(state, actionSet[i]));
        if (newV > v) {
            v = newV;
        }
    }

    return v;
}

/*
*   minValue
*
*   In our case player 1 (x) is expected to be going
*
*   Returns a utility value
*/
float ticTacToe::minValue(State state) {
    if (terminalTest(state)) {
        float util = utility(state);
        return util;
    }

    float v = posInf;
    vector<Action> actionSet = getActionSet(state, 1);

    // Compute the min utility of the max value from the action set
    for (unsigned int i=0; i < actionSet.size(); i++) {
        float newV = maxValue(result(state, actionSet[i]));
        if (newV < v) {
            v = newV;
        }
    }

    return v;
}

/*
*   getActionSet
*
*   Returns a vector of available Actions for the player 
*/
vector<Action> ticTacToe::getActionSet(State state, int player) {
    vector<Action> actionSet;

    for (int i = 0; i < 9; i++) {
        if (state[i] == 0) {
            Action newAction;
            newAction.player = player;
            newAction.space = i;
            actionSet.push_back(newAction);
        }
    }

    return actionSet;
}

/*
*   terminalTest
*
*   Returns true if the game is over
*/
bool ticTacToe::terminalTest(State state) {
    bool bValid = boardValid(state);
    return !bValid;
}

/*
*   utility
*
*   Returns the utlity value of the given state (w.r.t. player 2 as Max)
*/
float ticTacToe::utility(State state) {
    float util;

    if (winCheck(state, 2)) {
        util = 1.0;
    } else if (winCheck(state, 1)) {
        util = 0.0;
    } else {
        util = 0.5;
    }

    // if neither player won, it's a cats game!
    return util;
}


//////////////////////////////////////////////////////////////////////////////
//                                                                          //
//                                                                          //
//                         Helper Functions                                 //
//                                                                          //
//                                                                          //
//////////////////////////////////////////////////////////////////////////////


/*
*   Returns a random int from 0-8
*/
int ticTacToe::randSpace() {
    return floor(9*((double) rand())/RAND_MAX);
}


void ticTacToe::help() {
    cout << "Usage: " << endl << endl;

    cout << "   ./tic_tac_toe <seed> " << endl << endl;

    cout << "   where <seed> is an integer # used to seed the PRNG";
    cout << endl << endl;
}

void ticTacToe::printBoardToTerminal(vector<int> board) {
    cout << endl;
    cout << v2C(board[6]) <<","<< v2C(board[7]) <<","<< v2C(board[8]) << endl;
    cout << v2C(board[3]) <<","<< v2C(board[4]) <<","<< v2C(board[5]) << endl;
    cout << v2C(board[0]) <<","<< v2C(board[1]) <<","<< v2C(board[2]) << endl;
}

void ticTacToe::printBoardToFile(vector<int> board) {
    if (!myfile.is_open()) {
        myfile.open("tictactoe.txt");
    }

    if (!first_board_printed) {
        first_board_printed = true;
    } else {
        myfile << endl << endl;
    }

    myfile << v2C(board[6]) <<","<< v2C(board[7]) <<","<< v2C(board[8]) << endl;
    myfile << v2C(board[3]) <<","<< v2C(board[4]) <<","<< v2C(board[5]) << endl;
    myfile << v2C(board[0]) <<","<< v2C(board[1]) <<","<< v2C(board[2]);
}


/*
*   Value 2 Char
*/
char ticTacToe::v2C(int val) {
    switch (val) {
        case 0:
            return '-';
            break;
        case 1:
            return 'x';
            break;
        case 2:
            return 'o';
            break;
        default:
            return '-';
    }
}


/*
*   Super verbose wincheck for player p
*       Could make it faster but for now who cares...
*/
bool ticTacToe::winCheck(vector<int> board, int p) {
    // Column wins
    bool col1 = (board[6] == p) && (board[3] == p) && (board[0] == p);
    bool col2 = (board[7] == p) && (board[4] == p) && (board[1] == p);
    bool col3 = (board[8] == p) && (board[5] == p) && (board[2] == p);

    // Row wins
    bool row1 = (board[6] == p) && (board[7] == p) && (board[8] == p);
    bool row2 = (board[3] == p) && (board[4] == p) && (board[5] == p);
    bool row3 = (board[0] == p) && (board[1] == p) && (board[2] == p);

    // Diagonal wins
    bool diag1 = (board[0] == p) && (board[4] == p) && (board[8] == p);
    bool diag2 = (board[2] == p) && (board[4] == p) && (board[6] == p);

    return (col1 || col2 || col3 || row1 || row2 || row3 || diag1 || diag2);
}

/*
*   Again a super verbose no moves checker
*       could make it faster...
*/
bool ticTacToe::noMovesLeft(vector<int> board) {
    return ((board[6] != 0) && (board[7] != 0) && (board[8] != 0) &&
            (board[3] != 0) && (board[4] != 0) && (board[5] != 0) &&
            (board[0] != 0) && (board[1] != 0) && (board[2] != 0) );
}


/*
*   Executes an action (creating a new state)
*/
vector<int> ticTacToe::result(vector<int> board, Action action) {
    board[action.space] = action.player;
    return board;
}


/*
*   Returns false if someone has won OR if there are no moves to play
*
*   Returns true otherwise
*/
bool ticTacToe::boardValid(vector<int> board) {
    if (winCheck(board, 1) || winCheck(board, 2)) {
        return false;
    }

    if (noMovesLeft(board)) {
        return false;
    }

    return true;
}



































