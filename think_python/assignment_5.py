#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 10 14:57:38 2022

@author: bobrokerson
"""

# The time module provides a function, also named time, that returns the current
# Greenwich Mean Time in “the epoch”, which is an arbitrary time used as a reference
# point. On UNIX systems, the epoch is 1 January 1970.
# Write a script that reads the current time and converts it to a time of day in hours,
# minutes, and seconds, plus the number of days since the epoch.

    
import time
import datetime

bo = time.time()

currently = datetime.datetime.now()


day = 24*(60*60)

lenght = bo /day

print(' Time for now:\n', currently)

print(' Period from 01.01.1970:\n', round(lenght),'days')


# Fermat’s Last Theorem says that there are no positive integers a, b, and c 
# such that a**n + b**n = c**n
# for any values of n greater than 2.
# 1.Write a function named check_fermat that takes four parameters—a, b, c and n
# —and checks to see if Fermat’s theorem holds. If n is greater than 2 and
# a**n + b**n = c**n
# the program should print, “Holy smokes, Fermat was wrong!” Otherwise the pro‐
# gram should print, “No, that doesn’t work.”
# 2. Write a function that prompts the user to input values for a, b, c and n, converts
#them to integers, and uses check_fermat to check whether they violate Fermat’s
#theorem.

def check_fermat(a, b, c, n):
    if n > 2 and (a**n + b**n == c**n):
        print("Holy smokes, Fermat was wrong!")
    else:
        print("No, that doesn’t work.")

def check_numb():
    a = int(input("Number for a: "))
    b = int(input("Number for b: "))
    c = int(input("Number for c: "))
    n = int(input("Number for n: "))
    return check_fermat(a, b, c, n)

check_numb()

# ex. 3
import turtle

bob = turtle.Turtle()

def draw(t, length, n):
    if n == 0:
        return
    angle = 50
    t.fd(length*n)
    t.lt(angle)
    draw(t, length, n-1)
    t.rt(2*angle)
    draw(t, length, n-1)
    t.lt(angle)
    t.bk(length*n)
    
def draw_1(t, length, n):
    if n == 0:
        return
    angle = 50
    t.lt(length*n)
    t.lt(angle)
    draw(t, length, n-1)
    t.lt(2*angle)
    draw(t, length, n-1)
    t.fd(angle)
    t.bk(length*n)
    


draw(bob, 20, 5)
draw_1(bob, 20, 5)

turtle.mainloop()