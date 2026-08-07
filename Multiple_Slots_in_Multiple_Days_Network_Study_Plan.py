import pandas as pd
import numpy as np
index=[]
column=[]
d=int(input('Enter number of days'))
s=int(input('Enter number of slots'))
h=0
for i in range(s):
    print('Enter start time for slot ',i+1,'in H:M')
    st=pd.to_datetime(input())
    print('Enter end time for slot ',i+1,' in H:M')
    et=pd.to_datetime(input())
    h+=int((et-st).components.hours)
    string=str(st.time())+' - '+str(et.time())
    column+=[string]
l=[]
string='% of '+str(h)+' hours'
for i in range(d):
    print('Enter the date for day ',i+1,' in DD-MM-YYYY')
    dt=pd.to_datetime(input(),dayfirst=True)
    index+=[(dt,'Count(vehs)'),(dt,string)]
    l1=[np.nan for i in range(s)]
    l2=[np.nan for i in range(s)]
    for i in range(s):
        print('Enter count for slot',column[i])
        l1[i]=int(input())
    l+=[l1,l2]
index=pd.MultiIndex.from_tuples(index)
df=pd.DataFrame(l,columns=column,index=index)
for i in range(1,d*2,2):
    df.iloc[i]=((df.iloc[i-1])/np.sum(df.iloc[i-1]))*100
print('Control data and calibration of hourly variation pattern')
print(df)
df2=df.iloc[::s].copy()
string2=str(h)+'-Hour Control Count Location A (vehs)'
df2[string2]=np.nansum(df2,axis=1)
df2['Adjustment Factor']=np.nanmean(df2[string2])*((df2[string2])**(-1))
print('Calibration of daily variation factors')
print(df2)
index=list(index)
index=index[::s]
index2=[]
for i in list(index):
    t=list(i)
    index2+=[t[0]]*s
column=column*d
l=[]
ts=d*s
for i in range(ts):
    l1=[np.nan for i in range(3)]
    l1[0]=input('Enter Station Name')
    l1[1]=column[i]
    print('Enter count at ',l1[0],' on ',str(index2[i].date()),' between ',column[i])
    l1[2]=int(input())
    l+=[l1]
df3=pd.DataFrame(l,index=index2,columns=['Station Name','Slot','Count'])
df3[str(h)+'-Hour Expanded Count (vehs)']=np.nan
m=list(df3.index)
pos1=list(df3.columns).index(str(h)+'-Hour Expanded Count (vehs)')
for i in range(len(m)):
    a=df3.iloc[i]['Count']
    b=df.loc[(m[i],string),df3.iloc[i]['Slot']]
    df3.iloc[i,pos1]=a/(b/100)
df3[str(h)+'-Hour Adjusted Counts (vehs)']=np.nan
pos1=list(df3.columns).index(str(h)+'-Hour Expanded Count (vehs)')
pos2=list(df3.columns).index(str(h)+'-Hour Adjusted Counts (vehs)')
for i in range(len(m)):
    df3.iloc[i,pos2]=df3.iloc[i,pos1]*df2.loc[m[i],'Adjustment Factor']
print('Expansion and adjustment of coverage counts')
print(df3)

