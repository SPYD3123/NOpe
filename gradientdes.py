#Ques 8
import sympy as sp

def f(x):
    return x**2 + 5*x + 6
def f_prime(x):
    return 2*x +5

l_r=0.1
initial_x=0
for i in range(1000):
    gradient = f_prime(initial_x)
    initial_x = initial_x - l_r * gradient
    
print(initial_x)