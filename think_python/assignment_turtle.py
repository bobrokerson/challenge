#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan  9 12:15:56 2022

@author: bobrokerson
"""
# 1(2). Write a function called square that takes a parameter named t, 
#nwhich is a turtle.It should use the turtle to draw a square.
# Write a function call that passes bob as an argument to square, 
# and then run the program again.

# Add another parameter, named length, to square. Modify the body so 
# length of the sides is length, and then modify the function call to 
# provide a second argument. Run the program again. Test your program 
# with a range of values for length.

# 1.1 
import turtle

bob = turtle.Turtle()
length = int(input('number: '))

def square(t):
    for i in range(4):
        t.fd(length) 
        t.lt(90)
        
square(bob)

# 2.2
def square(t, length):
    for i in range(4):
        t.fd(length) 
        t.lt(90)
        
square(bob, 100)

        
# 3. Make a copy of square and change the name to polygon. Add another 
# parameter named n and modify the body so it draws an n-sided regular polygon.        

# 3.1
length = int(input('number: '))
length_1 = int(input('grad: '))

n = 360 / length_1

bob = turtle.Turtle()

def polygon(t):
    for i in range(9):
        t.fd
        t.lt(n)
    
polygon(bob)

# 3.2
def polygon(t, n, length): 
    angle = 360 / n
    for i in range(n): 
        t.fd(length)
        t.lt(angle) 
    
polygon(bob, 9, 70)


# 4 Write a function called circle that takes a turtle, t, and radius, r, as parameters
# and that draws an approximate circle by calling polygon with an appropriate
# length and number of sides. Test your function with a range of values of r

import math

def circle(t, r):
    circumference = 2 * math.pi * r 
    n = 50
    length = circumference / n 
    polygon(t, n, length)


#5 Make a more general version of circle called arc that takes an additional
# parameter angle, which determines what fraction of a circle to draw. angle is in
# units of degrees, so when angle=360, arc should draw a complete circle.

def circle_1(t, r):
    circumference = 2 * math.pi * r 
    n = int(circumference / 3) + 1

    length = circumference / n 
    polygon(t, n, length)

