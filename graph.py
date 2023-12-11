#ques 2 
from  scipy.optimize import linprog
import numpy as np
import matplotlib.pyplot as plt

z=[-3,-4]
a=[[1,4],[5,2]]
b=[2,4]

result=linprog(z,A_ub=a, b_ub=b,method='highs')
print(result)
x_values=np.linspace(0,10,400)
y_values=np.linspace(0,10,400)

plt.fill_between(x_values,0,(2-x_values)/4 ,where=(2-x_values)/4>=0,color='red',alpha=0.5)
plt.fill_between(x_values,0,(4-5*x_values)/2,where=(4-5*x_values)/2>=0,color='blue',alpha=0.5)
plt.scatter(result.x[0],result.x[1])