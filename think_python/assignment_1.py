#!/usr/bin/env python3
# -*- coding: utf-8 -*-

##Created on Sat Jan  8 09:56:19 2022

#@author: bobrokerson

# Exercise from book "Think Python: An Introduction to Software Design"

import math

# 1.simple execute
y = float(input('Data:'))
a = 2**3+8
c = (3-1)**2
result = math.sqrt(a+c)+y
d = math.cos(90)

print(result,d)

# 2. The volume of a sphere with radius r is 4 3πr3
# What is the volume of a sphere with radius 5?

radius=float(input('Input Sphere Radius: '))
pi = math.pi
v=(4/3)*pi*math.pow(radius,3)

print('V Sphere radius %s = %s' %(radius,v))

# 3. Suppose the cover price of a book is $24.95, but bookstores get a 40% discount.
# Shipping costs $3 for the first copy and 75 cents for each additional copy. 
# What is the total wholesale cost for 60 copies?

book_price = 24.95*0.6
ship_1 = 3
ship_2 = 0.75
out = (book_price+ship_1)+(book_price+ship_2)*59

print('Total $', out)
print('Total $', round(out,2))

# If I leave my house at 6:52 am and run 1 mile at an easy pace (8:15 per mile), 
# then 3 miles at tempo (7:12 per mile) and 1 mile at an easy pace again,
# what time do I get home for breakfast?

from datetime import datetime,timedelta,time

st_time = timedelta(hours=6,minutes=52,seconds=00)
way1 = timedelta(hours=0,minutes=8,seconds=15)
way2 = timedelta(hours=0,minutes=7,seconds=12)
way2 *=3
way3 = way1

time_all = way1+way2+way3

time_end = st_time+time_all

print('Time spent on the way = %s, time back home = %s' %(time_all,time_end))
