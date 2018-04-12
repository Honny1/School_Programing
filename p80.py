#RodakJan
import math 
def x():
    x=(-b)/(2*a)
    print("koren x je:",x)
def x12():
    x=((-b)+math.sqrt(D))/(2*a)
    print("koren x je:",x)
    x1=((-b)-math.sqrt(D))/(2*a)
    print("koren x1 je:",x1)


print("zadej koeficienty kvadratické rovnice podle: ax**2+bx+c=0")
a=int(input("zadej cislo A : "))
b=int(input("zadej cislo B : "))
c=int(input("zadej cislo C : "))
    
D=(b**2)-4*a*c

if (a==0):
    print("nelze dìlit nulou")
else:
    if (D<0):
        print("rovnice nemá reseni v R")
    elif(D!=0):
        x12()
    else:
        x()