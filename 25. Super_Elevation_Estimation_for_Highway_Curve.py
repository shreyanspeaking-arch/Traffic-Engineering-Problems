import sys
print('This code is based on the IRC 73,2023 Superelevation estimation model')
v=float(input('Enter design speed in kmph'))
R=float(input('Enter Radius of Curvature in m'))
e=float(input('Enter the value of superelevation desired'))
if e<=0 or e>=0.35: # According to Guinness World Records as of 3rd July 2026 maximum superelevation achieved is 0.348 in New Zealand
    print('Something went wrong')
    sys.exit()
e1=((0.75*v)**2)/(225*R)
if e1>=e:
    print('Maximum superelevation to be provided is',e)
    e1=e
else:
    print(e1,'is the estimated superelevation')
    sys.exit()
f=float(input('Enter coefficient of side friction between vehicle tyres and pavement'))
f1=((v**2)/(127*R))-e1
if f1<=f:
    print('Superelevation of',e1,'is safe')
    quit()
else:
    f1=f
    print('Maximum calculated speed is calculated considering superelevation as',e1,'and coefficient of friction as',f1)
    Va=(27.94*R)**0.5
    if Va>v:
        print('Design is adequate and provide superelevation equal to ',e1)
    else:
        print('Speed limit is ',Va)
