#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 15 16:59:47 2022

@author: jimmy
"""

# task_1
from __future__ import print_function, division


def invert_dict(d):
    """Inverts a dictionary, returning a map from val to a list of keys.
    If the mapping key->val appears in d, then in the new dictionary
    val maps to a list that includes key.
    d: dict
    Returns: dict
    """
    inverse = {}
    for key in d:
        val = d[key]
        inverse.setdefault(val, []).append(key)
    return inverse


if __name__ == '__main__':
    d = dict(a=1, b=2, c=3, z=1)
    inverse = invert_dict(d)
    for val in inverse:
        keys = inverse[val]
        print(val, keys)
        

# task_2

cache = {}

def ackermann(m, n):
    """Computes the Ackermann function A(m, n)
    See http://en.wikipedia.org/wiki/Ackermann_function
    n, m: non-negative integers
    """
    if m == 0:
        return n+1
    if n == 0:
        return ackermann(m-1, 1)

    if (m, n) in cache:
        return cache[m, n]
    else:
        cache[m, n] = ackermann(m-1, ackermann(m, n-1))
        return cache[m, n]


print(ackermann(3, 4))
print(ackermann(3, 6))



# task_3
def has_duplicates(t):
    """Checks whether any element appears more than once in a sequence.
    Simple version using a for loop.
    t: sequence
    """
    d = {}
    for x in t:
        if x in d:
            return True
        d[x] = True
    return False


def has_duplicates2(t):
    """Checks whether any element appears more than once in a sequence.
    Faster version using a set.
    t: sequence
    """
    return len(set(t)) < len(t)


if __name__ == '__main__':
    t = [1, 2, 3]
    print(has_duplicates(t))
    t.append(1)
    print(has_duplicates(t))

    t = [1, 2, 3]
    print(has_duplicates2(t))
    t.append(1)
    print(has_duplicates2(t))