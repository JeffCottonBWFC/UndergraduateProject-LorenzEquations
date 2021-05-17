#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 14 13:14:04 2019

@author: Richard
"""

import numpy as np , matplotlib.pyplot as plt , TimesteppingRK4 as ts
from mpl_toolkits.mplot3d import Axes3D

#Plotting locations of points which cross through the specified Poincare section and determining which direction the plane is passed

# parameters
b = 8/3
r = 200
sigma = 10

# time−stepping parameters
tmax = 100 # run to this time 
nsteps = 30000 # number of time steps
dt=tmax/ nsteps # calculate the time step

# initial conditions (x Array: 3 position vars)
t=0

x=np.array([1,0,0])

# number of timesteps taken; initialise to 0
n=0 

xValues = [x[0]]
yValues = [x[1]]
zValues = [x[2]]
tValues = [t]

# Storage of coordinates of points where the trajectory passes through the Poincare section
PoincarexUpValues = []
PoincareyUpValues = []

PoincarexDownValues = []
PoincareyDownValues = []

#Selected Poincare section
PoincarePlane = r-1


while n < nsteps:
    xOld = x[0]
    yOld = x[1]
    zOld = x[2]
    
    x=ts.step_rk4(x,dt,b,r,sigma)    
    
    xValues = np.append(xValues, x[0])
    yValues = np.append(yValues, x[1])
    zValues = np.append(zValues, x[2])
    tValues = np.append(tValues, t)
    
    if (zOld - PoincarePlane)*(x[2]-PoincarePlane) < 0:
        
        #Interpolate
        a = (PoincarePlane - zOld)/(x[2] - zOld)
        PCxValue = xOld + a*(x[0] - xOld)
        PCyValue = yOld + a*(x[1] - yOld)
        
        if (zOld - x[2]) < 0:
            PoincarexUpValues.append(PCxValue)
            PoincareyUpValues.append(PCyValue)
        else:
            PoincarexDownValues.append(PCxValue)
            PoincareyDownValues.append(PCyValue)
    
    t = t+dt
    n = n+1
    


plt.figure(1)
 
# Ignore first 10 values as may be affected by IC
PoincarexUpValues = PoincarexUpValues[10:]
PoincareyUpValues = PoincareyUpValues[10:]
PoincarexDownValues = PoincarexDownValues[10:]
PoincareyDownValues = PoincareyDownValues[10:]


plt.plot(PoincarexUpValues,PoincareyUpValues,'r.', markersize=2)
plt.plot(PoincarexDownValues,PoincareyDownValues,'b.', markersize=2)

plt.title(r'Poincare section with the plane $z = r - 1$')
plt.xlabel('x')
plt.ylabel('y')
plt.grid(b=True, which='major', axis='both', color='k', linestyle='-', linewidth=0.5)


plt.show()


#Ignore first 400 (x,y,z) values
xValues = xValues[400:]
yValues = yValues[400:]
zValues = zValues[400:]




fig = plt.figure(2)
ax = fig.add_subplot(111, projection='3d')
ax.set_xlabel('x Axis')
ax.set_ylabel('y Axis')
ax.set_zlabel('z Axis')

ax.view_init(elev = 90., azim = 90)

ax.set_title(r'3D plot with trajectory and Poincaré section')

limit = r

xs = np.linspace(-limit, limit, 10)
ys = np.linspace(-limit, limit, 10)
X, Y = np.meshgrid(xs, ys)
Z = np.zeros_like(X)


# Plot the poincare section
ax.plot(xValues, yValues, zValues, c= 'red')
ax.plot_surface(X,Y,Z+(PoincarePlane), alpha = 0.3)

ax.set_zticks([])

plt.show()
