#matika
#rodak jan
o="y"
while(o=="y"):
    print("\n")
    print("+_-_*_/")
    print("vyber z nabídky:")
    print("+ scitani")
    print("- nasobeni")
    print("* nasobeni")
    print("/ deleni")
    x=input("vyber operaci : ")
    a=int(input("zadej è1.: "))    
    b=int(input("zadej è2.: "))
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
    o=input("chceš opakovat? (y/n) ")
input()        

