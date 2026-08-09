import pandas as pd
import numpy as np
import math as m
import sys
import scipy.interpolate as scpi
import scipy.stats as scpst
import matplotlib.pyplot as plt
uspeed=input('Enter the units of all speeds that will be entered, and make sure all are the same')
e=float(input('Enter maximum acceptable percentage error <x>% in results'))
pcount=int(input('Enter the number of points to be used for plotting the graph to make it perfect. Recommended more than 1000.'))
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
        df=pd.read_excel(f)
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
df=df.sort_index()
df['Observed Vehicles(n)']=df['Observed Vehicles(n)'].astype(int)
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
l1=df['Middle Speed (S)'].tolist()
l1new=np.linspace(min(l1),max(l1),pcount).tolist()
l2=df['% Frequency'].tolist()
spline1=scpi.PchipInterpolator(l1,l2)
l2new=spline1(l1new)
l3=df['Upper Limit'].tolist()
l3new=np.linspace(min(l3),max(l3),pcount).tolist()
l4=df['Cumulative % Frequency'].tolist()
spline2=scpi.PchipInterpolator(l3,l4)
l4new=spline2(l3new)
co3=0
median=0
for i in l3new:
    if spline2(i)<=50*(1+(e/100)) and spline2(i)>=50*(1-(e/100)):
        median+=i
        co3+=1
if co3>0:
    median/=co3
else:
    median=np.nan
co4=0
mode=0
maxl2=np.max(l2new)
for i in l1new:
    if spline1(i)<=maxl2*(1+(e/100)) and spline1(i)>=maxl2*(1-(e/100)):
        mode+=i
        co4+=1
if co4>0:
    mode/=co4
else:
    mode=np.nan
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
df=df.rename(columns={'Lower Limit':'Lower Limit in '+uspeed,'Upper Limit':'Upper Limit in '+uspeed,'Middle Speed (S)':'Middle Speed (S) in '+uspeed})
df=df.set_index(['Lower Limit in '+uspeed,'Upper Limit in '+uspeed])
df=df.sort_index(ascending=False)
df=df.reset_index()
df['Upper Limit in '+uspeed]=df['Upper Limit in '+uspeed].astype('float64')
df['Lower Limit in '+uspeed]=df['Lower Limit in '+uspeed].astype('float64')
df.loc[list(df.index)[0],'Upper Limit in '+uspeed]=np.inf
df.loc[list(df.index)[-1],'Lower Limit in '+uspeed]=-np.inf
N=np.nansum(df['Observed Vehicles(n)'])
mean=np.nansum(df['nS'])/N
var=(np.nansum(df['nS²'])-(N*(mean**2)))/(N-1)
std=var**0.5
df['z']=(df['Upper Limit in '+uspeed]-mean)/std
df['Probability of occurence (z≤zd)']=scpst.norm.cdf(df['z'])
for i in range(len(df)-1):
    df.loc[list(df.index)[i],'Probability of occurence (z≤zd)']=df.loc[list(df.index)[i],'Probability of occurence (z≤zd)']-df.loc[list(df.index)[i+1],'Probability of occurence (z≤zd)']
df['Theoretical Frequency f']=N*df['Probability of occurence (z≤zd)']
co=0
d1={}
d2={}
while co<=len(df)-1:
    m=df.loc[list(df.index)[co],'Observed Vehicles(n)']
    n=df.loc[list(df.index)[co],'Theoretical Frequency f']
    if m<=5:
        le=()
        le+=co,
        co+=1
        while m<=5 and co<len(df):
            m+=df.loc[list(df.index)[co],'Observed Vehicles(n)']
            n+=df.loc[list(df.index)[co],'Theoretical Frequency f']
            le+=co,
            co+=1
        d1[le]=m
        d2[le]=n
    else:
        le=co
        d1[le]=m
        d2[le]=n
        co+=1
df['Combined Group Observed Frequency (n)']=[np.nan for i in range(len(df))]
df['Combined Group Theoretical Frequency (f)']=[np.nan for i in range(len(df))]
for k in d1:
    if isinstance(k,int):
        df.loc[list(df.index)[k],'Combined Group Observed Frequency (n)']=d1[k]
        df.loc[list(df.index)[k],'Combined Group Theoretical Frequency (f)']=d2[k]
    elif isinstance(k,tuple):
        df.loc[list(df.index)[k[-1]],'Combined Group Observed Frequency (n)']=d1[k]
        df.loc[list(df.index)[k[-1]],'Combined Group Theoretical Frequency (f)']=d2[k]
df['Chi-Square Group χ²']=((df['Combined Group Observed Frequency (n)']-df['Combined Group Theoretical Frequency (f)'])**2)/df['Combined Group Theoretical Frequency (f)']
print(df)
chsum=np.nansum(df['Chi-Square Group χ²'])
defredm=len(df['Chi-Square Group χ²'].dropna())-3
P=float(scpst.chi2.sf(chsum,defredm))
print('The average value of spot speed is ',mean,uspeed)
print('The variance of the spot speed data is',var)
print('The standard deviation of spot speed data is',std)
print('The median speed is ',median,uspeed)
print('The mode speed/ most frequent speed is',mode,uspeed)
print('The P value is ',P)
if P<=0.05:
    print('There is a significant difference and speeds do not closely follow a normal distribution')
else:
    print('There is not much significant difference and speeds fit well in a normal distribution curve')
co5=input('Do you want to find out any percentile speeds for this stretch of road. If yes press anything/enter and if No, enter <No>')
while co5.upper()!='NO':
    pctlespeed=float(input('Enter the percentile speed you want to find out'))
    co6=0
    sp=0
    for i in l3new:
        if spline2(i)<=pctlespeed*(1+(e/100)) and spline2(i)>=pctlespeed*(1-(e/100)):
            sp+=i
            co6+=1
    if co6>0:
        print('The ',pctlespeed,' percentile speed is ',sp/co6,uspeed)
    else:
        print('Something went wrong. Try again')
    co5=input('Do you want to find out any percentile speeds for this stretch of road. If yes press anything/enter and if No, enter <No>')
f=input('Enter the desired output filename. Dont include .xlsx')
df.to_excel(f+'.xlsx',index=False)
