#include "enumeration.h"


using std::cout;
using std::endl;

using std::vector;
using std::string;

/*
*   Enumeration Constructor
*/
Enumeration::Enumeration() {
}

//////////////////////////////////////////////////////////////////////////////
//                                                                          //
//                                                                          //
//                          User Functions                                  //
//                                                                          //
//                                                                          //
//////////////////////////////////////////////////////////////////////////////

/*
*   read() 
*
*       reads in the Bayes Net and Query Files
*
*       Returns 0 on success, 1 on failure
*/
int Enumeration::read() {
    if (readBN()) {
        cout << "Failed to read in bn.txt" << endl;
        return 1;
    }
    if (readInput()) {
        cout << "Failed to read in input.txt" << endl;
        return 1;
    }

    return 0;
}

/*
*   inference
*
*       High Level Function called by main code for Enumeration Algorithm
*/
void Enumeration::inference() {
    vector<double> distribution = enumAsk(queryVar, queryEvidence);
    queryProb = distribution[0];
}

/*
*   print
*
*       Print Enumeration Results to Terminal
*/
void Enumeration::print() {
    cout << std::setprecision(5) << queryProb << endl;
}


//////////////////////////////////////////////////////////////////////////////
//                                                                          //
//                                                                          //
//                        Enumeration Functions                             //
//                                                                          //
//                                                                          //
//////////////////////////////////////////////////////////////////////////////


/*
*   enumAsk (R&N Figure 14.9)
*
*       Returns <True, False> distribution
*/
vector<double> Enumeration::enumAsk(int X, vector<int> e) {
    vector<double> Q_x(2, 0);
    vector<int> vars;
    for (int i=0; i < numVars; i++) {
        vars.push_back(i);
    }

    vector<int> e_x;
    e_x = e;

    // For each value in X (T,F) = (1,0)
    for (int j=0; j < 2; j++) {
        e_x[X] = j;
        Q_x[1 - j] = enumAll(vars, e_x);
    }

    return normalize(Q_x);
}

/*
*   enumAll (R&N Figure 14.9)
*/
double Enumeration::enumAll(vector<int> vars, vector<int> e) {
    if (vars.empty()) {
        return 1.0;
    }

    int Y = vars[0];

    // if Y has value y in e (any value other than -1, which is unassigned)
    int y = e[Y];
    if (y != -1) {
        return getProb(Y, y, getParents(Y, e)) * enumAll(Rest(vars), e);
    } else {
        vector<int> e_y;
        e_y = e;
        double sumVal = 0.0;
        for (int j = 0; j < 2; j++) {
            e_y[Y] = j;
            sumVal += getProb(Y, j, getParents(Y, e))
                           * enumAll(Rest(vars), e_y);
        }
        return sumVal;
    }

    return 0.0;
}



//////////////////////////////////////////////////////////////////////////////
//                                                                          //
//                                                                          //
//                           Helper Functions                               //
//                                                                          //
//                                                                          //
//////////////////////////////////////////////////////////////////////////////

/*
*   setProb
*
*       var: is the integer representation of the var prob we care about
*               (we assume it's true in the statement)
*
*       e: is the conditioned evidence, the "given", which must be parents
*
*       val: is the probability value that it has
*/
void Enumeration::setProb(int var, vector<int> e, double val) {
    // 1) First create an int that contains all of the info

    // Upper (32 - maxNumVars) bits come from var
    int var_e = 0;
    var_e = (var << maxNumVars);

    // lower maxNumVars bits come from e transformed into an int
    for (int j=0; j < numVars; j++) {
        if (e[j] == 1) {
            var_e = var_e + (1 << j);
        }
    }

    // 2) Next use your map and add an entry with var_e to val
    probMap[var_e] = val;
}

/*
*   getProb
*
*       var: is the integer representation of the var prob we care about
*
*       value: is either 0 or 1 (for false or true respectively) for what var is
*
*       e: is the conditioned evidence, the "given", which must be parents
*/
double Enumeration::getProb(int var, int value, vector<int> e) {
     // 1) First create an int that contains all of the info

    // Upper (32 - maxNumVars) bits come from var
    int var_e = 0;
    var_e = (var << maxNumVars);

    // lower maxNumVars bits come from e transformed into an int
    for (int j=0; j < numVars; j++) {
        if (e[j] == 1) {
            var_e = var_e + (1 << j);
        }
    }

    // 2) Next access the entry for var_e to get the val (and adjust for T/F)
    double probability = probMap[var_e];

    if (value) {
        return probability;
    } else {
        return (1 - probability);
    }
}

/*
*   Rest: Returns a vector of all elements without the first from input
*/
vector<int> Enumeration::Rest(vector<int> vars) {
    vars.erase(vars.begin());
    return vars;
}


/*
*   normalize
*
*       Assumes Q_x is of length 2
*
*       Returns a distribution normalized to w.r.t. the 1-norm
*/
vector<double> Enumeration::normalize(vector<double> Q_x) {
    double total = Q_x[0] + Q_x[1];

    if (total == 0) {
        return Q_x;
    }

    Q_x[0] = Q_x[0] / total;
    Q_x[1] = Q_x[1] / total;

    return Q_x;
}

/*
*   getParents: returns evidence vector only of parents being assigned
*
*       Y: the child
*
*       e: the full evidence
*
*       Returns evidence for only the parents
*/
vector<int> Enumeration::getParents(int Y, vector<int> e) {
    vector<int> e_P;
    e_P = e;

    vector<int> theParents = Parents[Y];

    for (int i=0; i < numVars; i++) {
        if (theParents[i] == 0) {
            e_P[i] = -1;
        }
    }

    return e_P;
}

//////////////////////////////////////////////////////////////////////////////
//                                                                          //
//                                                                          //
//                           Utility Functions                              //
//                                                                          //
//                                                                          //
//////////////////////////////////////////////////////////////////////////////

/*
*   readBN()
*
*       read in "bn.txt" and populate relevant variables
*
*       Returns 0 on success, 1 on failure
*/
int Enumeration::readBN() {
    // Need to populate variables (bnVars)
            // Edges to make graph so that Parent() function works
            // Probability Values

    std::ifstream bnFile(bnFilename);
    std::string line, val;

    // Read in the data
    if (bnFile.is_open()) {
        // 1) Random Variables
        getline(bnFile, line);
        if (getline(bnFile, line)) {
            for (unsigned i=0; i < line.length(); i = i + 3) {
                // Add the next variable
                char nextVar = line[i];
                bnVars.push_back(nextVar);
                varNameToNum[nextVar] = numVars;
                Parents.push_back(vector<int>());
                numVars++;
            }
        } else {
            cout << "error reading " << bnFilename << endl;
            return 1;
        }

        // 1.25) Make Sure # of Vars is maxNumVars or less (for "hashing")
        if (numVars > maxNumVars) {
            cout << "Too many variables: " << numVars;
            cout << " > " << maxNumVars << ". Failure!" << endl;
            return 1;
        }

        // 1.5) Populate Parents mapping (Graph edges prep) with 0s
        for (int i=0; i < numVars; i++) {
            for (int j=0; j < numVars; j++) {
                Parents[i].push_back(0);
            }
        }

        // 2) Graph Edges (From, To)
        getline(bnFile, line);
        while (1) {
            if (getline(bnFile, line)) {
                if (line[0] == '%') break;

                // Grab Graph Edge
                int from = varNameToNum[line[0]];
                int to   = varNameToNum[line[3]];

                Parents[to][from] = 1;

            } else {
                cout << "error reading " << bnFilename << endl;
                return 1;
            }
        }

        // 3) Probability Values (Read until End of File)
        while (1) {
            if (getline(bnFile, line)) {
                if (line[0] != 'P') break;

                // Get the variable
                int var = varNameToNum[line[2]];

                // Get the value
                std::size_t last_eq = line.find_last_of('=');
                double val = std::stod(line.substr(last_eq+1));
                if (line[4] == 'F') {
                    val = 1 - val;
                }

                // Handle weird corner case
                if (val == 0.0) {
                    val = 0.0000000000001;
                }

                // Get the "given"
                vector<int> e(numVars, -1);      // init to no assignments
                std::size_t first_hor = line.find_first_of('|');
                std::size_t i;
                if (first_hor != string::npos) {
                    for (i = first_hor+1; i < last_eq - 1; i = i + 4) {
                        int trueVal = (line[i+2] == 'T') ? (1) : (0);
                        int givenVar = varNameToNum[line[i]];
                        e[givenVar] = trueVal;
                    }
                }

                // Set the probability
                setProb(var, e, val);

            } else {
                break;
            }
        }

    } else {
        cout << "error opening " << bnFilename << endl;
        return 1;
    }


    bnFile.close();

    return 0;
}

/*
*   readInput()
*
*       read in "input.txt" and populate relevant variables
*
*       Returns 0 on success, 1 on failure
*/
int Enumeration::readInput() {
    std::ifstream inFile(inFilename);
    std::string line, val;

    // Read in the data
    if (inFile.is_open()) {
        // 1) Query random variable
        getline(inFile, line);
        if (getline(inFile, line)) {
            queryVar = varNameToNum[line[0]];
        } else {
            cout << "error reading " << inFilename << endl;
            return 1;
        }

        // 2) Evidence vector
        getline(inFile, line);
        if (getline(inFile, line)) {
            for (int i=0; i < numVars; i++) {
                queryEvidence.push_back(-1);
            }

            for (std::size_t j = 0; j < line.length(); j = j + 5) {
                int trueVal = (line[j+2] == 'T') ? (1) : (0);
                int givenVar = varNameToNum[line[j]];
                queryEvidence[givenVar] = trueVal;
            }
        } else {
            cout << "error reading " << inFilename << endl;
            return 1;
        }

    } else {
        cout << "error opening " << inFilename << endl;
        return 1;
    }


    inFile.close();

    return 0;
}



