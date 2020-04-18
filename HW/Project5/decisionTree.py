import csv

def parse_input_file(file_name): #Parsing mdpinput.txt file
    file = csv.reader(open(file_name, 'r'), delimiter=':', skipinitialspace='True')
    database = list(file)

    for i, line in enumerate(database):
        if '% Decision values' in line[0]:
            dv_idx = i
    for i, line in enumerate(database):
        if i == dv_idx + 1:
            output = line[0].replace(" ","").split(',')
            out1 = output[0]
            out2 = output[1]

    attr_dict = {}
    will_wait = []
    for line in database[1:dv_idx]:
        attr_dict[line[0]] = []
    for line in database[dv_idx + 4:]:
        splitline = line[0].replace(" ","").split(',')
        for i, key in enumerate(attr_dict.keys()):
            attr_dict[key].append(splitline[i])
        will_wait.append(splitline[-1])

    ct1 = will_wait.count(out1)
    ct2 = will_wait.count(out2)
    
############################################
# def learning(examples, attributes, par_examples=()):
#     # if not examples:
#     #     return plurality_value(parent_examples)
#     # else if same_class(examples):
#     #     return classification
#     # else if not attributes:
#     #     return plurality_value(examples)
#     # else:
#     attr = importance(attributes, examples)
#     tree = newDecisionTree(attr,...)
#     for value in attr:
#         exs = ?
#         vk = ?
#         subtree = learning(exs, attributes - attr, examples)
#         tree.add(vk, subtree)
#     return tree
#
# def plurality_value(examples):
#     #check most poupular class in examples?
#     return False
#
# def same_class(examples):
#     class = examples[0][]

parse_input_file('examples.txt')
