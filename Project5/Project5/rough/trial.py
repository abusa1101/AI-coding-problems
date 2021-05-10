from math import log
import numpy as np

# features = {    "alt": {'Yes':[3,3],'No':[3,3]},
#                 "bar": {'Yes':[3,3],'No':[3,3]},
#                 "fri": {'Yes':[2,3],'No':[4,3]},
#                 "hun": {'Yes':[5,2],'No':[1,4]},
#                 "patron": {'None':[0,2],'Some':[4,0],'Full':[2,4]},
#                 "price": {'$':[3,4],'$$':[2,0],'$$$':[1,2]},
#                 "rain": {'Yes':[3,2],'No':[3,4]},
#                 "res": {'Yes':[3,2],'No':[3,4]},
#                 "type": {'French':[1,1],'Thai':[2,2],'Burger':[2,2],'Italian':[1,1]},
#                 "est": {'0-10':[4,2],'10-30':[1,1],'30-60':[1,1],'>60':[0,2]}}


# values = {      "alt": ['Yes','No'], # Yes, No
#                 "bar": ['Yes','No'], # Yes, No
#                 "fri": ['Yes','No'], # Yes, No
#                 "hun": ['Yes','No'], # Yes, No
#                 "patron": ['None','Some','Full'], # Some, Full, None
#                 "price": ['$','$$','$$$'], #$,$$,$$$
#                 "rain": ['Yes', 'No'], # Yes, No
#                 "res": ['Yes', 'No'], # Yes, No
#                 "type": ['French','Thai','Burger','Italian'], #Fren, Thai, Burg, Ital
#                 "est": ['0-10','10-30','30-60','>60']} #0-10, 10-30, 30-60, >60


features = {    "alt": [[3,3], [3,3]], # Yes, No
                "bar": [[3,3], [3,3]], # Yes, No
                "fri": [[2,3], [4,3]], # Yes, No
                "hun": [[5,2], [1,4]], # Yes, No
                "price": [[3,4], [2,0], [1,2]], #$,$$,$$$
                "rain": [[3,2], [3,4]], # Yes, No
                "res": [[3,2], [3,4]], # Yes, No
                "type": [[1,1], [2,2], [2,2], [1,1]], #Fren, Thai, Burg, Ital
                "est": [[4,2], [1,1], [1,1], [0,2]]} #0-10, 10-30, 30-60, >60

[('alt', [[3, 2], [1, 0]]),
('bar', [[2, 1], [2, 1]]),
('fri', [[3, 2], [1, 0]]),
('hun', [[2, 2], [2, 0]]),
('price', [[0, 0], [0, 0], [0, 0]]),
('rain', [[0, 0], [0, 0]]),
('res', [[1, 1], [3, 1]]),
('type', [[0, 0], [0, 0], [0, 0], [0, 0]]),
('est', [[0, 0], [0, 0], [0, 0], [0, 0]])])

def entropy(pi):
    total = 0
    # print(pi)
    for p in pi:
        p = p / sum(pi)
        # print(p)
        if p != 0:
            total += p * log(p, 2)
        else:
            total += 0
    total *= -1
    # print('tot' + str(total))
    return total

def gain(d, a):
    total = 0
    for v in a:
        B = entropy(v)
        total += (sum(v) / sum(d)) * B
    gain = entropy(d) - total
    return gain

def information(features, target):
    args = []
    gains = []
    for key in features.keys():
        print(key)

        args.append(key)
        gains.append(gain(target, features[key]))
    print(gains)
    best_attr = args[np.argmax(gains)]
    return best_attr


print(information(features,[2,4]))
# print(gain([6,6], []))

{'patron': {'None': 'No', 'Some': 'Yes', 'Full':
{'hun': {'Yes':
{'type': {'French': 'pv', 'Thai':
{'fri': {'Yes': 'Yes', 'No': 'No'}}, 'Burger': 'Yes', 'Italian': 'No'}}, 'No': 'No'}}}}
