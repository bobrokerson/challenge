#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 10 14:57:38 2022

@author: bobrokerson
"""

# Read about spirals at http://en.wikipedia.org/wiki/Spiral; 
# then write a program that draws an Archimedian spiral (or one of the other kinds).

import turtle


def draw(t, n, length, x, y): #Draws an Archimedian spiral starting at the origin.
    
    theta = 0.0

    for i in range(n):
        t.fd(length)
        dtheta = 1 / (x + y * theta)

        t.lt(dtheta)
        theta += dtheta/2


# create the world and bob
bob = turtle.Turtle()
draw(bob, 1000, 3, 0.1, 0.0002)
 

turtle.mainloop()