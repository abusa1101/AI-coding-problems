import csv
import numpy as np

def parse_input_file(file_name): #Parsing mdpinput.txt file
    file = csv.reader(open(file_name, 'r'), skipinitialspace='True')
    input_list = list(file)

    states = input_list[1]
    actions = input_list[3]
    gamma_idx = 0
    for i, line in enumerate(input_list):
        if line[0] == "% Rewards (State":
            reward_idx = i + 1
        if line[0] == "% Discount factor (gamma)":
            gamma_idx = i + 1
    gamma = float(input_list[gamma_idx][0])
    epsilon = float(input_list[gamma_idx + 2][0])

    transitions = {a: [] for a in actions}
    a_num = 0
    for line in input_list[6:reward_idx - 1]:
        if '% Action ' in line[0]:
            a_num = int(line[0][9]) - 1
        key = 'a' + str(a_num)
        if '% Action ' not in line[0]:
            transitions[key].append(line)

    rewards = {}
    for line in input_list[reward_idx:gamma_idx - 1]:
        rewards[(line[0], line[1])] = float(line[2])
    return states, actions, transitions, rewards, gamma, epsilon

def find_max(state, utils, states, actions, transitions, rewards, gamma):
    values = []
    policies = []
    for action in actions:
        s_idx = int(state[1:])
        prob_list = transitions[action][s_idx]
        expectation = 0.0
        for s_next in states:
            s_next_idx = int(s_next[1:])
            prob = float(prob_list[s_next_idx])
            expectation += prob * utils[s_next]
        values.append(rewards[(state, action)] + gamma * expectation)
        policies.append(action)
        argmax_idx = np.argmax(values)
    return max(values), policies[argmax_idx]

def value_iteration(states, actions, transitions, rewards, gamma, epsilon):
    utils_prev = {state: 0 for state in states}
    utils_args = {state: '' for state in states}
    while True:
        utils = utils_prev.copy()
        delta = 0
        for state in states:
            max_val, argmax = find_max(state, utils, states, actions, transitions, rewards, gamma)
            utils_prev[state] = max_val
            delta = max(delta, abs(utils_prev[state] - utils[state]))
            utils_args[state] = argmax
        if delta <= (epsilon * (1 - gamma) / gamma):
            return utils, utils_args

#Parse input file and run value-policy iteration on it
STATES, ACTIONS, TRANSITIONS, REWARDS, GAMMA, EPSILON = parse_input_file('mdpinput.txt')
UTILITIES, POLICIES = value_iteration(STATES, ACTIONS, TRANSITIONS, REWARDS, GAMMA, EPSILON)

#Write to output file
with open('policy.txt', 'w') as writer:
    writer.write('% Format: State: Action (Value)\n')
    for state_key in UTILITIES.keys():
        writer.write(state_key + ': ' + POLICIES[state_key] + ' (' +
                     str(np.round(UTILITIES[state_key], decimals=2)) + ')\n')
        print(state_key + ': ' + POLICIES[state_key] + ' (' +
              str(np.round(UTILITIES[state_key], decimals=2)) + ')')
