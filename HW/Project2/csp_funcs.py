#!/usr/bin/python3
# import copy

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

# def BTS(variables, values, peers):
#     return backtrack({}, variables, values, peers)
#
# def backtrack(assignment, variables, values, peers):
#     print(assignment.keys())
#     if assignment_complete(assignment, variables):
#         # print("here")
#         return assignment
#     values_cpy = copy.deepcopy(values)
#     # print(values)
#     var = select_unassigned_variable(assignment, variables, values_cpy)
#     # print(var)
#     for value in order_domain_values(values_cpy, var, assignment):
#         # print("here")
#         if consistent(var, value, assignment, peers): #add var maybe
#             assignment[var] = value
#             inferences = {}
#             inferences = inference(assignment, inferences, values_cpy, peers, var, value)
#             if inferences!= False:
#                 result = backtrack(assignment, variables, values_cpy, peers)
#                 if result != False:
#                     return result
#         assignment[var] = None
#     return False
#
# def consistent(var, value, assignment, peers):
#     for neighbor in peers[var]:
#         if neighbor in assignment.keys():
#             if assignment[neighbor] == value:
#                 return False
#     return True
#
# def inference(assignment, inferences, values, peers, var, value):
#     inferences[var] = value
#     for neighbor in [var]:
#         if neighbor not in assignment:
#             if value in values[neighbor]:
#                 if len(values[neighbor]) == 1:
#                     return False
#                 remaining = values[neighbor] = values[neighbor].replace(value, "")
#                 if len(remaining) == 1:
#                     result = inference(assignment, inferences, values, peers, var, value)
#                     if not result:
#                     	return False
#     return inferences
#
# def assignment_complete(assignment, variables):
#     return set(assignment.keys()) == set(variables)
#
# def order_domain_values(values, var, assignment):
#     # if len(values[var]) == 1:
#     #     return values[var]
#     if var in values:
#         val = values[var]
#         return sorted(list(val))
#
# def select_unassigned_variable(assignment, variables, values):
#     # print(values)
#     unassigned_variables = {}
#     mrv = None
#     for variable in values:
#         if len(values[variable]) > 1:
#             if variable not in assignment.keys():
#                 # print(unassigned_variables)
#                 unassigned_variables.update([(variable, len(values[variable]))])
#     # print(unassigned_variables)
#     if unassigned_variables:
#         mrv = min(unassigned_variables, key=unassigned_variables.get)
#     # print(mrv)
#     return mrv
