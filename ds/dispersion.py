#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar  4 16:48:21 2022

@author: jimmy
"""

from matplotlib import pyplot as plt

variance = [1,2,4,8,16,32,64,128,256]

bias_squared = [256,128,64,32,16,8,4,2,1] 


total_error = [x+y for x,y in zip(variance,bias_squared)]

xs = [i for i, _ in enumerate(variance)]

print(total_error, xs)

plt.plot(xs, variance, 'd-', color ='green')


plt.plot(xs, bias_squared, 'r-.', color ='green')

plt.plot(xs, total_error, 'b:', color ='blue')

plt.legend(loc = 9)

plt.xlabel("Сложность модели")

plt.title("Комромисс между смещением и дисперсией")

plt.show()
