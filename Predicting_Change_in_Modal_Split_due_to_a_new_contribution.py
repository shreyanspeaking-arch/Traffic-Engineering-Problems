import numpy as np
import sympy as sp
import math as m
o=input('Enter the name of Origin')
d=input('Enter the name of Destination')
print('Enter a Yes or a No')
st=input('Has any kind of new transportation been added/removed?')
if st.upper()=='YES':
    print('Enter number of modes of transport from ',o,' to ',d,' before this project.')
    n=int(input())
    print('Enter number of modes of transport from ',o,' to ',d,' after this project.')
    n2=int(input())
elif st.upper()=='NO':
    print('Enter number of modes of transport from ',o,' to ',d,' before this project.')
    n=int(input())
    n2=n
s=input('What is the infrastructure change that has taken place')
print('Make sure that the units of all the values typed henceforth are the same')
print('Henceforth enter the values for the following parameters before \n',s)
print('Enter the number of commuters traveling from ',o,' to ',d)
cm=int(input())
lt1=[np.nan for i in range(n)]
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
    print('''Enter the Utility function for ',tt,' in the form of C, which is cost and T, which is travel time, only the expression. 
             Don' t include f(x)= or U=. Make sure to use * for multiplication. Don't write something like 4C-3T. It should be 4*C-3*T''')
    f=input()
    lf[i]=sp.sympify(f)
    lt1[i]=tt

le1=[np.nan for i in range(n)]
for i in range(n):
    print('Enter initial cost for ',lt1[i])
    c=float(input())
    print('Enter initial travel time for ',lt1[i])
    t=float(input())
    v=float(lf[i].subs({'C':c,'T':t}))
    le1[i]=m.exp(v)
sl=np.sum(le1)
for i in range(n):
    le1[i]/=sl
print('Before ',s)
for i in range(n):
    print('Probability of people using ',lt1[i],' is ',le1[i],' and no. of people using it is ',int(le1[i]*cm),' between ',o,' and ',d)
print('Henceforth enter the values for the following parameters after \n',s)
lt2=lt1.copy()
if n2>n:
    for i in range(n2-n):
        if n+i+1==1:
            tt=input('Enter the 1st kind of transport')
        elif n+i+1==2:
            tt=input('Enter the 2nd kind of transport')
        elif n+i+1==3:
            tt=input('Enter the 3rd kind of transport')
        else:
            print('Enter the ',i+1,' th kind of transport')
            tt=input()
    print(f'''Enter the Utility function for ,{tt}, in the form of C, which is cost and T, which is travel time, only the expression. 
             Don' t include f(x)= or U=. Make sure to use * for multiplication. Don't write something like 4C-3T. It should be 4*C-3*T''')
    f=input()
    lf+=[sp.sympify(f)]
    lt2+=[tt]
elif n2<n:
    for i in range(n-n2):
        print('Enter the kind of transport removed, case ',i+1)
        tr=input()
        if tr in lt2:
            y=lt2.index(tr)
            lt2.pop(y)
            lf.pop(y)
print('For the same number of commuters i.e. ',cm)
le2=[np.nan for i in range(n2)]
for i in range(n2):
    print('Enter final cost for ',lt2[i])
    c=float(input())
    print('Enter final travel time for ',lt2[i])
    t=float(input())
    v=float(lf[i].subs({'C':c,'T':t}))
    le2[i]=m.exp(v)
print('After ',s)
sl=np.sum(le2)
for i in range(n2):
    le2[i]/=sl
for i in range(n2):
    print('Probability of people using ',lt2[i],' is ',le2[i],' and no. of people using it is ',int(le2[i]*cm),' between ',o,' and ',d)
d1={lt1[i]:int(le1[i]*cm) for i in range(n)}
d2={lt2[i]:int(le2[i]*cm) for i in range(n2)}
for i in d1:
    if i in d2:
        x=d2[i]-d1[i]
        if x>0:
            print('Change in no. of passengers for ',i,' is ',x,' increase.')
        elif x<0:
            print('Change in no. of passengers for ',i,' is ',abs(x),' decrease.')
