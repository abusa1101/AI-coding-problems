from math import log
import numpy as np

features = {    "alt": [[3,3], [3,3]], # Yes, No
                "bar": [[3,3], [3,3]], # Yes, No
                "fri": [[2,3], [4,3]], # Yes, No
                "hun": [[5,2], [1,4]], # Yes, No
                "patron": [[0,2], [4,0], [2,4]], # None,Some,Full
                "price": [[3,4], [2,0], [1,2]], #$,$$,$$$
                "rain": [[3,2], [3,4]], # Yes, No
                "res": [[3,2], [3,4]], # Yes, No
                "type": [[1,1], [2,2], [2,2], [1,1]], #Fren, Thai, Burg, Ital
                "est": [[4,2], [1,1], [1,1], [0,2]]} #0-10, 10-30, 30-60, >60

values = {      "alt": ['Yes','No'], # Yes, No
                "bar": ['Yes','No'], # Yes, No
                "fri": ['Yes','No'], # Yes, No
                "hun": ['Yes','No'], # Yes, No
                "patron": ['None','Some','Full'], # Some, Full, None
                "price": ['$','$$','$$$'], #$,$$,$$$
                "rain": ['Yes', 'No'], # Yes, No
                "res": ['Yes', 'No'], # Yes, No
                "type": ['French','Thai','Burger','Italian'], #Fren, Thai, Burg, Ital
                "est": ['0-10','10-30','30-60','>60']} #0-10, 10-30, 30-60, >60

# attributes = ["Alt", "Bar", "Fri", "Hun", "Pat", "Price", "Rain", "Res", "Type", "Est"]


# set of example of the dataset
target = [6, 6] # Yes, No

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

def information(features,target):
    args = []
    gains = []
    for key in features.keys():
        args.append(key)
        gains.append(gain(target, features[key]))
    best_attr = args[np.argmax(gains)]
    return best_attr

# print(information(features,target))

def is_leaf(exs):
    for i, val in enumerate(exs):
        if val == 0:
            if i == 0:
                idx = 1
            else:
                idx = 0
            return True, idx
    return False, -100

def learning(exs, value, temp_example, attr_list, ct): #examples = features,
    ct += 1
    if ct > 10:
        return 'ct exceeded'
    # if not examples:
    #     # return plurality_value(parent_examples)
    #     return 'no examples'
    if exs:
        leaf, idx = is_leaf(exs)
        if leaf:
            if idx == 0:
                classification = 'Yes'
            else:
                classification = 'No'
            return classification
    if len(attr_list) == 0:
        # return plurality_value(examples)
        return 'no attributes'
    best_attr = information(features, target)
    tree = {best_attr: {}}
    new_attrs = [attr for attr in attr_list if attr != best_attr]
    print(new_attrs)
    for i, exs in enumerate(features[best_attr]):
        print(exs)
        vk = values[best_attr][i]
        print(vk)
        subtree = learning(exs, value, temp_example, new_attrs, ct)
        # subtree = 'leaf'
        tree[best_attr][vk] = subtree
        print(tree)
    # for attr_value in best_attr:
    #     exs = ?
    #     vk = ?
    #     subtree = learning(exs, new_attrs, examples)
    #     tree[best_attr][attr_val] = subtree # tree.add(vk, subtree)
    return tree

attr_list = features.keys()
learning(None, None, [], attr_list, 0)

def count_target(dataset, target):
    out1_ct = 0
    out2_ct = 0
    # for each_target in target:
    for items in dataset:
        if items[-1] == target[0]:
            out1_ct += 1
        elif items[-1] == target[1]:
            out2_ct += 1
    return [out1_ct, out2_ct]


def same_leaf(examples, target):
    leaf = ''
    if examples[0][-1] == target[0]:
        leaf = target[0]
    else:
        leaf = target[1]
    return leaf
