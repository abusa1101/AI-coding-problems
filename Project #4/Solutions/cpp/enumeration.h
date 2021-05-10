#ifndef ENUMERATION_H_
#define ENUMERATION_H_

// C++ includes
#include <iostream>
#include <vector>
#include <string>
#include <fstream>        // ifstream / ofstream
#include <unordered_map>  // unordered_map
#include <iomanip>        // std::setprecision



class Enumeration {
 public:
  Enumeration();

  // User Functions
  int read();
  void inference();
  void print();

  // Enumeration Functions
  std::vector<double> enumAsk(int X, std::vector<int> e);
  double enumAll(std::vector<int> vars, std::vector<int> e);

  // Helper Functions
  void setProb(int var, std::vector<int> e, double val);
  double getProb(int var, int value, std::vector<int> e);
  std::vector<int> Rest(std::vector<int> vars);
  std::vector<double> normalize(std::vector<double> Q_x);
  std::vector<int> getParents(int Y, std::vector<int> e);

  // Utility Functions
  int readBN();
  int readInput();


 private:
  std::string bnFilename = "bn.txt";
  std::string inFilename = "input.txt";

  int numVars = 0;
  int maxNumVars = 27;
  std::vector<char> bnVars;                   // Variables in the BN Ind->Name
  std::unordered_map<char, int> varNameToNum;  // 'A' => 0, ..       Name->Ind
  std::vector<std::vector<int>> Parents;      // Each has Yes/No Vectors

  int queryVar;
  std::vector<int> queryEvidence;

  std::unordered_map<int, double> probMap;     // (evidence & variable)->prob

  double queryProb = 0.42;
};

#endif  // ENUMERATION_H_

