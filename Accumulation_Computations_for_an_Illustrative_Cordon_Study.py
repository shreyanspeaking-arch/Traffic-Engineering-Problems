import pandas as pd
import numpy as np
import sys
import matplotlib.pyplot as plt
statement=int(input('''Enter 1 if you want to enter a csv/excel file
Enter 2 if you want to enter values manually'''))
if statement==1:
    f=input('Enter filename. Make sure the file is in the same directory')
    if f[-4:]=='.csv':
        d=pd.read_csv(f)
    elif f[-5:]=='.xlsx':
        d=pd.read_excel(f)
    else:
        print('Invalid file format. Enter a csv/xlsx file')
        sys.exit()
    print(list(d.columns))
    if 'Start Time' not in list(d.columns):
        m=input('Enter the column name containing the start time of each dataset')
        d=d.rename(columns={m:'Start Time'})
    if 'End Time' not in list(d.columns):
        m=input('Enter the column name containing the end time of each dataset')
        d=d.rename(columns={m:'End Time'})
    if 'No. of vehicles entering' not in list(d.columns):
        m=input('Enter the column name containing the no. of vehicles entering the cordon of each dataset')
        d=d.rename(columns={m:'No. of vehicles entering'})
    if 'No. of vehicles leaving' not in list(d.columns):
        m=input('Enter the column name containin the no. of vehicles leaving the cordon of each dataset')
        d=d.rename(columns={m:'No. of vehicles leaving'})
    d['Accumulation']=[np.nan for i in range(len(d))]
    d['Start Time']=pd.to_datetime(d['Start Time']).dt.time
    d['End Time']=pd.to_datetime(d['End Time']).dt.time
    d=d.set_index(['Start Time','End Time'])
elif statement==2:
    l=[]
    st=pd.to_datetime(input('Enter the start time in H:M when the beginning accumulation value is available'))
    e=pd.to_datetime(input('Enter the end time in H:M when the beginning accumulation value is available'))
    print('Enter the number of vehicles accumulated between ',st.time(),' and ',e.time())
    a=int(input())
    l+=[[st,e,np.nan,np.nan,a]]
    s=input('Do you want to enter any more values. If No enter <No> else press anything/enter')
    i=0
    if s.upper()!='NO':
        print('''Press 1 if the intervals of all times entered henceforth is the same as the first or
    Press 2 if you want to enter the start time and end time of each dataset seperately''')
        co=int(input())
        if co==1:
            h=e-st
            while s.upper()!='NO':
                print('Dataset ',i+1)
                st=l[i][1]
                e=st+h
                print('Enter the number of vehicles entering the queue between ',st.time(),' and ',e.time())
                ve=int(input())
                print('Enter the number of vehicles leaving the queue between ',st.time(),' and ',e.time())
                vl=int(input())
                l+=[[st,e,ve,vl,np.nan]]
                s=input('Do you want to enter any more values. If No enter <No> else press anything/enter')
                i+=1
        elif co==2:
            while s.upper()!='NO':
                print('Dataset ',i+1)
                print(f'''Press 1 if the start time for this dataset is same as the previous end time i.e. {e.time()} and
    Press 2 if different''')
                co2=int(input())
                if co2==1: 
                    st=l[i][1]
                elif co2==2:
                    st=pd.to_datetime(input('Enter the start time for dataset'))
                else:
                    print('Invalid Input')
                    sys.exit()
                e=pd.to_datetime(input('Enter the ending time for this dataset'))
                print('Enter the number of vehicles entering the queue between ',st.time(),' and ',e.time())
                ve=int(input())
                print('Enter the number of vehicles leaving the queue between ',st.time(),' and ',e.time())
                vl=int(input())
                l+=[[st,e,ve,vl,np.nan]]
                s=input('Do you want to enter any more values. If No enter <No> else press anything/enter')
                i+=1
        else:
            print('Invalid Input')
            sys.exit()
    d=pd.DataFrame(l,columns=['Start Time','End Time','No. of vehicles entering','No. of vehicles leaving','Accumulation'])
    d['Start Time']=pd.to_datetime(d['Start Time']).dt.time
    d['End Time']=pd.to_datetime(d['End Time']).dt.time
    d=d.set_index(['Start Time','End Time'])
else:
    print('Invalid Input')
    sys.exit()
d.loc[list(d.index)[0],'Accumulation']=0
for i in range(1,len(d)):
    d.loc[list(d.index)[i],'Accumulation']=d.loc[list(d.index)[i-1],'Accumulation']+d.loc[list(d.index)[i],'No. of vehicles entering']-d.loc[list(d.index)[i],'No. of vehicles leaving']
d=d[['No. of vehicles entering','No. of vehicles leaving','Accumulation']].astype('Int64')
print(d)
d=d.reset_index()
l1=d['End Time'].tolist()
for i in range(len(l1)):
    l1[i]=str(l1[i])
l2=d['Accumulation'].tolist()
fig,ax=plt.subplots(figsize=(10,8))
ax.plot(l1,l2,color='blue')
ax.grid(True,alpha=0.7,linestyle='--')
ax.set_title('Presentation of Accumulation Data w.r.t. Time')
ax.set_ylabel('Accumulated Vehicles→')
ax.set_xlabel('Time→')
plt.tight_layout()
plt.show()
