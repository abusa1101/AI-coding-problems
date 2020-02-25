#!/usr/bin/python3
import copy

#AC-3 FUNCTIONS
def ac_3(constraints, domain, neighbors):
    queue = list(constraints) #arcs of CSP
    while queue:
        x_i, x_j = queue.pop(0)
        if revise(domain, neighbors, x_i, x_j):
            if len(domain[x_i]) == 0:
                return False
            for x_k in neighbors[x_i] - set(x_j):
                queue.append([x_k, x_i])
    return True

def revise(domain, neighbors, x_i, x_j):
    revised = False
    domain_cpy = set(domain[x_i])
    for x_val in domain_cpy:
        if not arc_consistent(domain, neighbors, x_val, x_i, x_j):
            domain[x_i] = domain[x_i].replace(x_val, '') #check for a better way to replace maybe?
            revised = True
    return revised

def arc_consistent(domain, neighbors, x_val, x_i, x_j):
    domain_cpy = domain[x_j]
    for y_val in domain_cpy:
        if x_val != y_val:
            if x_j in neighbors[x_i]:
                return True
    return False


#BACKTRACKING SEARCH FUNCTIONS
def bt_search(variables, domain, neighbors):
    return backtrack({}, variables, domain, neighbors)

def backtrack(assignment, variables, domain, neighbors):
    if assignment_complete(assignment, variables):
        return assignment
    domain_cpy = copy.deepcopy(domain)
    var = select_unassigned_variable(assignment, domain_cpy)
    if var:
        for value in order_domain_values(domain_cpy, var):
            if consistent(var, value, assignment, neighbors):
                assignment[var] = value
                inferences = {}
                if inference(assignment, inferences, domain_cpy, neighbors, var, value):
                    result = backtrack(assignment, variables, domain_cpy, neighbors)
                    if result:
                        return result
            if var in assignment:
                del assignment[var]
    return False

def assignment_complete(assignment, variables):
    return len(assignment) == len(variables)

def select_unassigned_variable(assignment, domain):
    unassigned_variables = {}
    # domain_len = []
    selected_var = None
    for variable in domain:
        if variable not in assignment:
            # unassigned_variables.append(variable)
            # domain_len.append(len(domain[variable]))
            unassigned_variables.update([(variable, len(domain[variable]))])
    if unassigned_variables:
        selected_var = min(unassigned_variables, key=unassigned_variables.get)
    return selected_var

def order_domain_values(domain, var):
    if var in domain:
        sorted_value = sorted(list(domain[var]))
        return sorted_value
    return None

def consistent(var, value, assignment, neighbors):
    for neighbor in neighbors[var]:
        if neighbor in assignment:
            if assignment[neighbor] == value:
                return False
    return True

def inference(assignment, inferences, domain, neighbors, var, value):
    inferences[var] = value
    for neighbor in [var]:
        if neighbor not in assignment:
            if value in domain[neighbor]:
                if len(domain[neighbor]) == 1:
                    return False
                domain[neighbor] = domain[neighbor].replace(value, '')
                if len(domain[neighbor]) == 1:
                    result = inference(assignment, inferences, domain, neighbors, var, value)
                    if not result:
                        return False
    return inferences
