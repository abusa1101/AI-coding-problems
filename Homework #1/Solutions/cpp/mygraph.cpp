/*
 Matthew Romano
 EECS 592
 Problem #3 - mygraph.cpp
*/

#include <iostream>
#include <fstream>        // file input/output
#include <string>         // string
#include <vector>         // vector
#include <unordered_map>  // unordered_map

// Function Declarations
void addVertex(std::string newVertexLabel);
void addEdge(int vertex1, int vertex2, int weight);
int returnNumVertices();
int returnNumEdges();
int returnNumEdgesIter();

// Edge Class
class Edge {
 public:
  Edge() : source(-1), dest(-1), weight(-1) {}
  Edge(int s, int d, int w) : source(s), dest(d), weight(w) {}

  int source;
  int dest;
  int weight;
};


// Graph Variables
typedef std::unordered_map<int, Edge> EdgeMap;  // Need multiple instances
std::unordered_map<int, EdgeMap> vertexToEdgeMap;
std::unordered_map<std::string, int> vertexLabelToVertex;
int vertexCounter = 0;
int edgeCounter = 0;



int main() {
    // File Operation Variables
    std::ifstream inFile("graph.txt");
    std::string line, vertex1, vertex2, weight;
    char delim = 44;  // comma
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
            addVertex(vertex1);
            addVertex(vertex2);
            addEdge(vertexLabelToVertex[vertex1], vertexLabelToVertex[vertex2],
                                                                 stoi(weight));
        }
        inFile.close();
    } else {
        std::cout << "Unable to open file";
    }

    // 2) Report # of vertices and edges
    std::cout << "# of Vertices = " << returnNumVertices() << std::endl;
    std::cout << "# of Edges = " << returnNumEdges() << std::endl;


    return 0;
}


/*
*	addVertex (checks whether or not vertex is in the map, adds it if not)
*/
void addVertex(std::string newVertexLabel) {
    std::unordered_map<std::string, int>::iterator it;
    it = vertexLabelToVertex.find(newVertexLabel);
    if (it == vertexLabelToVertex.end()) {
        vertexLabelToVertex[newVertexLabel] = vertexCounter;
        vertexCounter++;
    }
}

/*
*	addEdge
*/
void addEdge(int vertex1, int vertex2, int weight) {
    std::unordered_map<int, EdgeMap>::iterator it;
    it = vertexToEdgeMap.find(vertex1);
    if (it == vertexToEdgeMap.end()) {
        vertexToEdgeMap[vertex1] = EdgeMap();
    }

    vertexToEdgeMap[vertex1][vertex2] = Edge(vertex1, vertex2, weight);
    edgeCounter++;
}

/*
*	returnNumVertices
*/
int returnNumVertices() {
    return vertexCounter;
}

/*
*	returnNumEdgesIter		(explicitly counts each edge)
*/
int returnNumEdgesIter() {
    int numEdges = 0;
    // Iterate over the vertexToEdgeMap incrementing # of edges in each map
    for (auto it = vertexToEdgeMap.begin(); it != vertexToEdgeMap.end(); ++it) {
        numEdges += (it->second).size();
    }

    return numEdges;
}

/*
*	returnNumEdges  		(based only on the counter)
*/
int returnNumEdges() {
    return edgeCounter;
}





















