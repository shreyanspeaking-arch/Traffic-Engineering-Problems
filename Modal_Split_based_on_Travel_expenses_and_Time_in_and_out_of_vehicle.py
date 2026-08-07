import sympy as sp
import numpy as np
import sys
import math as m
print('Make sure all the units for time and cost are taken the same')
ut=input('Enter units for time')
uc=input('Enter currency symbol')
n=int(input('Enter the number of modes of Transport'))
ti,to,te=sp.symbols('ti to te')
l1=[]
l5=[]
l6=[]
for i in range(n):
    print('Enter name of transport ',i+1)
    t=input()
    l1+=[t]
    l2={}
    l3={}
    l4={}
    print('For ',t,''' Enter a function with variables for Time in vehicle <ti>, 
Time out of vehicle <to>, 
Travel Expenses <te> and 
constant <a> (if present). 
Also the coefficient constant A,B and C.
The function should be of the form
U=a+(A*<ti>)+(B*<to>)+(C*<te>).
Don't include the part <U=>''')
    u=input()
    U=sp.sympify(u)
    print('Do you have any cost/time to take as input for ',t,'. If No, enter <No> else press anything/enter')
    s=input()
    while s.upper()!='NO':
        print('''Press 1 for Time in Vehicle
Press 2 for Time out of Vehicle
Press 3 for Travel expenses''')
        n2=input()
        if n2 not in ['1','2','3']:
            print('Invalid Input. Try Again')
        elif int(n2)==1:
            t2=input('What is the time taken for?')
            print('Enter amount of time taken in ',ut)
            l2[t2]=float(input())
        elif int(n2)==2:
            t2=input('What is the time taken for?')
            print('Enter amount of time taken in ',ut)
            l3[t2]=float(input())
        elif int(n2)==3:
            t2=input('What is the cost for')
            print('Enter the cost in ',uc)
            l4[t2]=float(input())
        else:
            print('Invalid Input. Try Again')
        print('Do you have any cost/time to take as input for ',t,'. If No, enter <No> else press anything/enter')
        s=input()
    f=U.subs({ti:np.nansum(list(l2.values())),to:np.nansum(list(l3.values())),te:np.nansum(list(l4.values()))})
    l6+=[f]    
    l5+=[[l2,l3,l4]]
d3=dict(zip(l1,l5))
print(d3)
d1={}
for i in range(len(l1)):
    d1[l1[i]]=m.exp(l6[i])
for i in d1:
    d1[i]/=np.nansum(list(d1.values()))
print('''Press 1 if you have total capacities and 
Press 2 if you have capacities of 1 transport, 
average passengers per vehicle for each kind of transport and
Modal Split Ratio''') 
co=int(input())
if co==1:
    C=int(input('Enter the number of commuters in the particular hour'))
    for i in d1:
        print('''The share of ''',i,''' is ''',d1[i],'''
and it' s capacity is ''',C*d1[i])
elif co==2:
    print('Enter modal split ratio in the format ',':'.join(list(d1.keys())))
    d2={}
    mso=input()
    mso=mso.split(':')
    for i in range(len(mso)):
        mso[i]=float(mso[i])
    d2=dict(zip(list(d1.keys()),mso))
    test=input('Enter the type of transport whose capacity, % average capacity filled, average headway')
    print('Enter average headway for ',test,' in min')
    h=int(input())
    sh=60/h
    print('The number of ',test,' travelling in the hour/peak hour is ',int(sh))
    print('Enter the capacity of ',test,' vehicle.')
    Ctest=int(input())
    print('Enter the average <x>% of capacity of ',test,' vehicle that is filled')
    PCtest=float(input())
    Utest=sh*Ctest*(PCtest/100)
    print('No. of commuters using ',test,' is ',int(Utest))
    for i in d1:
        if i!=test:
            print('No. of commuters using ',i,' is ',int(Utest*(d2[i]/d2[test])))
            print('Enter the statistically computed average no. of persons in a ',i)
            f=float(input())
            print('The total number of ',i,' in the hour/peak hour is ',int((Utest*(d2[i]/d2[test]))/f))
else:
    print('Invalid Input')
    sys.exit()
