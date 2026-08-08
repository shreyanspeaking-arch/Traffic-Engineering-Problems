import math as m
import pandas as pd
import sympy as sp
import sys
d=''
AADTmaj=float(input('Enter average annual daily traffic on major street in veh/day'))
AADTmin=float(input('Enter average annual daily traffic on minor street in veh/day'))
a,b,c,A,B=sp.symbols('a b c A B')
f=sp.sympify('exp(a+(b*log(A))+(c*log(B)))')
t1=pd.read_csv('Table_12_4_Calibration_Coefficients.csv')
t1=t1.set_index('Type of Crash')
Nbimvtotal=f.subs({a:t1.loc['Total','a'],b:t1.loc['Total','b'],c:t1.loc['Total','c'],A:AADTmaj,B:AADTmin})
NbimvFI=f.subs({a:t1.loc['Injury & Fatal','a'],b:t1.loc['Injury & Fatal','b'],c:t1.loc['Injury & Fatal','c'],A:AADTmaj,B:AADTmin})
NbimvPDO=f.subs({a:t1.loc['PDO','a'],b:t1.loc['PDO','b'],c:t1.loc['PDO','c'],A:AADTmaj,B:AADTmin})
NbimvFI=Nbimvtotal*(NbimvFI/(NbimvFI+NbimvPDO))
NbimvPDO=Nbimvtotal-NbimvFI
t2=pd.read_csv('Table_12_5_Calibration_Coefficients.csv')
t2=t2.set_index('Type of Crash')
Nbisvtotal=f.subs({a:t2.loc['Total','a'],b:t2.loc['Total','b'],c:t2.loc['Total','c'],A:AADTmaj,B:AADTmin})
NbisvFI=f.subs({a:t2.loc['Injury + Fatal','a'],b:t2.loc['Injury + Fatal','b'],c:t2.loc['Injury + Fatal','c'],A:AADTmaj,B:AADTmin})
NbisvPDO=f.subs({a:t2.loc['PDO','a'],b:t2.loc['PDO','b'],c:t2.loc['PDO','c'],A:AADTmaj,B:AADTmin})
NbisvFI=Nbisvtotal*(NbisvFI/(NbisvFI+NbisvPDO))
NbisvPDO=Nbisvtotal-NbisvFI
Nbmv=NbimvFI+NbimvPDO
Nbsv=NbisvFI+NbisvPDO
Nbi=Nbmv+Nbsv
t3=pd.read_csv('Table_12_6_Calibration_Coefficients.csv')
t3=t3.set_index('Coefficient')
t4=pd.read_csv('Table_12_7_Pedestrian_Volume_Default_Values.csv')
t4=t4.set_index('General Level of Pedestrian Activity')
d,e,C,D=sp.symbols('d e C D')
f2=sp.sympify('exp(a+(b*log(A+B))+(c*log(B/A))+(d*log(C))+(e*D))')
co=input('Do you have volume of pedestrians per day, <Yes> or <No>')
co=co.capitalize()
if co=='Yes':
    PedVol=int(input('Enter the volume of pedestrians per day'))
elif co=='No':
    for i in list(t4.index):
         print('<',i,'>')
    s=input('Just give me the guess range of pedestrians. Make sure only one of the above names is mentioned')
    PedVol=t4.loc[s,'Default Value for PedVol']
l=[str(i) for i in list(f2.free_symbols)]
l=[i for i in l if not i.isupper()]
nlanesxl=int(input('Enter the maximum number of lanes the pedestrian has to cross'))
d2={i:t3.loc[i,'Value'] for i in l}
Npedbase=f2.subs({a:d2['a'],b:d2['b'],c:d2['c'],d:d2['d'],e:d2['e'],A:AADTmaj,B:AADTmin,C:PedVol,D:nlanesxl})
t5=pd.read_csv('Table_12_9_CMF_Turn_Lanes.csv')
t5=t5.set_index('Number of Approaches with Exclusive Turn Lane(s)')
nlt=int(input('Number of approaches with left turn lanes. Enter a value between 0 and 4'))
nrt=int(input('Number of approaches with right turn lanes. Enter a value between 0 and 4'))
if nlt==0:
    CMFLT=1
elif nlt>=1 and nlt<=4:
    CMFLT=t5.loc[nlt,'LT Lane(s)']
else:
    print('Invalid Input')
    sys.exit()
if nrt==0:
    CMFRT=1
elif nrt>=1 and nrt<=4:
    CMRT=t5.loc[nrt,'RT Lane(s)']
else:
    print('Invalid Input')
    sys.exit()
nprohibited=int(input('Enter the number of intersection approaches that prohibit right turn on red. Enter 0 if None'))
CMFRTOR=0.98**nprohibited
pnight=0.235 #For 4SG Intersections
CMFL=1-(0.38*pnight)
co=input('Do you have data on number/proportion of multivehicle crashes that are at right angle collisions and rear end collisions. Enter <Yes1> if you have number of crashes. Enter <Yes2> if you have proportion of crashes. Enter<No> if you dont have any data')
co=co.upper()
if co=='NO':
    CMFRLC=1
elif co=='YES1':
    nra=int(input('Enter the number of multivehicle crashes that are right angle collisions'))
    nre=int(input('Enter the number of multivehicle crashes that are rear end collisions'))
    pra=nra/(nra+nre)
    pre=nre/(nra+nre)
    CMFRLC=1-(0.26*pra)+(0.18*pre)
elif co=='YES2':
    pra=int(input('Enter the proportion of multivehicle crashes that are right angle collisions'))
    pre=int(input('Enter the proportion of multivehicle crashes that are rear end collisions'))
    CMFRLC=1-(0.26*pra)+(0.18*pre)#'''
t6=pd.read_csv('Table_12_10_CMF_Left_Turn_Phasing.csv')
t6=t6.set_index('Type of LT Phasing')
t6=t6.rename(index={'Protected + Permitted, or Permitted + Protected':'Compound'})
naelt=int(input('Enter number of approaches with exclusive left turn phasing'))
for i in list(t6.index):
    print('<',i,'>')
kpl=input('Enter kind of phasing from the above 3 options')
CMFSP=t6.loc[kpl,str(naelt)]
Npredmv=Nbmv*CMFLT*CMFSP*CMFRT*CMFRTOR*CMFL*CMFRLC
Npredsv=Nbsv*CMFLT*CMFSP*CMFRT*CMFRTOR*CMFL*CMFRLC
fbikei=0.015 #For 4 SG intersections
Nbikei=(Npredmv+Npredsv)*fbikei
ci=float(input('Enter Local Calibration factor. Enter 1 if unknown'))
Nbi=Npredmv+Npredsv
nschool=int(input('Enter the number of schools within 1000 ft of intersection'))
nbusstop=int(input('Enter the number of bus stops within 1000 ft of intersection'))
nalcoholstore=int(input('Enter the number of alcohol selling stores within 1000 ft of intersection'))
t7=pd.read_csv('Table_12_11_Formatted.csv')
t7=t7.set_index(['Category','Condition'])
if nschool==0:
    CMFSCH=t7.loc[('Schools','0'),'Value']
elif nschool>=1:
    CMFSCH=t7.loc[('Schools','1 or more'),'Value']
else:
    print('Invalid Input')
    sys.exit()
if nbusstop==0:
    CMFBS=t7.loc[('Bus Stops','0'),'Value']
elif nbusstop>=1 and nbusstop<=2:
    CMFBS=t7.loc[('Bus Stops','1 or 2'),'Value']
elif nbusstop>=3:
    CMFBS=t7.loc[('Bus Stops','3 or more'),'Value']
else:
    print('Invalid Input')
    sys.exit()
if nalcoholstore==0:
    CMFALC=t7.loc[('Stores Selling Alcohol','0'),'Value']
elif nalcoholstore>=1 and nalcoholstore<=8:
    CMFALC=t7.loc[('Stores Selling Alcohol','1 to 8'),'Value']
elif nalcoholstore>=9:
    CMFALC=t7.loc[('Stores Selling Alcohol','9 or more'),'Value']
Npedpred=Npedbase*float(CMFSCH)*float(CMFBS)*float(CMFALC)
Npredint=ci*(Nbi+Npedpred+Nbikei)
print('The number of vehicle crashes is',Npredint,'crashes/year')





























