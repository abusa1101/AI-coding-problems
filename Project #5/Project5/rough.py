def valueIteration2(states, actions, transitions, rewards, gamma, epsilon):
    utils = {s: 0 for s in states}
    while True:
        utils_cpy = utils.copy()
        delta = 0
        for s in states:
            evals = {a: 0 for a in actions}
            for a in actions:
                for s_next in states:
                    evals[a] += prob * utils_cpy[s_next]
            utils[s] = reward[s] + gamma * max(evals)
            delta = max(delta, abs(utils_cpy[s] - utils[s]))
        if delta <= (epsilon * (1 - gamma) / gamma):
            return utils

# V = value_iteration()
# print('State - Value')
# for s in V:
#     print(s, ' - ' , V[s])
# pi = best_policy(V)
# print('\nOptimal policy is \nState - Action')
# for s in pi:
#     print(s, ' - ' , pi[s])

values = {each state : 0}
loop ITERATIONS times:
    previous = copy of values
    for all states:
        EVs = {each legal action : 0}
        for all legal actions:
            for each possible next_state:
                EVs[action] += prob * previous[next_state]
        values[state] = reward(state) + discount * max(EVs)


def valueIteration2():
    values = {s: 0 for s in states}
    while True:
        previous = values.copy()
        delta = 0
        for s in states:
            EVs = {a: 0 for a in actions}
            for a in actions:
                idx = int(s[1:])
                P = transitions[a][idx]
                for s_next in states:
                    idx_next = int(s_next[1:])
                    prob = float(P[idx_next])
                    EVs[a] += prob * previous[s_next]
            values[s] = rewards[(s,a)] + (gamma * max(EVs.values()))
            delta = max(delta, abs(previous[s] - values[s]))
            factor = (epsilon * (1 - gamma) / gamma)
        if delta <= factor:
            print(values)
            return values

#  def R(state):
#         return reward[state]
#
# def actions(state):
#     return transition[state].keys()
#
# def T(state, action):
#     return transition[state][action]
# transition_file contains tuple (state, action, result-state, probability)
# reward_file contains tuple (state, reward)


def value_iteration(mdp, epsilon=0.001):
    """Solving an MDP by value iteration. [Figure 17.4]"""

    U1 = {s: 0 for s in mdp.states}
    R, T, gamma = mdp.R, mdp.T, mdp.gamma
    while True:
        U = U1.copy()
        delta = 0
        for s in mdp.states:
            U1[s] = R(s) + gamma * max(sum(p * U[s1] for (p, s1) in T(s, a))
                                       for a in mdp.actions(s))
            delta = max(delta, abs(U1[s] - U[s]))
        if delta <= epsilon * (1 - gamma) / gamma:
            return U

def entropy(pi):
    '''
    return the Entropy of a probability distribution:
    entropy(p) = − SUM (Pi * log(Pi) )
    defintion:
            entropy is a metric to measure the uncertainty of a probability distribution.
    entropy ranges between 0 to 1
    Low entropy means the distribution varies (peaks and valleys).
    High entropy means the distribution is uniform.
    See:
            http://www.cs.csi.cuny.edu/~imberman/ai/Entropy%20and%20Information%20Gain.htm
    '''

    total = 0
    for p in pi:
        p = p / sum(pi)
        if p != 0:
            total += p * log(p, 2)
        else:
            total += 0
    total *= -1
    return total


def gain(d, a):
    '''
    return the information gain:
    gain(D, A) = entropy(D)−􏰋 SUM ( |Di| / |D| * entropy(Di) )
    '''

    total = 0
    for v in a:
        total += sum(v) / sum(d) * entropy(v)

    gain = entropy(d) - total
    return gain

# set of example of the dataset
willWait = [6, 6] # Yes, No

# attribute, number of members (feature)
patron = [[4,0], [2,4], [0,2]] # Some, Full, None
alt = [[3,3], [3,3]] # Yes, No
bar = [[3,3], [3,3]] # Yes, No
fri = [[2,3], [4,3]] # Yes, No
hun = [[5,2], [1,4]] # Yes, No
price = [[3, 4], [2, 0], [1, 2]]
rain = [[3, 2], [3, 4]]
res = [[3, 2], [3, 4]]
type = [[1,1], [2,2], [2,2], [1,1]]
est = [[4, 2], [1, 1], [1, 1], [0, 2]]

print(gain(willWait, patron))


# def bfs(tree, start):
#     # maintain a queue of paths
#     queue = []
#     # push the first path into the queue
#     queue.append([start])
#     while queue:
#         # get the first path from the queue
#         path = queue.pop(0)
#         # get the last node from the path
#         node = path[-1]
#         # path found
#         if node == end:
#             return path
#         # enumerate all adjacent nodes, construct a new path and push it into the queue
#         for adjacent in tree.get(node, []):
#             new_path = list(path)
#             new_path.append(adjacent)
#             queue.append(new_path)

    # for k, v in tree.items():
    #     # print(k)
    #     if isinstance(v,dict):
    #         # print(v.keys())
    #         tree_print(v)
    #     else:
    #         print("{0} : {1}".format(k,v))
