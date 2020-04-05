import csv
# import inference as inf

def read_input_file(file_name):
    file = csv.reader(open(file_name, 'r'), skipinitialspace='True')
    input_list = list(file)
    X = input_list[1]
    e = {}
    for evidence in input_list[3]:
        e[evidence[0]] = evidence[2]
    return (X,e)

def read_bn_file(file_name):
    f = open(file_name)
    lines = f.read().split("\n") # Create a list containing all lines
    f.close()

    vars = []
    for var in lines[1]: #create a bn dict with empty entries for [parents] and {probabilities}
        if var != ' ' and var != ',':
            vars.append(var)

    pv_idx = -1 #'% Probability Values' comment index (end of graph edges and start of P values)
    for i, item in enumerate(lines):
        if item == '% Probability values':
            pv_idx = i #idx where Probabilities start next

    p_list = [[],[],[],[],[],[]] #Node, Parent1, T/F1, Parent2, T/F2, Prob(Node | Parents and T/F)
    for i, item in enumerate(lines):
        if i > pv_idx and item:
            p_list[0].append(item[2]) #assign Node
            if item[6].isalpha(): #assign Parent1
                p_list[1].append(item[6])
            else:
                p_list[1].append('') #assign null if no Parent1
            if item[8].isalpha():
                p_list[2].append(item[8]) #assign Parent1 boolean (T/F)
            else:
                p_list[2].append('') #assign null if no Parent1
            if len(item) > 10 and item[10].isalpha():
                p_list[3].append(item[10]) #assign Parent2
            else:
                p_list[3].append('') #assign null if no Parent2
            if len(item) > 10 and item[12].isalpha():
                p_list[4].append(item[12]) #assign Parent2 boolean (T/F)
            else:
                p_list[4].append('') #assign null if no Parent2
            p_list[-1].append(float('0.' + item[-1])) #assign probabilities wrt nodes, parents and boolean values
    bn = {}
    for i in range(len(p_list[0])): #create a bn dict with empty entries for [parents] and {probabilities}
        if not p_list[2][i]:
            p_list[2][i] = 'None'
        if not p_list[4][i]:
            p_list[4][i] = 'None'
        if p_list[0][i] not in bn.keys():
            bn[p_list[0][i]] = [[], {(p_list[2][i], p_list[4][i]):p_list[5][i]}]
        else:
            rep_var = p_list[0][i] #repeated node
            prev_prob_entry = bn[rep_var][1] #previous probability entry
            merged_prob_entry = {(p_list[2][i], p_list[4][i]):p_list[5][i]} #new probability entry
            merged_prob_entry.update(prev_prob_entry) #merge previous and new probability entries
            del bn[rep_var] #delete previous prob entry
            bn[rep_var] = [[], merged_prob_entry] #replace with updated merged entry

    parent_dict = {}
    for var in vars:
        parent_dict[var] = []
    for i in range(3,pv_idx):
        parent_dict[lines[i][3]].append(lines[i][0])
    for var in vars:
        bn[var][0] = parent_dict[var]
    # print(bn)
    return (vars, bn)

(X, e) = read_input_file("input.txt")
(vars, bn) = read_bn_file("bn2.txt")
#
# bn = {'B':[[[],[]],{(None, None):.001}],
#       'E':[[[], []],{(None,None):.002}],
#       'A':[['B','E'],
#                {(False,False):.001,(False,True):.29,
#                 (True,False):.94,(True,True):.95}],
#       'J':[['A'],
#                    {(False,None):.05,(True,None):.90}],
#       'M':[['A'],
#                    {(False,None):.01,(True,None):.70}]}
# vars = ['M','J','A','B','E']

print(X)
print(e)
print(vars)
print(bn)

# print(inf.enumerationAsk(X[0],e,bn,vars))
# enumerationAsk(X, e, bn,vars):
