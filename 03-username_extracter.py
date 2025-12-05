#!/usr/bin/env python
# Author: Vishwas K Singh
# Email: vishwas@cloudthat.com
# Username extracter
# Example: vishwas@cloudthat.com
# Username: vishwas

user_inp = input('Enter the user email: ')
print(f"The extracted username is: {user_inp[:user_inp.find('@')]}")