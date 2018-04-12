from Dostih import *
from Kun import *

kone = []
dostihy = []

# pridani noveho kone do seznamu koni ve staji - vstup vlastnosti kone z klavesnice (4 body)
def nakup_kone(kone):
    JMENO = input("zadej jmeno kone: ")
    ROK = int(input("zadej rok narozeni: "))
    kone.append(Kun(JMENO, ROK))

# vypis vsech koni ve staji (2 body)
def vypis_koni(kone):
    for kun in kone:
        print(kun)
def vytvor_dostih(dostihy, kone):
    nazev = input("zadej nazev dostihu: ")    
    dostih = Dostih(nazev)
    pocet = int(input("zadej, kolik chces na tento dostih prihlasit koni: "))
    for i in range(pocet):
        jmeno = input("zadej jmeno kone: ")
        for kun in kone:
            if kun.jmeno == jmeno:
                break    
        dostih.prihlasit_kone_do_dostihu(kun)
    dostihy.append(dostih)
    
# vypis vsech dostihu (2 body)
def vypis_dostihu(dostihy):
    for dostih in dostihy:
        print(dostih)
        
def urcit_viteze(dostih, jmeno_kone):
    dostih.vyhlaseni_viteze(jmeno_kone)
    
# nakupte do staje aspon 3 kone (2 body)
a=int(input("kolik koupiš koňů:"))
for i in range(a):
    nakup_kone(kone)
kone.append(Kun("PAWEL", 2000))
kone.append(Kun("ANNA", 2008))
kone.append(Kun("HONZA", 1999))
# vytvorte aspon 2 dostihy (2 body)
a=int(input("kolik bude dostihů:"))
for i in range(a):
    vytvor_dostih(dostihy,kone)
# vypiste vsechny dostihy (2 body)
vypis_dostihu(dostihy)

# urcete viteze vsech dostihu (uzivatel zada jmeno kone) (4 body)
for dostih in dostihy:
    jmeno_kone=input("zadej výteze:")
    dostih.vyhlaseni_viteze(jmeno_kone)

#vypiste vsechny kone ve staji (2 body)
vypis_koni(kone)
    
    
        

