#!/usr/bin/env python
# Author: Vishwas K Singh
# Email: vishwas@cloudthat.com
# Vowel Frequency Counter

# Take the input from the user
inp_str = input("Enter the string: ").lower()
vowels = 'aeiou'
# Define empty dict
freq_counter = {}

for chr in vowels:
    freq_counter[chr]  = inp_str.count(chr)
    
print(f"{freq_counter}")