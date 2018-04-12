from tkinter import *

def hello():   # tuto funkci volam, protoze nemam vytvoreny dalsi funkce pro vypocty
               # vytvoren pouze obdelnik
    print ( "Ahoj!")
 

def obdelnik():
    def obvod():            # provede po stisku tlacitka
        x = float( E1.get() ) # metoda get - text z ENTRY
        y = float( E2.get() )
        o.set( str(2*( x + y )) ) # metoda set() vlozi text na vlostnost z    
       
        L4 = Label(okno2,textvariable=o)# vytvori label 
        L4.grid(row=4, column=0)      
                      
    def obsah():            # provede po stisku tlacitka
        x = float( E1.get() ) # metoda get - text z ENTRY
        y = float( E2.get() )
        s.set( str( x * y ) ) # metoda set() vlozi text na vlostnost z    
       
        L4 = Label(okno2,textvariable=s)# vytvori label 
        L4.grid(row=4, column=1)     
    
    okno2 = Toplevel()    # vytvori dalsi okno
    okno2.geometry("300x200+400+100")
    okno2.title("Vypocet obdelniku")
          # tady pokracujete stejne, jak to znate
          # zadat strany atd.
    o=StringVar()                # promenna
    s=StringVar()           
    L1 = Label(okno2, text="delka:")   # vytvori label (popisek)
    L1.grid(row=0, column=0)          # umisteni        
    E1 = Entry(okno2)
    E1.grid(row=0, column=1)
    E1.insert(INSERT,"0") # vlozi text do policka
                    
    L2 = Label(okno2, text="sirka:",fg="blue",bg="white")   # vytvori label (popisek)
    L2.grid(row=1, column=0)               # umisteni                     
    E2 = Entry(okno2)
    E2.grid(row=1, column=1)
    E2.insert(INSERT,"0") 
              
          # button      
    B1 = Button(okno2, text="Obvod", bg="yellow", command=obvod)
                                    # vytvori tlacitko
                                    # ommand=scitani   co se stane po stisknuti 
    B1.grid(row=2, column=0) 
    B2 = Button(okno2, text="Obsah", bg="blue", command=obsah)
                                     # vytvori tlacitko
                                     # ommand=odcitani  co se stane po stisknuti 
    B2.grid(row=2, column=1)              

okno = Tk()   
hlavniMenu = Menu(okno)

# vytvori rozbalovaci menu
menu2D = Menu(hlavniMenu, tearoff=0)
menu2D.add_command(label="ctverec", command=hello)
menu2D.add_command(label="obdelnik", command=obdelnik)
menu2D.add_separator()
menu2D.add_command(label="trojuhelnik", command=hello)
hlavniMenu.add_cascade(label="2D", menu=menu2D)

# dalsi rozbalovaci menu
menu3D = Menu(hlavniMenu, tearoff=0)
menu3D.add_command(label="krychle", command=hello)
menu3D.add_command(label="kvadr", command=hello)
menu3D.add_separator()
menu3D.add_command(label="koule", command=hello)
menu3D.add_command(label="valec", command=hello)
hlavniMenu.add_cascade(label="3D", menu=menu3D)

# dalsi rozbalovaci menu
menuHelp = Menu(hlavniMenu, tearoff=0)
menuHelp.add_command(label="O aplikaci", command=hello)
hlavniMenu.add_cascade(label="Navod", menu=menuHelp)

# zobrazeni menu
okno.config(menu=hlavniMenu)

mainloop()
