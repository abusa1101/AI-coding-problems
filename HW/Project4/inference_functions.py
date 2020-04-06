import copy as cp

def probability(y_var, e_dict, bayes_net):
    parents = bayes_net[y_var][0]
    if not parents: #If y_var is a parent node (with no parents)
        prob = bayes_net[y_var][1][(None, None)] #Grab the independent Prob values from BN
    else: #If y_var does have parent/s
        p_vals_list = []
        for parent in parents:
            p_vals_list.append(e_dict[parent])
        if len(p_vals_list) != 2: #will have to change this for more than 2
            p_vals_list.append(None)
        parent_vals = tuple(p_vals_list)
        prob = bayes_net[y_var][1][parent_vals] #Probability of Parent(y_var) values
    return prob if e_dict[y_var] else (1.0 - prob)

def enum_all(vars, e_dict, bayes_net):
    if not vars: #return if there are no variables
        return 1.0
    y_var = vars.pop() #Parents listed first, then children
    if y_var in e_dict: #If variable is in evidence
        query = probability(y_var, e_dict, bayes_net) * enum_all(vars, e_dict, bayes_net)
        #Check input arg1 to prob func
        vars.append(y_var) #add popped value back to original variables list
        return query
    else: #If variable is hidden instead
        query_sum = 0
        e_cpy = cp.deepcopy(e_dict) #copy e again because extending with y_var = y this time
        for y_val in [True, False]: #y can take on T/F values
            e_cpy[y_var] = y_val #extending e with y_var = y
            query_sum += probability(y_var, e_cpy, bayes_net) * enum_all(vars, e_cpy, bayes_net)
            #Sum of probabilities for hidden variable
        vars.append(y_var) #add popped value back to original variables list
        return query_sum

def normalize(q_dist):
    n_factor = 1/sum(q_dist.values()) #Normalizing factor -> Total sum of X = T,F values in Q
    for key in q_dist.keys(): #For each value of X
        q_dist[key] = q_dist[key] * n_factor #Normalize associated probability value
    return q_dist

def enum_ask(x_var, e_dict, bayes_net, vars):
    if x_var in e_dict.keys(): #If query is in evidence, return with error msg
        return 'Query var must NOT be in evidence vars'
    q_dist = {} #probability distr of query var X (initially empty)
    for x_i in [True, False]: #xi is each value of X
        e_cpy = cp.deepcopy(e_dict) #copy e because extending it below
        e_cpy[x_var] = x_i #extending e with X = xi
        q_dist[x_i] = enum_all(vars, e_cpy, bayes_net)
        #Call recursive func and get Q for X = xi value
    return normalize(q_dist) #Normalize distribution over X
