d=float(input('Enter Degree of Curve'))
r=1750/d
v=float(input('Enter Speed of vehicle in km/h'))
g=float(input('Enter guage length in mm'))
ca=(g*(v**2))/(127*r)
cd={'BG':75,'MG':50,'NG':0}
ce={'BG':75,'MG':65,'NG':0}
ga=input('Enter BG for Broad Guage, MG for Meter Guage, NG for Narrow Guage')
ga=ga.upper()
cd=cd[ga]
ce=ce[ga]
l=max([0.008*ca*v,0.008*cd*v,0.72*cd])
if ca<cd:
   ca=cd-ca
   print('Permissible cant is ',ca,'mm')
elif ca>ce:
   ca=ca-ce
   print('Permissible cant is ',ca,'mm')
if ga=='BG':
   v=0.27*(((ca+cd)*r)**0.5)
elif ga=='MG':
   v=0.347(((ca+cd)*r)**0.5)
elif ga=='NG':
   v=3.65*((r-6)**0.5)
print('Speed of vehicle is ',v,' km/h.')
