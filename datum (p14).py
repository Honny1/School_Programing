#Jan_Rodak
#spravne_datum

print("++++spravnost_zadani_datumu++++")
d=int(input("zadej den : "))
m=int(input("zadej mesic : "))
r=int(input("zadej rok : "))
if(((m==1)or(m==3)or(m==5)or(m==7)or(m==8)or(m==10)or(m==12))and(d<=31)and(m<=12)and(r>=1)):
    print("datum je ok")
elif(((m==4)or(m==6)or(m==9)or(m==11))and(d<=31)and(m<=12)and(r>=1)):
    print("datum je ok")
else:
    if(((r%100==0)and(r%400==0)and(r%4==0)and(m==2)and(d<=29)and(m<=12)and(r>=1))):
        print("datum je ok")
    elif((m==2)and(d<29)and(m<=12)and(r>=1)):
        print("datum je ok")
    else:
        print("spatne zadane duatum")
input()