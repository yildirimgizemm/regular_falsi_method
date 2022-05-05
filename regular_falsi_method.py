# Gizem Yıldırım


import pandas as pd
import math

def RegulaFalsiMethod(x0, x1, e):
    is_true = True
    while is_true:
        x2 = x0 - ((x1-x0) * f(x0))/(f(x1) - f(x0))
        
        if f(x0) * f(x2) < 0:
            x1 = x2
        else:
            x0 = x2

        is_true = abs(f(x2)) > e
    print("Root is:", x2)
    return None




# Function #1

def f(x):
    return 4*(x**5)+10*(x**4)+2*(x**2)-5

# Enter inputs for funtion 1 

x0 = float(input("Lower guess, x0: "))
x1 = float(input("Upper guess, x1: "))
e = float(input("Tolerable error, e: "))

if f(x0) * f(x1) > 0:
    print("Incorrect initial guesses.")
else:
    RegulaFalsiMethod(x0,x1,e)


# ## Input and Output for Function 1
# * Lower guess, x0: -20
# * Upper guess, x1: 20
# * Tolerable error, e: 0.00001
# * Root is: -2.547367011194602




# Function #2
    
def f(x):
    return (x**3)-math.cos(x)

# Enter inputs for funtion 2

x0 = float(input("Lower guess, x0: "))
x1 = float(input("Upper guess, x1: "))
e = float(input("Tolerable error, e: "))

if f(x0) * f(x1) > 0:
    print("Incorrect initial guesses.")
else:
    RegulaFalsiMethod(x0,x1,e)


# ## Input and Output for Function 2
# * Lower guess, x0: 0
# * Upper guess, x1: 1
# * Tolerable error, e: 0.00001
# * Root is: 0.8654734334829766




# Funtion #3
    
def f(x):
    return math.exp(x)-x-2

# Enter inputs for funtion 3

x0 = float(input("Lower guess, x0: "))
x1 = float(input("Upper guess, x1: "))
e = float(input("Tolerable error, e: "))

if f(x0) * f(x1) > 0:
    print("Incorrect initial guesses.")
else:
    RegulaFalsiMethod(x0,x1,e)


# ## Input and Output for Function 3
# * Lower guess, x0: -2.4
# * Upper guess, x1: -1.6
# * Tolerable error, e: 0.00001
# * Root is: -1.8414048042295494
