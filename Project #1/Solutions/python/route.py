""" Route Problem Domain Module """

import csv
import graph



class RouteState:
    """ State used for Route Problem """
    def __init__(self, vertex_index=-1):
        """ add stuff here """
        self.vertex_index = vertex_index

    def get_hash(self):
        """ Grab a unique integer from the state for efficient set() operations """
        return self.vertex_index


class Route:
    """ Route Domain Class """
    def __init__(self):
        self.start_state = RouteState()
        self.goal_state = RouteState()
        self.method = 'B'

        self.my_graph = graph.Graph()
        self.read_problem_file()

    def print_state(self, state):
        """ Print state to terminal """
        print(self.my_graph.index_to_name[state.vertex_index])

    def goal_test(self, state):
        """ Test if given state is at the goal """
        return state.vertex_index == self.goal_state.vertex_index

    def heuristic(self, state):
        """ Heurisitc used for A* """
        return self.my_graph.get_distance(state.vertex_index, self.goal_state.vertex_index)

    def get_actions(self, state):
        """ Get Actions for General Search Code """
        actions = []

        for neighbor, cost in self.my_graph.index_to_vertices[state.vertex_index].neighbors.items():
            nbr_state = RouteState(neighbor.index)
            action = [nbr_state, cost]
            actions.append(action)

        return actions

    def read_problem_file(self, fname="route.txt"):
        """ Grab problem details to search """
        with open(fname, 'r') as infile:
            csvreader = csv.reader(infile)
            lines = []

            for line in csvreader:
                lines.append(line)

            start_city = lines[0][0]
            goal_city = lines[1][0]
            method = lines[2][0]

            print("\nStart City = ", start_city)
            print("Goal City = ", goal_city)
            print("Method = ", method, "\n")

            self.start_state = RouteState(self.my_graph.vertices[start_city].index)
            self.goal_state = RouteState(self.my_graph.vertices[goal_city].index)
            self.method = method
