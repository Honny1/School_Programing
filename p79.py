#JanRodak
print("+++Evidence+++")
JmenoAVek=[]					
E=[["Hony",17], ["Tereza", 20]]
o="y"
while(o=="y"):
    o="y"
    print("1 - PridatOsobu")
    print("2 - VypsatEvidenci")
    print("3 - VypsatOsobu")
    print("4 - OpravitVekUzadaneOsoby")
    print("5 - SmazatOsobuPodleJmena")
    x=input("\nVyberCinnost: ")
    if(x=="1"):
        print("\n1 - PridatOsobu")
        for j in range(1): 
            Jmeno=input("ZadeJmeno:")
            Vek=int(input("ZadejVek:"))    
            for i in range(1): 
                JmenoAVek.append(Jmeno)
                JmenoAVek.append(Vek)
                print(JmenoAVek)				
                E.append(JmenoAVek)
                JmenoAVek=[]
                o=input("\nnavrat do nabidky? (y/n):")
    elif(x=="2"):
        print("\n2 - VypsatEvidenci")
        print(E)
        o=input("\nnavrat do nabidky? (y/n):")
    elif(x=="3"):
        print("\n3 - VypsatOsobu")
        Jmeno=input("ZadejJmeno:")
        for j in range(len(E)):
            for i in range(1):
                if(E[j][0]==Jmeno):
                    print(E[j][:2])
                    break
        o=input("\nnavrat do nabidky? (y/n):")
    elif(x=="4"):
        print("\n4 - OpravitVekUzadaneOsoby")
        Jmeno=input("ZadejJmeno:")
        for j in range(len(E)):
            for i in range(1):
                if(E[j][0]==Jmeno):
                    print(E[j][:2])
                    del E[j][1]
                    E[j].insert(1,int(input("ZadejNovyVek:")))
                    print(E[j][:2])
                    break
        o=input("\nnavrat do nabidky? (y/n):")
    elif(x=="5"):
        print("\n5 - SmazatOsobuPodleJmena")
        Jmeno=input("ZadejJmeno:")
        for j in range(len(E)):
            for i in range(1):
                if(E[j][0]==Jmeno):
                    print(E[j][:2])
                    del E[j]
                    print(E)    
                    break
        o=input("\nnavrat do nabidky? (y/n):")