from Lod2 import *
from lyze import *
from kola import *

kajak = Lod2(2, "kajak", 150, 2)
print(kajak)
kajak.pujcit()
print(kajak)
kajak.vratit()
print(kajak)

lode=[]
lode.append(Lod2(89, "Silniční",300,36))
lode.append(Lod2(99, "horské",200, 96))
lode.append(Lod2(777, "horské",150, 88))
def printLod():
    for lod in lode:
        print(lod)
def pujcitLod():
    x= int(input("Zadej číslo:"))
    for lod in lode:
        if(lod.cislo==x):
            lod.pujcit()

def vLod():
    x= int(input("Zadej číslo:"))
    for lod in lode:
        if(lod.cislo==x):
            lod.vratit()


lyze2 = lyze(66, "sjezd", 150, 190)
print(lyze2)
lyze2.pujcit()
print(lyze2)
lyze2.vratit()
print(lyze2)

lyze1=[]
lyze1.append(lyze(99, "sjezd",250,136))
lyze1.append(lyze(109, "bězky",300, 196))
lyze1.append(lyze(767, "kratké",150, 50))
def printLyze():
    for lyze3 in lyze1:
        print(lyze3)

def pujcitLyze():
    x = int(input("Zadej číslo:"))
    for lyze3 in lyze1:
        if(lyze3.cislo==x):
            lyze3.pujcit()
def vLyze():
    x = int(input("Zadej číslo:"))
    for lyze3 in lyze1:
        if(lyze3.cislo==x):
            lyze3.vratit()


kolo = kola(77, "horske", 190, 80)
print(kolo)
kolo.pujcit()
print(kolo)
kolo.vratit()
print(kolo)

kola1=[]
kola1.append(kola(89, "Silniční",300,36))
kola1.append(kola(99, "horské",200, 96))
kola1.append(kola(777, "horské",150, 88))
def printkolo():
    for kolo in kola1:
        print(kolo)
def pujcitKolo():
    x = int(input("Zadej číslo:"))
    for kolo in kola1:
        if(kolo.cislo==x):
            kolo.pujcit()

def vKolo():
    x = int(input("Zadej číslo:"))
    for kolo in kola1:
        if(kolo.cislo==x):
            kolo.vratit()

def pridatKolo():
    x = int(input("Zadej číslo:"))
    x1 = input("Zadej typ:")
    x2 = int(input("Zadej cena:"))
    x3 = int(input("Zadej velikost:"))
    kola1.append(kola(x, x1, x2, x3))
def pridatlod():
    x = int(input("Zadej číslo:"))
    x1 = input("Zadej typ:")
    x2 = int(input("Zadej cena:"))
    x3 = int(input("Zadej pocet osob:"))
    lode.append(Lod2(x, x1, x2, x3))

def pridatLyze():
    x = int(input("Zadej číslo:"))
    x1 = input("Zadej typ:")
    x2 = int(input("Zadej cena:"))
    x3 = int(input("Zadej velikost:"))
    lyze1.append(lyze(x, x1, x2, x3))

def printVypujcene():
    for lod in lode:
        if(lod.pujceno==True):
            print(lod)
    for lyze3 in lyze1:
        if(lyze3.pujceno==True):
            print(lyze3)
    for kolo in kola1:
        if(kolo.pujceno==True):
            print(kolo)

while True:
    print("i end")
    print("pujcovna")
    print("1 pujcit kolo")
    print("2 pujcit Lod")
    print("3 pujcit Lyze")
    print("4 vratit kolo")
    print("5 vratit Lod")
    print("6 vratit lyže")
    print("7 přidat lyze")
    print("8 přidat kolo")
    print("9 přidat lod")
    print("10 print lode")
    print("11 print kola")
    print("12 print lyze")
    print("13 print vypujcené")
    x=input("vyber operaci : ")

    if(x=="1"):
        pujcitKolo()
    elif (x=="2"):
           pujcitLod()
    elif (x=="3"):
        pujcitLyze()
    elif (x=="4"):
        vKolo()
    elif (x=="5"):
        vLod()
    elif (x=="6"):
        vLyze()
    elif (x=="7"):
        pridatLyze()
    elif(x=="8"):
        pridatKolo()
    elif(x=="9"):
        pridatlod()
    elif(x=="i"):
        break;
    elif(x=="10"):
        printLod()
    elif(x=="11"):
        printkolo()
    elif(x=="12"):
        printLyze()
    elif(x=="13"):
        printVypujcene()
    else:
        print("chybně zadaná oparace")