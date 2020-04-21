from math import log
import numpy as np
import copy
# import decisionTree as input

def entropy(pi):
    # entropy(p) = − SUM (Pi * log(Pi) )
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
    total = 0
    for v in a:
        total += sum(v) / sum(d) * entropy(v)
    gain = entropy(d) - total
    return gain

def information(features, target):
    args = []
    gains = []
    for key in features.keys():
        args.append(key)
        gains.append(gain(target, features[key]))
    best_attr = args[np.argmax(gains)]
    return best_attr

def same_class(examples):
    is_same = False
    out = []
    for example in examples:
        out.append(example[-1])
    # print(out.count(out[1]))
    if out.count(out[0]) == len(out):
        is_same = True
        return out[0]
    return is_same

def get_values(idx, attr_key, attributes, examples, target_decision):
    prob_list = []
    target_ct = [0,0]
    for value in attributes[attr_key]:
        for example in examples:
            if example[idx] == value:
                if example[-1] == target_decision[0]:
                    target_ct[0] += 1
                elif example[-1] == target_decision[1]:
                    target_ct[1] += 1
        prob_list.append(target_ct)
        target_ct = [0,0]
    return prob_list

def get_prob(attributes, examples):
    decision = []
    decision_set = ()
    for example in examples:
        decision.append(example[-1])
    decision_set = list(set(decision))
    dec1_ct = decision.count(decision_set[0])
    dec2_ct = decision.count(decision_set[1])
    target_decision = [decision_set[0], decision_set[1]]
    target_value = [dec1_ct, dec2_ct]

    features = {}
    for idx, attr in enumerate(attributes.keys()):
        features[attr] = get_values(idx, attr, attributes, examples, target_decision)
    # print(features)
    return target_value, features

def remove_attribute(A, attributes):
    modified_attr = attributes.copy()

    return modified_attr

def dtlearner(examples, attributes, parent_examples=()):
    if len(examples) == 0:
        return 'pv'
    if same_class(examples) != False:
        return same_class(examples)
    if len(attributes) == 0:
        return 'pv'

    target_value, features = get_prob(attributes, examples)
    best_attr = information(features, target_value)
    tree = {best_attr: {}}
    print(tree)
    # print(zed_leppelin)
    for value in attributes[best_attr]:
        subtree = dtlearner(exs, remove_attribute(A, attributes), examples)
        subtree = 'leaf'
        tree[best_attr][value] = subtree
    print(tree)
    return tree

examples = [['Yes', 'No', 'No', 'Yes', 'Some', '$$$', 'No', 'Yes', 'French', '0-10', 'Yes'],
            ['Yes', 'No', 'No', 'Yes', 'Full', '$', 'No', 'No', 'Thai', '30-60', 'No'],
            ['No', 'Yes','No', 'No', 'Some', '$', 'No', 'No', 'Burger', '0-10', 'Yes'],
            ['Yes', 'No', 'Yes', 'Yes', 'Full', '$', 'Yes', 'No', 'Thai', '10-30', 'Yes'],
            ['Yes', 'No', 'Yes', 'No', 'Full', '$$$', 'No', 'Yes', 'French', '>60', 'No'],
            ['No', 'Yes', 'No', 'Yes', 'Some', '$$', 'Yes', 'Yes', 'Italian', '0-10', 'Yes'],
            ['No', 'Yes', 'No', 'No', 'None', '$', 'Yes', 'No', 'Burger', '0-10', 'No'],
            ['No', 'No', 'No', 'Yes', 'Some', '$$', 'Yes', 'Yes', 'Thai', '0-10', 'Yes'],
            ['No', 'Yes', 'Yes', 'No', 'Full', '$', 'Yes', 'No', 'Burger', '>60', 'No'],
            ['Yes', 'Yes', 'Yes', 'Yes', 'Full', '$$$', 'No', 'Yes', 'Italian', '10-30', 'No'],
            ['No', 'No', 'No', 'No', 'None', '$', 'No', 'No', 'Thai', '0-10', 'No'],
            ['Yes', 'Yes', 'Yes', 'Yes', 'Full', '$', 'No', 'No', 'Burger', '30-60', 'Yes']]

attributes = {  "alt": ['Yes','No'], # Yes, No
                "bar": ['Yes','No'], # Yes, No
                "fri": ['Yes','No'], # Yes, No
                "hun": ['Yes','No'], # Yes, No
                "patron": ['None','Some','Full'], # Some, Full, None
                "price": ['$','$$','$$$'], #$,$$,$$$
                "rain": ['Yes', 'No'], # Yes, No
                "res": ['Yes', 'No'], # Yes, No
                "type": ['French','Thai','Burger','Italian'], #Fren, Thai, Burg, Ital
                "est": ['0-10','10-30','30-60','>60']} #0-10, 10-30, 30-60, >60

target = ['Yes', 'No']

dtlearner(examples, attributes, parent_examples=())
