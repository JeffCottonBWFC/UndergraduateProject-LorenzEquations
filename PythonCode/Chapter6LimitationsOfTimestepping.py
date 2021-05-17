#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct  9 12:49:09 2018

@author: Richard
"""

#Calculating the different endpoints for the Lorenz system (RK4 timestepping), using different values of dt (time step width)

# time steps the Lorenz equations
import numpy as np , matplotlib.pyplot as plt , TimesteppingRK4 as ts

# parameters
b = 8/3
r = 28
sigma = 10

dtArray = [0.01, 0.005, 0.002, 0.001]

# time−stepping parameters
tmax = 19 # run to this time 

print(tmax)

for dt in dtArray:
    
    # initial conditions (x Array: 3 position vars)
    t=0

    x=np.array([-10,0,27])

    # number of timesteps taken; initialise to 0
    n=0 

    xValues = [x[0]]
    yValues = [x[1]]
    zValues = [x[2]]
    tValues = [t]


    nsteps = tmax/dt
    while n < nsteps:
        x=ts.step_rk4(x,dt,b,r,sigma)    
    
        xValues = np.append(xValues, x[0])
        yValues = np.append(yValues, x[1])
        zValues = np.append(zValues, x[2])
        tValues = np.append(tValues, t)
    
    
        t = t+dt
        n = n+1
        
    print(dt, x[0], x[1], x[2])

# =============================================================================
# #3D Plot
# fig = plt.figure(1)
# ax = fig.add_subplot(111, projection='3d')
# ax.plot(xValues, yValues, zValues, c= 'red')
# 
# plt.show()
# =============================================================================



# =============================================================================
# #Axes plots against time
# plt.figure(2)
# plt.plot(tValues, xValues, 'r')
# plt.plot(tValues, 0*tValues, 'black')
# plt.ylim(-12,12)
# plt.title(r'Plot of x Values versus Time for $r \rightarrow \infty$')
# plt.xlabel('t')
# plt.ylabel('x(t)')
# 
# plt.figure(3)
# plt.plot(tValues, yValues, 'g')
# plt.plot(tValues, 0*tValues, 'black')
# plt.ylim(-12,12)
# plt.title(r'Plot of y Values versus Time for $r \rightarrow \infty$')
# plt.xlabel('t')
# plt.ylabel('y(t)')
# 
# plt.figure(4)
# plt.plot(tValues, zValues, 'b')
# plt.plot(tValues, 0*tValues, 'black')
# plt.ylim(-12,12)
# plt.title(r'Plot of z Values versus Time for $r \rightarrow \infty$')
# plt.xlabel('t')
# plt.ylabel('z(t)')
# =============================================================================







    





