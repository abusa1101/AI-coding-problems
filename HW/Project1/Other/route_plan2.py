#!/usr/bin/python3
import csv
from graphviz import Graph
import functions
# import search_algs as search


##Read unsorted input, sort and make graph for sorted input
UNSORTED_LIST = functions.read_file("transition_set.csv")
SORTED_LIST = functions.quicksort(UNSORTED_LIST, 0, len(UNSORTED_LIST) - 1)
functions.write_file("transition_set_sorted.csv", SORTED_LIST)
LIST = functions.read_file("transition_set_sorted.csv")

G = Graph('G', filename='michigan_map.gv', engine='sfdp')
UNIQUE_LIST = []
LIST_LEN = range(len(LIST))
for i in LIST_LEN:
    if LIST[i][0] not in UNIQUE_LIST:
        UNIQUE_LIST.append(LIST[i][0])
    if LIST[i][1] not in UNIQUE_LIST:
        UNIQUE_LIST.append(LIST[i][1])
    G.edge(LIST[i][0], LIST[i][1], label=LIST[i][2])
# G.view()

print(len(UNIQUE_LIST)) # No. of nodes/vertices
print(len(LIST)) # No. of edges
