                EECS 592: Bayes Net Inference (Enumeration-Ask Program)

Based on R&N Figure 14.9

Input:  (1) input.txt- contains Query RV, Evidence vector (RV is short for random variables)
        (2) bn.txt- contains list of RV's, graph edges and probability values for CPT
        (3) parsing_functions.py- contains functions used to parse the input txt files and generate X, e, bn, vars parameters.
        (4) inference_functions.py- contains functions used to run the enumeration-ask algorithm given X, e, bn, vars inputs
        (5) run_inference.py- calls (3) and (4) to output prob distribution Q given the data in (1) and (2)

*Note: Please make sure the input.txt and bn.txt files are formatted EXACTLY as given in the template, to the spaces.
Also, it has been assumed that probabilities in the bn.txt file will be provided to the first decimal place only.

To run program: Run 'run_inference.py' with python3 as follows-> python3 run_inference.py

Output: Q(X) = {True: TrueProbValue, False: FalseProbValue} (for X = query RV)
