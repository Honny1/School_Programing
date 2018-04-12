#Jan Rodak
zz=[]
x=0
z=0
vetsi=0

for n in range (10):
    zz.append (int(input("Zadej prvek: ")))
print (zz)
print("\n")

print (zz[int(input("Zadej pozici prvku: "))])


for n in range (10):
    x+=zz[n]
print ("Souèet je: ",x)
print("\n")
k=int(input("Zadej poèet pøidanıch prvkù: "))
for n in range (k):
    zz.append(int(input("Zadej prvek: ")))
print (zz[10:10+k])
print("\n")

j=int(input("Zadej prvek ktery chceš smazat: "))
del zz[j]
print (zz)
print("\n")

a=min(zz)                       
b=max(zz)
print("Nejmensi prvek je: ",a)
print("Nejvetsi prvek je: ",b)

zz.sort()                       
print("Seøazené prvky od nejmenšího po nejvìtší jsou: ",zz)

for n in range(len(zz)):
    if zz[n]>5:
        vetsi=vetsi+1
print ("Èísel vìtších ne 5 je: ", vetsi)

for i in range(0,10,2):
    print("pièa",zz[i])

