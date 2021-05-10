
""" mygraph.py - Problem #1

    Matthew Romano
    eecs592
"""

import csv


class Node:
    """ Node class """
    def __init__(self, name, key):
        self.index = key
        self.name = name
        self.neighbors = {}

    def add_neighbor(self, neighbor, weight=0):
        """ adds a neighbor and associated edge weight """
        self.neighbors[neighbor] = weight

    def get_neighbors(self):
        """ retrieves list of neighbor nodes """
        return self.neighbors.keys()


class Graph:
    """ Graph class """
    def __init__(self):
        self.nodes = {}
        self.num_nodes = 0
        self.num_edges = 0

    def add_node(self, node_name):
        """ adds a node to the graph """
        if node_name not in self.nodes:
            new_node = Node(node_name, self.num_nodes)
            self.nodes[node_name] = new_node
            self.num_nodes += 1

    def add_edge(self, node1_name, node2_name, edge_weight):
        """ adds an edge to the graph """
        if node1_name not in self.nodes:
            print(node1_name, " is not in the graph")
            return
        if node2_name not in self.nodes:
            print(node2_name, " is not in the graph")
            return
        self.nodes[node1_name].add_neighbor(self.nodes[node2_name], edge_weight)
        self.nodes[node2_name].add_neighbor(self.nodes[node1_name], edge_weight)
        self.num_edges += 1


def main():
    """ main function """
    # 1) Instantiate a Graph
    my_graph = Graph()

    # 2) Read in the data to populate the graph
    with open('graph.txt', 'r') as infile:
        csvreader = csv.reader(infile)
        for line in csvreader:
            node1_name = line[0]
            node2_name = line[1][1:]
            edge_weight = float(line[2][1:])

            my_graph.add_node(node1_name)
            my_graph.add_node(node2_name)
            my_graph.add_edge(node1_name, node2_name, edge_weight)

    # 3) Return the number of Vertices and Edges to the terminal
    print("# of Nodes = ", my_graph.num_nodes)
    print("# of Edges = ", my_graph.num_edges)


if __name__ == "__main__":
    main()
