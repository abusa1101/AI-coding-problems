#include <sys/time.h>

#include "sudoku.h"



using std::cout;
using std::endl;

int64_t utime_now(void) {
    struct timeval tv;
    gettimeofday(&tv, NULL);
    return (int64_t) tv.tv_sec * 1000000 + tv.tv_usec;
}

int main(int argc, char** argv) {
    Sudoku mySudoku;

    // 1) Read in the sudoku board
    if (mySudoku.readInputFile()) {
        return 1;
    }

    // 2) Solve the sudoku board
    // int64_t time1 = utime_now();
    bool solved = mySudoku.solve();
    // int64_t time2 = utime_now();

    // 3) Report the solution and write the output board
    if (solved) {
        // cout << "Solved!" << endl;
        mySudoku.writeOutputFile();
    } else {
        // cout << "Failed!" << endl;
        mySudoku.writeOutputFileFail();
    }
    // cout << "Elapsed Time: " << (time2 - time1) / 1E6 << " seconds" <<endl;

    return 0;
}
