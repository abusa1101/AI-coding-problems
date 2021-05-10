""" Problem 3 Markov Decision Process """

import csv
import copy
import math

class MDP:
    """ MDP Value-Iteration Algorithm Class """
    def __init__(self):
        # Local Data
        self.states = []
        self.actions = []
        self.probs = {}
        self.rewards = {}
        self.gamma = 0.0
        self.epsilon = 0.0

        # Solution
        self.optimal_utils = []
        self.best_action_inds = []


    def read_mdp_file(self, fname="mdpinput.txt"):
        """ Reads in mdp from file """
        with open(fname, 'r') as infile:
            csvreader = csv.reader(infile)
            lines = []
            for line in csvreader:
                lines.append(line)

            # 1) Grab the States from the 2nd line (index 1)
            for char_val in lines[1]:
                self.states.append(char_val.strip())

            # 2) Grab the Actions from the 4th line (index 3)
            for char_val in lines[3]:
                a_str = char_val.strip()
                num_s = len(self.states)
                self.actions.append(a_str)
                self.probs[a_str] = [[0.0 for i in range(num_s)] for j in range(num_s)]

            # 3) Grab the Transition models starting on 8th line (index 7)
            line_section_idx = 7
            for a_idx, action in enumerate(self.actions):
                for i in range(0, 3):
                    line_idx = line_section_idx + a_idx*4 + i
                    for j in range(0, 3):
                        self.probs[action][i][j] = float(lines[line_idx][j])


            # 4) Grab the Rewards (assumes in correct order like example)
            line_section_idx = line_section_idx + len(self.actions)*4
            line_idx = line_section_idx
            for state in self.states:
                self.rewards[state] = {}
                for action in self.actions:
                    self.rewards[state][action] = float(lines[line_idx][-1])
                    line_idx += 1

            # 5) Grab the discount factor (gamma)
            line_section_idx = line_idx + 1
            self.gamma = float(lines[line_section_idx][-1])

            # 6) Grab the tolerance (epsilon)
            line_section_idx += 2
            self.epsilon = float(lines[line_section_idx][-1])


    def run(self):
        """ Obtain Optimal Policy """
        # 1) Run Value Iteration
        utils = self.value_iteration()

        # 2) Obtain the Optimal Policy given these values
        best_action_inds = self.compute_policy(utils)

        self.optimal_utils = utils
        self.best_action_inds = best_action_inds


    def value_iteration(self):
        """ Value Iteration Algorithm """
        # Init local variables
        # utils = [0.0] * len(self.states)
        utils_ = [0.0] * len(self.states)

        # Repeat
        while 1:
            # Start the next iteration, copy util over and reset delta
            utils = copy.deepcopy(utils_)
            delta = 0.0

            # loop over each state, computing next utilities
            for idx_s, state in enumerate(self.states):
                # 1) Compute U'[s]
                curr_best_util = -math.inf
                for _, action in enumerate(self.actions):
                    curr_util = 0.0
                    for idx_s_, _ in enumerate(self.states):
                        curr_util += self.probs[action][idx_s][idx_s_] * utils[idx_s_]
                    curr_util = curr_util * self.gamma + self.rewards[state][action]
                    if curr_util > curr_best_util:
                        curr_best_util = curr_util
                utils_[idx_s] = curr_best_util

                # 2) Update delta if difference is larger
                if abs(utils_[idx_s] - utils[idx_s]) > delta:
                    delta = abs(utils_[idx_s] - utils[idx_s])

            # Until error threshold is met
            if delta < self.epsilon * (1 - self.gamma) / self.gamma:
                return utils



    def compute_policy(self, utils):
        """ Computes optimal policy from utility values after value iteration is done """
        best_action_inds = []

        for idx_s, state in enumerate(self.states):
            curr_best_util = -math.inf
            curr_best_action_idx = 0
            for idx_a, action in enumerate(self.actions):
                curr_util = 0.0
                for idx_s_, _ in enumerate(self.states):
                    curr_util += self.probs[action][idx_s][idx_s_] * utils[idx_s_]
                curr_util = curr_util * self.gamma + self.rewards[state][action]
                if curr_util > curr_best_util:
                    curr_best_util = curr_util
                    curr_best_action_idx = idx_a
            best_action_inds.append(curr_best_action_idx)

        return best_action_inds


    def write_output(self, fname="policy.txt"):
        """ Write formatted output of to output file """
         # 1) Open the file for writing
        f = open(fname, "w")

        # 2) Construct the output string
        out_str = ""
        for idx_s, state in enumerate(self.states):
            out_str += state + ": "
            out_str += self.actions[self.best_action_inds[idx_s]]
            out_str += " (" + "{:.2f}".format(self.optimal_utils[idx_s]) + ")"

            if idx_s < (len(self.states) - 1):
                out_str += "\n"

        # 3) Write to the output file and then close it
        f.write(out_str)
        f.close()


def main():
    """ main function for calling mdp value iteration algorithm """
    my_mdp = MDP()

    # 1) Read in the input file
    my_mdp.read_mdp_file()

    # 2) Perform Value Iteration to compute the optimal policy
    my_mdp.run()

    # 3) Write Output
    my_mdp.write_output()



if __name__ == "__main__":
    main()
