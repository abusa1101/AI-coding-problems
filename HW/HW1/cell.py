import sys
import numpy as np

##Prompt/User input
# cell_num = int(input("Enter number of cells in 1dCA: "))
# gen_num = int(input("Enter number of generations to compute: "))

##Initialize cells in generations
cell_list = [0, 1, 1, 0, 1, 1, 1, 0, 0, 0]
cell_num = 10
gen_num = 6
# cell_list = [0] * cell_num
# rand_list = np.random.choice([0, 1], size=len(cell_list) - 2, p=[0.5, 0.5]) #NOT HALF :(
# for i in range(1, len(cell_list) - 1):
#     cell_list[i] = rand_list[i - 1]

##Compute generations
nextgen_cell_list = [0] * cell_num
print(cell_list)

for i in range(gen_num):
    if i != 0:
        print(nextgen_cell_list)
        cell_list = nextgen_cell_list;
    for j in range(1, cell_num - 1):
        # print("main " + str(j) + " " + str(cell_list[j]))
        # print("1: " + str(cell_list))
        if (cell_list[j] == 0):
            # print("pos, val: " + str(j) + " " + str(cell_list[j]))
            # print("j + 1: " + str(j + 1) + " " + str(cell_list[j + 1]))
            # print("j - 1: " + str(j - 1) + " " + str(cell_list[j - 1]))
            if (cell_list[j + 1] == 1) or (cell_list[j - 1] == 1):
                nextgen_cell_list[j] = 1
        else:
            nextgen_cell_list[j] = 0
        # print("2: " + str(cell_list))
        # print("\n")
