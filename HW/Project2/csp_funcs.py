#!/usr/bin/python3
# import copy

def AC3(constraints, domain, neighbors):
    # print(domain)
    queue = list(constraints) #arcs of CSP
    while queue:
        xi, xj = queue.pop(0)
        # print(domain)
        if revise(domain, neighbors, xi, xj):
            if len(domain[xi]) == 0:
            	return False
            for Xk in (neighbors[xi] - set(xj)):
            	queue.append([Xk, xi])
    return True

def revise(domain, neighbors, xi, xj):
    revised = False
    domain_cpy = set(domain[xi])
    for x in domain_cpy:
        if not arc_consistent(domain, neighbors, x, xi, xj):
            domain[xi] = domain[xi].replace(x, '') #can change this
            revised = True
    return revised

def arc_consistent(domain, neighbors, x, xi, xj):
    domain_cpy = domain[xj]
    for y in domain_cpy:
        if x != y:
            if xj in neighbors[xi]:
                return True
    return False

# def BTS(variables, domain, neighbors):
#     return backtrack({}, variables, domain, neighbors)
#
# def backtrack(assignment, variables, domain, neighbors):
#     print(assignment.keys())
#     if assignment_complete(assignment, variables):
#         # print("here")
#         return assignment
#     domain_cpy = copy.deepcopy(domain)
#     # print(domain)
#     var = select_unassigned_variable(assignment, variables, domain_cpy)
#     # print(var)
#     for value in order_domain_domain(domain_cpy, var, assignment):
#         # print("here")
#         if consistent(var, value, assignment, neighbors): #add var maybe
#             assignment[var] = value
#             inferences = {}
#             inferences = inference(assignment, inferences, domain_cpy, neighbors, var, value)
#             if inferences!= False:
#                 result = backtrack(assignment, variables, domain_cpy, neighbors)
#                 if result != False:
#                     return result
#         assignment[var] = None
#     return False
#
# def consistent(var, value, assignment, neighbors):
#     for neighbor in neighbors[var]:
#         if neighbor in assignment.keys():
#             if assignment[neighbor] == value:
#                 return False
#     return True
#
# def inference(assignment, inferences, domain, neighbors, var, value):
#     inferences[var] = value
#     for neighbor in [var]:
#         if neighbor not in assignment:
#             if value in domain[neighbor]:
#                 if len(domain[neighbor]) == 1:
#                     return False
#                 remaining = domain[neighbor] = domain[neighbor].replace(value, "")
#                 if len(remaining) == 1:
#                     result = inference(assignment, inferences, domain, neighbors, var, value)
#                     if not result:
#                     	return False
#     return inferences
#
# def assignment_complete(assignment, variables):
#     return set(assignment.keys()) == set(variables)
#
# def order_domain_domain(domain, var, assignment):
#     # if len(domain[var]) == 1:
#     #     return domain[var]
#     if var in domain:
#         val = domain[var]
#         return sorted(list(val))
#
# def select_unassigned_variable(assignment, variables, domain):
#     # print(domain)
#     unassigned_variables = {}
#     mrv = None
#     for variable in domain:
#         if len(domain[variable]) > 1:
#             if variable not in assignment.keys():
#                 # print(unassigned_variables)
#                 unassigned_variables.update([(variable, len(domain[variable]))])
#     # print(unassigned_variables)
#     if unassigned_variables:
#         mrv = min(unassigned_variables, key=unassigned_variables.get)
#     # print(mrv)
#     return mrv
