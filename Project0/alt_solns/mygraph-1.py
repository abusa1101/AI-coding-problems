#!/usr/bin/python3
import csv
from graphviz import Graph

##Read input from file
FILE = csv.reader(open('graph.txt', 'r'), skipinitialspace='True')
LIST = list(FILE)

##Graphing the network
#Make Graph Structure:
G = Graph('G', filename='roadmap.gv', engine='sfdp')

#Make a (unique) list of cities (# cities = # nodes):
UNIQUE_LIST = []
LIST_LEN = range(len(LIST))
for i in LIST_LEN:
    if LIST[i][0] not in UNIQUE_LIST:
        UNIQUE_LIST.append(LIST[i][0])
    if LIST[i][1] not in UNIQUE_LIST:
        UNIQUE_LIST.append(LIST[i][1])
    G.edge(LIST[i][0], LIST[i][1], label=LIST[i][2])
G.view()

print(len(UNIQUE_LIST)) # No. of nodes/vertices
print(len(LIST)) # No. of edges
# print(G.source) # Print Graph structure
