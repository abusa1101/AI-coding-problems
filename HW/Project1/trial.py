import functions
import numpy as np


# D= {} #initializes the empty dictionary
# D['A'] = {} #Creates a key 'A' in the dictionaries and assigns the key to a value of another empty hash
# (D['A'])['B'] = 1 #Creates a Sub-Hash for key 'A' of the hash,Sub-hash is {'B':1}
# D['C'] = {}
# (D['C'])['D'] = 2
# (D['C'])['E'] = [3, 4]
# print(D)
# print(D['C'])
# print((D['C'])['E'])
# print((D['C'])['E'][1])
# #
# LIST = functions.read_file('trial_data.csv')
# graph = {}
# for i in range(len(UNIQUE_LIST)):
#     graph[LIST[i][0]] = {}
# for i in range(len(LIST)):
#     graph[LIST[i][0]] = {}
# for i in range(len(LIST)):
#     graph[LIST[i][0]] = {}
#     graph[LIST[i][1]] = {}
#     (graph[LIST[i][0]])[LIST[i][1]] = [LIST[i][2]]
#     (graph[LIST[i][0]])[LIST[i][1]] = [LIST[i][2]]
#
# f = open("graph.txt","w")
# f.write(str(graph))
# f.close()
# print(graph['Ann Arbor'])
#
# for child in graph['Ann Arbor']:
#     print(child)
#
# print(graph)
# UNSORTED_LIST = functions.read_file('trial_data.csv')
# SORTED_LIST = functions.quicksort(UNSORTED_LIST, 0, len(UNSORTED_LIST) - 1)
# functions.write_file("trial_data_sorted.csv", SORTED_LIST)
# graph_list = functions.read_file("trial_data.csv")
# graph = functions.make_graph(graph_list)
# print(graph['Ann Arbor'][0][0])

list = functions.read_file("latlon_coords.csv")

origin = 'Ann Arbor'
destination = 'Detroit'

city = list[0][0]
lat = float(list[0][1])
lon = float(list[0][2])

for i in range(len(list)):
    if list[i][0] == origin:
        lat_1 = float(list[i][1])
        lon_1 = float(list[i][2])
    if list[i][0] == destination:
        lat_2 = float(list[i][1])
        lon_2 = float(list[i][2])
print(lat_1)
print(lat_2)
print(lon_1)
print(lon_2)
# if not lat_1 or not lat_2 or not lon_1 or not lon_2:
#     return None

R = 3959            #miles
x_1 = np.cos(lat_1) * np.cos(lon_1) * R
y_1 = np.cos(lat_1) * np.sin(lon_1) * R
# z_1 = np.sin(lat_1) * R #z is 'up'
x_2 = np.cos(lat_2) * np.cos(lon_2) * R
y_2 = np.cos(lat_2) * np.sin(lon_2) * R

dist = ((x_2 - x_1)**2 + (y_2 - y_1)**2)**(0.5)
print(dist)
