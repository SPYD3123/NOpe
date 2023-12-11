def f(x):
    return x**2 - 4*x + 4

def f_prime(x):
    return 2*x-4

def f_dp(x):
    return 2

x0=4

tolerance =1e-6

for i in range(100):
    x1=x0-f_prime(x0)/f_dp(x0)
    
    if abs(x1-x0)<tolerance:
        break
    x0=x1

print(x0)

