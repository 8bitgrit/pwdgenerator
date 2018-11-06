#!/usr/bin/env bash
'''
Stephen Mandelbaum - 10/8/2018
Random Number Generator used to create passwords
not cryptographically secure
'''
#import string, random and time modules
import string as s
import random as r
import time as t
import sys

#set some variables

r.seed(t.clock())
characters = s.ascii_letters + s.digits + s.punctuation

#define the password generation function
def gen(length):
    for i in range(length):
        print(r.choice(characters),end='')
        r.seed()

while True:
#    try:
    pwd_length = input("Please enter the length for password generation or type (q)uit to exit: ")
#        if pwd_length == 'q':
#            sys.quit()
#        else:
#            pwd_length = int(pwd_length)
#        break
    if pwd_length.lower() == 'q' or pwd_length.lower() == 'quit':
        sys.exit()
    try:
        pwd_length = int(pwd_length)
        break
    except:
        print('You did not enter a valid number')
gen(pwd_length)
print('\n')
