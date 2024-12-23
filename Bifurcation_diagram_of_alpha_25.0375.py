
"""

Filename: Bifurcation_diagram_with_alpha_value_equal_25.0375.py
Name: Khang Ly 
Description: 
    This script creates the bifurcation diagram with the alpha value 
    equal to 25.0375

"""

import random

import matplotlib.pyplot as plt 

# Set the value of parameters a, sigma (o), and meu (u) 
a = 25.0375
o = 0.2
u = 0.25
 
omin = -4.8
omax = -2.1
bifn = 120

X = []
Y = []
Q = []
M = []

epsilon = 1e-5

# Give x and y a value as the initial conditions

x = -1.2
y = -3.93

# Define a function to represent f(x,y)

def nonlinear_function(a,x,y):
    if x <= 0:
        return (a / (1-x)) + y
    elif x < (a+y):
        return (a+y)
    else:
        return -1 
   # return nonlinear_function 
   
# Create a for loop to get rid of the transient
for j in range(bifn):
    o = (((omax - omin)/bifn) * j) + omin
    print(o)
    x = ((random.random()) * 20) - 10
    y = ((random.random()) * 2.5) - 10
    #xpre = x # First point 
    xnow = x # Second point 
    for n in range(20000):      
      #  print(n,x,y)
        #xnow = x 
        x1 = nonlinear_function(a, x, y)
        y1 = y - u*(x+1) + (u*o)
        #xnext = x1   # Last point 
        xpre = xnow
        xnow = x        # Serve as a place holder 
        xnext = x1 
        x = x1
        y = y1
        
            
    
# Create another for loop to plot the map without the transient

    for n in range(2000):
      #  print(o,n,x,y)
        x1 = nonlinear_function(a, x, y)
        y1 = y - u*(x+1) + (u*o)
        xpre = xnow
        xnow = x        # Serve as a place holder 
        xnext = x1 
        if (xnext > xnow and xpre > xnow) or (abs(xnow-xpre) < epsilon and abs(xnow - xnext) < epsilon):
       # if x1 == -1:
            Q.append(x)     # Add each y into the 
            M.append(o)
        #if abs(xnow-xpre) < epsilon and abs(xnow - xnext) < epsilon:
        X.append(x1)
        Y.append(y1)
    
        x = x1
        y = y1

plt.plot(X,',k',alpha=0.25)
plt.xlabel('o')
plt.ylabel('Q')
plt.title('Plot of spike and burst')
plt.show()


