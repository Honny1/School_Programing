#JanRodak
import random 
P=[]
k=0
for i in range(10): 
  P.insert(i,random.randint(0,10))
h=int(input("HledaneCislo:"))
for i in range(10):
  if(P[i]==h):
    k+=1
print("HledaneCisloSeVyskytuje",k,"Krat")

