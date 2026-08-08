import pandas as pd
import numpy as np
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
#The equation for average vehicle operation cost savings per km
#has to be entered in the program as a function of average vehicle speed 
print('The equation for average vehicle operation cost savings per km per vehicle per year \n','has to be entered in the program as a function of average vehicle speed. \n','Change it if needed.')
def avoc(x):
    return (2+(35/x)+(0.00005*(x**2)))/100
avoc1=avoc(avs1)
avoc2=avoc(avs2)
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
print(d)
d.to_excel('output.xlsx', sheet_name='Sheet1', index=False)