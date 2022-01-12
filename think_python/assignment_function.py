#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: bobrokerson
"""
# 1. Write a function named right_justify that takes a string named s as a parameter
# and prints the string with enough leading spaces 
# so that the last letter of the string is in column 70 of the display:
    
def right_justify(s):
    
    print ('Number of chars: ' + str(len(s)))
   
    print (' '* (70 - len(s)) + s)

word = input('Enter word: ')
right_justify(word)
    

# 2. Type this example into a script and test it.
# Modify do_twice so that it takes two arguments, a function object and a value,
# and calls the function twice, passing the value as an argument.
# Copy the definition of print_twice from earlier in this chapter to your script.
# Use the modified version of do_twice to call print_twice twice, passing 'spam'as an argument.
# Define a new function called do_four that takes a function object and a value and
# calls the function four times, passing the value as a paramet

def do_twice(f, y): # Runs a function twice
    f(y)
    f(y)

def print_twice_1(y): # prints the argument twice
    print(y)
    print(y)

def do_four(f, y):
   
    do_twice(f, y)
    do_twice(f, y)

do_twice(print, 'spam')

print('')

do_four(print, 'spam')

# 3. Write a function that draws a grid like the following:
# + - - - - + - - - - +
# |         |         |
# |         |         |
# |         |         |
# |         |         |
# + - - - - + - - - - +
# |         |         |
# |         |         |
# |         |         |
# |         |         |
# + - - - - + - - - - +

def do_twice(f):
    f()
    f()

def do_four(f):
    do_twice(f)
    do_twice(f)

def print_a():
    print('+ - - - -', end=' ')


def print_b():
    print('|        ', end=' ')
    
def print_a1():
    do_twice(print_a)
    print('+')


def print_b1():
    do_twice(print_b)
    print('|')  

def print_almost():
    print_a1()
    do_four(print_b1)
    

def print_out():
    do_twice(print_almost)
    print_a1()
    
print_out()



