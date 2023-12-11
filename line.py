#ques 1

from scipy.optimize import minimize_scalar
def f(x):
  return x**2 + 2*x + 4

result=minimize_scalar(f)
print(result)