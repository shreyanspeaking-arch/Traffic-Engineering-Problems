import sys
import math as m
print('''Press 1 if you have average headway of vehicles in s
Press 2 if you have average departure rate of vehicles in veh/min
Press 3 if you have the total no of departures within a timeframe and the time taken''')
co=int(input())
if co==1:
    dn=60/float(input('Enter the average headway of vehicles in s'))
elif co==2:
    dn=float(input('Enter the average departure rate of vehicles in veh/min'))
elif co==3:
    dn=0
    t=0
    co2='YES'
    i=1
    while co2.upper()!='NO':
        print(f'For dataset {i}')
        t+=float(input('Enter the time interval in minutes'))
        dn+=float(input('Enter the no of departures in no. of PCUs or vehicles'))
        co2=input('Do you have any more datasets or do you want to go to the next part. If <Yes> press anything/Enter else enter <No>')
        i+=1
    dn/=t
else:
    sys.exit()
print('''Press 1 if you have average arrival rate of vehicles in veh/min
Press 2 if you have the no of arrivals within a timeframe and the time taken''')
co=int(input())
if co==1:
    an=float(input('Enter the average arrival rate of vehicles in veh/min'))
elif co==2:
    an=0
    t=0
    co2='YES'
    i=1
    while co2.upper()!='NO':
        print(f'For dataset {i}')
        t+=float(input('Enter the time interval in minutes'))
        an+=float(input('Enter the no of arrivals in no. of PCUs or vehicles'))
        co2=input('Do you have any more datasets or do you want to go to the next part. If <Yes> press anything/Enter and if <No> enter No')
        i+=1
    an/=t
else:
    sys.exit()
lmda=an/dn
N=int(input('Enter the number of departure channels'))
s=0
for i in range(N):
    s+=(lmda**i)/m.factorial(i)
P0=1/(s+((lmda**N)/(m.factorial(N)*(1-(lmda/N)))))
co=input('Do you want to find the probability of a particular number of vehicles in the queuing system. If <Yes> press anything/enter and if <No> enter No')
PngeN=((lmda**(N+1))*P0)/(m.factorial(N)*N*(1-(lmda/N)))
Q=PngeN/(1-(lmda/N))
W=((lmda+Q)/an)-(1/dn)
t=(lmda+Q)/an
print('The probability of having 0 vehicles in the system is ',P0)
while co.upper()!='NO':
    n=int(input('Enter the number of vehicles whose probability you want to find out'))
    if n<=N:
        Pn=((lmda**n)*P0)/m.factorial(n)
    else:
        Pn=((lmda**n)*P0)/((N**(n-N))*m.factorial(N))
    print('The probability of ',n,'number of vehicles in the queuing system is ',Pn)
    co=input('Do you want to find the probability of a particular number of vehicles in the queuing system. If <Yes> press anything/enter and if <No> enter No')
print('The probability of having no.of vehicles greater than the number of departure lanes is ',PngeN)
print('The average queue length is ',Q,' vehicles.')
print('The average waiting time per vehicle is ',W,' min.')
print('The average queuing time is ',t,' min.')