#!/usr/bin/python3
import other_funcs as f
import search_funcs as sf

# board = '000000002100360540000708900040020100060901080002080030004105000058034006200000000'
# board1 = '900760340428500006070084590043206009600053024290400670009047205762305000004020937'

board = f.read_file()
game = list(board)

variables = f.set_variables()
values = f.getDict(variables, board)
# domain = f.set_domain(game, variables)
peers, constraints = f.set_constraints(variables)

solved = sf.AC3(constraints, values, peers)
print(f.solved(values))
f.write_file(values)


# print(values)
