import inference_functions as inf
import parsing_functions as pf

(X, e) = pf.read_input_file("input.txt")
(vars, bn) = pf.read_bn_file("bn.txt")

Q = inf.enum_ask(X, e, bn, vars)
print(Q)
# print(X)
# print(e)
# print(vars)
# print(bn)
