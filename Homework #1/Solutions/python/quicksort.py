""" quicksort - Problem #2

    Matthew Romano
    eecs592
"""

import csv


class Entry:
    """ Class to hold details for each entry """

    def __init__(self, lastname, firstname, grade):
        self.lastname = lastname
        self.firstname = firstname
        self.grade = grade
    def __lt__(self, other): # overload < operator
        return self.grade < other.grade


def partition(entries, low, high):
    """ Partitions entries using the Lomuto partition scheme.

        https://en.wikipedia.org/wiki/Quicksort#Lomuto_partition_scheme
     """

    pivot = entries[high]
    i = low-1
    for j in range(low, high):
        if entries[j] < pivot:
            i += 1
            entries[i], entries[j] = entries[j], entries[i]
    if entries[high] < entries[i+1]:
        entries[high], entries[i+1] = entries[i+1], entries[high]
    return i+1


def quicksort(entries, low, high):
    """ Recursive quicksort function

        Sorts entries from least to greatest between the low and high indices
     """
    if low < high:
        p_index = partition(entries, low, high)
        quicksort(entries, low, p_index-1)
        quicksort(entries, p_index+1, high)


def main():
    """ Main function

        1) Reads in the input file
        2) Calls the quicksort algorithm
        3) Writes the sorted array to an output file
    """

    entries = []

    # 1) Read in the data
    with open('unsorted.txt', 'r') as infile:
        csvreader = csv.reader(infile)
        for line in csvreader:
            lastname = line[0]
            firstname = line[1][1:]
            grade = int(line[2][1:])
            an_entry = Entry(lastname, firstname, grade)
            entries.append(an_entry)

    # 2) Sort the data
    quicksort(entries, 0, len(entries)-1)

    # 3) Write the sorted data to the output file
    with open('sorted.txt', 'w') as outfile:
        for entry in entries:
            outfile.write(entry.lastname + ', ' + entry.firstname + ', ' + str(entry.grade) + '\n')


if __name__ == "__main__":
    main()
