import random 
p=[] 

def  bubble(pocet, pole):          			 
 for i in range(pocet-1):               			 
        for j in range(pocet-1): 
              if pole[j] >  pole[j+1]:   		
                  pom =   pole[j]
                  pole[j] = pole[j+1]
                  pole[j+1] = pom
def newPole(a):
 for i in range(a): 
   p.insert(i,random.randint(0,10))
def newPole1(a):
 for i in range(a):
  p.append(int(input("Zadej prvek: ")))  
   
def polePodSebou(pocet, pole):
 for i in range (pocet):
  print(pole[i])

def plusJeden():
 p.append(int(input("Zadej prvek: ")))
 

print("++++++  vyber generovani pole  ++++++++++\n")     
print("1 NacteniSeznamuZeVstupu")
print("2 Vygenerovani")
x=input("vyber operaci : ")
pp=int(input("zadej velikost pole:"))
if x=="1":
 newPole1(pp)
 print(p) 
elif x=="2":
 newPole(pp)
 print(p)
else:
	print("chybne zadana matematicka operace")

print("++++++  vyber praci s polem  ++++++++++\n")     
print("1 vypis prvku podsebou")
print("2 BubbleSort")
print("3 pridat prvek na konec seznamu")
print("\n")	                                    
x=input("vyber operaci : ")

if x=="1":
	polePodSebou(pp, p)
elif x=="2":
	bubble(pp,p)                         
	print(p)
elif x=="3":
	plusJeden()
	print(p)
else:
	print("chybne zadana matematicka operace")
