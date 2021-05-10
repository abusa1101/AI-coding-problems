""" Traveling Salesman Problem Domain Module """

import csv
import graph


class TSPState:
    """ State used for TSP """
    def __init__(self, vertex_index=-1, visited_indices=0):
        """ add stuff here """
        self.vertex_index = vertex_index
        self.visited_indices = visited_indices

    def get_hash(self):
        """ Grab a unique integer from the state for efficient set() operations """
        return (self.visited_indices << 8) | (0xFF & self.vertex_index)


class TSP:
    """ TSP Domain Class """
    def __init__(self):
        self.start_state = TSPState()
        self.goal_visits = 0
        self.method = 'B'

        self.my_graph = graph.Graph()
        self.read_problem_file()

    def print_state(self, state):
        """ Print state to terminal """
        print(self.my_graph.index_to_name[state.vertex_index])

    def goal_test(self, state):
        """ Test if goal has been reached (visiting every city) """
        return state.visited_indices == self.goal_visits

    def heuristic(self, state):
        """ Heurisitc used for A* """
        return self.heuristic_fn(state)

    def heuristic_fn(self, state):
        """ Furthest Unexplored Neighbor Heurisitc """
        max_dist = 0.0
        for i in range(0, self.my_graph.num_vertices):
            if state.visited_indices & (1 << i) == 0:
                next_dist = self.my_graph.get_distance(state.vertex_index, i)
                if next_dist > max_dist:
                    max_dist = next_dist
        return max_dist


    def get_actions(self, state):
        """ Get Actions for General Search Code """
        actions = []

        for neighbor, cost in self.my_graph.index_to_vertices[state.vertex_index].neighbors.items():
            nbr_state = TSPState(neighbor.index, state.visited_indices | (1 << neighbor.index))
            action = [nbr_state, cost]
            actions.append(action)

        return actions

    def read_problem_file(self, fname="tsp.txt"):
        """ Grab problem details to search """
        with open(fname, 'r') as infile:
            csvreader = csv.reader(infile)
            lines = []

            for line in csvreader:
                lines.append(line)

            start_city = lines[0][0]
            method = lines[1][0]

            print("\nStart City = ", start_city)
            print("Method = ", method, "\n")

            start_index = self.my_graph.vertices[start_city].index
            self.start_state = TSPState(start_index, (1 << start_index))
            self.method = method

            for i in range(0, self.my_graph.num_vertices):
                self.goal_visits = self.goal_visits | (1 << i)
