from scipy.optimize import minimize
def f(x):
    return x[0]**2 + x[1]**2
def const(x):
    return x[0]+2*x[1]-3

constraint=({'type':'ineq','fun':const})

initial_guess = [0.0, 0.0]
result=minimize(f,[0,0],constraints=constraint)
print(result)