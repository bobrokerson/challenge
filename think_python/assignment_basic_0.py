#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 24 15:20:51 2022

@author: bobrokerson
"""

# Если вы пробежали 10 километров за 42 минуты 42 секунды, каков
# ваш средний темп бега (время, затраченное на преодоление мили, в минутах и секундах)? 
# Какова ваша средняя скорость в милях в час?

from datetime import datetime,timedelta,time


indata = int(input('input data: '))

def calc(x):
    x = x/1.61  
    miles = timedelta(minutes=42,seconds=42) / x
    return miles

print(calc(indata))
