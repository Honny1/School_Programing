import string
import random
a=int(input("zadej velikost:"))
A=[]
S=[]
for j in range(a): 				  
    for i in range(a):
        x=i**2
        if (x<10):
            z=str(x)
            s="0"+z
        else:
            s=str(x)
        S.insert(i,s)
    del S[0]
    S.insert(j,"00")
    print(S)
   
				
    A.append(S)		
    S=[]
print(A)