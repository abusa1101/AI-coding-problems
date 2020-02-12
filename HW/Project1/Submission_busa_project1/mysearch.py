#!/usr/bin/python3
import sys
import route_plan as rp

if not sys.argv[1]:
    sys.stderr.write("Error: expected DOMAIN arguments\n")
    sys.exit()

DOMAIN = str(sys.argv[1])

#Implement SEARCH on DOMAIN
if DOMAIN == "route.txt": #Breadth First
    [ORIGIN, DESTINATION, SEARCH] = open("route.txt", "r").read().splitlines()
    rp.route_planning(ORIGIN, DESTINATION, SEARCH)
if DOMAIN == "tsp.txt": #Depth First
    [CITY, SEARCH] = open("route.txt", "r").read().splitlines()
