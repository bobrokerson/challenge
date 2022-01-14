#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 14 12:10:29 2022

@author: bobrokerson
"""


t = [[1, 2], [3], [4, 5, 6]]


def nested_sum(t):
    count = 0
    for i in t:
        count += sum(i)
    return count
   
print(nested_sum(t))


def cumsum(t):
    total = 0
    res = []
    for i in t:
        total += i
        res.append(total)
    return res   


def middle(t):
    """Returns all but the first and last elements of t.
    t: list
    returns: new list
    """
    return t[0:-1]

print(middle(t))


def chop(t):
    """Removes the first and last elements of t.
    t: list
    returns: None
    """
    del t[0]
    del t[-1]

print(chop(t))


def is_sorted(t):
    """Checks whether a list is sorted.
    t: list
    returns: boolean
    """
    return t == sorted(t)

print(is_sorted(t))

def is_anagram(w1, w2):
    """Checks whether two words are anagrams
    word1: string or list
    word2: string or list
    returns: boolean
    """
    return sorted(w1) == sorted(w2)

print(is_anagram('',''))


def has_duplicates(s):
    """Returns True if any element appears more than once in a sequence.
    s: string or list
    returns: bool
    """
    t = list(s)
    t.sort()

    for i in range(len(t)-1):
        if t[i] == t[i+1]:
            return True
    return False

print(has_duplicates(''))
