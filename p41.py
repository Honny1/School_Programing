import string
rc=input("zadej rodne cislo:")
while (6!=len(rc)):
    print("spatně zadane rodne cislo")
    break
rcd=rc[4:6]
rcm=rc[2:4]
rcr=rc[0:2]
d=int(rcd)
m=int(rcm)
r=int(rcr)
if(m>50):
    print("pohlavi: zena")
    m=m-50
else:
    print("pohlavi: muz")
print("rok:",1900+r,"\nmesic:",m,"\nden:",d)
