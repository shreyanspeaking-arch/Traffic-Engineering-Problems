import pandas as pd
import numpy as np
import math as m
statement=''
column=pd.MultiIndex.from_tuples([('Speed Group','Lower Limit'),('Speed Group','Upper Limit')])
df=pd.DataFrame(columns=column)
df=df.set_index([('Speed Group','Lower Limit'),('Speed Group','Upper Limit')])
interval=int(input('Enter interval of speeds'))
print('Enter the speeds one by one per input. You can''t enter multiple values at once')
while statement.upper()!='N':
    s=float(input('Enter Speed'))
    l=m.floor(s)
    rm=l%interval
    l=l-rm
    g=l+interval
    if (l,g) not in df.index:
        df.loc[(l,g),'Observed Vehicles']=1
    else:
        df.loc[(l,g),'Observed Vehicles']+=1
    statement=input('If you have any data to enter, just press enter or anything and when you want to stop type N')
df['Observed Vehicles']=df['Observed Vehicles'].astype(int)
print(df)
    