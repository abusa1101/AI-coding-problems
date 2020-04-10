                EECS 592: Bayes Net Inference (Enumeration-Ask Program)

Based on R&N Figure 14.9
(RV is short for random variables)

Input:  (1) input.txt-          Contains Query RV, Evidence vector.
        (2) bn.txt-             Contains list of RV's, graph edges and probability values
                                for CPT.
        (3) parse_funcs.py-     Contains functions used to parse the input txt files and
                                generate X, e, bn, vars parameters.
        (4) inference_funcs.py- Contains functions used to run the enumeration-ask
                                algorithm given X, e, bn, vars inputs.
        (5) run_inference.py-   Calls (3) and (4) to output prob distribution Q given
                                the data in (1) and (2).

        *Note: Please make sure the input.txt and bn.txt files are formatted as given in
               the template, to the spaces (because program is parsing Probability values
               character by character).

To run program: (1) Enter filenames as required (default- 'bn.txt', 'input.txt')
                (2) Run 'run_inference.py' with python3 as follows,

                    python3 run_inference.py

Output: (1) Q(X) = {True: TrueProbValue, False: FalseProbValue} (for X = Query RV)
