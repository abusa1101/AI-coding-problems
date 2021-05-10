""" Graph Class and utilities """

import math


TRANSITION_SET = [["Ann Arbor", "Brighton", 19.2],
                  ["Ann Arbor", "Plymouth", 17.2],
                  ["Ann Arbor", "Romulus", 23.1],
                  ["Brighton", "Farmington Hills", 21.4],
                  ["Brighton", "Pontiac", 34.1],
                  ["Plymouth", "Romulus", 23.1],
                  ["Plymouth", "Farmington Hills", 14.0],
                  ["Plymouth", "Detroit", 27.9],
                  ["Romulus", "Detroit", 31.0],
                  ["Farmington Hills", "Royal Oak", 16.9],
                  ["Farmington Hills", "Detroit", 28.3],
                  ["Farmington Hills", "Pontiac", 15.5],
                  ["Pontiac", "Sterling Heights", 17.2],
                  ["Pontiac", "Royal Oak", 13.3],
                  ["Romeo", "Pontiac", 27.8],
                  ["Romeo", "Sterling Heights", 16.5]]

LATLON_COORDS = [["Ann Arbor", 42.280826, -83.743038],
                 ["Brighton", 42.529477, -83.780221],
                 ["Detroit", 42.331427, -83.045754],
                 ["Farmington Hills", 42.482822, -83.418382],
                 ["Plymouth", 42.37309, -83.50202],
                 ["Pontiac", 42.638922, -83.291047],
                 ["Romeo", 42.802808, -83.012987],
                 ["Romulus", 42.24115, -83.612994],
                 ["Royal Oak", 42.48948, -83.144648],
                 ["Sterling Heights", 42.580312, -83.030203]]


class Vertex:
    """ Vertex class """
    def __init__(self, name, key):
        self.index = key
        self.name = name
        self.neighbors = {}
        self.lat = 0.0
        self.lon = 0.0
        self.ecef = [0, 0, 0]

    def add_neighbor(self, neighbor, weight=0):
        """ adds a neighbor and associated edge weight """
        self.neighbors[neighbor] = weight

    def get_neighbors(self):
        """ retrieves list of neighbor vertices """
        return self.neighbors.keys()


class Graph:
    """ Graph class """
    def __init__(self):
        self.vertices = {}
        self.index_to_name = {}
        self.index_to_vertices = {}
        self.num_vertices = 0
        self.num_edges = 0
        self.load_graph()
        self.calc_distances()

    def add_vertex(self, vertex_name):
        """ adds a node to the graph """
        if vertex_name not in self.vertices:
            new_vertex = Vertex(vertex_name, self.num_vertices)
            self.vertices[vertex_name] = new_vertex
            self.index_to_name[self.num_vertices] = vertex_name
            self.index_to_vertices[self.num_vertices] = new_vertex
            self.num_vertices += 1

    def add_edge(self, vertex1_name, vertex2_name, edge_weight):
        """ adds an edge to the graph """
        if vertex1_name not in self.vertices:
            print(vertex1_name, " is not in the graph")
            return
        if vertex2_name not in self.vertices:
            print(vertex2_name, " is not in the graph")
            return
        self.vertices[vertex1_name].add_neighbor(self.vertices[vertex2_name], edge_weight)
        self.vertices[vertex2_name].add_neighbor(self.vertices[vertex1_name], edge_weight)
        self.num_edges += 1

    def load_graph(self):
        """ add vertices and edges from hardcoded values """
        for transition in TRANSITION_SET:
            self.add_vertex(transition[0])
            self.add_vertex(transition[1])
            self.add_edge(transition[0], transition[1], transition[2])
        for lat_lon in LATLON_COORDS:
            self.vertices[lat_lon[0]].lat = lat_lon[1]
            self.vertices[lat_lon[0]].lon = lat_lon[2]

    def get_distance(self, vertex1_index, vertex2_index):
        """ return distances by index pairs """
        vertex1_name = self.index_to_name[vertex1_index]
        vertex2_name = self.index_to_name[vertex2_index]
        return self.distances[vertex1_name][vertex2_name]

    def get_distance_by_name(self, vertex1_name, vertex2_name):
        """ return distances by name pairs """
        return self.distances[vertex1_name][vertex2_name]

    def calc_distances(self):
        """ 1-time calculation of pair-wise distances """
        for vertex_name in self.vertices:
            self.calc_ecef(vertex_name)

        self.distances = {}
        for vertex1_name in self.vertices:
            vertex1_dists = {}
            for vertex2_name in self.vertices:
                vertex1_dists[vertex2_name] = self.calc_distance(vertex1_name, vertex2_name)
            self.distances[vertex1_name] = vertex1_dists

    def calc_ecef(self, vertex_name):
        """ calc ECEF coordinates for dist calc later """
        R = 3959
        phi = math.radians(self.vertices[vertex_name].lat)
        theta = math.radians(self.vertices[vertex_name].lon)

        x = math.cos(phi) * math.cos(theta) * R
        y = math.cos(phi) * math.sin(theta) * R
        z = math.sin(phi) * R # z is 'up'

        self.vertices[vertex_name].ecef = [x, y, z]

    def calc_distance(self, vertex1_name, vertex2_name):
        """ 3-D distance calculation """
        [x1, y1, z1] = self.vertices[vertex1_name].ecef
        [x2, y2, z2] = self.vertices[vertex2_name].ecef
        return ((x2-x1)**2 + (y2-y1)**2 + (z2-z1)**2) ** 0.5


def test_graph():
    my_graph = Graph()

    # 1) Return the number of Vertices and Edges to the terminal
    print("# of Vertices = ", my_graph.num_vertices)
    print("# of Edges = ", my_graph.num_edges)

    # 2) Return a list of the vertices
    print("\nList of vertices: ")
    for vertex in my_graph.vertices:
        print("  ", vertex)

    # 3) Print SLD
    print("\nStraight Line Distances")
    for vertex1_name in my_graph.vertices:
        print("         ", vertex1_name,)
        for vertex2_name in my_graph.vertices:
            print(vertex2_name, ": ", my_graph.get_distance_by_name(vertex1_name, vertex2_name))
        print()

if __name__ == "__main__":
    test_graph()
