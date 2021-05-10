#ifndef GRAPH_H
#define GRAPH_H

#include <math.h>       // sin, cos
#include <string>       // string
#include <vector>       // vector
#include <unordered_map>  // unordered_map


#define PI 3.14159265
using std::string;


// Edge Class
class Edge {
 public:
  Edge() : source(-1), dest(-1), weight(-1) {}
  Edge(int s, int d, float w) : source(s), dest(d), weight(w) {}

  int source;
  int dest;
  float weight;
};

typedef std::unordered_map<int, Edge> EdgeMap;


class Graph {
 public:
  Graph() {}

  void addVertex(std::string newVertexLabel);

  void addEdge(int vertex1, int vertex2, float weight);

  void addEdge(string vertex1Label, string vertex2Label, float weight);

  int returnNumVertices();

  int returnNumEdges();

  int returnNumEdgesIter();

  EdgeMap* getEdgeMap(int vertex) {
      return &(vertexToEdgeMap[vertex]);
  }


  // Graph Variables
  std::unordered_map<int, EdgeMap> vertexToEdgeMap;
  std::unordered_map<std::string, int> vertexLabelToVertex;
  std::unordered_map<int, std::string> vertexToVertexLabel;
  int vertexCounter = 0;
  int edgeCounter = 0;

  // Distance Stuff
  float calc(int vertex1, int vertex2);
  void addCoords(string vertexLabel, float coord1, float coord2);
  std::unordered_map<int, float> vertexToLat;
  std::unordered_map<int, float> vertexToLon;
  float R = 3959.0;  // radius of earth
};

#endif  // GRAPH_H
