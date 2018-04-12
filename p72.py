#JanRodak
import random 
P=[] 
s=0
for i in range(5): 
  P.append(random.randint(0,10))
for i in range(5):
  d=P[i]
  if(d%2==0):
    s+=1
print("PoscetSudychCisel:",s)
