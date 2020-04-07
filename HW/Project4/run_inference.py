import inference_functions as inf
import parsing_functions as pf

(X, e) = pf.read_input_file("input.txt")
(vars, bn) = pf.read_bn_file("bn.txt")

bn = {'A': [[], {(None, None): 0.4}], 'C': [[], {(None, None): 0.7}], 'E': [[], {(None, None): 0.2}], 'B': [['A'], {(True, None): 0.3, (False, None): 0.9}], 'D': [[
'B', 'C', 'E'], {(False, True): 0.3, (False, False): 0.8, (True, False): 0.5, (True, True): 0.1}]}

# Q = inf.enum_ask(X, e, bn, vars)
print(X)
print(e)
print(vars)
print(bn)
