from math import log
from collections import OrderedDict
import numpy as np


def remove_attribute(best_attr, attributes):
    modified_attr = attributes.copy()
    if best_attr in modified_attr.keys():
        del modified_attr[best_attr]
    return modified_attr

def get_examples(value, best_attr, attributes, examples):
    for i, attr_key in enumerate(attributes.keys()):
        if attr_key == best_attr:
            idx = i
    value_exs = []
    for example in examples:
        if example[idx] == value:
            value_exs.append(example)
    return value_exs

def entropy(prob_k):
    entrpy = 0
    for prob in prob_k:
        if sum(prob_k) == 0:
            continue
        prob = prob / sum(prob_k)
        if prob != 0:
            entrpy += prob * log(prob, 2)
    entrpy *= -1
    return entrpy

def gain(decision, attr):
    remainder = 0
    for value in attr:
        remainder += (sum(value) / sum(decision)) * entropy(value)
    return entropy(decision) - remainder

def get_values(idx, attr_key, attributes, examples, target_decision):
    prob_list = []
    target_ct = [0, 0]
    for value in attributes[attr_key]:
        for _, example in enumerate(examples):
            if example[idx] == value:
                # print(value + ' | ' + example[idx])
                if example[-1] == target_decision[0]:
                    target_ct[0] += 1
                elif example[-1] == target_decision[1]:
                    target_ct[1] += 1
        prob_list.append(target_ct)
        target_ct = [0, 0]
    return prob_list

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
        for _, exs in enumerate(ex_cpy):
            val = exs.pop(trim_idx)

    for idx, attr in enumerate(attributes.keys()):
        features[attr] = get_values(idx, attr, attributes, ex_cpy, target_decision)
    return target_value, features

def information(trim_idx, attributes, examples):
    target_value, features = get_prob(trim_idx, attributes, examples)
    args = []
    gains = []
    for key in features.keys():
        args.append(key)
        gains.append(gain(target_value, features[key]))
    best_attr = args[np.argmax(gains)]
    return best_attr

def same_class(examples):
    is_same = False
    out = []
    for example in examples:
        out.append(example[-1])
    if out.count(out[0]) == len(out):
        is_same = True
        return out[0]
    return is_same

def plurality_value(examples):
    if examples:
        out = []
        for example in examples:
            out.append(example[-1])
        # print(out)
        mode = max(set(out), key=out.count)
    return mode

def dtlearner(trim_idx, examples, attributes, parent_examples):
    if len(examples) == 0:
        return plurality_value(parent_examples)
    if same_class(examples) != False:
        return same_class(examples)
    if len(attributes) == 0:
        return plurality_value(examples)

    parent_examples = examples
    best_attr = information(trim_idx, attributes, examples)
    tree = {best_attr: {}}

    attr_list = list(attributes.keys())
    trim_idx = attr_list.index(best_attr)

    for value in attributes[best_attr]:
        exs = get_examples(value, best_attr, attributes, examples)
        subtree = dtlearner(trim_idx, exs, remove_attribute(best_attr, attributes), examples)
        tree[best_attr][value] = subtree
    return tree
