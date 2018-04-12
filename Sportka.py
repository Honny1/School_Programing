from random import randint
from tkinter import *

def zviditelneniOkna():
    okno.config(menu=hlavniMenu)
    okno.mainloop()
def obsahOkna():
    okno.title("Sportka")
    okno.geometry("300x130+400+100")
    okno.option_add('*Font', 'Arial 20')
    # vytvori rozbalovaci menu


    B1 = Button(okno, text="Spin", bg="yellow", command=random)
    B1.grid(row=0, column=0,padx=5, pady=5)
    B2 = Button(okno, text="END", bg="blue", command=end)
    B2.grid(row=1, column=0, padx=5, pady=5)
    global L1,L2,L3,L4
    L1 = Label(okno, text="0")
    L1.grid(row=0, column=1,padx=5, pady=20)
    L2 = Label(okno, text="0")
    L2.grid(row=0, column=2,padx=5, pady=20)
    L3 = Label(okno, text="0")
    L3.grid(row=0, column=3,padx=5, pady=20)
    L4 = Label(okno, text="                 ")
    L4.grid(row=1, column=2)



def end():
    okno.destroy()

def random():
    a=randint(0,9)
    b=randint(0,9)
    c=randint(0,9)
    L1 = Label(okno, text=a)
    L1.grid(row=0, column=1,padx=5, pady=20)
    L2 = Label(okno, text=b)
    L2.grid(row=0, column=2, padx=5, pady=20)
    L3 = Label(okno, text=c)
    L3.grid(row=0, column=3, padx=5, pady=20)

    if(a==7 or b==7 or c==7):
        x="YOU WIN"

    else:
        x="                "

    L4 = Label(okno, text=x)
    L4.grid(row=1, column=2,sticky=N+S+E+W)
okno = Tk()
hlavniMenu = Menu(okno)
obsahOkna()
zviditelneniOkna()