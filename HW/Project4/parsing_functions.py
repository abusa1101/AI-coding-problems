import csv

def give_bool(bval):
    if bval == 'T':
        bval = True
    elif bval == 'F':
        bval = False
    return bval

def give_pv_idx(lines):
    pv_idx = -1 #'% Probability Values' comment index (end of graph edges and start of P values)
    for i, item in enumerate(lines):
        if item == '% Probability values':
            pv_idx = i #idx where Probabilities start next
    return pv_idx

def give_bn_list(lines, pv_idx):
    vars = []
    p_list = [[], [], [], [], [], []]
    #Node, Parent1, T/F1, Parent2, T/F2, Prob(Node | Parents and T/F)
    for i, item in enumerate(lines):
        if i > pv_idx and item:
            if item[2] not in vars:
                vars.append(item[2])
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
            p_list[-1].append(float('0.' + item[-1]))
            #assign probabilities wrt nodes, parents and boolean values
    vars.reverse()
    return vars, p_list

def give_bn_dict(p_list):
    bayes_net = {}
    for i in range(len(p_list[0])):
        #create bayes_net dict with empty entries for [parents] and {prob}
        if not p_list[2][i]:
            p_list[2][i] = None
        if not p_list[4][i]:
            p_list[4][i] = None
        if p_list[0][i] not in bayes_net.keys():
            bayes_net[p_list[0][i]] = [[], {(give_bool(p_list[2][i]),
                                             give_bool(p_list[4][i])):p_list[5][i]}]
        else:
            rep_var = p_list[0][i] #repeated node
            prev_prob_entry = bayes_net[rep_var][1] #previous probability entry
            merged_prob_entry = {(give_bool(p_list[2][i]),
                                  give_bool(p_list[4][i])):p_list[5][i]} #new prob entry
            merged_prob_entry.update(prev_prob_entry) #merge previous and new prob entries
            del bayes_net[rep_var] #delete previous prob entry
            bayes_net[rep_var] = [[], merged_prob_entry] #replace with updated merged entry
    return bayes_net

def format_bn_dict(lines, bayes_net, vars, pv_idx):
    parent_dict = {}
    for var in vars:
        parent_dict[var] = []
    for i in range(3, pv_idx):
        parent_dict[lines[i][3]].append(lines[i][0])
    for var in vars:
        bayes_net[var][0] = parent_dict[var]
    return bayes_net

def read_input_file(file_name): #Parsing input.txt file
    file = csv.reader(open(file_name, 'r'), skipinitialspace='True')
    input_list = list(file)
    x_var = input_list[1]
    e_dict = {}
    for evidence in input_list[3]:
        e_dict[give_bool(evidence[0])] = give_bool(evidence[2])
    return (x_var[0], e_dict)

def read_bn_file(file_name): #Parsing bayes_net.txt to bayes_net dict
    bn_file = open(file_name)
    lines = bn_file.read().split("\n") # Create a list containing all lines
    bn_file.close()

    pv_idx = give_pv_idx(lines)
    vars, p_list = give_bn_list(lines, pv_idx)
    bayes_net = give_bn_dict(p_list)
    bayes_net = format_bn_dict(lines, bayes_net, vars, pv_idx)
    return vars, bayes_net

# #PROJECT EXAMPLE
# X = 'D'
# e = {'A': True, 'C': False}
# # vars = ['A', 'C', 'B', 'D']
# vars = ['D', 'B', 'C', 'A']
# bayes_net = {'A': [[], {(None,None): 0.4}],
#       'C': [[], {(None,None): 0.7}],
#       'B': [['A'], {(True,None): 0.3, (False,None): 0.9}],
#       'D': [['B', 'C'], {(True,True): 0.1, (True,False): 0.5,
                         # (False,True): 0.3, (False,False): 0.8}]}
