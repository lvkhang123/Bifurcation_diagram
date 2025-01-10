
"""

Filename: Bifurcation_diagram_of_Rulkov_map_with_the_given_parameters
Name: Khang Ly 
Date: July 8th, 2024
Description: 
    Create the bifurcation diagram of the Rulkov map with the given parameters.
    Plot the bifurcation diagram between sigma vs x and sigma vs y 
    

"""

import time 
import random
import matplotlib.pyplot as plt 
import numpy as np 
from datetime import datetime

# Define a function to clear the data file

def clear_data_file(filename):
    with open(filename, 'w') as file:
        file.truncate()
        
# Define the filename 
filename = 'bifurcation_x_&_y_data.txt'

# Clear the previous data in the file
clear_data_file(filename)

# Create a header in the txt file 

def write_header_to_file(filename, script_name, description, author, date):
    header = f"""
    =====================================
Script Name: {script_name}
Description: {description}
Author: {author}
Date: {date}

This script is to plot the bifurcation diagram of Rulkov map 
with the alpha value of 25.0375, mu value of 0.25, and sigma 
value from -4.8 to -2.1 with 500 bifurcation values. 
=====================================
    """
    with open(filename, 'w') as file:
        file.write(header.strip() + "\n")

# Example usage
def main():
    script_name = 'bifurcation_diagram_of_Rulkov_Map.py'
    description = "Examining the bifurcation diagram of the Rulkov Map, looking for the x and y values"
    author = 'Khang Ly'
    date = datetime.now()

    write_header_to_file(filename, script_name, description, author, date)

if __name__ == "__main__":
    main()


# Set the value of parameters a, sigma (o), and meu (u) 
a = 25.0375
u = 0.25

omin = -4.3
omax = -2.1
bifn = 500

d = np.linspace(omin,omax,bifn*5000)

X = []
Y = []
Q1 = []
Q2 = []
M = []

epsilon = 1e-5

# Give x and y a value as the initial conditions

x = -1.2
y = -3.93

# Start the timer 

start_time = time.time()

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

    for n in range(5000):
      #  print(o,n,x,y)
        x1 = nonlinear_function(a, x, y)
        y1 = y - u*(x+1) + (u*o)
        xpre = xnow
        xnow = x        # Serve as a place holder 
        xnext = x1 
        if (xnext > xnow and xpre > xnow) or (abs(xnow-xpre) < epsilon and abs(xnow - xnext) < epsilon):
       # if x1 == -1:
            Q1.append(x)     # Add each y into the 
            Q2.append(y)
            M.append(o)
        #if abs(xnow-xpre) < epsilon and abs(xnow - xnext) < epsilon:
        X.append(x1)
        Y.append(y1)
    
        x = x1
        y = y1

    # Save the data into a txt file

    coordinate = list(zip([o],[x],[y]))
    for element in coordinate:
        file1 = open("bifurcation_x_&_y_data.txt","a")
        file1.write(f"{element} \n")
        file1.close()

# End the timer 

end_time = time.time()

# Plotting 
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(8, 12))

# Plot for ax1
ax1.plot(d, X, 'bo', label='o vs x', markersize=0.2)
ax1.set_title('Bifurcation Diagram, o vs x')
ax1.set_xlabel('sigma')
ax1.set_ylabel('x values')
ax1.legend()

# Plot for ax2
ax2.plot(d, Y, 'ro', label='o vs y', markersize=0.2)
ax2.set_title('Bifurcation Diagram, o vs y')
ax2.set_xlabel('sigma')
ax2.set_ylabel('y values')
ax2.legend()

plt.tight_layout()
plt.show()

# Show the runtime 

runtime = end_time - start_time 
print(f'Runtime is {runtime} seconds')

