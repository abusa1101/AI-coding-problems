#!/usr/bin/python3
import sys
import route_plan as rp

if not sys.argv[1]:
    sys.stderr.write("Error: expected domain arguments\n")
    exit()

domain = str(sys.argv[1])

#Implement search on domain
if domain == "route.txt": #Breadth First
    [origin, destination, search] = open("route.txt", "r").read().splitlines()
    rp.route_planning(origin, destination, search)
if domain == "tsp.txt": #Depth First
    [city, search] = open("route.txt", "r").read().splitlines()
