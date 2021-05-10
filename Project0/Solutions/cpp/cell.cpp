/*
 Matthew Romano
 EECS 592
 Problem #1 - cell.cpp
*/

#include <stdlib.h>     // srand, rand
#include <time.h>       // time
#include <iostream>     // cout
#include <vector>       // vector

using std::vector;
using std::cout;
using std::cin;
using std::endl;

// Helper Functions
void userInput();
void initCells();
void printCells();
void updateCells();

// Global Variables
int numCells, numGens;
vector<bool> cellAutoCurr, cellAutoNext;


int main() {
    // Ask user for # of cells and generations
    userInput();

    // Initialize Cell Automaton
    initCells();

    // Print Initial Cell Automaton to terminal
    printCells();

    // Update the Cells for each new generation and print
    for (int i = 1; i < numGens; i++) {
        updateCells();
        printCells();
    }

    return 0;
}


/*
*	userInput
*
*/
void userInput() {
    cout << "# of cells in 1dCA: ";
    cin >> numCells;
    cout << "# of generations to compute: ";
    cin >> numGens;
}

/*
*	initCells
*
*/
void initCells() {
    // Set random seed and generate random values for cell automaton
    srand(time(NULL));
    for (int i = 0; i < numCells; i++) {
        cellAutoCurr.push_back(rand() % 2);
    }

    // Keep first and last values 0
    cellAutoCurr.front() = 0;
    cellAutoCurr.back() = 0;

    // Copy contents to "next" variable for initialization
    cellAutoNext = cellAutoCurr;
}

/*
*	printCells
*
*/
void printCells() {
    for (vector<bool>::iterator it = cellAutoCurr.begin();
                it != cellAutoCurr.end(); ++it) {
        if (*it == 0)
            cout << ".";
        else
            cout << "*";
    }
    cout << endl;
}

/*
*	updateCells
*
*/
void updateCells() {
    // 1) Populate cellAutoNext based on the update rule
    for (int i = 1; i < (cellAutoCurr.size()-1); i++) {
        if ( (cellAutoCurr[i] == 0) && (cellAutoCurr[i-1] ^ cellAutoCurr[i+1]) )
            cellAutoNext[i] = 1;
        else
            cellAutoNext[i] = 0;
    }

    // 2) Copy next to curr
    cellAutoCurr = cellAutoNext;
}




























