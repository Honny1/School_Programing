#Jan Rodak
o="y"
o1="y"
o2="y"
while(o=="y"):
    o="y"
    o1="y"
    o2="y"
    print("1 - trojúhelník")
    print("2 - obdélník/ètverec")
    x=input("vyber utvar: ")
    if(x=="1"):
        while(o1=="y"):
            print("1 - trojúhelník")
            a=int(input("zadej stranu a:"))
            b=int(input("zadej stranu b:"))
            c=int(input("zadej stranu c:"))
            if(a+b>c and a+c>b and c+b>a):
                print("trojuhelnik lze sestrojit")
                if(a==b and b==a and a==c and c==a and c==b and b==c):
                    print("trojuhelnik je rovnostrany")
                elif(a==b and a==c)or(b==a and b==c)or(c==b and c==a):
                    print("trojuhelnik je rovnoramenny")
                else:
                    print("trojuhelnik je obecny")                   
                if(a**2+b**2==c**2 or c**2+b**2==a**2 or a**2+c**2==b**2):
                    print("trojuhelnik je pravouhly")
                    o1=input("\nnavrat do 1 - trojúhelník? (y/n):")
                    o=input("\nnavrat do nabidky? (y/n):")               
                else:
                    print("trojuhelnik neni pravouhly")
                    o=input("\nnavrat do nabidky? (y/n):")
            else:
                print("trojuhelnik nelze sestrojit")
                o1=input("\nnavrat do 1 - trojúhelník? (y/n):")
                o=input("\nnavrat do nabidky? (y/n):")
    elif(x==2):
        while(o2=="y"):
            print("2 - obdélník/ètverec")
            a=int(input("zadej stranu a:"))
            b=int(input("zadej stranu b:"))
            if(a==b):
                print("je to ètverec")
                o=input("\nnavrat do nabidky? (y/n):")
                o2=input("\nnavrat do 2 - obdélník/ètverec (y/n):")                
            else:
                print("je to obdelink")
                o=input("\nnavrat do nabidky? (y/n):")
                o2=input("\nnavrat do 2 - obdélník/ètverec (y/n):")

            