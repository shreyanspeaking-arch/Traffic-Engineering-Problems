import sympy as sp
import numpy as np
import math as m
o=input('Enter the name of Origin')
d=input('Enter the name of Destination')
print('Enter the number of commuters traveling from ',o,' to ',d)
cm=int(input())
print('Enter number of modes of transport from ',o,' to ',d)
n=int(input())
lt=[np.nan for i in range(n)]
lf=[np.nan for i in range(n)]
C,T=sp.symbols('C T')
for i in range(n):
    if i+1==1:
        tt=input('Enter the 1st kind of transport')
    elif i+1==2:
        tt=input('Enter the 2nd kind of transport')
    elif i+1==3:
        tt=input('Enter the 3rd kind of transport')
    else:
        print('Enter the ',i+1,' th kind of transport')
        tt=input()
    print(f'''Enter the Utility function for {tt} in the form of C, which is cost and T, which is travel time, only the expression. 
             Don' t include f(x)= or U=. Make sure to use * for multiplication. Don't write something like 4C-3T. It should be 4*C-3*T''')
    f=input()
    lf[i]=sp.sympify(f)
    lt[i]=tt
print('Make sure that the units of all the values typed henceforth are the same')
le=[np.nan for i in range(n)]
for i in range(n):
    print('Enter cost for ',lt[i])
    c=float(input())
    print('Enter travel time for ',lt[i])
    t=float(input())
    v=lf[i].subs({'C':c,'T':t})
    le[i]=m.exp(v)
s=np.sum(le)
for i in range(n):
    le[i]/=s
for i in range(n):
    print('Probability of people using ',lt[i],' is ',le[i],' and no. of people using it is ',int(le[i]*cm),' between ',o,' and ',d)
