import sympy as sp
import numpy as np
import matplotlib.pyplot as plt
import sys
import math as m
K=sp.symbols('K')
print('''Ensure the format of equation is just like the one mentioned.
Otherwise everything will go wrong.''')
V=input('Enter the expression of volume in terms of K in the format a*exp(-(<K>/b))')
V=sp.sympify(V)
Kj=float(input('Enter the maximum traffic density you can think of on this road in veh/km. This estimate how long the speed-density graph will plot'))
Vf=V.subs(K,0)
l1=np.linspace(0,Kj,1000).tolist()
l2=[]
for i in range(1000):
    l2+=[V.subs(K,float(l1[i]))]
V2=V
V=sp.symbols('V')
Q=Kj*V*sp.ln(Vf/V)
dQs=sp.diff(Q,V)
Vo=sp.solve(dQs,V)
for i in Vo:
    Vo=i
sV=sp.solve(V2-Vo,K)

for i in sV:
    Ko=i
print('Capacity of road is ',(Ko*Vo),'veh/h.')
l3=[]
for i in range(1000):
    l3+=[Q.subs(V,float(l2[i]))] 
fig,ax=plt.subplots(2,1,figsize=(9,9))
fig.suptitle("Underwood Model", fontsize=16)
ax[0].plot(l1,l2,color='red')
ax[0].set_title('Speed vs Density Graph')
ax[0].set_xlabel('Traffic Density in veh/km')
ax[0].set_ylabel('Speed in km/h')
ax[0].grid(True,linestyle='--',alpha=0.7)
ax[1].plot(l3,l2,color='blue')
ax[1].set_title('Speed vs Volume Graph')
ax[1].set_xlabel('Volume in veh/h')
ax[1].set_ylabel('Speed in km/h')
ax[1].grid(True,linestyle='--',alpha=0.7)
plt.tight_layout()
plt.show()
