#!/usr/bin/python3
import csv
from graphviz import Graph

##Functions
def swap_line(arr, pos1, pos2): #swap arr_1 with arr_2
    temp_line = arr[pos1]
    arr[pos1] = arr[pos2]
    arr[pos2] = temp_line

def partition(arr, low_val, high_val):
    pivot = int(arr[high_val][2])
    i = low_val
    for j in range(low_val, high_val):
        if int(arr[j][2]) <= pivot:
            swap_line(arr, i, j) #i with j
            i += 1
    swap_line(arr, i, high_val)
    return i

def quicksort(arr, low_val, high_val):
    if low_val < high_val:
        part_val = partition(arr, low_val, high_val)
        quicksort(arr, low_val, part_val - 1)
        quicksort(arr, part_val + 1, high_val)
    return arr

##Read input from file
UNSORTED_FILE = csv.reader(open("paris_data.csv", "r"))
UNSORTED_LIST = list(UNSORTED_FILE)

##Sort entire input list using Quicksort (lomuto Partition Scheme)
SORTED_LIST = quicksort(UNSORTED_LIST, 0, len(UNSORTED_LIST) - 1)

with open('paris_sorted.csv', 'w') as sorted_f:
    FILE = csv.writer(sorted_f, delimiter=',')
    FILE.writerows(SORTED_LIST)

##Read input from file
FILE = csv.reader(open('paris_sorted.csv', 'r'), skipinitialspace='True')
LIST = list(FILE)

G = Graph('G', filename='paris_map.gv')

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
