#JanRodak
import random
A=[]					
S=[]
f=0
a=int(input("PocetPrvku:"))
for j in range(a): 				  
    for i in range(a): 
        S.append(random.randint(0,2147483647))  
    print(S)				
    A.append(S)		
    S=[]
print(A)
for i in range(a):
    f+=A[i][i]
print("SoucetVDiagonale",f)
input()
