from tkinter import *
from math import *
def zviditelneniOkna():
    okno.config(menu=hlavniMenu)
    okno.mainloop()

def hello():
    pass

def obsahOkna():
    okno.title("Vypocty")
    okno.geometry("300x200+400+100")
    # vytvori rozbalovaci menu
    menu2D = Menu(hlavniMenu, tearoff=0)
    menu2D.add_command(label="ctverec", command=ctverec)
    menu2D.add_command(label="obdelnik", command=obdelnik)
    menu2D.add_separator()
    menu2D.add_command(label="trojuhelnik", command=trojuhelnik)
    hlavniMenu.add_cascade(label="2D", menu=menu2D)

    # dalsi rozbalovaci menu
    menu3D = Menu(hlavniMenu, tearoff=0)
    menu3D.add_command(label="krychle", command=krychle)
    menu3D.add_command(label="kvadr", command=kvadr)
    menu3D.add_separator()
    menu3D.add_command(label="koule", command=koule)
    menu3D.add_command(label="valec", command=valec)
    hlavniMenu.add_cascade(label="3D", menu=menu3D)

def ctverec():
    def obvod():
        x = float(E1.get())
        o.set(str(4*x))

        L4 = Label(okno2, textvariable=o)
        L4.grid(row=4, column=0)

    def obsah():
        x = float(E1.get())
        s.set(str(x * x))

        L4 = Label(okno2, textvariable=s)
        L4.grid(row=4, column=1)

    def obsahOkna2():
        global okno2
        okno2 = Toplevel()
        okno2.geometry("300x200+400+100")
        okno2.title("Vypocet ctverce")

        L1 = Label(okno2, text="Strana A:")
        L1.grid(row=0, column=0)
        global E1
        E1 = Entry(okno2)
        E1.grid(row=0, column=1)
        E1.insert(INSERT, "0")

        # button
        B1 = Button(okno2, text="Obvod", bg="yellow", command=obvod)
        B1.grid(row=2, column=0)
        B2 = Button(okno2, text="Obsah", bg="blue", command=obsah)
        B2.grid(row=2, column=1)

    obsahOkna2()
    o = StringVar()
    s = StringVar()

def trojuhelnik():
    def obvod():
        x = float(E1.get())
        o.set(str(3*x))

        L4 = Label(okno2, textvariable=o)
        L4.grid(row=4, column=0)

    def obsah():
        x = float(E1.get())
        s.set(str((x * x)/2))

        L4 = Label(okno2, textvariable=s)
        L4.grid(row=4, column=1)

    def obsahOkna2():
        global okno2
        okno2 = Toplevel()
        okno2.geometry("300x200+400+100")
        okno2.title("Vypocet rovnostrany trojuhelnik")

        L1 = Label(okno2, text="Strana A:")
        L1.grid(row=0, column=0)
        global E1
        E1 = Entry(okno2)
        E1.grid(row=0, column=1)
        E1.insert(INSERT, "0")


        # button
        B1 = Button(okno2, text="Obvod", bg="yellow", command=obvod)
        B1.grid(row=2, column=0)
        B2 = Button(okno2, text="Obsah", bg="blue", command=obsah)
        B2.grid(row=2, column=1)

    obsahOkna2()
    o = StringVar()
    s = StringVar()

def obdelnik():
    def obvod():
        x = float(E1.get())
        y = float(E2.get())
        o.set(str(2 * (x + y)))

        L4 = Label(okno2, textvariable=o)
        L4.grid(row=4, column=0)

    def obsah():
        x = float(E1.get())
        y = float(E2.get())
        s.set(str(x * y))

        L4 = Label(okno2, textvariable=s)
        L4.grid(row=4, column=1)

    def obsahOkna1():
        global okno2
        okno2 = Toplevel()
        okno2.geometry("300x200+400+100")
        okno2.title("Vypocet obdelniku")

        L1 = Label(okno2, text="delka:")
        L1.grid(row=0, column=0)
        global E1
        E1 = Entry(okno2)
        E1.grid(row=0, column=1)
        E1.insert(INSERT, "0")

        L2 = Label(okno2, text="sirka:", fg="blue", bg="white")
        L2.grid(row=1, column=0)
        global E2
        E2 = Entry(okno2)
        E2.grid(row=1, column=1)
        E2.insert(INSERT, "0")

        # button
        B1 = Button(okno2, text="Obvod", bg="yellow", command=obvod)
        B1.grid(row=2, column=0)
        B2 = Button(okno2, text="Obsah", bg="blue", command=obsah)
        B2.grid(row=2, column=1)

    obsahOkna1()
    o = StringVar()
    s = StringVar()
#----------------------------------------------------------------------------------
def kvadr():
    def povrch():
        x = float(E1.get())
        y = float(E2.get())

        o.set(str(6 * (x * y)))

        L4 = Label(okno2, textvariable=o)
        L4.grid(row=4, column=0)

    def obejm():
        x = float(E1.get())
        y = float(E2.get())
        z = float(E3.get())
        s.set(str((x * y)*z))

        L4 = Label(okno2, textvariable=s)
        L4.grid(row=4, column=1)

    def obsahOkna1():
        global okno2
        okno2 = Toplevel()
        okno2.geometry("300x200+400+100")
        okno2.title("Vypocet kvadr")

        L1 = Label(okno2, text="delka:")
        L1.grid(row=0, column=0)
        global E1
        E1 = Entry(okno2)
        E1.grid(row=0, column=1)
        E1.insert(INSERT, "0")

        L2 = Label(okno2, text="sirka:", fg="blue", bg="white")
        L2.grid(row=1, column=0)
        global E2
        E2 = Entry(okno2)
        E2.grid(row=1, column=1)
        E2.insert(INSERT, "0")

        L3 = Label(okno2, text="vyska:")
        L3.grid(row=2, column=0)
        global E3
        E3 = Entry(okno2)
        E3.grid(row=2, column=1)
        E3.insert(INSERT, "0")

        # button
        B1 = Button(okno2, text="Povrch", bg="yellow", command=povrch)
        B1.grid(row=3, column=0)
        B2 = Button(okno2, text="Obejm", bg="blue", command=obejm)
        B2.grid(row=3, column=1)

    obsahOkna1()
    o = StringVar()
    s = StringVar()

def krychle():
    def povrch():
        x = float(E1.get())
        o.set(str((x*x)*6))

        L4 = Label(okno2, textvariable=o)
        L4.grid(row=4, column=0)

    def obejm():
        x = float(E1.get())
        s.set(str((x * x)*x))

        L4 = Label(okno2, textvariable=s)
        L4.grid(row=4, column=1)

    def obsahOkna2():
        global okno2
        okno2 = Toplevel()
        okno2.geometry("300x200+400+100")
        okno2.title("Vypocet Krychle")

        L1 = Label(okno2, text="Strana A:")
        L1.grid(row=0, column=0)
        global E1
        E1 = Entry(okno2)
        E1.grid(row=0, column=1)
        E1.insert(INSERT, "0")

        # button
        B1 = Button(okno2, text="Povrch", bg="yellow", command=povrch)
        B1.grid(row=2, column=0)
        B2 = Button(okno2, text="Obejm", bg="blue", command=obejm)
        B2.grid(row=2, column=1)

    obsahOkna2()
    o = StringVar()
    s = StringVar()

def koule():
    def povrch():
        x = float(E1.get())
        o.set(str(round(4*z*x,2)))

        L4 = Label(okno2, textvariable=o)
        L4.grid(row=4, column=0)

    def obejm():

        x = float(E1.get())
        s.set(str(round((4/3)*z*x**3,2)))

        L4 = Label(okno2, textvariable=s)
        L4.grid(row=4, column=1)

    def obsahOkna2():
        global okno2
        okno2 = Toplevel()
        okno2.geometry("300x200+400+100")
        okno2.title("Vypocet koule")

        L1 = Label(okno2, text="Polomer:")
        L1.grid(row=0, column=0)
        global E1
        E1 = Entry(okno2)
        E1.grid(row=0, column=1)
        E1.insert(INSERT, "0")

        # button
        B1 = Button(okno2, text="Povrch", bg="yellow", command=povrch)
        B1.grid(row=2, column=0)
        B2 = Button(okno2, text="Obejm", bg="blue", command=obejm)
        B2.grid(row=2, column=1)

    obsahOkna2()
    o = StringVar()
    s = StringVar()

def valec():
    def povrch():
        x = float(E1.get())
        y = float(E2.get())
        o.set(str(round(2*z*x*(x+y),2)))

        L4 = Label(okno2, textvariable=o)
        L4.grid(row=4, column=0)

    def obejm():
        x = float(E1.get())
        y = float(E2.get())
        s.set(str(round(z*x**2*y,2)))

        L4 = Label(okno2, textvariable=s)
        L4.grid(row=4, column=1)

    def obsahOkna1():
        global okno2
        okno2 = Toplevel()
        okno2.geometry("300x200+400+100")
        okno2.title("Vypocet Valec")

        L1 = Label(okno2, text="polomer:")
        L1.grid(row=0, column=0)
        global E1
        E1 = Entry(okno2)
        E1.grid(row=0, column=1)
        E1.insert(INSERT, "0")

        L2 = Label(okno2, text="vyska:", fg="blue", bg="white")
        L2.grid(row=1, column=0)
        global E2
        E2 = Entry(okno2)
        E2.grid(row=1, column=1)
        E2.insert(INSERT, "0")

        # button
        B1 = Button(okno2, text="Povrch", bg="yellow", command=povrch)
        B1.grid(row=2, column=0)
        B2 = Button(okno2, text="Obejm", bg="blue", command=obejm)
        B2.grid(row=2, column=1)

    obsahOkna1()
    o = StringVar()
    s = StringVar()
#----------------------------------------------------------------------------------
okno = Tk()
hlavniMenu = Menu(okno)
z=pi
obsahOkna()
zviditelneniOkna()