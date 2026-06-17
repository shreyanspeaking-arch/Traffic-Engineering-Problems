import numpy as np
n=int(input('Enter number of years taken for analysis'))
d=float(input('Discount Rate per annum'))
s=0
for i in range(n+1):
    if i==0:
        
    print('Enter Value of Benefits in year',1)
    b=float(input())
    print('Enter Value of Cost in year',1)
    c=float(input())
    s+=(b-c)/((1+d)**i)
print('Net Present Value is',s)
