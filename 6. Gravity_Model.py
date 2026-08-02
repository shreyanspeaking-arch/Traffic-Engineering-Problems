print('This program only works for cost function expressed in terms of time')
import pandas as pd
import numpy as np
n=int(input('Enter the no of zones'))
o=int(input('Enter originating zone'))
α=float(input('Enter modal parameter'))
l=[]
for i in range(n):
    k=[np.nan for i in range(4)]
    if o!=i+1:
        print('Enter Generalised Cost in time for zone',i+1)
        k[1]=int(input())
    k[0]=i+1
    print('Enter Productions for zone',i+1)
    k[2]=int(input())
    print('Enter Attractions for zone',i+1)
    k[3]=int(input())
    l+=[k]
print(l)
#breakpoint()
d=pd.DataFrame(l,index=[i for i in range(1,n+1)],columns=['Zone','Generalised Cost','Productions','Attractions'])
d['Impedance of Travel']=d['Generalised Cost']**(-α)
d=d.set_index('Zone')
d['Attractions*Impedance']=d['Attractions']*d['Impedance of Travel']
d['Trips from zone origin to destination']=(d.loc[o,'Productions']*d['Attractions*Impedance'])/np.sum(d['Attractions*Impedance'])
d['Trips from zone origin to destination'].astype(int)
d.to_excel("output.xlsx", index=False)
