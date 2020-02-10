#!/usr/bin/python3
from collections import defaultdict
import csv
import numpy as np

def swap_line(arr, pos1, pos2): #swap arr_1 with arr_2
    temp_line = arr[pos1]
    arr[pos1] = arr[pos2]
    arr[pos2] = temp_line

def partition(arr, low_val, high_val):
    pivot = float(arr[high_val][2])
    i = low_val
    for j in range(low_val, high_val):
        if float(arr[j][2]) <= pivot:
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

def read_file(file_name):
    FILE = csv.reader(open(file_name, 'r'), skipinitialspace='True')
    LIST = sorted(list(FILE))
    return LIST

def write_file(file_name, sorted_list):
    with open(file_name, 'w') as sorted_f:
        FILE = csv.writer(sorted_f, delimiter=',')
        FILE.writerows(sorted_list)

def get_dist(file_name, origin, destination):
    list = read_file(file_name)
    for i in range(len(list)):
        if list[i][0] == origin:
            lat_1 = float(list[i][1])
            lon_1 = float(list[i][2])
        if list[i][0] == destination:
            lat_2 = float(list[i][1])
            lon_2 = float(list[i][2])
    if not lat_1 or not lat_2 or not lon_1 or not lon_2:
        return 0

    R = 3959 #miles
    x_1 = np.cos(lat_1) * np.cos(lon_1) * R
    y_1 = np.cos(lat_1) * np.sin(lon_1) * R
    x_2 = np.cos(lat_2) * np.cos(lon_2) * R
    y_2 = np.cos(lat_2) * np.sin(lon_2) * R
    dist = ((x_2 - x_1)**2 + (y_2 - y_1)**2)**(0.5)
    return dist

def make_graph(graph_list):
    graph = defaultdict(list)
    h_dist_1 = 0.0
    h_dist_1 = 0.0
    for i in graph_list:
        dist_1 = get_dist("latlon_coords.csv", i[0], i[1])
        dist_2 = get_dist("latlon_coords.csv", i[1], i[0])
        if dist_1 != 0:
            h_dist_1 = dist_1
        if dist_2 != 0:
            h_dist_2 = dist_2
        graph[i[0]].append((i[1], float(i[2]), h_dist_1))
        graph[i[1]].append((i[0], float(i[2]), h_dist_2))
    print(graph)
    return graph

def check_conditions(graph, start_node, goal_node):
    is_good = True
    if start_node not in graph:
        is_good = False
        print('start node not in graph')
    if goal_node not in graph:
        is_good = False
        print('goal node not in graph')
    return is_good

def output_parameters(total_nodes, total_path, total_cost):
    print("(1) Total number of nodes expanded: " + str(total_nodes))
    print("(2) Solution path as follows (start -> end):")
    print(total_path)
    print("(3) Total solution cost g(n): " + str(total_cost))
