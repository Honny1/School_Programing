#Jan Rodak
import string
v=input("Zadejte vìtu, mezi slovy 1 mezeru, na konci teèku:")
print("veta ma znakù:",len(v),"\nveta ma slov:",1+v.count(" "))
s=input("nahrazovane slovo:")
n=input("nove slovo:")
v=str.replace(v,s,n)
print(v)
print(str.upper(v))
x=0
d=0
V=""
l=len(v)
h=v.count(" ")
for i in range(len(v)):
        p1=""
        p2=""
        p3=""
        if(v[x]==" "):
                d=d+1
                p1=str.upper(v[x])
        elif(d==h):
                p2=str.lower(v[x])        
        else:
                p3=str.upper(v[x])
        x=1+x
        V=V+p1+p2+p3
print(V)


       