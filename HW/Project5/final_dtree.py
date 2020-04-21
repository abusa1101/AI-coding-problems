from math import log
import numpy as np
import copy
from collections import OrderedDict
# import decisionTree as input

def entropy(pi):
    total = 0
    for p in pi:
        if sum(pi) == 0:
            continue
        p = p / sum(pi)
        if p != 0:
            total += p * log(p, 2)
        else:
            total += 0
    total *= -1
    return total

def gain(d, a):
    total = 0
    # print(d)
    # print(a)
    # print('entr(v):')
    for v in a:
        B = entropy(v)
        # if not B:
        #     return 0
        total += (sum(v) / sum(d)) * B
    # print('entr(d):')
    gain = entropy(d) - total
    # print(entropy(d))
    # print(total)
    # print(gain)
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
        for i, example in enumerate(examples):
            if example[idx] == value:
                # print(value + ' | ' + example[idx])
                if example[-1] == target_decision[0]:
                    target_ct[0] += 1
                elif example[-1] == target_decision[1]:
                    target_ct[1] += 1
        prob_list.append(target_ct)
        target_ct = [0,0]
    return prob_list

def remove_attribute(best_attr, attributes):
    modified_attr = attributes.copy()
    if best_attr in modified_attr.keys():
        del modified_attr[best_attr]
    return modified_attr

def get_prob(trim_idx, attributes, examples):
    decision = []
    decision_set = ()
    for example in examples:
        decision.append(example[-1])
    decision_set = list(set(decision))
    dec1_ct = decision.count(decision_set[0])
    dec2_ct = decision.count(decision_set[1])
    target_decision = [decision_set[0], decision_set[1]]
    target_value = [dec1_ct, dec2_ct]

    features = OrderedDict()
    ex_cpy = examples.copy()

    if trim_idx:
        for i, exs in enumerate(ex_cpy):
            val = exs.pop(trim_idx)

    for idx, attr in enumerate(attributes.keys()):
        features[attr] = get_values(idx, attr, attributes, ex_cpy, target_decision)
    return target_value, features

def get_examples(value, best_attr, attributes, examples):
    for i,attr_key in enumerate(attributes.keys()):
        if attr_key == best_attr:
            idx = i
    value_exs = []
    for example in examples:
        if example[idx] == value:
            value_exs.append(example)
    return value_exs

def plurality_value(examples):
    if examples:
        out = []
        for example in examples:
            for ex in example:
                out.append(ex[-1])
        mode = max(set(out), key=out.count)
        print(out)
        print(mode)
    return mode

def dtlearner(trim_idx, examples, attributes, parent_examples):
    print("enter")
    # print(parent_examples)
    if len(examples) == 0:
        plurality_value(parent_examples)
        return 'pv'
    if same_class(examples) != False:
        return same_class(examples)
    if len(attributes) == 0:
        plurality_value(examples)
        return 'pv'
    parent_examples = examples
    target_value, features = get_prob(trim_idx, attributes, examples)
    best_attr = information(features, target_value)
    tree = {best_attr: {}}
    attr_list = list(attributes.keys())
    trim_idx = attr_list.index(best_attr)
    print(best_attr)
    for value in attributes[best_attr]:
        exs = get_examples(value, best_attr, attributes, examples)
        subtree = dtlearner(trim_idx, exs, remove_attribute(best_attr, attributes), examples)
        tree[best_attr][value] = subtree
        # print(tree)
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

tree = dtlearner(False, examples, attributes, [])
print(tree)
