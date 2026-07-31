import pandas as pd
import sys
import numpy as np
import matplotlib.pyplot as plt
print('''Enter 1 if you want to enter a csv file or
Enter 2 if you want to enter values manually one by one''')
co3=int(input())
l=[]
print('''Enter 1 if arrival rates are in veh/h
Enter 2 if arrival rates are in veh/h/ln''')
l+=[int(input())]
print('''Enter 1 if departure rates are in veh/h
Enter 2 if departure rates are in veh/h/ln''')
l+=[int(input())]
if l not in [[1,1],[1,2],[2,1],[2,2]]:
    print('Invalid Input')
    sys.exit()
if co3==1:
    f=input('Enter filename. Make sure that the file and the program are in the same directory')
    if f[-5:]=='.xlsx':
        df=pd.read_excel(f)
    elif f[-4:]=='.csv':
        df=pd.read_csv(f)
    else:
        print('Only CSV/Excel files')
        sys.exit()
    ldf=list(df.columns)
    d={}
    print('The columns in the dataframe are ',ldf)
    if 'Start Time' not in ldf:
        c=input('Enter the name of the column containing the start times of the datasets')
        d[c]='Start Time'
    if 'End Time' not in ldf:
        c=input('Enter the name of the column containing the end times of the datasets')
        d[c]='End Time'
    if l[0]==2 and 'Arrival Rate (in veh/h/ln)' not in ldf:
        c=input('Enter the name of the column containing the arrival rate of vehicles (in veh/h/ln)')
        d[c]='Arrival Rate (in veh/h/ln)'
    elif l[0]==1 and 'Arrival Rate (in veh/h)' not in ldf:
        c=input('Enter the name of the column containing the arrival rate of vehicles (in veh/h)')
        d[c]='Arrival Rate (in veh/h)'
    if l[1]==2 and 'Departure Rate (in veh/h/ln)' not in ldf:
        c=input('Enter the name of the column containing the departure rate of vehicles (in veh/h/ln)')
        d[c]='Departure Rate (in veh/h/ln)'
    elif l[1]==1 and 'Departure Rate (in veh/h)' not in ldf:
        c=input('Enter the name of the column containing the departure rate of vehicles (in veh/h)')
        d[c]='Departure Rate (in veh/h)'
    if l[0]==2 and 'No. of lanes used for arrival' not in ldf:
        c=input('Enter the No. of lanes used for arrival')
        d[c]='No. of lanes used for arrival'
    if l[1]==2 and 'No. of lanes used for departure' not in ldf:
        c=input('Enter the No. of lanes used for departure')
        d[c]='No. of lanes used for departure'
    if l[0]==1:
        df['No. of lanes used for arrival']=[np.nan for i in range(len(df))]
    if l[1]==1:
        df['No. of lanes used for departure']=[np.nan for i in range(len(df))]
    df=df.rename(columns=d)
    df2=df.copy()
    if l[0]==1:
        df2['No. of lanes used for arrival']=df2['No. of lanes used for arrival'].fillna(1)
    if l[1]==1:
        df2['No. of lanes used for departure']=df2['No. of lanes used for departure'].fillna(1)
elif co3==2:
    co=''
    i=1
    col=['Start Time','End Time','Arrival Rate','No. of lanes used for arrival','Departure Rate','No. of lanes used for departure']
    if l[0]==2:
        col[2]+=' (in veh/h/ln)'
    elif l[0]==1:
        col[2]+=' (in veh/h)'
    else:
        print('Invalid Input')
        sys.exit()
    if l[1]==2:
        col[-2]+=' (in veh/h/ln)'
    elif l[1]==1:
        col[-2]+=' (in veh/h)'
    df=pd.DataFrame([],columns=col)
    while co.upper()!='NO':
        print('Dataset ',i)
        stpc=''
        if i==1:
            st=pd.to_datetime(input('Enter Start Time for dataset '+str(i))).time()
            et=pd.to_datetime(input('Enter End Time for dataset '+str(i))).time()
        else:
            print(f'''Is the start time for dataset {i} the same as the end time of dataset {i-1}. 
    If <Yes> press anything/enter and if <No> enter No
    Enter L if this is the last dataset and doesn't have an end time. If it has an end time no need to enter L''')
            co2=input()
            if co2.upper()!='NO' and co2.upper()!='L':
                st=et
                print('Starting time for dataset is ',st)
                et=pd.to_datetime(input('Enter End Time for dataset '+str(i))).time()
            elif co2.upper()=='NO':
                st=pd.to_datetime(input('Enter Start Time for dataset '+str(i))).time()
                et=pd.to_datetime(input('Enter End Time for dataset '+str(i))).time()
            elif co2.upper()=='L':
                st=et
                et=np.nan
                stpc=co2.upper()
        ar=float(input('Enter '+col[2]))
        dr=float(input('Enter '+col[-2]))
        if l[0]==2:
            an=float(input('Enter '+col[3]))
        else:
            an=np.nan
        if l[1]==2:
            dn=float(input('Enter '+col[-1]))
        else:
            dn=np.nan               
        df.loc[len(df)]=[st,et,ar,an,dr,dn]
        if stpc.upper()=='L':
            break
        i+=1
        co=input('Do you want to enter any more datasets. If <Yes>, press anything/enter. If <No> enter No')
    df2=df.copy()
    if l[0]==1:
        df2['No. of lanes used for arrival']=df2['No. of lanes used for arrival'].fillna(1)
    if l[1]==1:
        df2['No. of lanes used for departure']=df2['No. of lanes used for departure'].fillna(1)
else:
    print('Invalid Input')
    sys.exit()
df['Arrivals (veh)']=[np.nan for j in range(len(df))]
df['Departures (veh)']=[np.nan for j in range(len(df))]
df['Size of Queue (veh)']=[np.nan for j in range(len(df))]
col=list(df.columns)
for j in range(len(df)):
    h=(((pd.to_datetime(str(df.loc[j,col[1]]))-pd.to_datetime(str(df.loc[j,col[0]]))).total_seconds())/3600)
    if pd.isna(h):
        h=1
    if l[0]==1:
        df.loc[j,'Arrivals (veh)']=df.loc[j,col[col.index('Arrival Rate (in veh/h)')]]*df2.loc[j,col[col.index('No. of lanes used for arrival')]]*h
    if l[1]==1:
        df.loc[j,'Departures (veh)']=df.loc[j,col[col.index('Departure Rate (in veh/h)')]]*df2.loc[j,col[col.index('No. of lanes used for departure')]]*h
    if l[0]==2:
        df.loc[j,'Arrivals (veh)']=df.loc[j,col[col.index('Arrival Rate (in veh/h/ln)')]]*df2.loc[j,col[col.index('No. of lanes used for arrival')]]*h
    if l[1]==2:
        df.loc[j,'Departures (veh)']=df.loc[j,col[col.index('Departure Rate (in veh/h/ln)')]]*df2.loc[j,col[col.index('No. of lanes used for departure')]]*h
    if j==0:
        df.loc[j,'Size of Queue (veh)']=df.loc[j,'Arrivals (veh)']-df.loc[j,'Departures (veh)']
    else:
        df.loc[j,'Size of Queue (veh)']=df.loc[j,'Arrivals (veh)']-df.loc[j,'Departures (veh)']+df.loc[j-1,'Size of Queue (veh)']
ci=None
for i in range(len(df)):
  if df.loc[df.index[i],'Size of Queue (veh)']<0:
    ci=i
    break
if ci is not None and ci<len(df)-1:
  df=df.iloc[:ci+1]
if pd.isna(df.loc[list(df.index)[len(df)-1],'End Time']):
    print('Assuming that arrival and departure rates after ',df.loc[list(df.index)[len(df)-1],'Start Time'],' is constant')
h=df.loc[list(df.index)[len(df)-2],'Size of Queue (veh)']/abs(df.loc[list(df.index)[len(df)-1],col[col.index('Arrivals (veh)')]]-df.loc[list(df.index)[len(df)-1],col[col.index('Departures (veh)')]])
s1=str(pd.Timestamp.today().date())+' '+str(df.loc[list(df.index)[0],'Start Time'])
s2=str(pd.Timestamp.today().date())+' '+str(df.loc[list(df.index)[len(df)-1],'Start Time'])
s1=pd.to_datetime(s1)
eqt=(pd.to_datetime(s2)+pd.to_timedelta(h,unit='h'))
n=(eqt-s1).days
if n==0:
    print('The queue clears at ',eqt.time())
else:
    print('The queue clears at ',eqt.time(),' after ',n,' day(s)')
df.loc[list(df.index)[len(df)-1],'Size of Queue (veh)']=np.nan
print(df)
f=input('Enter name of output filename. Dont include .xlsx')
df.to_excel(f+'.xlsx',index=False)
l=[]
s3=pd.to_datetime(str(pd.Timestamp.today().date())+' '+str(list(df['End Time'])[0]))
for i in list(df['End Time'])[:-1]:
    j=pd.to_datetime(str(pd.Timestamp.today().date())+' '+str(i))
    l+=[(j-s3.normalize()).total_seconds()]
l+=[(eqt-s3.normalize()).total_seconds()]
plt.figure(figsize=(10,8))
plt.title('Size of Queue vs End Time')
plt.plot(l,list(df['Size of Queue (veh)'])[:-1]+[0],color='maroon')
plt.xlabel('End Time')
plt.ylabel('Size of Queue (veh)')
if n==0:
    plt.xticks(l,list(df['End Time'])[:-1]+[eqt.time()],rotation=45,ha='right')
else:
    plt.xticks(l,list(df['End Time'])[:-1]+[str(eqt.time())+','+str(n)+'D'],rotation=45,ha='right')
plt.grid(True,alpha=0.7)
plt.tight_layout()
plt.show()
