#Jan Rod�k 
#obsah+obvod kruhu
import math
o="y"
while(o=="y"):
    print("\n")
    print("obsah+obvod kruhu")
    print("o obsah")
    print("s obvod")
    x=input("vyber operaci : ")  
    r=int(input("zadej polom�r: "))
    if((r>0)and(x=="o")):
        print("obsah: ",math.pi*r**2)
    elif ((r>0)and(x=="s")):
        print("obvod: ",2*math.pi*r)
    else:
        print("chybn� zadan� polom�r nebo oparace")
    o=input("chce� opakovat? (y/n) ")
input()
