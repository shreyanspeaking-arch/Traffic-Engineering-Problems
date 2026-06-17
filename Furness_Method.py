import pandas as pd
n=int(input('Enter the number of zones'))
l=[]
for i in range(n):
    k=[0 for i in range(n)]
    for j in range(n):
        if i==j:
            k[j]=0
        else:
            print('Enter the no of trips with origin as zone',i+1,'and destination as zone',j+1)
            k[j]=int(input())
    l+=[k]
a=pd.DataFrame(l,index=[i for i in range(1,n+1)],columns=[i for i in range(1,n+1)])
j=[0 for i in range(n)]
k=[0 for i in range(n)]
for i in range(n):
    print('Enter forecasted no of origins in zone',i+1)
    j[i]=int(input())
for i in range(n):
    print('Enter forecasted no of destinations in zone',i+1)
    k[i]=int(input())
js=[0 for i in range(n)]
ks=[0 for i in range(n)]
for i in range(n):
    js[i]=float(j[i])/a.iloc[i].sum()
    ks[i]=float(k[i])/a.iloc[:,i].sum()
def f(a,b):
    for i in a:
        if i>1.05 or i<0.95:
            return False
    for i in b:
        if i>1.05 or i<0.95:
            return False
    return True
while f(js,ks)==False:
    for i in range(n):
        s1=a.iloc[i].sum()
        js[i]=float(j[i])/s1
    for i in range(n):
        a.iloc[i]*=js[i]
    for i in range(n):
        s2=a.iloc[:,i].sum()
        ks[i]=float(k[i])/s2
    for i in range(n):
        a.iloc[:,i]*=ks[i]
a=a.astype(int)
print(a)
