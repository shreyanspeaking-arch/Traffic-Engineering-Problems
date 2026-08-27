import math as m
import matplotlib.pyplot as plt
import sys
import numpy as np
import pandas as pd
u=input('Enter units of speed used in this program. Either kmph or mph')
i=1
print('''In this problem we are taking 2 model vehicles A & B for studying the 
Safe Stopping Distance vs Reaction Time + Maneuver time of driver.
Vehicle A is to the left and Vehicle B is to the right if I view the road from the side.
If the vehicles are moving in the same direction they are moving from left to right''')
co=int(input('''Enter 1 if the highway is horizontal 
Enter 2 if the highway is inclined'''))
if co==1:
    G=0
    a=1
    b=1
elif co==2:
    G=input('Enter the slope of the highway. If it is in degrees just enter the <Angle><o> and if in % grade enter <Grade><%>')
    if G.strip()[-1]=='o':
        G=m.tan(m.radians(float(G[:-1])))*100
    elif G.strip()[-1]=='%':
        G=float(G[:-1])
    else:
        print('Invalid Input')
        sys.exit()
co2=''
l=[]
G/=100
while co2.upper()!='NO':
    print('Case ',i)
    t=float(input('Enter total reaction + maneuver time in seconds'))
    va=float(input('Enter the speed of vehicle A in '+u))
    vb=float(input('Enter the speed of vehicle B in '+u))
    if co==2:
        na=int(input('''Enter 1 if vehicle A is going uphill
Enter 2 if vehicle A is going downhill'''))
        nb=int(input('''Enter 1 if vehicle B is going uphill
Enter 2 if vehicle B is going downhill'''))
        if na==1:
            a=1
        elif na==2:
            a=-1
        else:
            print('Invalid Input')
            sys.exit()
        if nb==1:
            b=1
        elif nb==2:
            b=-1
        else:
            print('Invalid Input')
            sys.exit()
    if u=='kmph':
        va=float(va)
    elif u=='mph':
        va=float(va)*1.60934
    else:
        print('Invalid Input')
        sys.exit()
    if u=='kmph':
        vb=float(vb)
    elif u=='mph':
        vb=float(vb)*1.60934
    else:
        print('Invalid Input')
        sys.exit()
    if va!=0 and vb!=0 and co!=2:
        o=input('Enter whether in <same> or <opposite> direction')
    elif a==1 and b==1:
        o='same'
    elif a==-1 and b==-1:
        o='same'
    else:
        o='opposite'
    va*=5/18
    vb*=5/18
    hsd=float(input('Enter head start distance between A and B. If unknown enter 0.'))
    f=float(input('Enter coefficient of friction between the wheels of the vehicle and the road surface'))
    if o.upper()=='SAME':
        SSD=max(0,abs((va*t)+((va**2)/(2*9.81*(f+(a*G))))-(vb*t)-((vb**2)/(2*9.81*(f+(b*G)))))-hsd)
    elif o.upper()=='OPPOSITE' or o=='':
        SSD=max(0,abs((va*t)+((va**2)/(2*9.81*(f+(a*G))))+(vb*t)+((vb**2)/(2*9.81*(f+(b*G)))))-hsd)
    else:
        print('Invalid Input')
        sys.exit()
    if vb>va and o=='same':
        SSD=0
    l+=[[va*(18/5),vb*(18/5),f,t,o,hsd,SSD]]
    i+=1
    co2=input('Do you want to compare any more cases. If yes press anything/enter, else enter <No>')
df=pd.DataFrame(l,columns=['Velocity of Vehicle A','Velocity of Vehicle B','Coefficient of Friction','Total Reaction + Maneuver Time','Direction of movement wrt each other','Head Start Distance','Safe Stopping Distance'])
df=df.set_index(['Velocity of Vehicle A','Velocity of Vehicle B','Direction of movement wrt each other'])
print(df)
f=input('Enter the output filename for this table. Exclude .xlsx')
df.to_excel(f+'.xlsx',index=False)
