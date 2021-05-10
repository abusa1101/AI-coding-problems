import inference_funcs as inf
import parse_funcs as pf

(QUERY, E) = pf.parse_input_file("input.txt")
(VAR, BN) = pf.parse_bn_file("bn.txt")

Q = inf.enum_ask(QUERY, E, BN, VAR)
print(Q)
