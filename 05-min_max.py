#!/usr/bin/env python
# Author: Vishwas K Singh
# Email: vishwas@cloudthat.com
# Script to find 2nd highest & 2nd lowest in a list of numbers

# Take the input of list of numbers, seperated by spaces
numbers = list(map(int,input("Enter list of numbers seperated by spaces: " ).split()))
length_of_list = len(numbers)
numbers.sort()

print(f"The second lowest number is: {numbers[1]}")
print(f"The second highest number is: {numbers[-2]}")