#!/usr/bin/env python
# Author: Vishwas K Singh
# Email: vishwas@cloudthat.com

data = [
    ("Vishwas", 95),
    ("Arjun", 88),
    ("Seema", 96),
    ("Raju", 75)
]

sorted_by_score = sorted(data, key=lambda x: x[1])
print(sorted_by_score)