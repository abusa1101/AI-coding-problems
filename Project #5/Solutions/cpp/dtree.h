#ifndef DTREE_H_
#define DTREE_H_

// C++ includes
#include <iostream>
#include <vector>
#include <string>
#include <fstream>        // ifstream / ofstream
#include <unordered_map>  // unordered_map
#include <iomanip>        // std::setprecision

using std::string;
using std::vector;

class Node {
 public:
  // Constructors
  Node();
  explicit Node(string v) : value(v) {}

  // Destructor
  ~Node() {
    for (int i=0; i < numChildren; i++) {
        delete[] children[i];
    }
  }

  // Functions
  void addChild(Node* c, string e) {
    children.push_back(c);
    edges.push_back(e);
    numChildren++;
  }

  // Node Variables
  string value;

  // Children Variables
  int numChildren = 0;
  vector<Node*> children;
  vector<string> edges;
};

class Dtree {
 public:
  Dtree();

  // User Functions
  int readInput();
  void run();
  int writeOutput();

  // Decision Tree Learning Functions
  Node* decisionTreeLearning(vector<vector<string>> examples,
                             vector<int> attributes,
                             vector<vector<string>> parent_examples);

  // Dtree Helper Functions
  Node* pluralityValue(vector<vector<string>> examples);
  bool sameClassification(vector<vector<string>> examples);
  int maxImportance(vector<int> attributes, vector<vector<string>> examples);

  // maxImportance Helper Functions
  double importance(int attribute, vector<vector<string>> examples);
  double B(int p, int n);
  double Remainder(int attr, vector<vector<string>> examples, int p, int n);

  // maxImportance Helper Functions (Generalized)
  double importance_Gen(int attribute, vector<vector<string>> examples);
  double B_Gen(vector<double> vals);
  double Remainder_Gen(int attr,
                       vector<vector<string>> examples,
                       vector<double> varProb,
                       double totalCount);

 private:
  // Attribute Variables
  std::unordered_map<string, int> attNameToInd;  // name  -> index
  vector<string> Attributes;                     // index -> name
  vector<vector<string>> attValues;              // Attribute Values
  int numAttributes = 0;

  // Decision Variables
  vector<string> decisionVars;                  // Decision Variables
  std::unordered_map<string, int> decNameToInd;  // name -> index
  int numDecisionVars = 0;

  // Examples
  vector<vector<string>> Examples;
  int numExamples = 0;

  // File I/O
  string inFilename = "examples.txt";
  string outFilename = "dtree.txt";

  double negInf = -10000;

  // Final Decision Tree
  Node* decisionTree;
};

#endif  // DTREE_H_

