import pandas as pd
import sys
t1=pd.read_csv('Table1.csv')
t2=pd.read_csv('Table2.csv')
t1=t1.rename(columns={'Design speed (mi/h)':'DS','Cj (veh/h)':'Capacity'})
t1=t1.set_index('DS')
t2=t2.rename(columns={'Level of service':'LOS','(v/c) (C70)':70,'(v/c) (C60)':60,'(v/c) (C50)':50})
t2=t2.set_index('LOS')
print('Table containing values of Capacities of Standard Highway Lane in veh/h for different design speeds in mi/h provided by Transportation Research Board')
print(t1)
print('Table containing ratios of flow to capacity for different levels of service and design speed provided by Transportation Research Board')
print(t2)
t2=t2.reset_index()
n=int(input('Enter no. of lanes in highway, total both ways'))
n//=2
V=float(input('Enter Peak Hour Volumne in veh/h'))
PHF=float(input('Enter Peak Hour Factor'))
SF=V/PHF
DS=int(input('Enter Design Speed in mi/h. Only 50,60 and 70 are acceptable'))
if DS not in [i for i in range(50,80,10)]:
    print('Invalid Input')
    sys.exit()
C=t1.loc[DS,'Capacity']
vbc=SF/(C*n)
if vbc>1:
    print('Level of Service(LOS) for this highway is F')
    sys.exit()
l2=list(t2.index)
for i in range(len(list(l2))-2):
    l=float(t2.loc[l2[i],DS])
    u=float(t2.loc[l2[i+1],DS])
    if vbc<=l:
        print('Level of Service(LOS) for this highway is ',t2.loc[l2[i],'LOS'])
        sys.exit()
    elif vbc>l and vbc<u:
        print('Level of Service(LOS) for this highway is ',t2.loc[l2[i+1],'LOS'])
        sys.exit()
