#JanRodak
x=[]
for i in range(5):
    w=input("PridejJmeno:")
    x.append(w)
a=0
w=input("HledejJmeno:")
for i in range(5):
    if(x[i]==w):
        print("VSeznamJeJmeno",w)
        a+=1
print("VSeznamuSeViskituje",a,"Krat")
        
