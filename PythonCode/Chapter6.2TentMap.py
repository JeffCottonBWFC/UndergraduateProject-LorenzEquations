#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb  6 14:19:50 2019

@author: Richard
"""

import numpy as np , matplotlib.pyplot as plt


#Plotting the tent map for report

title_font = {'fontname':'Arial', 'size':'15'}
axis_font = {'fontname':'Arial', 'size':'15'}


MapXValues = [0,0.5,1]
MapYValues = [0,1,0]

LineXValues = [0,1]
LineYValues = [0,1]

#Plots
plt.figure(3)
plt.plot(MapXValues,MapYValues, 'b-')
plt.plot(LineXValues,LineYValues, 'k-')

plt.xlim(0,1)
plt.ylim(0,1)


plt.title('The Tent Map', **title_font)
plt.xlabel(r'$x_{n}$', **axis_font)
plt.ylabel(r'$x_{n+1}$', **axis_font)
