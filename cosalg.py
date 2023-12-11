from scipy.optimize import minimize
import numpy as np
def f(x):
    return -10*np.cos(np.pi*x-2.2) + x*(x+1.5)

result=minimize(f,[0.0])
print(result)