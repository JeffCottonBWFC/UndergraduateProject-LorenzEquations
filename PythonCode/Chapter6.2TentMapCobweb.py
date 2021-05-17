#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 21 13:32:31 2019

@author: Richard
"""

import numpy as np, matplotlib.pyplot as plt
#Plot of cobweb diagram for the Tent Map

#Initial Variables
n = 20
xinit = 0.151

#Map 
def TentMap(x):
    return min(2*x,2*(1-x))

#Draw Map and line y=x
MapValues = []
xValues = np.linspace(0,1,num = 1000)

for i in xValues:
    MapValues.append(TentMap(i))

plt.figure(1)
plt.plot(xValues,MapValues, c= 'red')
plt.plot([0,1], [0,1] , 'k')

plt.plot([xinit,xinit],[0,xinit],'b')

#Draw cobweb trajectories
x = xinit

for i in range(n):
    y = TentMap(x)
    plt.plot([x,x], [x,y], 'b')
    plt.plot([x,y], [y,y], 'b')
    x = y
    
plt.xlabel('x')
plt.ylabel('y')
plt.title('Cobweb Diagram for the Tent Map')

plt.show()
