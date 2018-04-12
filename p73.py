#JanRodak
import random 
P=[] 
s=0
b=int(input("PocetPrvkuPole:"))
for i in range(b): 
  P.append(random.randint(0,10))
print(P)
a=max(P)
print(a)
P.sort()
P.reverse()
print(P[0],P[1])