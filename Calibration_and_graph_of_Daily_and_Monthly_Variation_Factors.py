import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import sys
print('Make sure the dates in the file are entered properly in the date format of csv/excel')
f=input('Enter filename')
if f.split('.')[-1]=='csv':
    d1=pd.read_csv(f)
elif f.split('.')[-1]=='xlsx':
    d1=pd.read_excel(f)
if 'date' not in list(d1.columns):
   s=input('Enter the name of the column containing the dates')
   d1=d1.rename(columns={s:'date'})
if 'vehicle_volume' not in list(d1.columns):
   s=input('Enter the name of the column containing vehicle volumes')
   d1=d1.rename(columns={s:'vehicle_volume'})
d1['date']=pd.to_datetime(d1['date'])
d1=d1.set_index('date')
l1=['Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday']
l3=[]

for i in l1:
    l3+=[[i,0]]
d2=pd.DataFrame(l3,columns=['Day','Yearly Average Volume for this day (veh/day)'])
d2=d2.set_index('Day')
l2=[0 for i in range(7)]
l4=[0 for i in range(7)]
for i in range(len(d1)):
    for j in range(len(l1)):
        if list(d1.index)[i].day_name()==l1[j]:
            l2[j]+=d1.loc[list(d1.index)[i],'vehicle_volume']
            l4[j]+=1
l5=[]
for i in range(len(l2)):
    l5+=[int(l2[i]/l4[i])]
d2['Yearly Average Volume for this day (veh/day)']=l5
m=np.nanmean(d2['Yearly Average Volume for this day (veh/day)'])
d2['Daily Adjustment Factor DF']=m/d2['Yearly Average Volume for this day (veh/day)']
print(d2)
l6=['January','February','March','April','May','June','July','August','September','October','November','December']
l7=[]
for i in l6:
    l7+=[[i,0,0]]
d3=pd.DataFrame(l7,columns=['Month','Total Traffic(vehs)','ADT for Month(veh/day)'])
d3=d3.set_index('Month')
l8=[0 for i in range(12)]
l9=[0 for i in range(12)]
for i in range(len(d1)):
    for j in range(len(l6)):
        if list(d1.index)[i].month_name()==l6[j]:
            l8[j]+=d1.loc[list(d1.index)[i],'vehicle_volume']
            l9[j]+=1
l10=[]
for i in range(12):
   l10+=[int(l8[i]/l9[i])]
   l8[i]=int(l8[i])
d3['Total Traffic(vehs)']=l8
d3['ADT for Month(veh/day)']=l10
m=np.nansum(d3['Total Traffic(vehs)'])/np.nansum(l9)
d3['Monthly Adjustment Factor MF']=m/d3['ADT for Month(veh/day)']
print(d3)
co2=input('Do you want to estimate Average Annual Traffic based on a particular day. Enter <Yes> if you need it or just anything else/enter for aborting')
so=0
co=0
while co2.upper()=='YES':
    d=pd.to_datetime(input('Enter date in DD-MM-YYYY format'),dayfirst=True)
    print('Enter volume on ',str(d.date()),'in veh')
    V=int(input())
    AADT=float(d2.loc[d.day_name(),'Daily Adjustment Factor DF'])*float(d3.loc[d.month_name(),'Monthly Adjustment Factor MF'])*V
    print('Average Annual Daily Traffic is estimated to be ',AADT,'veh/day based on date ',str(d.date()))
    co2=input('Do you want to estimate Average Annual Traffic based on a particular day. Enter <Yes> if you need it or just anything else/enter for aborting')
    so+=AADT
    co+=1
if co!=0:
    AADT=so/co
co3=input('Do you want to estimate Annual Vehicle Miles travelled. Enter <Yes> if you need it or just anything else/enter for aborting')
if co3.upper()=='YES' and co!=0:
    L=float(input('Enter length of segment in km'))
    VMT365=AADT*365*L
    print('Annual Vehicle Miles Travelled over the segment is ',VMT365,'vehicle-km')
else:
    print('Average Annual Daily Traffic (AADT) has not been computed')
fig,ax=plt.subplots(2,1,figsize=(12,12),constrained_layout=True)
fig.suptitle('Variation of Daily and Monthly Variation Parameters')
d2['Daily Adjustment Factor DF'].plot(kind='line',color='b',ax=ax[0])
ax[0].set_title('Variation of Daily Adjustment Parameters with respect to days of a week')
ax[0].grid(True,linestyle='--',alpha=0.7)
ax[0].set_xticks(range(len(d2)))
ax[0].set_ylabel('Daily Adjustment Factor DF')
ax[0].set_xticklabels(d2.index, rotation=45)
d3['Monthly Adjustment Factor MF'].plot(kind='line',color='r',ax=ax[1])
ax[1].set_title('Variation of Monthly Adjustment Parameters with respect to month')
ax[1].grid(True,linestyle='--',alpha=0.7)
ax[1].set_ylabel('Monthly Adjustment Factor MF')
ax[1].set_xticks(range(len(d3)))
ax[1].set_xticklabels(d3.index, rotation=45)
plt.show()
d2=d2.reset_index()
d3=d3.reset_index()
d2.to_excel('Daily_Variation_Factors_Data_Output.xlsx',index=False)
d3.to_excel('Monthly_Variation_Factors_Data_Output.xlsx',index=False)
