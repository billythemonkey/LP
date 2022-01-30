import math
import numpy as np

# x, y, z 
# 4x + 3y + 2z = 25
# -2x + 2y + 3z = -10
# 3x -5y + 2z = -4

a = np.array([[4,3,2],[-2,2,3],[3,-5,2]])

b = np.array([[25],[-10],[-4]])

def solve_linear(a, b):
    x = np.linalg.solve(a,b)
    return x

r = solve_linear(a,b)

print(r)
