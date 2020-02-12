EECS 592: FOUNDATIONS OF AI- PROJECT 1

PART 2: To change testing parameters, you can simply change the values in the .txt files (route.txt, tsp.txt),
        and run mysearch.py with command line input of 'route.txt' or 'tsp.txt' respectively.

        This program consists of the following files:
            (1) mysearch.py (main program with domain-dependent functionality)
            (2) route_plan.py (Problem 2)
            (3) search_algs.py (Problem 1)
            (4) functions.py (modularized functions)
            (5) tsp.py (Problem 3)

            (6) route.txt (Problem 2 input file)
            (7) tsp.txt (Problem 3 input file)
            (8) transition_set.csv (City data)
            (9) latlon_coords.csv (Lat/Long data)

        -> To run either of the domains, please give the .txt file name as a command line input argument.
        -> That is, for route planning, you can run 'python3 mysearch.py route.txt', and for tsp.txt, you can run 'python3 mysearch.py tsp.txt'.
        -> NOTE: To change testing parameters, you can simply change the values in the .txt files (route.txt, tsp.txt)!

        Overall structure overview:
        1. mysearch.py calls route_plan.py and tsp.py
        2. route_plan.py and tsp.py call search_algs.py and functions.py respectively
        3. search_algs.py contains all the general search algorithms (Problem 1)
        4. route_plan calls the search algorithms for


PART 1: (For your reference)
        Problem 3
            (8) Train routes data taken from the map of France
            (9) Python graph of France
            (10) Manually evaluated search trees (BFS, DFS, UCS, A*)

        Problem 2
            (11) Scan of hand-writtens hw

        Problem 1
            (12) Scan of hand-written hw
