#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 13 14:20:15 2022

@author: bobrokerson
"""
# Task:
# Two words “interlock” if taking alternating letters from each forms a new
# word. For example, “shoe” and “cold” interlock to form “schooled.”

# 1. Write a program that finds all pairs of words that interlock. Hint: don’t enumerate all pairs!
# 2. Can you find any words that are three-way interlocked; that is, every third letter forms a
# word, starting from the first, second or third?

from __future__ import print_function, division

from inlist import make_word_list, in_bisect


def interlock(word_list, word):
    """Checks whether a word contains two interleaved words.
    word_list: list of strings
    word: string
    """
    evens = word[::2]
    odds = word[1::2]
    return in_bisect(word_list, evens) and in_bisect(word_list, odds) 
        

def interlock_general(word_list, word, n=3):
    """Checks whether a word contains n interleaved words.
    word_list: list of strings
    word: string
    n: number of interleaved words
    """
    for i in range(n):
        inter = word[i::n]
        if not in_bisect(word_list, inter):
            return False
    return True
        

if __name__ == '__main__':
    word_list = make_word_list()
    
    for word in word_list:
        if interlock(word_list, word):
            print(word, word[::2], word[1::2])

    for word in word_list:
        if interlock_general(word_list, word, 3):
            print(word, word[0::3], word[1::3], word[2::3])
