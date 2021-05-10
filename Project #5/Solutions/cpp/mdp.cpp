#include "mdp.h"

using std::cout;
using std::endl;

/*
*   MDP Constructor
*/
MDP::MDP() {
}

//////////////////////////////////////////////////////////////////////////////
//                                                                          //
//                                                                          //
//                              User Functions                              //
//                                                                          //
//                                                                          //
//////////////////////////////////////////////////////////////////////////////

/*
*   readInput:  Reads in inFilename and populates mdp data
*
*       Returns 0 on success, 1 on failure
*/
int MDP::readInput() {
    std::ifstream inFile(inFilename);
    std::string line, val;
    double probVal;

    // Read in the data
    if (inFile.is_open()) {
        // 1) States
        getline(inFile, line);
        if (getline(inFile, line)) {
            while (line.length() > 0) {
                std::size_t first_comma = line.find_first_of(',');
                if (first_comma == string::npos) {
                    states.push_back(line);
                    nameToState[line] = numStates;
                    numStates++;
                    break;
                }
                states.push_back(line.substr(0, first_comma));
                nameToState[line.substr(0, first_comma)] = numStates;
                line = line.substr(first_comma + 2);
                numStates++;
            }
        } else { return 1; }

        // 2) Actions
        getline(inFile, line);
        if (getline(inFile, line)) {
            while (line.length() > 0) {
                std::size_t first_comma = line.find_first_of(',');
                if (first_comma == string::npos) {
                    actions.push_back(line);
                    nameToAction[line] = numActions;
                    numActions++;
                    break;
                }
                actions.push_back(line.substr(0, first_comma));
                nameToAction[line.substr(0, first_comma)] = numActions;
                line = line.substr(first_comma + 2);
                numActions++;
            }

        } else { return 1; }

        // 2.5) Set up P_ Variable
        for (int i=0; i < numActions; i++) {
            P_.push_back(vector<vector<double>>());
            for (int j=0; j < numStates; j++) {
                P_[i].push_back(vector<double>());
            }
        }

        // 3) Transition Model
        getline(inFile, line);
        getline(inFile, line);
        for (int i=0; i < numActions; i++) {
            getline(inFile, line);
            for (int j=0; j < numStates; j++) {
                if (getline(inFile, line)) {
                    while (line.length() > 0) {
                        std::size_t first_comma = line.find_first_of(',');
                        if (first_comma == string::npos) {
                            probVal = std::stod(line);
                            P_[i][j].push_back(probVal);
                            break;
                        }
                        probVal = std::stod(line.substr(0, first_comma));
                        P_[i][j].push_back(probVal);
                        line = line.substr(first_comma + 2);
                    }
                } else { return 1; }
            }
        }

        // 3.5) Set up R_ Vector
        for (int i=0; i < numStates; i++) {
            R_.push_back(vector<double>());
            for (int j=0; j < numActions; j++) {
                R_[i].push_back(0);
            }
        }

        // 4) Rewards
        getline(inFile, line);
        for (int i=0; i < numStates; i++) {
            for (int j=0; j < numActions; j++) {
                if (getline(inFile, line)) {
                    std::size_t first_comma = line.find_first_of(',');
                    std::size_t last_comma = line.find_last_of(',');

                    string theState = line.substr(0, first_comma);
                    string theAction = line.substr(first_comma+2,
                                                   last_comma-first_comma-2);
                    string theValue = line.substr(last_comma+2);

                    int s = nameToState[theState];
                    int a = nameToAction[theAction];
                    double zeValue = std::stod(theValue);

                    R_[s][a] = zeValue;
                } else { return 1; }
            }
        }

        // 5) Discount Factor
        getline(inFile, line);
        if (getline(inFile, line)) {
            gamma = std::stod(line);
        } else { return 1; }

        // 6) Epsilon (tolerance)
        getline(inFile, line);
        if (getline(inFile, line)) {
            eps = std::stod(line);
        } else { return 1; }
    } else {
        std::cout << "Error Opening " << inFilename << std::endl;
        std::cout << "Double Check Spelling, its presence, etc." << std::endl;
        return 1;
    }

    inFile.close();

    return 0;
}


/*
*   run
*/
void MDP::run() {
    // 1) Obtain the Utilities using valueIteration
    U_final = valueIteration();

    // 2) Obtain the Policy
    for (int s=0; s < numStates; s++) {
        double maxValue = negInf;
        int maxAction = 0;

        for (int a=0; a < numActions; a++) {
            double currValue = 0;
            for (int s_ = 0; s_ < numStates; s_++) {
                currValue += P(s_, s, a) * U_final[s_];
            }
            currValue = currValue * gamma + R(s, a);

            if (currValue > maxValue) {
                maxValue = currValue;
                maxAction = a;
            }
        }

        policy.push_back(maxAction);
    }
}


/*
*   writeOutput
*/
int MDP::writeOutput() {
    std::ofstream outFile(outFilename);

    outFile << "% Format: State: Action (Value)" << endl;
    for (int s=0; s < numStates; s++) {
        outFile << states[s] << ": ";
        outFile << actions[policy[s]] << " ";
        outFile << "(" << U_final[s] << ")" << endl;
    }

    outFile.close();
    return 0;
}

//////////////////////////////////////////////////////////////////////////////
//                                                                          //
//                                                                          //
//                       Value Iteration Functions                          //
//                                                                          //
//                                                                          //
//////////////////////////////////////////////////////////////////////////////

/*
*   valueIteration  (R&N Figure 17.4)
*/
vector<double> MDP::valueIteration() {
    // local variables
    vector<double> U(numStates, 0);
    vector<double> U_(numStates, 0);
    double delta = 0;

    while (1) {
        U = U_;
        delta = 0;
        for (int s=0; s < numStates; s++) {
            double maxValue = negInf;
            for (int a=0; a < numActions; a++) {
                double nextVal = 0;
                for (int s_=0; s_ < numStates; s_++) {
                    nextVal += P(s_, s, a) * U[s_];
                }
                nextVal = nextVal * gamma + R(s, a);

                if (nextVal > maxValue) {
                    maxValue = nextVal;
                }
            }
            U_[s] = maxValue;

            if (fabs(U_[s] - U[s]) > delta) {
                delta = fabs(U_[s] - U[s]);
            }
        }

        if (delta < eps * (1 - gamma) / gamma) {
            break;
        }
    }

    return U;
}


//////////////////////////////////////////////////////////////////////////////
//                                                                          //
//                                                                          //
//                           Helper Functions                               //
//                                                                          //
//                                                                          //
//////////////////////////////////////////////////////////////////////////////






















