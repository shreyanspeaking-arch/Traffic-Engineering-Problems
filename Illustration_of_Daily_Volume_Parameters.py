import pandas as pd
import numpy as np
import sys
import matplotlib.pyplot as plt
print('''Press 1 if you have a CSV file containing dates and daily vehicle volumes or
Press 2 if you want to enter values manually''')
co=int(input())
if co==1:
    f=input('Enter filename')
    if f[-4:]=='.csv':
        df1=pd.read_csv(f)
    elif f[-5:]=='.xlsx':
        df1=pd.read_excel(f)
    else:
        print('Enter only csv or excel file')
        sys.exit()
    l=list(df1.columns)
    print(l)
    if 'Date' not in l:
        c=input('Enter the name of the column containing the dates')
        df1=df1.rename(columns={c:'Date'})
    if 'Vehicular Volume' not in l:
        c=input('Enter the name of the column containing the vehicular volume in these dates')
        df1=df1.rename(columns={c:'Vehicular Volume'}) 
elif co==2:
    co2='YES'
    l=[]
    while co2.upper()!='NO':
        s=input('Enter date in DD-MM-YYYY')
        d=pd.to_datetime(s,dayfirst=True)
        print('Enter the enter daily vehicle volume recorded on ',s)
        v=int(input())
        l+=[[d,v]]
    df1=pd.DataFrame(l,columns=['Date','Vehicular Volume'])
df2=pd.DataFrame([],columns=['Month','No. of weekdays in month (days)','No. of days in month (days)','Total Monthly Volume (veh)','Total Weekday Volume (veh)'])
df1['Date']=pd.to_datetime(df1['Date'],dayfirst=True)
df2=df2.set_index('Month')
df1=df1.set_index('Date')
for i in range(len(list(df1.index))):
    if list(df1.index)[i].month_name() not in list(df2.index):
        df2.loc[list(df1.index)[i].month_name(),'No. of days in month (days)']=1
        df2.loc[list(df1.index)[i].month_name(),'Total Monthly Volume (veh)']=df1.loc[list(df1.index)[i],'Vehicular Volume']
        if list(df1.index)[i].day_name() not in ['Saturday','Sunday']:
            df2.loc[list(df1.index)[i].month_name(),'No. of weekdays in month (days)']=1
            df2.loc[list(df1.index)[i].month_name(),'Total Weekday Volume (veh)']=df1.loc[list(df1.index)[i],'Vehicular Volume']
        else:
            df2.loc[list(df1.index)[i].month_name(),'No. of weekdays in month (days)']=0
            df2.loc[list(df1.index)[i].month_name(),'Total Weekday Volume (veh)']=0 
    else:
        df2.loc[list(df1.index)[i].month_name(),'No. of days in month (days)']+=1
        df2.loc[list(df1.index)[i].month_name(),'Total Monthly Volume (veh)']+=df1.loc[list(df1.index)[i],'Vehicular Volume']
        if list(df1.index)[i].day_name() not in ['Saturday','Sunday']:
            df2.loc[list(df1.index)[i].month_name(),'No. of weekdays in month (days)']+=1
            df2.loc[list(df1.index)[i].month_name(),'Total Weekday Volume (veh)']+=df1.loc[list(df1.index)[i],'Vehicular Volume']
df2['Average Weekday Traffic (AWT)']=df2['Total Weekday Volume (veh)']/df2['No. of weekdays in month (days)']
df2['Average Daily Traffic (ADT)']=df2['Total Monthly Volume (veh)']/df2['No. of days in month (days)']
f=input('Enter the name of output file. Dont include .xlsx')
df2.to_excel(f+'.xlsx',index=False)
AAWT=np.nansum(df2['Total Weekday Volume (veh)'])/np.nansum(df2['No. of weekdays in month (days)'])
AADT=np.nansum(df2['Total Monthly Volume (veh)'])/np.nansum(df2['No. of days in month (days)'])
print('Average Annual Daily Traffic is ',AADT,' veh/day.')
print('Average Annual Weekday Traffic is ',AAWT,' veh/day.')
print('Total Annual Traffic on all days is ',np.nansum(df2['Total Monthly Volume (veh)']),' vehicles.')
print('Total Annual Traffic on weekdays is ',np.nansum(df2['Total Weekday Volume (veh)']),' vehicles.')
print('Total Annual Traffic on weekends is ',np.nansum(df2['Total Monthly Volume (veh)'])-np.nansum(df2['Total Weekday Volume (veh)']),' vehicles.')
print('Average Annual Weekend Traffic is ',(np.nansum(df2['Total Monthly Volume (veh)'])-np.nansum(df2['Total Weekday Volume (veh)']))/(np.nansum(df2['No. of days in month (days)'])-np.nansum(df2['No. of weekdays in month (days)'])),' veh/day')
plt.figure(figsize=(8,8))
plt.bar(list(df2.index),list(df2['Total Monthly Volume (veh)']),color='darkgreen',label='Total Monthly Volume (veh)')
plt.bar(list(df2.index),list(df2['Total Weekday Volume (veh)']),color='orange',label='Total Weekday Volume (veh)')
plt.bar(list(df2.index),list(df2['Total Monthly Volume (veh)']-df2['Total Weekday Volume (veh)']),color='cornflowerblue',label='Total Volume on Weekends')
plt.title('Variation of Total Monthly and Total Weekday Volume per Month')
plt.xlabel('Months')
plt.xticks(rotation=45, ha='right')
plt.ylabel('Total Volume (veh)')
plt.grid(True,alpha=0.7)
plt.legend()
plt.tight_layout()
plt.show()
plt.figure(figsize=(8,8))
plt.plot(list(df2.index),list(df2['Average Daily Traffic (ADT)']),color='maroon',label='Average Daily Traffic (ADT)')
plt.plot(list(df2.index),list(df2['Average Weekday Traffic (AWT)']),color='blue',label='Average Weekday Traffic (AWT)')
plt.plot(list(df2.index),list((df2['Total Monthly Volume (veh)']-df2['Total Weekday Volume (veh)'])/(df2['No. of days in month (days)']-df2['No. of weekdays in month (days)'])),color='goldenrod',label='Average Daily Traffic on weekends')
plt.title('Variation of Average Daily Traffic on all days, weekdays & weekends based on months')
plt.xlabel('Months')
plt.xticks(rotation=45,ha='right')
plt.ylabel('Average Daily Traffic')
plt.grid(True,alpha=0.7)
plt.legend()
plt.tight_layout()
plt.show()
plt.figure(figsize=(15,10))
plt.plot(list(df1.index),list(df1['Vehicular Volume']),color='lime')
plt.xlabel('Days')
plt.xticks(rotation=45,ha='right')
plt.ylabel('Vehicular Volumes')
plt.grid(True,alpha=0.7)
plt.tight_layout()
plt.show()







