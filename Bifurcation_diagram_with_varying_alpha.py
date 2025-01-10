# -*- coding: utf-8 -*-
"""

Filename: Bifurcation_diagram_of_Rulkov_map_with varying_alpha_values.py
Name: Khang Ly 
Date: September 5th, 2024 
Description:
    The script generate a data file with alpha values in respect to the number of iterations 

"""

# Import necessary packages 

import numpy as np

# Define a function to clear data file 

def clear_data_file(filename):
    with open(filename, 'w') as file:
        file.truncate()
        
# Define the filename 
filename = 'bifurcation_x_&_y_data_alpha.txt'

# Clear the previous data in the file
clear_data_file(filename)

# Set the value of parameters sigma (s), and mu (m)

s = 1.0
m = 0.25

# Set the minimum value and maximum value for alpha (a)

amin = 0
amax = 50 

# Se the interval for alpha value 

bifn = 500 

# Create a linear space for the alpha as domain 

d = np.linspace(amin, amax, bifn*5000)

# Create an array for x, y, and alpha 

X  = []
Y  = []
Q1 = []
Q2 = []
M  = []

# An epsilon value to plot the point 

epsilon = 1e-5

# Set the equilibrium point for x and y 

xp = -5.379999999999999
yp = -9.30437304075235 

# Give xi and yi as the initial conditions equal to the equilibrium point 

xi = xp 
yi = yp 

# Define the Rulkov map function 

def nonlinear_function(a, x, y):
    if x <= 0:
        return (a / (1-x)) + y
    elif x < (a+y):
        return (a+y)
    else:
        return -1 
    
# Creeat a for loop to get rid of the transient 
file1 = open("bifurcation_x_&_y_data_alpha.txt","a")
file1.write("Para, Rulkov_x, Rulkov_y\n")
    
# Create a for loop to get rid of the transient 

for j in range(bifn):
    a = (((amax - amin) / bifn) * j) + amin
    print(a)
    
    x = xi 
    y = yi 
    for n in range (2000):
        x1    = nonlinear_function(a, x, y)
        y1    = y - m * (x + 1) + (m * s)
        x     = x1 
        y     = y1 
        

    # Create another for loop to plot the map without the transient 
    for n in range(200):
        x1    = nonlinear_function(a, x, y)
        y1    = y - m * (x + 1) + (m * s)
        x     = x1 
        y     = y1
        
        X.append(x1)
        Y.append(y1)
        
        file1.write(f"{a},{x},{y}\n")
        
    xi = x1
    yi = y1 
    
file1.close()