#!/usr/bin/env python
# Author: Vishwas K Singh
# Email: vishwas@cloudthat.com
# Given a string replace the vowels with x
# Example: vishwas k singh
# output: vxshwxs k sxngh

# Take the input string from the user
vowels = 'aeiou'
inp_str = input("Enter the string: ").lower()
inp_lst = list(inp_str)

for idx in range(len(inp_lst)):
    if inp_lst[idx] in vowels:
        inp_lst[idx] = 'x'

output_string = ''.join(inp_lst)
print(f'The processed string is: {output_string}')