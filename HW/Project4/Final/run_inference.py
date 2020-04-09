import inference_funcs as inf
import parse_funcs as pf

(X, e) = pf.parse_input_file("input.txt")
(vars, bn) = pf.parse_bn_file("bn.txt")

Q = inf.enum_ask(X, e, bn, vars)
print(Q)
