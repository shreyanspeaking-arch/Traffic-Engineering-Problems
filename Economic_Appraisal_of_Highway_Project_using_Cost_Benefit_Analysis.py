import pandas as pd
import numpy as np
import sympy as sp
print('Make sure all the monetary values are of the same currency')
t=int(input('Enter the economic life of Highway Proposal'))
l=[np.nan for i in range(t)]
t1=int(input('Enter no of years taken for initial construction of highway before inauguration'))
t2=t-t1
acr1=float(input('Enter accident rate on existing road per million vehicle km'))
acr2=float(input('Enter accident rate on upgraded road per million vehicle km'))
aac=int(input('Enter average accident cost'))
avts=int(input('Enter average vehicle time savings per hour'))
avs1=float(input('Average vehicle speed on existing road in km/h'))
avs2=float(input('Average vehicle speed on upgraded road in km/h'))
dis=int(input('Enter discount rate in %'))
V=sp.symbols('V')
print('''Enter the function for Average Vehicle Operating Costs as single variable function of Average Vehicle speeds V. 
Don''t include LHS and = like f(x)= and the output unit should be in cost/km''')
f1=input()
f2=sp.sympify(f1)
avoc1=f2.subs({V:avs1})
avoc2=f2.subs({V:avs2})
for i in range(t):
    k=[np.nan for i in range(4)]
    k[0]=i+1
    if i+1<=t1:
        print('Enter annual construction cost for year',i+1)
        k[2]=int(input())
    else:
        print('Enter predicted flow per million vehicle kms for year',i+1)
        k[1]=int(input())
        print('Enter the annual operating cost for year',i+1)
        k[3]=int(input())
    l[i]=k
d=pd.DataFrame(l,columns=['Year','Predicted flow per million vehicle km','Construction Cost','Operating Cost'])
d=d.set_index('Year')
d['Accident Savings']=(acr1-acr2)*aac*d['Predicted flow per million vehicle km']
d['Operating Cost Savings']=(avoc1-avoc2)*d['Predicted flow per million vehicle km']*(10**6)
d['Travel Time Savings']=((1/avs1)-(1/avs2))*avts*d['Predicted flow per million vehicle km']*(10**6)
d['Total User Benefits']=d['Accident Savings']+d['Operating Cost Savings']+d['Travel Time Savings']
d=d.reset_index()
d['Discounted Benefits']=d['Total User Benefits']/((1+(dis/100))**d['Year'])
d['Construction and Maintenance Cost']=d['Construction Cost'].fillna(0)+d['Operating Cost'].fillna(0)
d['Discounted Costs']=d['Construction and Maintenance Cost']/((1+(dis/100))**d['Year'])
d=d.set_index('Year')
d['Discounted Benefits']=d['Discounted Benefits'].fillna(0)
d['Discounted Costs']=d['Discounted Costs'].fillna(0)
del sp
Net_Present_Value=float(np.nansum(d['Discounted Benefits'])-np.nansum(d['Discounted Costs']))
if Net_Present_Value>0:
    print('This project is acceptable with a Net Present Value of ',Net_Present_Value)
else:
    print('This project is not suitable')
d.to_excel('output_Program1.xlsx', sheet_name='Sheet1', index=False)
