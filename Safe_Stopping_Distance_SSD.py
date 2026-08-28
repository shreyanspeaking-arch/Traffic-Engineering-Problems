import math as m
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
u=input('Enter units of speed used in this program. Either kmph or mph')
i=1
print('''In this problem we are taking 2 model vehicles A & B for studying the 
Safe Stopping Distance vs Reaction Time + Maneuver time of driver.
Vehicle A is to the left and Vehicle B is to the right if I view the road from the side.
If the vehicles are moving in the same direction they are moving from left to right''')
co2=''
l=[]
while co2.upper()!='NO':
    try:
        print('Case ',i)
        t=float(input('Enter total reaction + maneuver time in seconds'))
        va=float(input('Enter the speed of vehicle A in '+u))
        vb=float(input('Enter the speed of vehicle B in '+u))
        if u=='kmph':
            va=float(va)
        elif u=='mph':
            va=float(va)*1.60934
        if u=='kmph':
            vb=float(vb)
        elif u=='mph':
            vb=float(vb)*1.60934
        co3=input('''If grade of A is the same as grade of B press anything/enter
    else enter <No>''')
        print('If the highway is perfectly horizontal enter the grade as 0')
        Ga=input('Enter the slope of the highway for vehicle A. If it is in degrees just enter the <Angle><o> and if in % grade enter <Grade><%>')
        if Ga.strip()[-1]=='o':
            Ga=m.tan(m.radians(float(Ga[:-1])))*100
        elif Ga.strip()[-1]=='%':
            Ga=float(Ga[:-1])
        elif Ga.strip()=='0':
            Ga=0
        if co3.upper()!='NO':
            Gb=Ga
        else:
            Gb=input('Enter the slope of the highway for vehicle B. If it is in degrees just enter the <Angle><o> and if in % grade enter <Grade><%>')
            if Gb.strip()[-1]=='o':
                Gb=m.tan(m.radians(float(Gb[:-1])))*100
            elif Gb.strip()[-1]=='%':
                Gb=float(Gb[:-1])
            elif Gb.strip()=='0':
                Gb=0
        Ga/=100
        Gb/=100
        co4=input('''If coefficient of friction of A is the same as the coefficient of friction of B press anything/enter
    else enter <No>''')
        fa=float(input('Enter the coefficient of friction between the wheels of vehicle A and the pavement surface.'))
        if co4.upper()!='NO':
            fb=fa
        else:
            fb=float(input('Enter the coefficient of friction between the wheels of vehicle B and the pavement surface.'))
        va*=5/18
        vb*=5/18
        hsd=float(input('Enter head start distance between A and B (in m). If unknown enter 0.'))
        if Ga!=0:
            oa=int(input('''Enter 1 if vehicle A is moving uphill
    Enter 2 if vehicle is moving downhill'''))
            if oa==2:
                Ga*=-1
        if Gb!=0:
            ob=int(input('''Enter 1 if vehicle B is moving uphill
    Enter 2 if vehicle is moving downhill'''))
            if ob==2:
                Gb*=-1
        if va==0 or vb==0:
            o='opposite'
        elif Ga==0 or Gb==0 and (vb!=0 or va!=0):
            o=input('Enter the direction in which the vehicles are moving. Either <same> or <opposite>')
        elif Ga!=0 or Gb!=0:
            if (oa==1 and ob==2) or (oa==2 and ob==1):
                o='opposite'
            else:
                o='same' 
        if o.upper()=='SAME':
            c=-1
        elif o.upper()=='OPPOSITE':
            c=1
        SSDa=(va*t)+((va**2)/(2*9.81*(fa+Ga)))
        SSDb=(vb*t)+((vb**2)/(2*9.81*(fb+Gb)))
        SSD=max(0,SSDa+(c*SSDb)-hsd)
        rs=input('Add any statement for this dataset if you want to else press enter')
        l+=[[va*(18/5),vb*(18/5),o.upper(),fa,fb,t,hsd,Ga*100,Gb*100,SSD,rs]]
        i+=1
        co2=input('Do you want to compare any more cases. If yes press anything/enter, else enter <No>')
    except:
        print('There was some invalid input/error')
        co2=input('Do you want to compare any more cases. If yes press anything/enter, else enter <No>')
df=pd.DataFrame(l,columns=['Velocity of Vehicle A','Velocity of Vehicle B','Direction of movement wrt each other','Coefficient of Friction between Vehicle A and Pavement Surface','Coefficient of Friction between Vehicle B and Pavement Surface','Total Reaction + Maneuver Time','Head Start Distance','Grade of Slope of road of Vehicle A','Grade of Slope of road of Vehicle B','Safe Stopping Distance','Related Statement'])
print(df)
f=input('Enter the output filename for this table. Exclude .xlsx')
df.to_excel(f+'.xlsx',index=False)

