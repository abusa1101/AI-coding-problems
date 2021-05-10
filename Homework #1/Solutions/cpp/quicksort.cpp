/*
 Matthew Romano
 EECS 592
 Problem #2 - quicksort.cpp
*/

#include <iostream>
#include <fstream>      // file input/output
#include <string>       // string
#include <vector>       // vector


// Class Declarations
class entry {
 public:
  entry(void) {}
  entry(std::string lN, std::string fN, int g) : lastName(lN),
                                                 firstName(fN),
                                                 grade(g) {}

  std::string lastName;
  std::string firstName;
  int grade;
};

// Function Declarations
void quicksort(std::vector<entry>* entries, int lo, int hi);
int partition(std::vector<entry>* entries, int lo, int hi);

int main() {
    // File Operation Variables
    std::ifstream inFile("unsorted.txt");
    std::ofstream outFile("sorted.txt");
    std::string line, last, first, grade;
    char delim = 44;  // comma
    size_t p, q;

    // Entries to be sorted by quicksort() function
    std::vector<entry> entries;

    // 1) Read in the data
    if (inFile.is_open()) {
        while (getline(inFile, line)) {
            p = line.find_first_of(delim);
            q = line.find_last_of(delim);

            last = line.substr(0, p);
            first = line.substr(p+2, q-(p+2));
            grade = line.substr(q+2);

            entry anEntry(last, first, stoi(grade));
            entries.push_back(anEntry);
        }
        inFile.close();
    } else {
        std::cout << "Unable to open file";
    }

    // 2) Sort the data
    quicksort(&entries, 0, entries.size()-1);

    // 3) Write the sorted data to the output file
    for (std::vector<entry>::iterator it = entries.begin();
                                      it != entries.end(); ++it) {
        outFile << (*it).lastName  << ", " <<
                   (*it).firstName << ", " <<
                   (*it).grade     << std::endl;
                       }
    outFile.close();

    return 0;
}



void quicksort(std::vector<entry>* entries, int lo, int hi) {
    if (lo < hi) {
        int p = partition(entries, lo, hi);
        quicksort(entries, lo, p-1);
        quicksort(entries, p+1, hi);
    }
}

int partition(std::vector<entry>* entries, int lo, int hi) {
    entry temp;

    int pivot = (*entries)[hi].grade;
    int i = lo -1;

    for (int j = lo; j < hi; j++) {
        if ((*entries)[j].grade < pivot) {
            i++;
            temp = (*entries)[i];
            (*entries)[i] = (*entries)[j];
            (*entries)[j] = temp;
        }
    }
    if ((*entries)[hi].grade < (*entries)[i+1].grade) {
        temp = (*entries)[i+1];
        (*entries)[i+1] = (*entries)[hi];
        (*entries)[hi] = temp;
    }

    return i+1;
}























