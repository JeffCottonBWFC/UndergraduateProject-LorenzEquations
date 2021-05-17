#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 24 13:52:37 2018

@author: Richard
"""
import math 
import numpy as np
import matplotlib.pyplot as pt

#Lorenz Equation variables
sigma = 10
b = 8/3
r = 50

#Fixed point x_+
x = np.sqrt(b*(r-1))
y = np.sqrt(b*(r-1))
z = r-1

Jacobian = np.array([[-sigma,sigma,0],[r-z,-1,-x],[y,x,-b]])
    
evals = np.linalg.eigvals(Jacobian)

print(evals)

