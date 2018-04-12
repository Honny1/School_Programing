#hony 
def kontrolaobrazce(a, b):
    if(a==b):
        x=1
    else:
        x=0
    return x

def kontrola(x):
    while x<=0:
        print("error zadej znovu stranu a/b")
        x=int(input("zadej stranu a/b: "))
    return x
        
x=int(input("zadej stranu a: "))
x1=int(input("zadej stranu b: "))

y=kontrola(x)
y1=kontrola(x1)
a=kontrolaobrazce(y, y1)

if a==1:
    print("obrazec je ctverec")
else:
    print("obrazec je obdelnik")
