x=0
d=0
V=""
v="Máma mele maso."
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
