""" General Search Code Module """

import sys
from queue import Queue, Stack, PriorityQueue
import route
import tsp

DEPTH_LIMIT = 15

class Solution:
    """ Node used by search class """
    def __init__(self, nodes_expanded=0, goal_node=None):
        self.num_nodes_expanded = nodes_expanded
        self.sol_path = []
        self.sol_cost = 0.0

        if goal_node is not None:
            self.traceback_solution(goal_node)

    def traceback_solution(self, goal_node):
        """ Retrace solution through parents """
        self.sol_cost = goal_node.g
        curr_node = goal_node

        while curr_node.parent is not None:
            self.sol_path.append(curr_node.state)
            curr_node = curr_node.parent
        self.sol_path.append(curr_node.state)

        self.sol_path.reverse()

    def is_success(self):
        """ Return True if solution found """
        return len(self.sol_path) > 0



class Node:
    """ Node used by search class """
    def __init__(self, state=None, parent=None, f=0, g=0):
        self.state = state
        self.parent = parent
        if parent is None:
            self.depth = 0
        else:
            self.depth = parent.depth + 1
        self.f = f
        self.g = g

    def __lt__(self, other): # overload < operator
        return self.f < other.f


class Search:
    """ General Search Class """
    def __init__(self, my_domain):
        self.my_domain = my_domain

    def run_search(self):
        """ General Search function that selects method for workhorse """
        method = self.my_domain.method

        if method == 'B':
            solution = self.bfs()
        elif method == 'D':
            solution = self.dfs()
        elif method == 'I':
            solution = self.iter_deep()
        elif method == 'U':
            solution = self.uni_cost()
        elif method == 'A':
            solution = self.a_star()
        else:
            print("Could not parse search method correctly!")
            return

        if solution.is_success():
            print("Found a solution!")
            print("Total # of nodes expanded = ", solution.num_nodes_expanded, "\n")
            for state in solution.sol_path:
                self.my_domain.print_state(state)
            print("\nSolution Cost = ", solution.sol_cost, "\n")
        else:
            print("Failure!")
            print("Total # of nodes expanded = ", solution.num_nodes_expanded)


    def bfs(self):
        """ Breadth-First Search """
        return self.search(Queue())

    def dfs(self):
        """ Depth-First Search """
        return self.search(Stack())

    def iter_deep(self):
        """ Iterative Deepening Search """
        for depth in range(1, DEPTH_LIMIT):
            solution = self.search(Stack(), False, depth)
            if solution.is_success():
                return solution
        return Solution()

    def uni_cost(self):
        """ Uniform Cost Search """
        return self.search(PriorityQueue())

    def a_star(self):
        """ A* Search """
        return self.search(PriorityQueue(), True)

    def search(self, open_list, use_heuristic=False, depth_limit=DEPTH_LIMIT):
        """ Workhorse function that performs the search """
        # Init open list with start state
        new_node = Node(self.my_domain.start_state)
        open_list.push(new_node)
        num_nodes_expanded = 0

        # Init closed list
        closed_list = set()

        while 1:
            # 1) Return failure if open list is empty
            if open_list.is_empty():
                return Solution()

            # 2) Otherwise grab next node from open list
            node = open_list.pop()
            num_nodes_expanded += 1

            # 3) Run goal test
            if self.my_domain.goal_test(node.state):
                return Solution(num_nodes_expanded, node)

            # 4) Expand the node (if not in closed list)
            hash_val = node.state.get_hash()
            if (hash_val not in closed_list) and (node.depth < depth_limit):
                closed_list.add(hash_val)
                for action in self.my_domain.get_actions(node.state):
                    g = node.g + action[1]
                    f = g
                    if use_heuristic:
                        f += self.my_domain.heuristic(node.state)
                    child_node = Node(action[0], node, f, g)
                    open_list.push(child_node)


def main(domain_type=2):
    """ main function to call search code """

    # 1) Instantiate Specific Domain
    if domain_type == 2:
        my_domain = route.Route()
    else:
        my_domain = tsp.TSP()

    # 2) Instantiate the General Search Class
    my_search = Search(my_domain)

    # 3) Search
    my_search.run_search()





def cli_help():
    """ Command Line Interface Help Function """
    print("-- Incorrect Command Line Input --")
    print()
    print("Please call mysearch.py as follows: python mysearch.py <Domain> ")
    print("<Domain> = 2 (Route Planning),")
    print("           3 (Travelling Salesman)")
    print()
    print("Example - Running the Route Planning Domain: python mysearch.py 2")

if __name__ == "__main__":
    if len(sys.argv) is not 2:
        cli_help()
    elif sys.argv[1] == "2":
        print("\nRoute Planning Domain Selected!")
        main(2)
    elif sys.argv[1] == "3":
        print("\nTravelling Salesman Problem Domain Selected!")
        main(3)
    else:
        cli_help()
