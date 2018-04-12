def nacti_cislo():
    while (True):
        try:
            cislo = int(input("zadej cislo:"))
        except ValueError:
            print("není to cislo(CHCI INT :* )")
        else:
            return cislo
def deleni(x,y):
    try:
        z = x / y
    except (ZeroDivisionError):
        print("POZOR, JSI HŇUP CO DELI NULOU")
    else:
        return (z)
print(deleni(nacti_cislo(),nacti_cislo()))