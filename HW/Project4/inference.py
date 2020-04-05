import copy as cp

def prob(Y, e, bn):
    parents = bn[Y][0]
    if not parents:
        P = bn[Y][1][None] #CHANGE THIS WRT INPUT
    else: #Parents exist
        p_vals = tuple(e[p] for p in parents)  #value of parents(Y)
        P = bn[Y][1][p_vals] #Probability of Parent(Y) values
    return P if e[Y] else (1.0 - P)

def enumerateAll(vars, e,bn):
    if not vars:
        return 1.0
    Y = vars.pop()
    if Y in e:
        query = prob(Y,e,bn) * enumerateAll(vars,e,bn)
        vars.append(Y)
        return query
    else:
        query_sum = 0
        e_cpy = cp.deepcopy(e)
        for boolval in [False, True]:
            e_cpy[Y] = boolval
            query_sum += prob(Y,e_cpy,bn) * enumerateAll(vars,e_cpy,bn)
        vars.append(Y)
        return query_sum

def normalize(Q):
    N_factor = 1/sum(Q.values())
    for key in Q.keys():
        Q[key] = Q[key] * N_factor
    return Q

def enumerationAsk(X, e, bn,vars):
    Q = {}
    for xi in [False,True]: #because boolean values
        e_cpy = cp.deepcopy(e)
        e_cpy[X] = xi
        Q[xi] = enumerateAll(vars,e_cpy,bn)
    return normalize(Q)

# # Run Program for given input
# bn = {'B':[[],{None:.001}],
#       'E':[[],{None:.002}],
#       'A':[['B','E'],
#                {(False,False):.001,(False,True):.29,
#                 (True,False):.94,(True,True):.95}],
#       'J':[['A'],
#                    {(False,):.05,(True,):.90}],
#       'M':[['A'],
#                    {(False,):.01,(True,):.70}]}
# vars = ['M','J','A','B','E']
# print(enumerationAsk('B',{'J':True,'M':True},bn,vars))
