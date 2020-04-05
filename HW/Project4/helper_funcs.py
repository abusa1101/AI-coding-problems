import csv
import inference as inf
from collections import Counter

def read_input_file(file_name):
    file = csv.reader(open(file_name, 'r'), skipinitialspace='True')
    in_list = list(file)
    X = in_list[1]
    e = {}
    for evidence in in_list[3]:
        e[evidence[0]] = evidence[2]
    return (X,e)

def read_bn_file(file_name):
    f = open(file_name) # Open file on read mode
    lines = f.read().split("\n") # Create a list containing all lines
    f.close() # Close file

    pv_idx = -1
    for i, item in enumerate(lines):
        if item == '% Probability values':
            pv_idx = i #idx where Probabilities start next

    vars = []
    for var in lines[1]: #create a bn dict with empty entries for [parents] and {probabilities}
        if var != ' ' and var != ',':
            vars.append(var)

    # for i, item in enumerate(lines): #add [parents] to bn from graph edges
    #     if i > 2 and i < pv_idx:
    #         bn[item[3]][0].append(item[0])

    p_list = [[],[],[],[],[],[]] #Node, Parent1, T/F1, Parent2, T/F2, Prob(Node | Parents and T/F)
    for i, item in enumerate(lines):
        if i > pv_idx and item:
            p_list[0].append(item[2])
            if item[6].isalpha():
                p_list[1].append(item[6])
            else:
                p_list[1].append([])
            if item[8].isalpha():
                p_list[2].append(item[8])
            else:
                p_list[2].append([])
            if len(item) > 10 and item[10].isalpha():
                p_list[3].append(item[10])
            else:
                p_list[3].append([])
            if len(item) > 10 and item[12].isalpha():
                p_list[4].append(item[12])
            else:
                p_list[4].append([])
            p_list[-1].append('0.' + item[-1])
    bn2 = {}
    prob = {}
    for i in range(len(p_list[0])): #create a bn dict with empty entries for [parents] and {probabilities}
        if not p_list[2][i]:
            p_list[2][i] = 'None'
        if not p_list[4][i]:
            p_list[4][i] = 'None'
        if p_list[0][i] not in bn2.keys():
            bn2[p_list[0][i]] = [[p_list[1][i], p_list[3][i]], {(p_list[2][i], p_list[4][i]):p_list[5][i]}]
        else:
            temp_var = p_list[0][i]
            temp_dict1 = bn2[p_list[0][i]][1]
            temp_dict2 = {(p_list[2][i], p_list[4][i]):p_list[5][i]}
            temp_dict2.update(temp_dict1)
            del bn2[p_list[0][i]]
            bn2[p_list[0][i]] = [[p_list[1][i], p_list[3][i]], temp_dict2]
    return (vars, bn2)

(X, e) = read_input_file("input2.txt")
vars, bn = read_bn_file("bn2.txt") #vars,bn

print(type(vars))
print(bn)
# print(inf.enumerationAsk(X[0],e,bn,vars))
# enumerationAsk(X, e, bn,vars):
