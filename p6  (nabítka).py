#Jan Rodák 
#obsah+obvod kruhu /w nabitka
import math
print("obsah+obvod kruhu")
print("O obsah")
print("S obvod")

x=input("vyber operaci : ")  
r=int(input("zadej polomìr: "))
if((r>0)and(x=="O")):
    print("obsah: ",math.pi*r**2)
elif ((r>0)and(x=="S")):
       print("obvod: ",2*math.pi*r)
else:
    print("chybnì zadaný polomìr nebo oparace")
input()