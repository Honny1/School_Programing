from tkinter import *

def inicializaceOkna():
    okno.title("Pocitani")
    okno.geometry("400x200+400+100")
    okno.option_add('*Font', 'Arial 12')

def zviditelneniOkna():
    okno.mainloop()

def obsahOkna():
    L1 = Label(okno, text="prvni cislo:")
    L1.grid(row=0, column=0)
    global E1
    E1 = Entry(okno, fg="blue", bg="yellow")
    E1.grid(row=0, column=1)
    E1.insert(INSERT, "0")

    L2 = Label(okno, text="druhe cislo:", fg="blue", bg="white")
    L2.grid(row=1, column=0)
    global E2
    E2 = Entry(okno)
    E2.grid(row=1, column=1)
    E2.insert(INSERT, "0")

    L3 = Label(okno, text="Vysledek:", fg="blue", bg="white")
    L3.grid(row=3, column=0)

    Radiobutton(okno, text="Scitani", variable=v, value=1).grid(row=2, column=0)
    Radiobutton(okno, text="Odecitani", variable=v, value=2).grid(row=2, column=1)
    Radiobutton(okno, text="Nasobeni", variable=v, value=3).grid(row=2, column=2)
    B1 = Button(okno, text="=", bg="yellow", command=vyber)
    B1.grid(row=0, column=2)

def scitani(x,y):
    soucet.set(str(x + y))
    L4 = Label(okno, textvariable=soucet)
    L4.grid(row=3, column=1)

def odcitani(x,y):
    rozdil.set(str(x - y))
    L5 = Label(okno, textvariable=rozdil)
    L5.grid(row=3, column=1)

def nasobeni(x,y):
    nasobek.set(str(x * y))
    L6 = Label(okno, textvariable=nasobek)
    L6.grid(row=3, column=1)

def vyber():
    z = v.get()
    x = int(E1.get())
    y = int(E2.get())
    if(z==1):
        scitani(x,y)
    elif(z==2):
        odcitani(x,y)
    elif(z==3):
        nasobeni(x,y)
    else:
        pass

# -----------------------------------------------------------
okno = Tk()

v = IntVar()
soucet = StringVar()
rozdil = StringVar()
nasobek = StringVar()

inicializaceOkna()
obsahOkna()
zviditelneniOkna()