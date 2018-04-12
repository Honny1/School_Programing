#Jan Rodák 
#obsah+obvod kruhu
import math
o="y"
while(o=="y"):
    print("\n")
    print("obsah+obvod kruhu")
    print("o obsah")
    print("s obvod")
    x=input("vyber operaci : ")  
    r=int(input("zadej polomìr: "))
    if((r>0)and(x=="o")):
        print("obsah: ",math.pi*r**2)
    elif ((r>0)and(x=="s")):
        print("obvod: ",2*math.pi*r)
    else:
        print("chybnì zadaný polomìr nebo oparace")
    o=input("chceš opakovat? (y/n) ")
input()
