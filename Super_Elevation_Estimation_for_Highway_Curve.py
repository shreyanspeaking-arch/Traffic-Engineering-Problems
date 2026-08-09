import sys
print('This code is based on the IRC 73,2023 Superelevation estimation model')
v=float(input('Enter design speed in kmph'))
R=float(input('Enter Radius of Curvature in m'))
co=int(input('''Enter 1 if the value of desired superelevation is 0.07 and
Enter 2 if it is something else'''))
if co==2:
    e=float(input('Enter the value of superelevation desired'))
elif co==1:
    e=0.07
else:
    print('Invalid Input')
    sys.exit()
if e<=0 or e>=0.35: # According to Guinness World Records as of 3rd July 2026 maximum superelevation achieved is 0.348 in New Zealand
    print('Value of superelevation is not possible')
    sys.exit()
e1=((0.75*v)**2)/(127*R)
if e1>=e:
    print('Maximum superelevation to be provided is',e)
    e1=e
else:
    print(e1,'is the estimated superelevation')
    sys.exit()

f1=((v**2)/(127*R))-e1
co=int(input('''Enter 1 if the value of desired coefficient of friction is 0.15 and
Enter 2 if it is something else'''))
if co==2:
    f=float(input('Enter coefficient of side friction between vehicle tyres and pavement'))
elif co==1:
    f=0.15
else:
    print('Invalid Input')
    sys.exit()
if f1<f:
    print('Superelevation of',e1,'is safe')
    sys.exit()
else:
    f1=f
    print('Maximum calculated speed is calculated considering superelevation as',e1,'and coefficient of friction as',f1)
    Va=(127*(e1+f1)*R)**0.5
    if Va>v:
        print('Design is adequate and provide superelevation equal to ',e1)
    else:
        print('Speed limit is ',Va)
