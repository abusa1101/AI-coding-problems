import copy as cp

def prob(Y, e, bn):
    parents = bn[Y][0]
    if not parents:
        P = bn[Y][1][('None','None')]
    else: #Parents exist
        # print(Y)
        # print(bn[Y])
        print(parents)
        print(e)
        p_vals_list = []
        for parent in parents:
            p_vals_list.append(str(e[parent]))
        if len(p_vals_list) != 2:
            p_vals_list.append('None')
        p_vals = tuple(p_vals_list)
        print(bn[Y][1])
        print(p_vals)
        P = bn[Y][1][p_vals] #Probability of Parent(Y) values
    return P if e[Y] else (1.0 - P)

def enumerateAll(vars, e, bn):
    if not vars:
        return 1.0
    Y = vars.pop()
    # print(Y)
    # print(e)
    if Y in e:
        # print("in")
        query = prob(Y,e,bn) * enumerateAll(vars,e,bn)
        vars.append(Y)
        return query
    else:
        # print('else')
        query_sum = 0
        e_cpy = cp.deepcopy(e)
        # print(e_cpy)
        for boolval in [False, True]:
            # print(Y)
            e_cpy[Y] = boolval
            print(e_cpy)
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
        Q[xi] = enumerateAll(vars, e_cpy, bn)
    return normalize(Q)# Run Program for given input


# Run Program for given input
bn = {'B':[[],{('None','None'):.001}],
      'E':[[],{('None','None'):.002}],
      'A':[['B','E'],
               {('False','False'):.001,('False','True'):.29,
                ('True','False'):.94,('True','True'):.95}],
      'J':[['A'],
                   {('False','None'):.05,('True','None'):.90}],
      'M':[['A'],
                   {('False','None'):.01,('True','None'):.70}]}
vars = ['M','J','A','B','E']
print(enumerationAsk('B',{'J':'True','M':'True'}, bn, vars))
