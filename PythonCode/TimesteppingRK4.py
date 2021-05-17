#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov  1 12:10:14 2018

@author: Richard
"""

def step_rk4(x,dt,b,r,sigma):
    #Advances the input array x at time t to the returned value x_out at time t+dt
    
    dxdt1 = calc_dxdt(x,b,r,sigma)
    xtemp1 = x + 0.5 * dt*dxdt1
    dxdt2 = calc_dxdt(xtemp1,b,r,sigma)
    xtemp2 = x + 0.5 * dt*dxdt2
    dxdt3 = calc_dxdt(xtemp2,b,r,sigma)
    xtemp3 = x + dt * dxdt3
    dxdt4 = calc_dxdt(xtemp3,b,r,sigma)
    
    x_out = x+dt*(dxdt1+2*(dxdt2+dxdt3)+dxdt4)/6
    
    return x_out

def calc_dxdt(x,b,r,sigma):
    #Calculates the vector dx/dt for the Lorenz Equations
    dxdt = 0*x
    dxdt[0] = sigma*(x[1]-x[0])
    dxdt[1] = r*x[0]-x[1]-x[0]*x[2]
    dxdt[2] = x[0]*x[1]-b*x[2]
    
    return dxdt

