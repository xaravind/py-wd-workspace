#!/usr/bin/env python
# Author: Vishwas K Singh
# Email: vishwas@cloudthat.com

import csv

with open("data.csv") as csv_file:
    # reader = csv.reader(csv_file)
    reader = csv.DictReader(csv_file)
    print(type(reader))
    print(reader.fieldnames)
    for row in reader:
        print(row['Name'], row['Email'])
    # for row in reader:
    #     print(row[0],row[1])