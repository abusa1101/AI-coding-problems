import parse_dtree as io #manages input/output files
import dtree_funcs as dtree #executes dtree algorithm with given input


EXAMPLES, ATTRIBUTES = io.parse_input_file('examples.txt')
TREE = dtree.dtlearner(False, EXAMPLES, ATTRIBUTES, [])
io.write_output_file(TREE)
print(TREE)
