#!/usr/bin/python3
import functions as f
import search_algs as search

#Find costs
#gn = path len = curr loc - origin #edge cost
#hn = dist = goal based given latlon - curr loc #heuristic function
# gn =

def route_planning(origin, destination, search_method):
    #Load graph
    graph_list = f.read_file("transition_set.csv")
    graph = f.make_graph(graph_list)

    #Search
    depth_limit = 15
    if search_method == 'B': #Breadth-First
        [nodes, path, cost] = search.BFS(graph, origin, destination)
        f.output_parameters(nodes, path, cost)
    elif search_method == 'D': #Depth-First
        # print(search.DLS(graph, origin, destination, [], depth_limit, 0))
        [nodes, path, cost] = search.DFS(graph, origin, destination)
        f.output_parameters(nodes, path, cost)
    elif search_method == 'I': #Iterative Deepening
        [nodes, path, cost] = search.IDS(graph, origin, destination, depth_limit)
        f.output_parameters(nodes, path, cost)
    elif search_method == 'U': #Uniform Cost
        [nodes, path, cost] = search.UCS(graph, origin, destination)
        f.output_parameters(nodes, path, cost)
    elif search_method == 'A': #A* Search
        [nodes, path, cost] = search.Astar(graph, origin, destination)
        f.output_parameters(nodes, path, cost)
