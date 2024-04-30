# MAIN SCRIPT

#region: Importing Modules

from Functions import *
import random

#endregion

#region: Main

# Generate 10 random nucleotides.
random_seq = "".join([random.choice(nucs) for nuc in range(50)])

# Validate whether the nucleotides are sequences using Function 1.
seq = seq_validator(random_seq)
print(seq)

# Count and print the frequency of each nucleotide using Function 2.
nuc_freq = nuc_freq_counter(seq)
print(nuc_freq)

#endregion