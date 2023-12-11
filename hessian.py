import sympy as sp
import numpy as np
x1,x2=sp.symbols('x1,x2')
f = 100 * (x2**2 - x1**2)**2 + (1 - x1)**2
grad=[sp.diff(f,x1),(f,x2)]
hessian=sp.hessian(f,(x1,x2))
print(grad)
print(hessian)