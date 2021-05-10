#include "graph.h"


/*
*	addVertex (checks whether or not vertex is in the map, adds it if not)
*/
void Graph::addVertex(std::string newVertexLabel) {
    std::unordered_map<std::string, int>::iterator it;
    it = vertexLabelToVertex.find(newVertexLabel);
    if (it == vertexLabelToVertex.end()) {
        vertexLabelToVertex[newVertexLabel] = vertexCounter;
        vertexToVertexLabel[vertexCounter] = newVertexLabel;
        vertexCounter++;
    }
}


/*
*   addEdge (convenience function)
*/
void Graph::addEdge(string vertex1Label, string vertex2Label, float weight) {
    int vertex1 = vertexLabelToVertex[vertex1Label];
    int vertex2 = vertexLabelToVertex[vertex2Label];
    addEdge(vertex1, vertex2, weight);
}

/*
*	addEdge
*/
void Graph::addEdge(int vertex1, int vertex2, float weight) {
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
int Graph::returnNumVertices() {
    return vertexCounter;
}

/*
*	returnNumEdgesIter		(explicitly counts each edge)
*/
int Graph::returnNumEdgesIter() {
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
int Graph::returnNumEdges() {
    return edgeCounter;
}



float Graph::calc(int vertex1, int vertex2) {
    float x1 = cos(vertexToLat[vertex1] * PI / 180.0) * cos(vertexToLon[vertex1] * PI / 180.0) * R;
    float y1 = cos(vertexToLat[vertex1] * PI / 180.0) * sin(vertexToLon[vertex1] * PI / 180.0) * R;
    float z1 = sin(vertexToLat[vertex1] * PI / 180.0) * R;  // z is 'up'

    float x2 = cos(vertexToLat[vertex2] * PI / 180.0) * cos(vertexToLon[vertex2] * PI / 180.0) * R;
    float y2 = cos(vertexToLat[vertex2] * PI / 180.0) * sin(vertexToLon[vertex2] * PI / 180.0) * R;
    float z2 = sin(vertexToLat[vertex2] * PI / 180.0) * R;  // z is 'up'

    return sqrt( (x1-x2)*(x1-x2) + (y1-y2)*(y1-y2) + (z1-z2)*(z1-z2) );
}

void Graph::addCoords(string vertexLabel, float coord1, float coord2) {
    int vertex = vertexLabelToVertex[vertexLabel];

    // Populate maps from vertices to their coords
    vertexToLat[vertex] = coord1;
    vertexToLon[vertex] = coord2;
}



