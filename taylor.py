import sympy as sp

x,a=sp.symbols('x a')
f=sp.sin(x)

taylor=sp.series(f,x,a,5)
print(taylor)
print(taylor.subs(a,0))
