# -*- coding: utf-8 -*-
"""
Created on Fri Jun 23 09:11:28 2017

@author: Bananin
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation


# define the discretization grid
dx = 0.01  # space increment (default 0.1)
dt = 0.01 # time increment  (default 0.01)

tmin =   0.0  # initial time
tmax = 100.0  # final time
xmin =  -3.0  # left bound
xmax =   3.0  # right bound

nx = int((xmax-xmin)/dx) + 1 # number of points on x grid
nt = int((tmax-tmin)/dt) + 2 # number of points on t grid

u = np.zeros((nt,nx)) # solution array

#set initial pulse shape
def init_zero(x):
    return 0

def step_wave(t):
    c = 1.0 # wave speed
    if t<2:
        print( 'stability:', (c*dt/dx)**2 )

        # set initial condition
        for i in range(0,nx):
            u[t,i] = init_zero( xmin + i*dx )
    else:
        # compute second x-derivative using central differences
        ddx = (u[t-1,0:nx-2]-2*u[t-1,1:nx-1]+u[t-1,2:nx])/(dx**2)

        # apply second-order central differences in time
        u[t,1:nx-1] = 2*u[t-1,1:nx-1] - u[t-2,1:nx-1] + (c*dt)**2 * ddx
        #u[t,1]+=np.sin(t)/5

        # apply boundary conditions
        u[t,nx-1] = 0
        if (t-2)/(120/np.pi)<=5*2*np.pi:
            u[t,0]=np.sin((t-2)/(120/np.pi))*0.5
        else: u[t,0] = 0

    l.set_data(np.linspace(xmin,xmax,nx), u[t,:])
    return l,

fig1 = plt.figure()
l, = plt.plot([], [], 'k-')
plt.xlim(xmin, xmax)
plt.ylim(-1.5, 1.5)
plt.xlabel('u')

line_ani = animation.FuncAnimation(fig1, step_wave, nt-1, interval=5, repeat=False, blit=True)
plt.show()