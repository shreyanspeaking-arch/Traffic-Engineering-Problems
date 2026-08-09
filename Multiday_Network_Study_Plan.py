import pandas as pd
import numpy as np
h=int(input('Enter no of hours counted per day'))
n=int(input('Enter the number of datasets'))
string=str(h)+'-Hour Count(vehs)'
c1=['Day',string]
c2=['Coverage Location','Day',string]
print('Enter Control Count Data as directed')
t1=[np.nan for i in range(n)]
t2=[np.nan for i in range(n)]
l1=[]
for i in range(n):
    print('Dataset ',i+1)
    l=[np.nan for i in range(2)]
    l[0]=pd.to_datetime(input('Enter date in the form of DD/MM/YYYY'),dayfirst=True)
    print('Enter ',string,' on ',l[0].date())
    l[1]=int(input())
    l1+=[l]
d1=pd.DataFrame(l1,columns=c1)
print('Enter Coverage Count Data')
l2=[]
for i in range(n):
    l=[np.nan for i in range(3)]
    print('Dataset ',i+1)
    l[0]=input('Enter coverage location')
    print('Enter ',string,' on ',d1.loc[list(d1.index)[i],'Day'].date(),' at ',l[0])
    l[2]=int(input())
    l2+=[l]
d2=pd.DataFrame(l2,columns=c2)
d2['Day']=d1['Day']
d1=d1.set_index('Day')
d2=d2.set_index('Day')
print('Data for a/an',n,'day study')
print(d1)
print(d2)
d1['Adjustment Factor']=(np.nanmean(d1[string]))/d1[string]
d2['Adjusted '+string]=d2[string]*d1['Adjustment Factor']
d2['Adjusted '+string]=d2['Adjusted '+string].astype('int64')
print('Computation of Adjustment Factors')
print(d1)
print('Adjustment of Coverage Counts')
print(d2)
d2=d2.reset_index()
f=input('Enter output filename for Adjustment of Coverage Counts Table. Exclude .xlsx')
d2.to_excel(f+'.xlsx',index=False)
