#!/usr/bin/python3

def AC3(constraints, values, peers):
    # print(values)
    queue = list(constraints) #arcs of CSP
    while queue:
        (Xi, Xj) = queue.pop(0)
        # print(values)
        if revise(values, peers, Xi, Xj):
            if len(values[Xi]) == 0: #values = domains
            	return False
            for Xk in (peers[Xi] - set(Xj)): #peers = neighbors
            	queue.append([Xk, Xi])
    return True

def revise(values, peers, Xi, Xj):
    revised = False
    values_cpy = set(values[Xi])
    for x in values_cpy:
        if not arc_consistent(values, peers, x, Xi, Xj):
            values[Xi] = values[Xi].replace(x, '') #can change this
            revised = True
    return revised

def arc_consistent(values, peers, x, Xi, Xj):
    values_cpy = values[Xj]
    for y in values_cpy:
        if x != y and Xj in peers[Xi]:
            return True
    return False
