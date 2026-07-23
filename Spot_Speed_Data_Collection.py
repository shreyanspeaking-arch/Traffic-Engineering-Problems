import pandas as pd
import numpy as np
import math as m
import sys
print('''Enter 1 if you want to enter values one by one (Good for manual counting) or
Enter 2 if you have the intervals and number of vehicles for each of them (For database not yet created) or
Enter 3 if you have a .csv or .xlsx file to import''')  
co=int(input())
if co==1:
    statement=''
    column=['Lower Limit','Upper Limit']
    df=pd.DataFrame(columns=column)
    df=df.set_index(['Lower Limit','Upper Limit'])
    interval=int(input('Enter interval of speeds'))
    while statement.upper()!='N': 
        s=float(input('Enter Speed'))
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
        l=int(input('Enter lower limit'))
        g=int(input('Enter upper limit'))
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
df=df.set_index(['Lower Limit','Upper Limit'])
print(df)
df=df.reset_index()
df.to_excel('output2.xlsx',index=False)
