#Jan rodak

z=0
k=0
c=0
print("secti cisela")
y=int(input("zadej kolik cisel zadas:"))
for n in range(y):
    x=int(input("zadej cislo:"))
    if(x>0):
        k=k+1
    else:
        if(x<0):
            z=z+1
        else:
            c=c+1
print("kladna cisla",k,"\nzaporna cisla",z,"\nnulova cisla",c)
