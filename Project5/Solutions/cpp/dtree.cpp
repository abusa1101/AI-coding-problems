#include "dtree.h"

#include <math.h>       /* log2 */
#include <queue>          // std::queue

/*
*   Dtree Constructor
*/
Dtree::Dtree() {
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
int Dtree::readInput() {
    std::ifstream inFile(inFilename);
    std::string line, val;

    // Read in the data
    if (inFile.is_open()) {
        // 1) Attributes
        getline(inFile, line);
        while (getline(inFile, line)) {
            // check if we finished the section
            if (line[0] == '%') {
                break;
            }

            // Find the Attribute Name
            std::size_t colon = line.find_first_of(':');
            string attribute = line.substr(0, colon);

            // Add the Attribute to our variables
            Attributes.push_back(attribute);
            attNameToInd[attribute] = numAttributes;
            attValues.push_back(vector<string>());

            // Add the Attribute Values to our variables
            line = line.substr(colon + 2);

            while (line.length() > 0) {
                std::size_t first_comma = line.find_first_of(',');
                if (first_comma == string::npos) {
                    attValues[numAttributes].push_back(line);
                    break;
                }
                attValues[numAttributes].push_back(line.substr(0, first_comma));
                line = line.substr(first_comma + 2);
            }

            // Increment # of Attributes
            numAttributes++;
        }

        // 2) Decision Values
        if (getline(inFile, line)) {
            while (line.length() > 0) {
                std::size_t first_comma = line.find_first_of(',');
                if (first_comma == string::npos) {
                    decisionVars.push_back(line);
                    decNameToInd[line] = numDecisionVars;
                    numDecisionVars++;
                    break;
                }
                decisionVars.push_back(line.substr(0, first_comma));
                decNameToInd[line.substr(0, first_comma)] = numDecisionVars;
                line = line.substr(first_comma + 2);
                numDecisionVars++;
            }
        } else { return 1; }

        // 3) Example Instances
        getline(inFile, line);
        getline(inFile, line);
        while (getline(inFile, line)) {
            // Create New Empty Example Vector
            Examples.push_back(vector<string>());

            // Populate the Example
            while (line.length() > 0) {
                std::size_t first_comma = line.find_first_of(',');
                if (first_comma == string::npos) {
                    Examples[numExamples].push_back(line);
                    break;
                }
                Examples[numExamples].push_back(line.substr(0, first_comma));
                line = line.substr(first_comma + 2);
            }

            // Increment the Number of Examples
            numExamples++;
        }
    } else {
        std::cout << "Error Opening Input File" << std::endl;
        return 1;
    }
    inFile.close();

    return 0;
}


/*
*   run
*/
void Dtree::run() {
    vector<int> attributes;
    for (int i=0; i < numAttributes; i++) {
        attributes.push_back(i);
    }

    decisionTree = decisionTreeLearning(Examples, attributes, Examples);
}


/*
*   writeOutput
*/
int Dtree::writeOutput() {
    std::ofstream outFile(outFilename);

    // BFS on tree
    std::queue<Node*> openList;
    openList.push(decisionTree);

    while (!openList.empty()) {
        // Grab Next Node off of the open list
        Node* currNode = openList.front(); openList.pop();

        // If its an Attribute Decision
        if (currNode->numChildren > 0) {
            // Print each edge to its children
            for (int i=0; i < currNode->numChildren; i++) {
                Node* child = currNode->children[i];

                // Print the line
                outFile << currNode->value << "? ";
                outFile << currNode->edges[i] << ", ";
                outFile << child->value;
                if (child->numChildren > 0) {
                    outFile << "?";
                }
                outFile << std::endl;

                // Add the child to the open list
                openList.push(child);
            }
        }
    }

    outFile.close();
    return 0;
}

//////////////////////////////////////////////////////////////////////////////
//                                                                          //
//                                                                          //
//                    Decision Tree Learning Functions                      //
//                                                                          //
//                                                                          //
//////////////////////////////////////////////////////////////////////////////

/*
*
*/
Node* Dtree::decisionTreeLearning(vector<vector<string>> examples,
                                 vector<int> attributes,
                                 vector<vector<string>> parent_examples) {
    Node* tree;

    if (examples.empty()) {
        return pluralityValue(parent_examples);
    } else if (sameClassification(examples)) {
        return pluralityValue(examples);            // the classification
    } else if (attributes.empty()) {
        return pluralityValue(examples);
    } else {
        // vector<string> A = maxImportance(attributes, examples);
        int A = maxImportance(attributes, examples);

        // A new decision tree with root test A
        tree = new Node(Attributes[A]);

        // Next Attributes (erase curr maxImportance)
        vector<int> nextAttr = attributes;
        for (int i=0; i < nextAttr.size(); i++) {
            if (nextAttr[i] == A) {
                nextAttr.erase(nextAttr.begin() + i);
            }
        }

        for (int i=0; i < attValues[A].size(); i++) {
            // Compute exs
            vector<vector<string>> exs;
            for (int j=0; j < examples.size(); j++) {
                if (examples[j][A] == attValues[A][i]) {
                    exs.push_back(examples[j]);
                }
            }

            // Recursively Call dTL to populate subtrees
            Node* subtree = decisionTreeLearning(exs, nextAttr, examples);

            // Add a branch to the tree
            tree->addChild(subtree, attValues[A][i]);
        }
    }

    // Return the decision tree
    return tree;
}

//////////////////////////////////////////////////////////////////////////////
//                                                                          //
//                                                                          //
//                    Decision Tree Helper Functions                        //
//                                                                          //
//                                                                          //
//////////////////////////////////////////////////////////////////////////////

/*
*
*/
Node* Dtree::pluralityValue(vector<vector<string>> examples) {
    vector<int> values(numDecisionVars, 0);

    // Tally up # of values
    for (int i=0; i < examples.size(); i++) {
        string value = examples[i][numAttributes];
        values[decNameToInd[value]]++;
    }

    // Find the plurality value (max # of tallies)
    int maxNum = 0;
    int maxVal = 0;
    for (int i=0; i < values.size(); i++) {
        if (values[i] > maxNum) {
            maxNum = values[i];
            maxVal = i;
        }
    }

    // Construct a subtree and return it
    Node* tree = new Node(decisionVars[maxVal]);
    return tree;
}


/*
*   sameClassification
*
*       Returns 1 if all examples have the same classification
*               0 otherwise
*/
bool Dtree::sameClassification(vector<vector<string>> examples) {
    string value = examples[0][numAttributes];

    for (int i=1; i < examples.size(); i++) {
        if (value != examples[i][numAttributes]) {
            return 0;
        }
    }

    return 1;
}


/*
*   maxImportance
*
*       Returns the attribute of max importance
*/
int Dtree::maxImportance(vector<int> attributes,
                         vector<vector<string>> examples) {
    // Compute first attribute's importance for comparison
    double maxValue = importance_Gen(attributes[0], examples);
    int maxAttribute = attributes[0];

    // Loop over all others, keeping track of the most important attribute
    for (int i=1; i < attributes.size(); i++) {
        double nextValue = importance_Gen(attributes[i], examples);
        if (nextValue > maxValue) {
            maxValue = nextValue;
            maxAttribute = attributes[i];
        }
    }

    // return the most important attribute
    return maxAttribute;
}

//////////////////////////////////////////////////////////////////////////////
//                                                                          //
//                                                                          //
//                    maxImportance Helper Functions                        //
//                                                                          //
//                                                                          //
//////////////////////////////////////////////////////////////////////////////

/*
*   importance
*       We assume that there are only 2 decision variables
*
*       Returns the importance of the given attribute on the examples 
*/
double Dtree::importance(int attribute, vector<vector<string>> examples) {
    // Calculate p & n
    string yes = decisionVars[0];
    int p = 0;
    for (int i=0; i < examples.size(); i++) {
        if (examples[i][numAttributes] == yes) {
            p++;
        }
    }
    int n = examples.size() - p;

    // Calculate the importance
    // double importanceValue = B(p,n) - Remainder(attribute, examples, p, n);

    // Calculate the importance
    double B_Val = B(p, n);
    double R_Val = Remainder(attribute, examples, p, n);
    double importanceValue = B_Val - R_Val;

    /*
    std::cout << "Regular Function" << std::endl;
    std::cout << "attribute = " << attribute << std::endl;
    std::cout << "B_Val = " << B_Val << std::endl;
    std::cout << "R_Val = " << R_Val << std::endl;
    std::cout << "importanceValue = " << importanceValue;
    std::cout << std::endl;
    */

    return importanceValue;
}


/*
*   B
*       Returns the entropy of a boolean R.V. with prob q
*/
double Dtree::B(int p, int n) {
    // Catch 0-entropy case to avoid NANs
    if ( (p == 0) || (n == 0) ) {
        return 0;
    }

    double q = static_cast<double>(p / (p+n));
    double entropy = -1 * (q*log2(q) + (1-q)*log2(1-q));

    return entropy;
}


/*
*   Remainder
*/
double Dtree::Remainder(int attr,
                        vector<vector<string>> examples,
                        int p,
                        int n) {
    double value = 0;

    for (int k=0; k < attValues[attr].size(); k++) {
        // Calculate pk and nk
        int pk = 0;
        int nk = 0;

        // Loop over all of the examples
        for (int j=0; j < examples.size(); j++) {
            // for every example with the attr value, calculate pk/nk
            if (examples[j][attr] == attValues[attr][k]) {
                if (examples[j][numAttributes] == decisionVars[0]) {
                    pk++;
                } else {
                    nk++;
                }
            }
        }

        if ((pk + nk) == 0) {
            continue;
        } else {
            // Calculate term for this k
            double firstPart = static_cast<double> ((pk+nk)/(p+n));
            value += firstPart * B(pk, nk);
        }
    }

    // return the value
    return value;
}
//////////////////////////////////////////////////////////////////////////////
//                                                                          //
//                                                                          //
//            maxImportance Helper Functions   (General Case)               //
//                                                                          //
//                                                                          //
//////////////////////////////////////////////////////////////////////////////

/*
*   importance
*       We assume that there are only 2 decision variables
*
*       Returns the importance of the given attribute on the examples 
*/
double Dtree::importance_Gen(int attribute, vector<vector<string>> examples) {
    // 1) Calculate occurances of each decision variables
    vector<double> varCount(numDecisionVars, 0);
    double totalCount = 0;
    for (int i=0; i < numDecisionVars; i++) {
        for (int j=0; j < examples.size(); j++) {
            if (examples[j][numAttributes] == decisionVars[i]) {
                varCount[i]++;
                totalCount++;
            }
        }
    }

    // 1.5) If totalCount == 0, quit
    if (totalCount == 0) {
        return 0;
    }

    // 2) Normalize to obtain probabilities
    vector<double> varProb(numDecisionVars, 0);
    for (int i=0; i < numDecisionVars; i++) {
        varProb[i] = varCount[i] / totalCount;
    }

    // 3) Calculate the importance
    double B_Val = B_Gen(varProb);
    double R_Val = Remainder_Gen(attribute, examples, varProb, totalCount);
    double importanceValue = B_Val - R_Val;

    /*
    std::cout << "  General Function" << std::endl;
    std::cout << "attribute = " << attribute << std::endl;
    std::cout << "B_Val = " << B_Val << std::endl;
    std::cout << "R_Val = " << R_Val << std::endl;
    std::cout << "importanceValue = " << importanceValue << std::endl;
    std::cout << std::endl;
    */

    return importanceValue;
}


/*
*   B_Gen
*       Returns the entropy of any R.V. with probs in vector
*/
double Dtree::B_Gen(vector<double> vals) {
    double entropy = 0;
    for (int i=0; i < vals.size(); i++) {
        if (vals[i] == 0) {
            continue;
        }
        entropy += -1 * vals[i] * log2(vals[i]);
    }

    return entropy;
}

/*
*   Remainder_Gen
*/
double Dtree::Remainder_Gen(int attr,
                            vector<vector<string>> examples,
                            vector<double> varProb,
                            double totalCount) {
    double value = 0;

    for (int k=0; k < attValues[attr].size(); k++) {
        vector<double> vals(numDecisionVars, 0);
        double total = 0;

        // 1) Count Occurences of specified Attribute for each output
        for (int j=0; j < examples.size(); j++) {
            if (examples[j][attr] == attValues[attr][k]) {
                for (int i=0; i < numDecisionVars; i++) {
                    if (examples[j][numAttributes] == decisionVars[i]) {
                        vals[i]++;
                        total++;
                    }
                }
            }
        }

        // 1.5) Check for dividing by zero
        if (total == 0) {
            continue;
        }

        // 2) Normalize
        vector<double> probs(numDecisionVars, 0);
        for (int i=0; i < numDecisionVars; i++) {
            probs[i] = vals[i] / total;
        }

        // 3) Calculate term for this k
        value += total / totalCount * B_Gen(probs);
    }

    // return the value
    return value;
}






