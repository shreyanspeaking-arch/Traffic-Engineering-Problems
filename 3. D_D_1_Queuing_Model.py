import sympy as sp
import numpy as np
import sys
import matplotlib.pyplot as plt
t=[]
dn=int(input('Enter the number of instances of time in which changes in departure rates (including the start i.e. if it is constant it should be 1 else 1+ no. of changes) is taking place'))
an=int(input('Enter the number of instances of time in which changes in arrival rates (including the start i.e. if it is constant it should be 1 else 1+ no. of changes) is taking place'))
dl=[]
al=[]
for i in range(max([an,dn])):
    if i==0:
        t+=[0]
        print('Initially')
        print('''Press 1 if you have the average headway of vehicles in s
Press 2 if you have the departure rate in veh/min''')
        co1=int(input())
        if co1==1: 
            dl+=[60/(float(input('Enter the initial average headway of vehicles in s')))]
        if co1==2:
            dl+=[float(input('Enter the initial departure rate in veh/min'))]
        al+=[float(input('Enter the initial arrival rate in veh/min'))]
    else:
        print('Enter the time in min when change in either departure or arrival rate takes place for instant ',i+1)
        t+=[float(input())]
        print('Is there any change in departure rate at ',t[i],' min. Enter <Yes> or <No>')
        co2=input()
        if co2.upper()=='YES':
            print('''Press 1 if you have the average headway of vehicles in s
Press 2 if you have the departure rate in veh/min''')
            co3=int(input())
            if co3==1:
                print('Enter the average headway of vehicles in s at time ',t[i],' min') 
                dl+=[60/(float(input()))]
            if co3==2:
                print('Enter the departure rate in veh/min at time ',t[i],'min')
                dl+=[float(input())]
        elif co2.upper()=='NO':
            dl+=[dl[-1]]
        else:
            print('Invalid Input')
            sys.exit()
        print('Is there any change in arrival rate at ',t[i],' min. Enter <Yes> or <No>')
        co4=input()
        if co2.upper()=='NO' and co4.upper()=='NO':
            print('Something might be wrong with your inputs but proceeding with the program unless aborted')
        if co4.upper()=='YES':
            print('Enter the arrival rate in veh/min at time ',t[i],'min')
            al+=[float(input())]
        elif co4.upper()=='NO':
            al+=[al[-1]]
        else:
            print('Invalid Input')
            sys.exit()
T=sp.symbols('T')
vni=int(input('Enter the no. of vehicles just initially in queue when the study was started. If None enter 0'))
lfd=[]
lfa=[]
for i in range(max([an,dn])):
    if i==0:
        fd=vni+(dl[i]*(T-t[i]))
        fa=vni+(al[i]*(T-t[i]))
        lfd+=[fd]
        lfa+=[fa]
    else:
        fd=(lfd[i-1].subs(T,t[i]))+(dl[i]*(T-t[i]))
        fa=(lfa[i-1].subs(T,t[i]))+(al[i]*(T-t[i]))
        lfd+=[fd]
        lfa+=[fa]
QDT=sp.solve(lfd[-1]-lfa[-1],T)[0]
print('Queue Dissipation time is ',QDT,' min.')
t+=[QDT]
NVQ=lfd[-1].subs(T,t[-1])
print('Number of vehicles that have been in queue since the beginning of study is',int(NVQ))
m=[]
P1=[0]
P2=[0]
for i in range(max([an,dn])):
    P1+=[lfd[i].subs(T,t[i+1])]
for i in range(max([an,dn])):
    P2+=[lfa[i].subs(T,t[i+1])]
for i in range(1,len(t)):
    plt.scatter([t[i]],[P1[i]],label=str((t[i],P1[i])))
    plt.scatter([t[i]],[P2[i]],label=str((t[i],P2[i])))
for i in range(max([an,dn])):
    m+=[abs((lfd[i]-lfa[i]).subs(T,t[i+1]))]
print('The maximum queue length is ',int(np.max(m)))
A=[]
for i in range(max([an,dn])):
    A+=[abs(-sp.integrate(lfd[i],(T,t[i],t[i+1]))+sp.integrate(lfa[i],(T,t[i],t[i+1])))]
print('The average delay per vehicle is ',float(np.sum(A)/NVQ),' min')
print('The average queue length of vehicle is ',int(np.sum(A)/QDT),' veh')
for i in range(max([an,dn])):
    x=np.linspace(t[i],t[i+1],1000).tolist()
    y1=[]
    y2=[]
    for j in range(len(x)):
        y1+=[lfd[i].subs(T,x[j])]
    for j in range(len(x)):
        y2+=[lfa[i].subs(T,x[j])]
    if i==0:
        plt.plot(x,y1,color='blue',label='Departure')
        plt.plot(x,y2,color='red',label='Arrival')
    else:
        plt.plot(x,y1,color='blue')
        plt.plot(x,y2,color='red')
plt.title('No. of vehicle vs Time Graph')
plt.xlabel('Time (in min)')
plt.ylabel('No. of vehicles (veh)')
plt.grid(True,alpha=0.7)
plt.legend()
plt.tight_layout()
plt.show()
