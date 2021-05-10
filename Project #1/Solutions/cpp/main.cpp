#include <iostream>
#include <fstream>      // file input/output
#include <string>       // string
#include <vector>       // vector


#ifdef USING_ROUTE
    #include "route.h"
#else
    #include "tsp.h"
#endif

#include "mysearch.h"


using std::cout;
using std::endl;


int main(int argc, char** argv) {
    #ifdef USING_ROUTE
        cout << "Problem 2 (Route Planning) Domain Selected!" << endl;
    #else
        cout << "Problem 3 (Traveling Salesman Problem) Domain Selected!"
             << endl;
    #endif

    // 1) Instantiate the specific domain
    Domain myDomain;

    // 2) Instantiate the general search
    Search mySearch(&myDomain);

    // 3) Search
    mySearch.generalSearch();

    return 0;
}
