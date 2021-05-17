#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct  9 12:49:09 2018

@author: Richard
"""

#Plotting for a reduced system of equations to evaluate the efficacy of RK2 and RK4 timestepping schemes

# time steps the Lorenz equations
import numpy as np , matplotlib.pyplot as plt , TimesteppingRK2 as ts, matplotlib.lines as mlines
from mpl_toolkits.mplot3d import Axes3D

# parameters
b = 1
r = 4
sigma = 1


# time−stepping parameters
tmax = 1 # run to this time 

dtArray = [0.001, 0.005, 0.01, 0.05, 0.1]
ErrorArray = []
#X 3D VECTOR!!!
    
for dt in dtArray:
    x=np.array([1,-1,2])
    t=0
    n=0 
    nsteps=tmax/ dt # calculate number of steps
    
    while n < nsteps:
        x=ts.step_rk2(x,dt,b,r,sigma)    
    
        t = t+dt
        n = n+1
    
	#Calculate deviancy from true value
    Error = np.sqrt((x[0] - (1/4*np.e+3/4*np.e**(-3)))**2 + (x[1] - (1/2*np.e-3/2*np.e**(-3)))**2 + (x[2]-2*np.e**(-1))**2)
    ErrorArray.append(Error)

print(dtArray)
print(ErrorArray)

fig=plt.figure()
ax = fig.add_subplot(111)


plt.xlabel(r'$Log(\Delta t)$')
plt.ylabel(r'$Log (E)$')

plt.title('Plot of Error versus Time Increment using RK2')

#Plotting error points
LogdtArray = np.log10(dtArray)
LogErrorArray = np.log10(ErrorArray)

plt.plot(LogdtArray, LogErrorArray, '.', color = 'r')

#Plotting line of best fit for error points
LogdtArrayPrime = LogdtArray[:-1]
LogErrorArrayPrime = LogErrorArray[:-1]

Slope, Intercept = np.polyfit(LogdtArrayPrime, LogErrorArrayPrime, 1)

y_fit = np.exp(Slope * LogdtArray + Intercept)

plt.plot(LogdtArray, np.log(y_fit), "-")

#Legend labels
blue_line = mlines.Line2D([], [], color='blue', marker='.', markersize=0, label='Linear Regression Line')
plt.legend(handles=[blue_line])

print(Slope)

plt.show()
















