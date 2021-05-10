import random
import numpy as np

##Prompt/User input
CELL_NUM = int(input("Enter number of cells in 1dCA: "))
GEN_NUM = int(input("Enter number of generations to compute: "))

##Initialize cells in generations
CELL_LIST = [0] * CELL_NUM
CELL_NUM_HALF = CELL_NUM / 2
if CELL_NUM_HALF.is_integer() is False:
    CELL_NUM_HALF = np.ceil(CELL_NUM_HALF)
TEMP_LIST = [0] * (CELL_NUM - 2)
TEMP_LIST[0:int(CELL_NUM_HALF)] = [1] * int(CELL_NUM_HALF)
random.shuffle(TEMP_LIST)
for i in range(1, len(CELL_LIST) - 1):
    CELL_LIST[i] = TEMP_LIST[i - 1]

##Initialize next gen and print first gen
NEXTGEN_CELL_LIST = [0] * CELL_NUM
print(str(CELL_LIST)[1:-1])

# CELL_LIST = LIST[i].replace("0", ".")
# CELL_LIST = LIST[i].replace("1", "*")

##Compute next generations (n = GEN_NUM)
for i in range(GEN_NUM):
    if i != 0:
        print(str(NEXTGEN_CELL_LIST)[1:-1])
        CELL_LIST = NEXTGEN_CELL_LIST
        NEXTGEN_CELL_LIST = [0] * CELL_NUM
    for j in range(1, CELL_NUM - 1):
        if CELL_LIST[j] == 0:
            if (CELL_LIST[j + 1] == 1) or (CELL_LIST[j - 1] == 1):
                NEXTGEN_CELL_LIST[j] = 1
            if (CELL_LIST[j + 1] == 1) and (CELL_LIST[j - 1] == 1):
                NEXTGEN_CELL_LIST[j] = 0
        else:
            NEXTGEN_CELL_LIST[j] = 0
