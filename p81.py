#JANRODAK
p1=[]
p2=[]
fix=[]
temp=[]
P3=[]
import random  
def f1():
    q=0
    for i in range(len(p1)):
        for j in range(len(p2)):
            if(p1[i]==p2[j]):
                q+=1
    return q

def gen():         
    p1=random.sample(range(1,10), 7)
    return p1        
    

def genUser():
    p2=[]
    x=6
    for i in range(x):
        h=1+i
        z=int(input("Zadej svoji sazku pro {}. cislo:".format(h)))
        while(z<0 or z>49):
            print("error number out of range(1-49)")
            print("zadej znovu")
            z=int(input("Zadej svoji sazku pro {}. cislo:".format(h)))
        else:
            p2.insert(i,z)
    return p2
          
            
def kontrolaAutizmu(data):
    
    
    for x in data:
	    if x in temp:
		    
		    fixAutizmu(x)
		    pass
		    
	    else:
		    temp.append(x)
    return temp
	
def fixAutizmu(x):
    print ("zadali jste vice krat cislo {}",format(x))
    h=x
    z=int(input("zadejte cislo jine nez {} cislo:".format(h)))
    while(z<0 or z>49 or z==x):
	    print("error number out of range(1-49) or same number")
	    print("zadej znovu")
	    z=int(input("zadejte cislo jine nez {} cislo:".format(h)))
    else:
	    fix.append(z)    
    return fix

def okP2():
    
    for i in range (len(temp)):
	            P3.append(temp[i])
    for j in range (len(fix)):
	            P3.append(fix[j])    
                
def dc():
    Dc=p1[0]
    del p1[0]
    return Dc

def dck(DC, A):
    x=0
    if (DC==A):
        x+=1
    return x

def qqq():
    w=0
    a=int(input("Zadej dodatkove cislo:"))
    
    for i in range(len(p2)):
	    while(a<0 or a>49 or a==p2[i]):
			    print("error number out of range(1-49) or same number")
			    print("zadej znovu")
			    a=int(input("zadejte cislo jine nez jste zadali cislo:"))
    return a

def clear():
    del p1[:]
    del p2[:]    
    del fix[:]
    del temp[:]	
    del P3[:]

    
a="y"
while(a=="y"):
    
    clear()
    
    p2=genUser()
    kontrolaAutizmu(p2)    
    okP2()
    p2=P3
    
    p1=gen()
    
    Dc=dc() 
    nwm=qqq()
    
    c=f1()
    a=dck(Dc, nwm)
    
    print("\n")
    print("vygenerovna cisla:",p1,"\ndodoatkove cislo:",Dc)
    print("vase cisla:",p2, "\nvase dodatkove cislo:", nwm)
    if(c==6):
        print("prvni cena")    
    elif(c==6 and a>=1):
        print("druha cena")
    elif(c==5):
        print("treti cena")
    elif(c==4):
        print("ctvrta cena")
    elif(c==3):
        print("pata cena")
    else:
        print("smula")
    a=input("znovu sazet? y/n :") 
    