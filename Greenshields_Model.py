import sympy as sp
import numpy as np
import matplotlib.pyplot as plt
import sys
K=sp.symbols('K')
print('''Ensure the format of equation is just like the one mentioned.
Otherwise everything will go wrong.''')
V=input('Enter the expression of volume in terms of K in the format a-b<K>')
V=sp.sympify(V)
Vf=V.subs({K:0})
Kjl=sp.solve(V,K)
for i in Kjl:
    Kj=i
l1=np.linspace(0,Kj,1000).tolist()
l2=[]
for i in range(1000):
    l2+=[V.subs(K,float(l1[i]))]
V2=V
V=sp.symbols('V')
Q=(Kj*V)-((Kj/Vf)*(V**2))
dQs=sp.diff(Q,V)
sdQs=sp.solve(dQs,V)
for i in sdQs:
    Vo=i
sV=sp.solve(V2-Vo,K)
for i in sV:
    Ko=i
print('Capacity of road is ',(Ko*Vo),'veh/h.')
l3=[]
for i in range(1000):
    l3+=[Q.subs(V,float(l2[i]))] 
fig,ax=plt.subplots(2,1,figsize=(9,9))
fig.suptitle("Greenshields Model", fontsize=16)
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
