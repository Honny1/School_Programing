print("++++++  spojeni retezcu  ++++++++++++++++++++\n")    
print("\n")	                               
a = "sviti" 
b = " " 
c = "slunce " 
vysl=a+b
vysl=vysl+c
print(" vysledek spojeni je: " ,vysl)   
print("\n")

print("++++++  delka retezcu  ++++++++++++++++++++++\n")    
print("\n")
print(" delka retezce a je: " ,len(a))
   # nebo takhle
delka=len(c)
print(" delka retezce c je: " ,delka)
print("\n")

print("++++++  je znak v retezci?  ++++++++++++++++++\n")    
print("\n")
zn="t"
print(" je zn v retezci a?  " ,zn in a)
   # nebo takhle
jetam=zn in c				# not in   …. Neni tam
print(" je zn v retezci c?  " ,jetam)
print("\n")

print("++++++  cast retezce +++++  ++++++++++++++++++\n")    
print("\n")
print(" od 3 do 5 znaku  " ,a [3:5])
   # nebo takhle
cast=c [3:5]
print(" od 3 do 5 znaku  " ,cast)
print("\n")

print("++++++  koverze retezce na cislo++++++++++++++\n")    
print("\n")
cislice=input(" zadej retezec z cislic: " )
cislo=int(cislice)
print(cislo+1)
input()

Øetìzcové funkce
import string

print("++++++  koverze retezce na cislo++++++++++++++\n")    
print("\n")
cislice=input(" zadej retezec z cislic: " )
cislo=int(cislice)
print(cislo+1)
input()

print("++++++  pismena na velka a na mala++++++++++++++\n")    
print("\n")
slovo=input(" zadej slovo: " )
velke=str.upper(slovo)         #prevede pismena na velka
male=str.lower(slovo)          #prevede pismena na mala
print(velke)
print(male)
input() 

print("++++++  nahrada podretezce jinym podretezcem++++++++++++++\n")    
print("\n")
veta=input(" zadej vetu: " )
veta=str.replace(veta,"zima","teplo")    # misto zima vlozi teplo
print(veta)
      #  nebo takhle
stary=input(" co chces zmenit: " )
novy=input(" co tam napsat: " )
veta=str.replace(veta,stary,novy)        
print(veta)
input()
