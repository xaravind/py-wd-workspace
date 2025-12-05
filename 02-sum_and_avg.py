'''
Author: Vishwas K Singh
Email: vishwas@cloudthat.com
Script to find sum and average of n numbers taken from user
until he enters -999 ( excluding )
'''

total = 0
count = 0
while True:
    num = int(input("Enter the numbers: "))
    if num == -999:
        break
    total += num
    count += 1

print("The sum of 10 numbers is: ", total)
print(f"The average of 10 numbers is: {total/count}")
