import math as m
AADTmaj=float(input('Enter average annual daily traffic on major street'))
AADTmin=float(input('Enter average annual daily traffic on minor street'))
c1=int(input('''Enter the serial no. for the general level of pedestrian activity
                1.High
                2.Medium-High
                3.Medium
                4.Medium-Low
                5.Low'''))
if c1==1:
    PedVol=3200
elif c1==2:
    PedVol=1500
elif c1==3:
    PedVol=700
elif c1==4:
    PedVol=240
elif c1==5:
    PedVol=50
nlanes=int(input('Enter the number of lanes on the road'))
AADTtotal=AADTmaj+AADTmin
Nbimv=exp(-10.99+1.07*m.log(AADTmaj)+0.23*m.log(AADTmin))
Nbisv=exp(-10.21+0.68*m.log(AADTmaj)+0.27*m.log(AADTmin))
Npedbase=exp(-9.53+0.4*m.log(AADTtotal)+0.26*m.log(AADTmin/AADTmax)+0.45*m.log(PedVol)+0.04*nlanes)
Nbikei=(Nbimv