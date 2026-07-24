import pandas as pd
import numpy as np
import math as m
import sys
import scipy.interpolate as scpi
import matplotlib.pyplot as plt
uspeed=input('Enter the units of all speeds that will be entered, and make sure all are the same')
print('''Enter 1 if you want to enter values one by one (Good for manual counting) or
Enter 2 if you have the intervals and number of vehicles for each of them (For database not yet created) or
Enter 3 if you have a .csv or .xlsx file to import''')  
co=int(input())
if co==1:
    co2=1
    statement=''
    column=['Lower Limit','Upper Limit']
    df=pd.DataFrame(columns=column)
    df=df.set_index(['Lower Limit','Upper Limit'])
    interval=int(input('Enter interval of speeds'))
    while statement.upper()!='N':
        print('Enter Dataset ',co2) 
        print('Enter Speed in ',uspeed)
        s=float(input())
        l=m.floor(s)
        rm=l%interval
        l=l-rm
        g=l+interval
        if (l,g) not in df.index:
            df.loc[(l,g),'Observed Vehicles(n)']=1
        else:
            df.loc[(l,g),'Observed Vehicles(n)']+=1
        statement=input('If you have any data to enter, just press enter or anything and when you want to stop type N')
elif co==2:
    column=['Lower Limit','Upper Limit']
    df=pd.DataFrame(columns=column)
    df=df.set_index(['Lower Limit','Upper Limit'])
    n=int(input('Enter number of datasets'))
    for i in range(n):
        print('Enter dataset ',i+1)
        print('Enter lower limit of speed in ',uspeed)
        l=int(input())
        print('Enter upper limit of speed in ',uspeed)
        g=int(input())
        print('Enter the number of vehicles between speed',l,'and',g)
        df.loc[(l,g),'Observed Vehicles(n)']=int(input())
elif co==3:
    print('Make sure that the file that is read is present in the same directory as the program')
    f=input('Enter filename')
    if f[-4:]=='.csv':
        df=pd.read_csv(f)
    elif f[-5:]=='.xlsx':
        df=pd.read_csv(f)
    l=list(df.columns)
    print('The list of columns in this file is ',l)
    if 'Lower Limit' not in l:
        nc=input('Enter the name of the column that contains the lower speed limit for each dataset')
        df=df.rename(columns={nc:'Lower Limit'})
    if 'Upper Limit' not in l:
        nc=input('Enter the name of the column that contains the upper speed limit for each dataset')
        df=df.rename(columns={nc:'Upper Limit'})
    if 'Observed Vehicles(n)' not in l:
        nc=input('Enter the name of the column that contains the number of observed vehicles for each dataset')
        df=df.rename(columns={nc:'Observed Vehicles(n)'})
    df=df.set_index(['Lower Limit','Upper Limit'])
else:
    print('Wrong input')
    sys.exit()
df['Observed Vehicles(n)']=df['Observed Vehicles(n)'].astype(int)
print(df)
df=df.reset_index()
df['Middle Speed (S)']=(df['Lower Limit']+df['Upper Limit'])/2
df['% Frequency']=(df['Observed Vehicles(n)']/np.sum(df['Observed Vehicles(n)']))*100
df['Cumulative % Frequency']=np.nan
p1=list(df.columns).index('% Frequency')
p2=list(df.columns).index('Cumulative % Frequency')
for i in range(len(df)):
    df.iloc[i,p2]=np.sum(df.iloc[:i+1,p1])
df['nS']=df['Middle Speed (S)']*df['Observed Vehicles(n)']
df['nS²']=df['Observed Vehicles(n)']*((df['Middle Speed (S)'])**2)
df2=df.copy()
df2=df2.rename(columns={'Lower Limit':'Lower Limit in '+uspeed,'Upper Limit':'Upper Limit in '+uspeed,'Middle Speed (S)':'Middle Speed (S) in '+uspeed})
df2=df2.set_index(['Lower Limit in '+uspeed,'Upper Limit in '+uspeed,'Middle Speed (S) in '+uspeed])
print(df2)
df2=df2.reset_index()
f2=input('Enter the desired output filename. Dont include .xlsx')
df2.to_excel(f2+'.xlsx',index=False)
l1=df['Middle Speed (S)'].tolist()
l1new=np.linspace(min(l1),max(l1),10000).tolist()
l2=df['% Frequency'].tolist()
spline1=scpi.PchipInterpolator(l1,l2)
l2new=spline1(l1new)
l3=df['Upper Limit'].tolist()
l3new=np.linspace(min(l3),max(l3),10000).tolist()
l4=df['Cumulative % Frequency'].tolist()
spline2=scpi.PchipInterpolator(l3,l4)
l4new=spline2(l3new)
fig,ax=plt.subplots(2,1,figsize=(8,6))
ax[0].scatter(l1,l2,color='red',label='Original Points')
ax[0].plot(l1new,l2new,color='navy',label='Approximate Curve')
ax[0].set_title('% Frequency vs Middle Speed Graph')
ax[0].set_xlabel('Middle Speed in '+uspeed)
ax[0].set_ylabel('% Frequency')
ax[0].grid(True,alpha=0.7,linestyle='--')
ax[0].legend()
ax[1].scatter(l3,l4,color='indigo',label='Original Points')
ax[1].plot(l3new,l4new,color='forestgreen',label='Approximate Curve')
ax[1].set_title('Cumulative % Frequency vs Upper Speed Limit Graph')
ax[1].set_xlabel('Upper Speed Limit in '+uspeed)
ax[1].set_ylabel('Cumulative % Frequency')
ax[1].grid(True,alpha=0.7,linestyle='--')
ax[1].legend()
plt.tight_layout()
plt.show()
