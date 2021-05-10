#include "route.h"


/*
    Domain() 
    
        Domain constructor
*/
Domain::Domain() {
    // Read in the Graph File
    if (readGraphFile()) {
        cout << "Error Reading in Graph" << endl;
    }

    // Read in the Coord File
    if (readCoordFile()) {
        cout << "Error Reading in Coordinates" << endl;
    }

    // Read in the Problem File
    if (readProbFile()) {
        cout << "Error Reading in Problem File" << endl;
    }

    // Print the loaded problem to the terminal
    cout << endl << "Search Problem:" << endl;
    cout << "   Starting at " <<  myGraph.vertexToVertexLabel[start] << endl;
    cout << "   Going to " << myGraph.vertexToVertexLabel[goal] << endl;
    cout << "   Using search method: " << method << endl << endl;
}

std::vector<Action> Domain::getActions(State state) {
    EdgeMap* edges = myGraph.getEdgeMap(state.vertex_index);

    std::vector<Action> actions;

    for (auto it = edges->begin(); it != edges->end(); ++it) {
        Action action;

        action.state.vertex_index = it->first;
        action.cost = (it->second).weight;

        actions.push_back(action);
    }

    return actions;
}

float Domain::heuristic(State state) {
    return myGraph.calc(state.vertex_index, goalState.vertex_index);
}

bool Domain::goalTest(State state) {
    return state.vertex_index == goalState.vertex_index;
}

void Domain::printState(State state) {
    string stateLabel = myGraph.vertexToVertexLabel[state.vertex_index];
    cout << "   " << stateLabel << endl;
}

int Domain::readGraphFile() {
    // File Operation Variables
    string transFilename = "data/southernMichigan_Trans.txt";
    std::ifstream inFile(transFilename);
    string line, vertex1, vertex2, weight;
    char delim = 44;    // comma
    size_t p, q;

    // 1) Read in the data
    if (inFile.is_open()) {
        while (getline(inFile, line)) {
            p = line.find_first_of(delim);
            q = line.find_last_of(delim);

            vertex1 = line.substr(0, p);
            vertex2 = line.substr(p+2, q-(p+2));
            weight = line.substr(q+2);

            // Add Vertices and Edges to Graph
            myGraph.addVertex(vertex1);
            myGraph.addVertex(vertex2);
            myGraph.addEdge(vertex1, vertex2, stof(weight));
            myGraph.addEdge(vertex2, vertex1, stof(weight));
        }
        inFile.close();
        return 0;
    } else {
        std::cout << "Unable to open " << transFilename << endl;
        return 1;
    }

    return 0;
}


int Domain::readCoordFile() {
    // File Operation Variables
    string coordFilename = "data/southernMichigan_Coords.txt";
    std::ifstream inFile(coordFilename);
    string line, name, coord1, coord2;
    char delim = 44;    // comma
    size_t p, q;

    // 1) Read in the data
    if (inFile.is_open()) {
        while (getline(inFile, line)) {
            p = line.find_first_of(delim);
            q = line.find_last_of(delim);

            name = line.substr(0, p);
            coord1 = line.substr(p+2, q-(p+2));
            coord2 = line.substr(q+2);

            // Add Coords to Search
            myGraph.addCoords(name, stof(coord1), stof(coord2));
        }
        inFile.close();
        return 0;
    } else {
        std::cout << "Unable to open " << coordFilename << endl;
        return 1;
    }
}

int Domain::readProbFile() {
    string probFilename = "route.txt";

    // File Operation Variables
    std::ifstream inFile(probFilename);
    string line;

    // 1) Read in the data
    if (inFile.is_open()) {
        if (getline(inFile, line)) {
            start = myGraph.vertexLabelToVertex[line];
            startState.vertex_index = start;
        }

        if (getline(inFile, line)) {
            goal = myGraph.vertexLabelToVertex[line];
            goalState.vertex_index = goal;
        }

        if (getline(inFile, line)) {
            method = line[0];
        }

        inFile.close();
        return 0;
    } else {
        std::cout << "Unable to open " << probFilename << endl;
        return 1;
    }
}
