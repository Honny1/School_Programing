#Jan rodak
s=0
print("pocet zaku ve tride")
y=int(input("zadej kolik je trid:"))
for n in range(y):
    x=int(input("zadej pocet zaku:"))
    s=s+x
print("pocet zaku ve skole:",s)
print("prumerny pocet zaku ve skole",s/y)
