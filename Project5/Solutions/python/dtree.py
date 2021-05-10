""" Problem 4 Decision Tree Generation """

import csv
import copy
import math
from collections import deque


class Queue:
    """ FIFO Queue class """
    def __init__(self):
        self.queue = deque()

    def push(self, item):
        """ Push items onto queue """
        self.queue.append(item)

    def pop(self):
        """ Pop items off of queue """
        return self.queue.popleft()

    def is_empty(self):
        """ empty check """
        return self.size() == 0

    def size(self):
        """ returns size of queue """
        return len(self.queue)

class Node:
    """ Node of a tree """
    def __init__(self, value):
        self.value = value
        self.children = []
        self.edges = []

    def add_child(self, child_node, edge):
        """ Add a child node """
        self.children.append(child_node)
        self.edges.append(edge)

class DecisionTree:
    """ Decision Tree Generation Algorithm Class """
    def __init__(self):
        self.attributes = []
        self.att_idxs = {}
        self.att_values = {}
        self.dec_values = []
        self.examples = []
        self.dtree = None

    def read_dtree_file(self, fname="examples.txt"):
        """ Reads in examples from file """
        with open(fname, 'r') as infile:
            csvreader = csv.reader(infile)
            lines = []
            for line in csvreader:
                lines.append(line)

            # 1) Grab the attributes and their possible values (index 1)
            curr_line_idx = 1
            for line_idx, next_line in enumerate(lines[1:]):
                # Check if we're done
                if next_line[0][0] == "%":
                    curr_line_idx += line_idx
                    break

                # Grab the attribute name and first option
                colon_ind = next_line[0].rfind(":")
                att_name = next_line[0][:colon_ind]
                self.attributes.append(att_name)
                self.att_idxs[att_name] = len(self.attributes) - 1

                self.att_values[att_name] = []
                self.att_values[att_name].append(next_line[0][colon_ind+1:].strip())

                # Grab the remaining options
                for att_val in next_line[1:]:
                    self.att_values[att_name].append(att_val.strip())

            # 2) Grab the decision values
            curr_line_idx += 1
            for dec_value in lines[curr_line_idx]:
                self.dec_values.append(dec_value.strip())

            # 3) Grab the example instances
            curr_line_idx += 3
            for ex_line in lines[curr_line_idx:]:
                # Check if we're done or there was a mismatch
                if len(ex_line) != (len(self.attributes) + 1):
                    break

                example = []
                for value in ex_line:
                    example.append(value.strip())
                self.examples.append(example)

    def run(self):
        """ Run the decision tree learning algorithm on the example data """
        self.dtree = self.decision_tree_learning(self.examples, self.attributes, self.examples)

    def decision_tree_learning(self, examples, attributes, parent_examples):
        """ Recursive decision tree learning algorithm """

        if len(examples) == 0:
            return self.plurality_value(parent_examples)
        elif self.same_classification(examples):
            return self.plurality_value(examples)
        elif len(attributes) == 0:
            return self.plurality_value(examples)
        else:
            next_attr = self.max_importance(attributes, examples)
            tree = Node(next_attr)

            for attr_value in self.att_values[next_attr]:
                # Collect examples in which next_attr has value attr_value
                exs = []
                for example in examples:
                    if example[self.att_idxs[next_attr]] == attr_value:
                        example_copy = copy.deepcopy(example)
                        exs.append(example_copy)

                # Remove next_attr from attributes
                next_attributes = copy.deepcopy(self.attributes)
                next_attributes.remove(next_attr)

                # Recursively call decision_tree_learning to populate subtrees
                sub_tree = self.decision_tree_learning(exs, next_attributes, examples)

                # Add a branch to the tree
                tree.add_child(sub_tree, attr_value)

            return tree

    def plurality_value(self, examples):
        """ Returns the plurality value for the given examples """
        # 1) Tally up # of values
        dec_value_counts = [0] * len(self.dec_values)
        for idx, dec_value in enumerate(self.dec_values):
            for example in examples:
                if example[-1] == dec_value:
                    dec_value_counts[idx] += 1

        # 2) Find the plurality value
        max_count = dec_value_counts[0]
        max_value = self.dec_values[0]
        for idx, dec_value in enumerate(self.dec_values):
            if dec_value_counts[idx] > max_count:
                max_count = dec_value_counts[idx]
                max_value = dec_value

        # 3) Construct a subtree and return it
        tree = Node(max_value)
        return tree


    def same_classification(self, examples):
        """ Returns true if all examples have the same classification, false otherwise """
        value = examples[0][-1]
        for example in examples[1:]:
            if value != example[-1]:
                return False
        return True

    def max_importance(self, attributes, examples):
        """ Returns the max importance attribute for given examples """
        # 1) Compute first elements importance for comparison
        max_value = self.importance(attributes[0], examples)
        max_attr = attributes[0]

        # 2) Loop over all others, keeping track of the most important attribute
        for attribute in attributes:
            next_value = self.importance(attribute, examples)
            if next_value > max_value:
                max_value = next_value
                max_attr = attribute

        return max_attr

    def importance(self, attribute, examples):
        """ Returns the importance of an attribute given examples """
        # 1) Calculate the occurences of each decision value
        dec_value_counts = [0] * len(self.dec_values)
        for idx, dec_value in enumerate(self.dec_values):
            for example in examples:
                if example[-1] == dec_value:
                    dec_value_counts[idx] += 1

        # 1.5) If no matches, quit
        total_count = sum(dec_value_counts)
        if total_count == 0:
            return 0

        # 2) Normalize to obtain probabilities
        dec_value_probs = [0.0] * len(self.dec_values)
        for i in range(0, len(self.dec_values)):
            dec_value_probs[i] = dec_value_counts[i] / total_count

        # 3) Calculate the importance
        b_val = self.b_calc(dec_value_probs)
        r_val = self.remainder_calc(attribute, examples, dec_value_probs, total_count)
        importance_value = b_val - r_val

        return importance_value

    def b_calc(self, dec_value_probs):
        """ Returns the entropy of and R.V. with probs in list """
        entropy = 0
        for dec_value_prob in dec_value_probs:
            if dec_value_prob != 0:
                entropy += -1 * dec_value_prob * math.log2(dec_value_prob)
        return entropy


    def remainder_calc(self, attribute, examples, dec_value_probs, total_count):
        """ Calculates remainder """
        value = 0

        # Loop over the attribute values
        for att_value in self.att_values[attribute]:
            vals = [0] * len(self.dec_values)
            total = 0

            # 1) Count occurences of specified attribute for each output
            for example in examples:
                if example[self.att_idxs[attribute]] == att_value:
                    for dec_idx, dec_value in enumerate(self.dec_values):
                        if example[-1] == dec_value:
                            vals[dec_idx] += 1
                            total += 1

            # 1.5) Check for dividing by zero
            if total == 0:
                continue

            # 2) Normalize
            probs = [0.0] * len(self.dec_values)
            for i in range(0, len(self.dec_values)):
                probs[i] = vals[i] / total

            # 3) Calculate term for this k
            value += total / total_count * self.b_calc(probs)

        return value

    def write_output(self, fname="dtree.txt"):
        """ Write the output to a file """

        # 1) Open the file for writing
        f = open(fname, "w")

        # 2) Construct the output string (BFS on tree)
        out_str = ""
        open_list = Queue()
        open_list.push(self.dtree)

        while not open_list.is_empty():
            # Grab the next node off of the open list
            curr_node = open_list.pop()

            # If it's an attribute decision, process it
            if len(curr_node.children) > 0:
                # And loop over each of its children
                for child_idx, child in enumerate(curr_node.children):
                    # Printing a line for each child
                    out_str += curr_node.value + "? "
                    out_str += curr_node.edges[child_idx] + ", "
                    out_str += child.value
                    if len(child.children) > 0:
                        out_str += "?"
                    out_str += "\n"

                    # And adding the children that are parents themselves to the open list
                    open_list.push(child)

        # Remove last new line
        # out_str = out_str[:-1]

        # 3) Write to the output file and then close it
        f.write(out_str)
        f.close()




def main():
    """ main function for calling dtree generation algorithm """
    my_dtree = DecisionTree()

    # 1) Read in the input file
    my_dtree.read_dtree_file()

    # 2) Run decision tree learning
    my_dtree.run()

    # 3) Write output file
    my_dtree.write_output()

if __name__ == "__main__":
    main()
