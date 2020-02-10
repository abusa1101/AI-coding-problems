import csv

##Functions
def swap_line(arr, pos1, pos2): #swap arr_1 with arr_2
    temp_line = arr[pos1]
    arr[pos1] = arr[pos2]
    arr[pos2] = temp_line

def partition(arr, low_val, high_val):
    pivot = int(arr[high_val][2])
    i = low_val
    for j in range(low_val, high_val):
        if int(arr[j][2]) <= pivot:
            swap_line(arr, i, j) #i with j
            i += 1
    swap_line(arr, i, high_val)
    return i

def quicksort(arr, low_val, high_val):
    if low_val < high_val:
        part_val = partition(arr, low_val, high_val)
        quicksort(arr, low_val, part_val - 1)
        quicksort(arr, part_val + 1, high_val)
    return arr

##Read input from file
UNSORTED_FILE = csv.reader(open("unsorted.txt", "r"))
UNSORTED_LIST = list(UNSORTED_FILE)

##Sort entire input list using Quicksort (lomuto Partition Scheme)
SORTED_LIST = quicksort(UNSORTED_LIST, 0, len(UNSORTED_LIST) - 1)

with open('sorted.txt', 'w') as sorted_f:
    FILE = csv.writer(sorted_f, delimiter=',')
    FILE.writerows(SORTED_LIST)
