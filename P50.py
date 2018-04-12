#Jan Rodak
l=0
p=1
df=0
o="y"
op1="y"
op2="y"
op3="y"
heslo="111"
h=input("zadej heslo:")
while(h!=heslo):
        print("spatne heslo")
        p=p+1
        if(p==3):
                break
        h=input("zadej znovu heslo:")
else:
        while(o=="y"):
                l=0
                p=1
                df=0
                o="y"
                op1="y"
                op2="y"
                op3="y"                
                print("1 - Podlahar")
                print("2 - Zahradnik")
                print("3 - Expedice")                            
                x=input("vyber profesi: ")  
                if(x=="1"):
                        while(op1=="y"):
                                print("\nPodlahar")
                                b=int(input("zadej pocet mistnosti:"))
                                for i in range(b):
                                        d=int(input("delka mistnosti(m):"))
                                        s=int(input("zadej sirku(m):"))
                                        ls=d*s
                                        l=ls+l
                                        df=(l/100)*102+df
                                print("plocha mistnosti(m^2):",l,"\nptrebny material(m^2):",(l/100)*102)
                                print("\ncelkovy material(m^2):",df)
                                op1=input("\nspustit znovu program pro Podlahare? (y/n):")
                        o=input("\nnavrat do nabitky? (y/n):")
                elif(x=="2"):
                        while(op2=="y"):
                                print("\nZahradnik")
                                z=int(input("zadej sirku zahonu(cm):"))
                                sz=int(input("zadej delku zahonu(cm):"))
                                vz=int(input("zadej vzdalenost sazenic(cm):"))
                                print("pocet sazenic v zahonu:",(z//vz)*(sz//vz))
                                op2=input("\nspustit znovu program pro Zahradnika? (y/n):")
                        o=input("\nnavrat do nabitky? (y/n):")
                elif(x=="3"):
                        while(op3=="y"):
                                print("\nExpedice")
                                ks=int(input("pocet zbozi(ks):"))
                                ksk=int(input("kapacita krabice(ks):"))
                                pk=ks//ksk
                                pkif=ks%ksk
                                if(pkif>=1):
                                        pk=pk+1
                                print("potrebny pocet krabic(ks):",pk)
                                op3=input("\nspustit znovu program pro Expedici? (y/n):")
                        o=input("\nnavrat do nabitky? (y/n):")
                else:
                        print("zadal jsi spatnou moznost nebo cislo")
                        o=input("\nnavrat do nabitky? (y/n):")

                
        