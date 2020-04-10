import csv

def find(line, letter):
    return [i for i, x in enumerate(line) if x == letter]

def make_bool(line):
    bool_list = []
    for item in line:
        if item == 'T':
            bool_list.append(True)
        elif item == 'F':
            bool_list.append(False)
    return bool_list

def give_bool(bval):
    if bval == 'T':
        bval = True
    elif bval == 'F':
        bval = False
    return bval

def give_prob_val(line):
    res = ''.join(filter(lambda item: item.isdigit(), line))
    dec = res[0] + '.' + res[1:-1] + res[-1]
    return dec

def give_pv_idx(lines):
    pv_idx = -1 #'% Probability Values' comment index (end of graph edges and start of P values)
    for i, item in enumerate(lines):
        if item == '% Probability values':
            pv_idx = i #idx where Probabilities start next
    return pv_idx

def parse_input_file(file_name): #Parsing input.txt file
    file = csv.reader(open(file_name, 'r'), skipinitialspace='True')
    input_list = list(file)
    x_var = input_list[1]
    e_dict = {}
    for evidence in input_list[3]:
        e_dict[give_bool(evidence[0])] = give_bool(evidence[2])
    return (x_var[0], e_dict)

def init_bn(lines):
    #CREATE BN DICT OF REQUIRED SIZE- POPULATE NODES, PARENTS
    pv_idx = give_pv_idx(lines)
    bayes_net = {}
    for i, item in enumerate(lines[1]):
        if item.isalpha():
            bayes_net[item] = [[], [], []]

    for i in range(3, pv_idx):
        bayes_net[lines[i][3]][0].append(lines[i][0])
    return bayes_net, pv_idx

def populate_bn(lines, bayes_net, pv_idx):
    #POPULATE VALUES AND PROBVALS
    vars = []
    prob_vals = []
    idx_list = []
    for i, item in enumerate(lines):
        if i > pv_idx and item:
            if item[2] not in vars:
                vars.append(item[2])
            prob_vals.append(float(give_prob_val(item)))
            idx = find(item, '=')
            idx_list.append(idx[1:-1])
    vars.reverse()

    for i, item in enumerate(idx_list):
        idx_list[i] = [x + 1 for x in item if item]

    values_list = []
    word = ''
    for i, item in enumerate(lines[pv_idx + 1:]):
        if item:
            for _, idx in enumerate(idx_list[i]):
                word = word + item[idx]
            values_list.append(item[2] + word)
            word = ''

    for i, item in enumerate(values_list):
        if item[1:]:
            bayes_net[item[0]][1].append(make_bool(item[1:]))
        else:
            bayes_net[item[0]][1].append(None)
        bayes_net[item[0]][2].append(prob_vals[i])
    return bayes_net, vars

def parse_bn_file(file_name): #Parsing bn.txt to bayes_net dict
    #OPEN FILE
    bn_file = open(file_name)
    lines = bn_file.read().split("\n") # Create a list containing all lines
    bn_file.close()

    bayes_net, pv_idx = init_bn(lines)
    bayes_net, vars = populate_bn(lines, bayes_net, pv_idx)
    return vars, bayes_net
