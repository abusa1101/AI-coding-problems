import inference_funcs as inf
import parse_funcs as pf

(X, e) = pf.read_input_file("input.txt")
(vars, bn) = pf.read_bn_file("bn.txt")

Q = inf.enum_ask(X, e, bn, vars)
print(Q)
