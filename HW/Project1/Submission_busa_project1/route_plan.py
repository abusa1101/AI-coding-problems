#!/usr/bin/python3
import functions as f
import search_algs as search


def route_planning(origin, destination, search_method):
    #Load graph
    graph_list = f.read_file("transition_set.csv")
    graph = f.make_graph(graph_list)

    if f.check_conditions(graph, origin, destination) is True:
        #Search
        depth_limit = 15
        if search_method == 'B': #Breadth-First
            [nodes, path, cost] = search.bf_search(graph, origin, destination)
            f.output_parameters(nodes, path, cost)
        elif search_method == 'D': #Depth-First
            # print(search.dl_search(graph, origin, destination, [], depth_limit, 0))
            [nodes, path, cost] = search.df_search(graph, origin, destination)
            f.output_parameters(nodes, path, cost)
        elif search_method == 'I': #Iterative Deepening
            [nodes, path, cost] = search.id_search(graph, origin, destination, depth_limit)
            f.output_parameters(nodes, path, cost)
        elif search_method == 'U': #Uniform Cost
            [nodes, path, cost] = search.uc_search(graph, origin, destination)
            f.output_parameters(nodes, path, cost)
        elif search_method == 'A': #A* Search
            [nodes, path, cost] = search.a_star(graph, origin, destination)
            f.output_parameters(nodes, path, cost)
        else:
            print('Error: origin or destination city not in given list')
