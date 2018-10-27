#!/usr/bin/env bash
'''
Stephen Mandelbaum - 10/8/2018
Random Number Generator used to create passwords
not cryptographically secure
'''
import string as s
import random as r
import time as t
r.seed(t.clock())
characters = s.ascii_letters + s.digits + s.punctuation
def gen(length):
    for i in range(length):
        print(r.choice(characters),end='')
length = int(input("Please enter the length for password generation: "))
gen(length)
