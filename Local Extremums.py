from sympy import Symbol, diff, solve, parse_expr

x = Symbol('x')
f_input = input("Enter a function of x: ")
f = parse_expr(f_input)
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
