#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 11 18:44:39 2022

@author: jimmy
"""


# exs 1. Iteration

import math

def mysqrt(a):
    x = a/5
    while True:
        y = (x+ a/x) / 2
        if y == x:
            return x
        x = y
        
def diff(a):
    d = (mysqrt(a)-math.sqrt(a))
    return d
    

def test_square():
    a = 1.0
    print("#", " "*5, 'mysqrt(a)', ' '*6, 'math.sqrt(a)', ' '*6, "diff")
    print("------"*12)
    while a < 10.0:
        
        print(a, "  ", round(mysqrt(a),4), "  "*6, round(math.sqrt(a),4), "  "*8, diff(a))
        a += 1

test_square()

# The first column is a number, a; the second column is the square root of a computed with the function
# from Section 7.5; the third column is the square root computed by math.sqrt; the fourth column is
# the absolute value of the difference between the two estimates.