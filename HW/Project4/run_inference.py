import inference_functions as inf
import helper_functions as hf

(X, e) = hf.read_input_file("input.txt")
(vars, bn) = hf.read_bn_file("bn.txt")

# print(vars)
Q = inf.enum_ask(X, e, bn, vars)
print(Q)
