

import numpy as np , matplotlib.pyplot as plt , TimesteppingRK4 as ts


title_font = {'fontname':'Arial', 'size':'15'}
axis_font = {'fontname':'Arial', 'size':'15'}

# parameters
b = 8/3
r = 47
sigma = 10

# time−stepping parameters
tmax = 305 # run to this time 
nsteps = 30501 # number of time steps
dt=tmax/ nsteps # calculate the time step

t=0

x=np.array([20,-10,27])

n=0 

xValues = [x[0]]
yValues = [x[1]]
zValues = [x[2]]
tValues = [t]

maxValuesList = []
plotListXValues = []
plotListYValues = []


while n < nsteps:
    x=ts.step_rk4(x,dt,b,r,sigma)    
    
    xValues = np.append(xValues, x[0])
    yValues = np.append(yValues, x[1])
    zValues = np.append(zValues, x[2])
    tValues = np.append(tValues, t)
    
    
    t = t+dt
    n = n+1
    
xValues = xValues[500:]
yValues = yValues[500:]
zValues = zValues[500:]

#Determines whether the middle point is larger than the two beside it
def maxFinder(left, middle, right):
    if (middle > left) and (middle > right):
        return True
    else:
        return False
    

#Finds all such max values
for i in range(1, 30000):
    if maxFinder(zValues[i-1], zValues[i], zValues[i+1]) == True:
        
        maxValuesList.append(zValues[i])
        

#Creates list of X and Y values
maxValuesListLength = len(maxValuesList)
       
for i in range(1, maxValuesListLength):
    
    plotListXValues.append(maxValuesList[i-1])
    plotListYValues.append(maxValuesList[i])
    
    
    
LineXValues = [50,85]
LineYValues = [50,85]


#Plots
plt.figure(1)
plt.plot(plotListXValues,plotListYValues, 'bo')
plt.plot(LineXValues,LineYValues, 'k-')

#plt.xlim(30,48)
#plt.ylim(30,48)


plt.title('The Lorenz Map', **title_font)
plt.xlabel(r'$z_{n}$', **axis_font)
plt.ylabel(r'$z_{n+1}$', **axis_font)



numbers = []

for i in range(0,150):
    numbers.append(i)

del maxValuesList[150:]

plt.figure(2)
plt.plot(numbers,maxValuesList, 'go-')

plt.title('Maxima Z Values Against Time', **title_font)
plt.xlabel(r'$t$', **axis_font)
plt.ylabel(r'$z_{max}$', **axis_font)











