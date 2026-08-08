import pandas as pd
import sys
print('Wherever there is <text> written in the print statements, they are the only acceptable answers')
t1=pd.read_csv('Table1.csv')
t2=pd.read_csv('Table2.csv')
t1=t1.rename(columns={'Design speed (mi/h)':'DS','Cj (veh/h)':'Capacity'})
t1=t1.set_index('DS')
t2=t2.rename(columns={'Level of service':'LOS','(v/c) (C70)':70,'(v/c) (C60)':60,'(v/c) (C50)':50})
t2=t2.set_index('LOS')
print('Table containing values of Capacities of Standard Highway Lane in veh/h for different design speeds in mi/h provided by Transportation Research Board')
print(t1)
print('Table containing ratios of flow to capacity for different levels of service and design speed provided by Transportation Research Board')
print(t2)
t2=t2.reset_index()
n=int(input('Enter no. of lanes in highway, total both ways'))
n//=2
V=float(input('Enter Peak Hour Volumne in veh/h'))
PHF=float(input('Enter Peak Hour Factor'))
SF=V/PHF
DS=int(input('Enter Design Speed in mi/h. Only <50>,<60> and <70> are acceptable'))
if DS not in [i for i in range(50,80,10)]:
    print('Invalid Input')
    sys.exit()
C=t1.loc[DS,'Capacity']
t3=pd.read_csv('Table_5_3_Correction_Factors.csv')
t3=t3.set_index('Distance_of_obstruction_from_travelled_edge_m')
print('Correction Factors for non-ideal lane widths and clearances from obstructions on multilane highways as provided by Transportation Research Board')
print(t3)
t3=t3.rename(columns={'OneSide_LaneWidth_3.65':'One3.65','OneSide_LaneWidth_3.36':'One3.36',
       'OneSide_LaneWidth_3.05':'One3.05', 'OneSide_LaneWidth_2.75':'One2.75',
       'BothSides_LaneWidth_3.65':'Both3.65', 'BothSides_LaneWidth_3.36':'Both3.36',
       'BothSides_LaneWidth_3.05':'Both3.05', 'BothSides_LaneWidth_2.75':'Both2.75'})
s=input('Enter whether the obstructions are on <One> or <Both> sides of the roadway')
if s.upper() not in ['ONE','BOTH']:
    print('Invalid Input')
    sys.exit()
s=s.capitalize()
lw=float(input('Enter lane width in m. Acceptable inputs are 3.65, 3.36, 3.05 and 2.75'))
if lw not in [3.65,3.36,3.05,2.75]:
    print('Invalid Input')
    sys.exit()
do=float(input('Enter distance of obstruction from travelled edge in m'))
l3=list(t3.index)
for i in range(len(l3)):
    if do>=float(l3[i][:4]):
        fw=t3.loc[l3[i],s+str(lw)]
        break
t4=pd.read_csv('Table_5_4_PCE_Heavy_Vehicles.csv')
t4=t4.set_index('Correction_factor')
t4=t4.rename(index={'ET for trucks':'Truck', 'EB for buses':'Bus', 'ER for recreational vehicles':'Recreational Vehicle'})
terrain=input('Enter type of terrain, either <Level>, <Rolling> or <Mountainous>')
terrain=terrain.capitalize()
if terrain not in ['Level','Rolling','Mountainous']:
    print('Invalid Input')
    sys.exit()
ET=float(t4.loc['Truck',terrain])
EB=float(t4.loc['Bus',terrain])
ERV=float(t4.loc['Recreational Vehicle',terrain])
print('All the following 3 values should be between 0 and 100. If there are none enter 0')
PT=float(input('Enter the percentage of trucks in traffic stream'))
PB=float(input('Enter the percentage of buses in traffic stream'))
PRV=float(input('Enter the percentage of recreational vehicles in traffic stream'))
if PT>100 or PT<0 or PB>100 or PB<0 or PRV>100 or PRV<0 or PT+PB+PRV>100:
    print('Invalid Input')
    sys.exit()
PT/=100
PB/=100
PRV/=100
fhv=1/(1+((PT*(ET-1))+(PB*(EB-1))+(PRV*(ERV-1))))
dvrtype=input('Is the driver a regular weekday commuter. Enter Yes or No')
dvrtype=dvrtype.upper()
if dvrtype=='YES':
    fp=1
elif dvrtype=='NO':
    fp=float(input('Enter the correction factor between 0.75 and 0.9'))
    if fp>0.9 or fp<0.75:
        print('Invalid Input')
        sys.exit()
else:
    print('Invalid Input')
    sys.exit()
highwaytype1=input('Is the highway <Divided> or <Undivided>.')
if highwaytype1.upper() not in ['DIVIDED','UNDIVIDED']:
    print('Invalid Input')
    sys.exit()
highwaytype2=input('Is the highway <Rural> or <Urban/suburban>.')
if highwaytype2.upper() not in ['RURAL','URBAN/SUBURBAN']:
    print('Invalid Input')
    sys.exit()
highwaytype1=highwaytype1.capitalize()
highwaytype2=highwaytype2.capitalize()
t5=pd.read_csv('Table_5_5_Highway_Environment_Correction_Factors.csv')
t5=t5.set_index('Highway_classification')
print('Correction Factors highway environment as provided by Transportation Research Board')
print(t5)
fe=t5.loc[highwaytype2,highwaytype1]
vbc=SF/(C*n*fw*fhv*fp*fe)
print('The v/c ratio is ',vbc)
if vbc>1:
    print('Level of Service(LOS) for this highway is F')
    sys.exit()
l2=list(t2.index)
for i in range(len(list(l2))-2):
    l=float(t2.loc[l2[i],DS])
    u=float(t2.loc[l2[i+1],DS])
    if vbc<=l:
        print('Level of Service(LOS) for this highway is ',t2.loc[l2[i],'LOS'])
        sys.exit()
    elif vbc>l and vbc<u:
        print('Level of Service(LOS) for this highway is ',t2.loc[l2[i+1],'LOS'])
        sys.exit()
