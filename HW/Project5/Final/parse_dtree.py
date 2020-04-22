import csv
from collections import OrderedDict
# from collections import deque

def parse_input_file(file_name): #Parsing mdpinput.txt file
    file = csv.reader(open(file_name, 'r'), skipinitialspace='True')
    database = list(file)

    for i, line in enumerate(database):
        if '% Decision values' in line[0]:
            dv_idx = i
    examples = [line for line in database[dv_idx + 4:]]

    attributes = OrderedDict()
    for line in database[1:dv_idx]:
        split_key = line[0].replace(" ", "").split(':')
        attributes[split_key[0]] = [split_key[1]]
        for i, value in enumerate(line):
            if i != 0:
                attributes[split_key[0]].append(value)

    return examples, attributes

def write_output_file(tree):
    with open('dtree.txt', 'w', newline="") as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(['% Format: decision? value, next node (leaf value or next decision?)'])
        writer.writerow(['% Use question mark and comma markers as indicated below.'])
        writer.writerow([' '])
        for key, value in tree.items():
            writer.writerow([key, value])
        # writer.writerow([' '])
        # writer.writerow(['or as shown below'])
        # writer.writerow([' '])
        # tree_print(tree, writer)


# def bfs(tree, start):
#     visited = set()
#     # parent = {}
#     queue = deque([])
#
#     visited.add(start)
#     queue.append(start)
#     print_list = []
#     while queue:
#         node = queue.popleft()
#         visited.add(node)
#         if node in tree.keys():
#             if isinstance(tree[node], dict):
#                 for child in tree[node]:
#                     # print(node + '?')
#                     print(child)
#                     print_list.append(child)
#                     if child not in visited:
#                         # parent[child] = node
#                         queue.append(child)
#         if node in tree.keys():
#             if isinstance(tree[node], dict):
#                 tree = tree[node]
#             else:
#                 print(tree[node])
#                 print_list.append(tree[node])
#

def tree_print(tree, writer):
    writer.writerow(['attr/value:'])
    writer.writerow(list(tree.keys()))
    for value in tree.values():
        if isinstance(value, dict):
            tree_print(value, writer)
        else:
            writer.writerow(['leaf:'])
            writer.writerow([value])


# tree = {'Pat': {'None': 'No', 'Some': 'Yes',
# 'Full': {'Hun': {'Yes': {'Type': {'French': 'No',
# 'Thai': {'Fri': {'Yes': 'Yes', 'No': 'No'}},
# 'Burger': 'Yes', 'Italian': 'No'}}, 'No': 'No'}}}}
# write_output_file(tree)
