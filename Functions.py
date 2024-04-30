# FUNCTIONS SCRIPT

#region: Importing Modules

import collections

#endregion

#region: Defining Prerequisites

# Create a list of nucleotides.
nucs = ["A", "T", "G", "C"]

#endregion

#region: Function 1

# Create a function that takes in a string.
def seq_validator(str):
    # Convert the string to an all-uppercase sequence.
    temp_seq = str.upper()
    # Check if ALL the nucleotides in the all-uppercase sequence are in the list of nucleotides. If true, return the all-uppercase sequence.
    if all(nuc in nucs for nuc in temp_seq):
        return temp_seq
    # If false, return "False".
    else:
        return False

#endregion

#region: Function 2

# Create a function that takes in the all-uppercase sequence returned by Function 1.
def nuc_freq_counter(temp_seq):
    # Create a dictionary with nucleotides as keys and 0s as values.
    temp_freq_dict = {"A": 0, "T": 0, "G": 0, "C": 0}
    # Iterate through every nucleotide in the all-uppercase sequence.
    for nuc in temp_seq:
        # Add the frequency of the corresponding nucleotide to the dictionary.
        temp_freq_dict[nuc] += 1
    # Return the dictionary, which now includes the frequency count of each nucleotide.
    return temp_freq_dict

#endregion

#region: Function 2 (v2)

# Optimize Function 2 using the "collections" module.
def nuc_freq_counter_v2(temp_seq):
    # Use the "Counter" function from "collections" to count the frequency of each nucleotide in the all-uppercase sequence returned by Function 1.
    return dict(collections.Counter(temp_seq))

#endregion