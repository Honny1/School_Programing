#Jan Rodak
a=100
b=int(input("zadej koncentraci:"))
c=int(input("zadej celkove mnozstvi:"))
while b>=100:
    b=int(input("spatna koncentrace zadej znovu:"))    
e=(c*b)/a
d=c-e
print("vody",e)
print("octa",d)
