"""
Author: Andrei Razvan Oproiu
Date: Sun Jan 30 2022
"""
import math
import numpy as np

# Alínea a)

def func(x, tuples,omega = 103, theta = math.pi):
    a, b, c = tuples
    result = a * x + math.sin(b * omega + theta) + math.cos(c * omega + theta)
    return result
    
    

# Alínea b)

def trapz(f,tuple, omega, theta,a, b, N=50):
    x = np.linspace(a, b, N+1)
    y = f(x, tuple, omega, theta)
    y_right = y[1:]
    y_left = y[:-1]
    dx = (b - a) / N
    T = (dx / 2) * np.sum(y_right + y_left)
    return T
    
    


if __name__ == "__main__":
    
    
    
    print(func(3, (1,2,3)))
    print(trapz(func, (1, 2, 3), 100, 27, 0, math.pi))
 