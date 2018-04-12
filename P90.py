def uvod():
    print("                *** autor: Rodák  ***")
    print("                *** ukazka funkci      ***")
    
def nacteni():
    a=int(input("Zadej èíslo: "))
    return a

def vypis(cislo1):
    print("Vypis cisla je: ", cislo1)
    
def soucet(cislo1, cislo2):
    vysledek=cislo1+cislo2
    return vysledek
    
def soucet1(cislo1, cislo2, cislo3):
    cislo3=cislo1+cislo2
    
def vymena(cislo1,cislo2):
    x=cislo1
    cislo1=cislo2
    cislo2=x
    
a=nacteni()
b=nacteni()
c=0
soucet1(a,b,c)

vypis(a)
vypis(b)

vysled=soucet(a,b)
print("Výsledek souètu je: ",vysled)


    