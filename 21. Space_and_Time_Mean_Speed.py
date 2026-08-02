def space_mean_speed(verbose=False):
    n=int(input('Enter the number of vehicles assessed'))
    L=float(input('Enter the length of the specv=0ific road (in m)'))
    t=0
    for i in range(n):
        print('Enter time taken by vehicle ',i+1,' in s.')
        t+=float(input())
    Vs=L/(t/n)
    if verbose:
        print('The Space Mean Speed is ',Vs,'m/s')
    else:
        return Vs
def time_mean_speed(verbose=False):
    n=int(input('Enter the number of vehicles assessed'))
    v=0
    for i in range(n):
        print('Enter the time taken by the vehicle ',i+1,' in m/s.')
        v+=float(input())
    Vt=v/n
    if verbose:
        print('The Time Mean Speed is ',Vt,'m/s')
    else:
        return Vt
time_mean_speed(True)
space_mean_speed(True)
