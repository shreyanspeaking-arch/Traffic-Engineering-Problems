import pandas as pd
import numpy as np
import datetime as dt
print('Enter the Data for Control-Count Data')
c=['Start Time','End Time','Count']
l1=[]
n1=int(input('Enter the number of datasets collected at control station'))
n=n1
t1=pd.Timestamp(input('Enter start time in the exact format H:M'))
t=t1
f1=pd.Timedelta(input('Enter time interval in the format x hours and/or y minutes'))
f=f1
l=[t]
for i in range (n):
    t+=f
    l.append(t)
for i in range(n):
    l2=[np.nan for j in range(3)]
    l2[0]=l[0].time()
    l2[1]=l[1].time()
    l.pop(0)
    print('Enter vehicle count between',l2[0],'and',l2[1])
    l2[2]=int(input())
    l1+=[l2]
d1=pd.DataFrame(l1,columns=c)
d1=d1.set_index(['Start Time','End Time'])
string1='Proportion of '+str(n)+' Volume'
d1[string1]=d1['Count']/np.sum(d1['Count'])
print(d1)
print('Enter the Data for Coverage-Count Data')
c=['Location','Start Time','End Time','Count']
l1=[]
n2=int(input('Enter the number of coverage stations'))
if n2>=n:
    print('No. of coverage stations should be less than',n)
    f=input('Do you want to proceed Yes/No')
    if f=='Yes':
        n2=int(input('Enter the number of coverage stations'))
        if n2>=n:
            print('Wrong Value')
            quit()
    else:
        quit()
n=n2
t=t1
f=f1
l=[t]
for i in range (n):
    t+=f
    l.append(t)
for i in range(n):
    l2=[np.nan for j in range(4)]
    l2[0]=input('Enter Location Name')
    l2[1]=l[0].time()
    l2[2]=l[1].time()
    l.pop(0)
    print('Enter vehicle count between',l2[1],'and',l2[2],'at location',l2[0])
    l2[3]=int(input())
    l1+=[l2]
d2=pd.DataFrame(l1,columns=c)
d2=d2.set_index(['Start Time','End Time'])
string2='Estimated '+str(n1)+' hour volume'
d2[string2]=d2['Count']/d1[string1].iloc[:len(d2)]
d2['Estimated Peak Hour Volume']=(d2[string2]*np.max(d1[string1])).astype(int)
print(d2)
with pd.ExcelWriter('One_Day_Network_Study_Plan.xlsx') as w:
    d1.to_excel(w,sheet_name='Control_Count_Data',index=False)
    d2.to_excel(w,sheet_name='Coverage_Count_Data',index=False)
