""" Problem 7 Enumeration-Ask Algorithm """

import csv
import copy

class Enumeration:
    """ Enumeration-Ask Algorithm Class """
    def __init__(self):
        # Bayes Net Data
        self.vars = []
        self.parents = {}
        self.probs = {}

        # Query Data
        self.query_var = 'A'
        self.given_vars = []
        self.given_vals = []
        self.query_prob = 0.42

    def read_bayes_net(self, fname="bn.txt"):
        """ Reads in Bayes net from file """
        with open(fname, 'r') as infile:
            csvreader = csv.reader(infile)
            lines = []
            for line in csvreader:
                lines.append(line)

            # 1) Grab the Variables from the 2nd line (index 1)
            for char_val in lines[1]:
                self.vars.append(char_val[-1])
                self.parents[char_val[-1]] = []

            # 2) Grab the Edges from the next several lines
            line_idx_prob_start = 0
            for line_idx, line in enumerate(lines[3:]):
                if line[0][0] == "%":
                    line_idx_prob_start = line_idx + 4
                    break
                # Grab Edges
                from_node = line[0][-1]
                to_node = line[1][-1]
                self.parents[to_node].append(from_node)

            # 2.5) Prep lists of probs for each variable
            for var in self.vars:
                num_parents = len(self.parents[var])
                num_entries = 2 ** num_parents
                self.probs[var] = [0.0] * num_entries

            # 3) Grab the Probability Values
            for line in lines[line_idx_prob_start:]:
                if line[0][0] != "P":
                    break

                # Convert back to full line from csv style
                full_line = ""
                full_line += line[0]
                if len(line) > 1:
                    for entry in line[1:]:
                        full_line += "," + entry

                # Grab Query Variable
                query_var = full_line[2]

                # Grab prob val
                last_equal_idx = full_line.rfind("=")
                prob_val = float(full_line[last_equal_idx+1:])
                if full_line[4] == "F":
                    prob_val = 1 - prob_val
                if prob_val == 0.0:
                    prob_val = 0.0000000000001

                # Get the "given"
                given_vars = []
                given_vals = []
                given_idx = full_line.find("|")
                if given_idx != -1:
                    given_string = full_line[given_idx+1:last_equal_idx]
                    num_given_vars = int(len(given_string)/4)
                    for i in range(0, num_given_vars):
                        given_vars.append(given_string[i*4])
                        given_vals.append(0 if (given_string[i*4+2] == "F") else 1)


                # Finally, set the probability for this line
                self.set_prob(query_var, given_vars, given_vals, prob_val)

    def read_query(self, fname="input.txt"):
        """ Reads in Query from file """
        with open(fname, 'r') as infile:
            csvreader = csv.reader(infile)
            lines = []
            for line in csvreader:
                lines.append(line)

            # 1) Grab the Query Variable from the 2nd line (index 1)
            self.query_var = lines[1][0]

            # 2) Grab the Evidence from the 4th line (index 3)
            self.given_vars = []
            self.given_vals = []
            for idx, evidence in enumerate(lines[3]):
                if idx == 0:
                    self.given_vars.append(evidence[0])
                    self.given_vals.append(0 if (evidence[2] == "F") else 1)
                else:
                    self.given_vars.append(evidence[1])
                    self.given_vals.append(0 if (evidence[3] == "F") else 1)

    def set_prob(self, query, given_vars, given_vals, prob_val):
        """ Stores conditional probability """

        # 1) Find the index to store the probability
        prob_idx = self.get_prob_storage_idx(query, given_vars, given_vals)

        # 2) Store the probability
        self.probs[query][prob_idx] = prob_val

    def get_prob(self, query, given_vars, given_vals, query_val):
        """ Retrieve stored cond. prob. """
        # 1) Find the index where the probability is stored
        prob_idx = self.get_prob_storage_idx(query, given_vars, given_vals)

        # 2 Retrieve it
        prob_val = self.probs[query][prob_idx]

        if query_val == 0:
            prob_val = 1.0 - prob_val

        return prob_val

    def get_prob_storage_idx(self, query, given_vars, given_vals):
        """ Grab the index where we are storing the prob for this var """
        parents = self.parents[query]
        prob_idx = 0
        for var_idx, given_var in enumerate(given_vars):
            if given_var in parents:
                idx = parents.index(given_var)
                prob_idx += int(given_vals[var_idx] * (2 ** idx))
        return prob_idx

    def inference(self):
        """ Performs inference using enumeration ask algorithm """
        distribution = self.enum_ask()
        self.query_prob = distribution[0]

    def enum_ask(self):
        """ Enumeration Ask Algorithm """
        q_x = [0.5, 0.5]  # T / F

        given_vars = copy.deepcopy(self.given_vars)
        given_vals = copy.deepcopy(self.given_vals)

        given_vars.append(self.query_var)
        given_vals.append(0)

        all_vars = copy.deepcopy(self.vars)

        # For each value x_i of X (T,F)
        for i in range(0, 2):
            given_vals[-1] = i
            q_x[i] = self.enum_all(all_vars, given_vars, given_vals)
        q_x.reverse()

        return self.normalize(q_x)

    def enum_all(self, variables, given_vars, given_vals):
        """ Enumerate All Algorithm """

        if len(variables) == 0:
            return 1.0

        Y = variables[0]

        # If Y has value y in e (i.e. it's in the evidence already)
        if Y in given_vars:
            y = given_vals[given_vars.index(Y)]
            return self.get_prob(Y, given_vars, given_vals, y) * \
                   self.enum_all(self.rest(variables), given_vars, given_vals)
        
        # Else, add prob of all possibilities
        sum_val = 0.0
        for y in range(0, 2):
            ext_given_vars = copy.deepcopy(given_vars)
            ext_given_vars.append(Y)

            ext_given_vals = copy.deepcopy(given_vals)
            ext_given_vals.append(y)

            sum_val += self.get_prob(Y, given_vars, given_vals, y) * \
                        self.enum_all(self.rest(variables), ext_given_vars, ext_given_vals)
        return sum_val

    def rest(self, variables):
        """ Removes first variable and returns the rest safely """
        return copy.deepcopy(variables[1:])

    def normalize(self, q_x):
        """ Normalizes the distribution to add to 1 """
        total = q_x[0] + q_x[1]

        if total == 0:
            return q_x

        q_x[0] = q_x[0] / total
        q_x[1] = q_x[1] / total

        return q_x


    def print_result(self):
        """ Print the result to the terminal """
        # print(self.query_prob)
        print('%.10f'%self.query_prob)



def main():
    """ main function for calling enumeration ask algorithm """

    my_enumeration = Enumeration()

    # 1) Read in the Bayes Net and Query
    my_enumeration.read_bayes_net()
    my_enumeration.read_query()

    # 2) Perform Exact Inference on the Bayes Net
    my_enumeration.inference()

    # 3) Print Answer to Terminal
    my_enumeration.print_result()






if __name__ == "__main__":
    main()
