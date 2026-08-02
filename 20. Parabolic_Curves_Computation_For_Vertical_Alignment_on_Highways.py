import sys
print('All values in this code are in m')
t1=tuple(eval(input('Enter coordinates of Tangent Point T1 in the form (x,y)')))
t2=tuple(eval(input('Enter coordinates of Tangent Point T1 in the form (x,y)')))
if len(t1)!=2 or len(t2)!=2:
    print('Invalid Input')
    sys.exit()
L=abs(float(t2[0])-float(t1[0]))
print('Enter slope with sign at '+str(t1)+' in %')
p=float(input())
p/=100
print('Enter slope with sign at '+str(t2)+' in %')
q=float(input())
q/=100
print('''Choose what you want to get:
         1. K value of highway (Horizontal distance required for 1% change in grade
         2. Coordinates of a point on the curve (requires x-coordinate)
         3. Vertical offset(e) at the point of intersection of two tangents
         4. Vertical offset at a point of the curve (requires x-coordinate)
         5. Horizontal and Vertical Offsets at the highest point on the curve
         ''')
c=''
while c.upper()!='N':
    o=int(input('Enter the number for the option you want to select'))
    if o==1:
        K=L/((p-q)*100)
        print('K factor is ',K)
    elif o==2:
        x=float(input('Enter x coordinate'))
        Y=(((q-p)/L)*((x**2)/2))+(p*x)
        print('The coordinates of point are x,Y taking T1 as origin are '+str(tuple(x,Y)))
    elif o==3:
        e=(p-q)*(L/8)
        print('The vertical offset at the point of two tangents at point of intersection is ',e)
    elif o==4:
        x=float(input('Enter x coordinate'))
        y=((p-q)/(2*L))*(x**2)
        Y=(((q-p)/L)*((x**2)/2))+(p*x)
        print('The vertical offset at '+str(tuple(x,Y))+' is ',y)
    elif o==5:
        x=(L*p)/(p-q)
        y=(L*(p**2))/(2*(p-q))
        print('The horizontal offset is ',x,'m and vertical offset is ',y,'m')
    else:
        print('Invalid Input')
    c=input('Do you want to continue. Enter N for no or anything else to continue')
