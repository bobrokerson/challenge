#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 12 19:47:35 2022

@author: jimmy
"""

# Task:
# “I was driving on the highway the other day and I happened to notice my odometer.
# Like most odometers, it shows six digits, in whole miles only. So, if my car had 300,000
# miles, for example, I’d see 3-0-0-0-0-0.
# “Now, what I saw that day was very interesting. I noticed that the last 4 digits were
# palindromic; that is, they read the same forward as backward. For example, 5-4-4-5 is a
# palindrome, so my odometer could have read 3-1-5-4-4-5.
# “One mile later, the last 5 numbers were palindromic. For example, it could have read
# 3-6-5-4-5-6. One mile after that, the middle 4 out of 6 numbers were palindromic. And
# you ready for this? One mile later, all 6 were palindromic!
# “The question is, what was on the odometer when I first looked?”

from __future__ import print_function, division


def has_palindrome(i, start, length):
    """Checks if the string representation of i has a palindrome.
    i: integer
    start: where in the string to start
    length: length of the palindrome to check for
    """
    s = str(i)[start:start+length]
    return s[::-1] == s

    
def check(i):
    """Checks if the integer (i) has the desired properties.
    i: int
    """
    return (has_palindrome(i, 2, 4) and
            has_palindrome(i+1, 1, 5) and
            has_palindrome(i+2, 1, 4) and
            has_palindrome(i+3, 0, 6))


def check_all():
    """Enumerate the six-digit numbers and print any winners.
    """
    i = 100000
    while i <= 999996:
        if check(i):
            print(i)
        i = i + 1


print('The following are the possible odometer readings:')
check_all()
print()

# Task:
# “Recently I had a visit with my mom and we realized that the two digits that make
# up my age when reversed resulted in her age. For example, if she’s 73, I’m 37. We
# wondered how often this has happened over the years but we got sidetracked with other
# topics and we never came up with an answer.
# “When I got home I figured out that the digits of our ages have been reversible six times
# so far. I also figured out that if we’re lucky it would happen again in a few years, and
# if we’re really lucky it would happen one more time after that. In other words, it would
# have happened 8 times over all. So the question is, how old am I now?”



def str_fill(i, n):
    """Returns i as a string with at least n digits.
    i: int
    n: int length
    returns: string
    """
    return str(i).zfill(n)


def are_reversed(i, j):
    """Checks if i and j are the reverse of each other.
    i: int
    j: int
    returns:bool
    """
    return str_fill(i, 2) == str_fill(j, 2)[::-1]


def num_instances(diff, flag=False):
    """Counts the number of palindromic ages.
    Returns the number of times the mother and daughter have
    palindromic ages in their lives, given the difference in age.
    diff: int difference in ages
    flag: bool, if True, prints the details
    """
    daughter = 0
    count = 0
    while True:
        mother = daughter + diff

        # assuming that mother and daughter don't have the same birthday,
        # they have two chances per year to have palindromic ages.
        if are_reversed(daughter, mother) or are_reversed(daughter, mother+1):
            count = count + 1
            if flag:
                print(daughter, mother)
        if mother > 120:
            break
        daughter = daughter + 1
    return count
    

def check_diffs():
    """Finds age differences that satisfy the problem.
    Enumerates the possible differences in age between mother
    and daughter, and for each difference, counts the number of times
    over their lives they will have ages that are the reverse of
    each other.
    """
    diff = 10
    while diff < 70:
        n = num_instances(diff)
        if n > 0:
            print(diff, n)
        diff = diff + 1

print('diff  #instances')
check_diffs()

print()
print('daughter  mother')
num_instances(18, True)

