#JanRodak
#A
import random 
P=[]
x=0
s=0
pocetprvku=0
for i in range(10): 
  P.append(random.randint(0,10))
print(P)
b=max(P)
print("NejvedsiCislo:",b)
print("IndexNejvedsihoCisla:",P.index(b)) 
P.sort()
P.reverse()
print("PoleSestupne:",P)
print ("DvaNejmensiPrvky:",P[-1],";",P[-2])
for n in range (10):
    x+=P[n]
print("PrumerPrvkuVPoly:",x/len(P))
for i in range(0,10,2):
     s+=P[i]
print("SoucetPrvkuSeSudymiIndexi:",s)

