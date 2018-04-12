#JanRodak
x=[]
for i in range(7):
    w=int(input("NamerenaHodnaota:"))
    x.append(w)
x.sort()
print(x)
w=int(input("NamerenaHodnaota:"))
for i in range(7):
    if (w<x[i]):
        x.insert(i,w)
        break
        

print(x)