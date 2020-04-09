import csv

def find(s, ch):
    return [i for i, ltr in enumerate(s) if ltr == ch]

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

def read_input_file(file_name): #Parsing input.txt file
    file = csv.reader(open(file_name, 'r'), skipinitialspace='True')
    input_list = list(file)
    x_var = input_list[1]
    e_dict = {}
    for evidence in input_list[3]:
        e_dict[give_bool(evidence[0])] = give_bool(evidence[2])
    return (x_var[0], e_dict)

def read_bn_file(file_name): #Parsing bayes_net.txt to bayes_net dict
    #OPEN FILE
    bn_file = open(file_name)
    lines = bn_file.read().split("\n") # Create a list containing all lines
    bn_file.close()

    #CREATE BN DICT OF REQUIRED SIZE- POPULATE NODES, PARENTS
    pv_idx = give_pv_idx(lines)

    # ct_list = []
    # nodes = ''
    # for node in lines[1]:
    #     if node.isalpha():
    #         nodes = nodes + node
    #         ct_list.append([node, 0])
    #
    # chars = ''
    # for i in range(3, pv_idx):
    #     chars = chars + lines[i][3]
    # for i, item in enumerate(ct_list):
    #     count = chars.count(item[0])
    #     ct_list[i][1] = count

    # values = [[],[]]
    # probval = 1
    # for i, item in enumerate(ct_list):
    #     n = ct_list[i][1]
    #     value_ct =  2**n
    #     if not n:
    #         values[0].append(None)
    #     else:
    #         values[0].append([['Value']*n]*value_ct)
    #     values[1].append(probval)
    # bn = {}
    # for i, item in enumerate(ct_list):
    # 	# bn[ct_list[i][0]] = [[], values[0][i],values[1][i]] #[Parents set], [values set], ProbVal
    #     bn[ct_list[i][0]] = [[], [], []]

    bn = {}
    for i, item in enumerate(lines[1]):
        if item.isalpha():
            bn[item] = [[], [], []]

    for i in range(3, pv_idx):
        bn[lines[i][3]][0].append(lines[i][0])

    #POPULATE VALUES AND PROBVALS
    vars = []
    p_list = [[], [], [], [], [], []]
    ProbVals = []
    ValueOrder = ''
    idx_list = []
    for i, item in enumerate(lines):
        if i > pv_idx and item:
            if item[2] not in vars:
                vars.append(item[2])
            ProbVals.append(float(give_prob_val(item)))
            idx = find(item,'=')
            idx_list.append(idx[1:-1])

    for i, item in enumerate(idx_list):
        idx_list[i] = [x + 1 for x in item if item]

    ValuesList = []
    word = ''
    for i, item in enumerate(lines[pv_idx + 1:]):
        if item:
            for j,idx in enumerate(idx_list[i]):
                word = word + item[idx]
            ValuesList.append(item[2] + word)
            word = ''

    for i, item in enumerate(ValuesList):
        if item[1:]:
            bn[item[0]][1].append(make_bool(item[1:]))
        else:
            bn[item[0]][1].append(None)
        bn[item[0]][2].append(ProbVals[i])

    vars.reverse()
    return vars, bn
