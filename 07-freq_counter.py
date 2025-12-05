#!/usr/bin/env python
# Author: Vishwas K Singh
# Email: vishwas@cloudthat.com
# Frequncy counter
# Example: vishwas
# output: {v:1,i:1,s:2,h:1,w:1,a:1}


# Take the input from the user
inp_str = input("Enter the string: ")

# Define empty dict
freq_counter = {}

for chr in inp_str:
    freq_counter[chr]  = freq_counter.get(chr,0) + 1
    

print(f"{freq_counter}")