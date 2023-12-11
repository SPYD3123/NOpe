import numpy as np
import matplotlib.pyplot as plt
def f(x):
    return -10*np.cos(np.pi*x-2.2) + x*(x+1.5)

x=np.linspace(-5,5,1000)
y=f(x)

optimal_x = x[np.argmin(y)]
optimal_y = min(y)
plt.plot(x,y)
plt.scatter(optimal_x,optimal_y)