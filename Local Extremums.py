from sympy import Symbol, diff , solve
x = Symbol('x')
f=x**3-9*x**2+2
f1=diff(f,x)
f2=diff(f1,x)
sol=solve(f1,x)
for i in sol:
    if f2.subs(x,i)>0:
        print("We get minimum for x=",i)
        print('Minimum =',f.subs(x,i))
    if f2.subs(x,i)<0:
        print("We get maximum for x=",i)
        print('Maximum =',f.subs(x,i))