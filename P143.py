x=input("Zadej čislo operace(+ - * / ) číslo:")

def scitani(x,y):
    print("Vysledek je", int(x)+int(y))
def odcitani(x,y):
    print("Vysledek je", int(x)-int(y))
def nasobeni(x,y):
    print("Vysledek je", int(x)*int(y))
def deleni(x,y):
    print("Vysledek je", int(x)/int(y))
for i in x:
    if(i=="+"):
        string = x.split("+")
        scitani(string[0],string[1])
    elif(i=="-"):
        string = x.split("-")
        odcitani(string[0], string[1])
    elif (i == "*"):
        string = x.split("*")
        nasobeni(string[0], string[1])
    elif (i == "/"):
        string = x.split("*")
        deleni(string[0], string[1])