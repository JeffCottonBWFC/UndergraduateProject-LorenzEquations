#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 30 18:37:56 2018

@author: Richard
"""

def step_rk2(x,dt,b,r,sigma):
    #Advances the input array x at time t to the returned value x_out at time t+dt
    
    dxdt1 = calc_dxdt(x,b,r,sigma)
    xtemp1 = x+0.5*dt*dxdt1
    dxdt2 = calc_dxdt(xtemp1,b,r,sigma)
    x_out = x+dt*dxdt2
    
    return x_out

def calc_dxdt(x,b,r,sigma):
    #Calculates the vector dx/dt for the Lorenz Equations
    
    dxdt = 0*x
    dxdt[0] = x[1]-x[0]
    dxdt[1] = 4*x[0]-x[1]
    dxdt[2] = -x[2]
    
    return dxdt


