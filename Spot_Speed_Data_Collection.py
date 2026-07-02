import pandas as pd
import numpy as np
import math as m
statement=''
column=pd.MultiIndex.from_tuples([('Speed Group','Lower Limit'),('Speed Group','Upper Limit')])
df=pd.DataFrame(columns=column)
df=df.set_index([('Speed Group','Lower Limit'),('Speed Group','Upper Limit')])
statement2=input('Enter 1 if you want to enter values one by one or 2 if you have the intervals and number of vehicles for each of them')
if int(statement2)==1:
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
elif int(statement2)==2:
    n=int(input('Enter number of datasets'))
    for i in range(n):
        l=int(input('Enter lower limit'))
        g=int(input('Enter upper limit'))
        print('Enter the number of vehicles between speed',l,'and',g)
        df.loc[(l,g),'Observed Vehicles(n)']=int(input())
else:
    print('Wrong input')
    quit()
df['Observed Vehicles(n)']=df['Observed Vehicles(n)'].astype(int)
print(df)
df=df.reset_index()
df['Middle Speed (S)']=(df[('Speed Group','Lower Limit')]+df[('Speed Group','Upper Limit')])/2
df['% Frequency']=(df['Observed Vehicles(n)']/np.sum(df['Observed Vehicles(n)']))*100
df['Cumulative % Frequency']=np.nan
p1=list(df.columns).index(('% Frequency',''))
p2=list(df.columns).index(('Cumulative % Frequency',''))
for i in range(len(df)):
    df.iloc[i,p2]=np.sum(df.iloc[:i+1,p1])
df['nS']=df['Middle Speed (S)']*df['Observed Vehicles(n)']
df['nS²']=df['Observed Vehicles(n)']*((df['Middle Speed (S)'])**2)
df=df.set_index([('Speed Group','Lower Limit'),('Speed Group','Upper Limit')])
print(df)
