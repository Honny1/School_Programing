#matika
#rodak jan
o="y"
while(o=="y"):
    print("\n")
    print("+_-_*_/")
    print("vyber z nab�dky:")
    print("+ scitani")
    print("- nasobeni")
    print("* nasobeni")
    print("/ deleni")
    x=input("vyber operaci : ")
    a=int(input("zadej �1.: "))    
    b=int(input("zadej �2.: "))
    if(x=="+"):
        print("soucet",a+b)
    elif(x=="-"):
        print("rozdil",a-b)
    elif(x=="*"):
        print("nasobek",a*b)
    elif(x=="/"):
        print("deleni",a/b)
    else:
        print("chibne zadana operace")
    o=input("chce� opakovat? (y/n) ")
input()        

