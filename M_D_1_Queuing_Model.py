import numpy as np
print('''Press 1 if you have average headway of vehicles in s
Press 2 if you have average departure rate of vehicles in veh/min''')
co=int(input())
if co==1:
    dn=60/float(input('Enter the average headway of vehicles in s'))
elif co==2:
    dn=float(input('Enter the average departure rate of vehicles in veh/min'))
an=float(input('Enter the average arrival rate of vehicles in veh/min'))
ur=an/dn
Q=(ur**2)/(2*(1-ur))
W=ur/(2*dn*(1-ur))
t=W+(1/dn)
print('The average number of vehicles in queue is ',Q)
print('The average waiting time per vehicle in queue is ',W,' min or ',W*60,'s')
print('The average queuing time is ',t,' min or ',t*60,'s')





