import sys
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
print('''Press 1 if you have average rate of vehicles in veh/min
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
Q=(lmda**2)/(1-lmda)
W=lmda/(dn*(1-lmda))
t=1/(dn-an)
print('The average queuing length is ',Q,' vehicles.')
print('The average queuing time is ',t,'min.')
print('The average waiting time per vehicle in queue is ',W,'min.')
co=input('Do you want to see find out the probability of any no of vehicles in the queuing system. If <Yes> press anything/enter and if <No> enter No')
while co.upper()!='NO':
    n=int(input('What is the number of vehicles whose probability you want to check'))
    Pn=(1-lmda)*(lmda**n)
    print('The probability of ',n,' vehicles in the queuing system is ',Pn)
    co=input('Do you want to see find out the probability of any no of vehicles in the queuing system. If <Yes> press anything/enter and if <No> enter No')