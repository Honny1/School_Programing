from tkinter import *

def inicializaceOkna():
    okno.title("Poèítání")            # titulek 
    okno.geometry("300x200+400+100")  # velikost a umisteni 
    okno.option_add('*Font', 'Arial 12') #  pismo  pro cele okno 
                                     #(pokud nezmenime pro jednotlive objekty)
 
def zviditelneniOkna():
    okno.mainloop()

def scitani():            # provede po stisku tlacitka
    x = float( E1.get() ) # metoda get - text z ENTRY
    y = float( E2.get() )
    soucet.set( str( x + y ) ) # metoda set() vlozi text na vlostnost z    
   
    L4 = Label(okno,textvariable=soucet)# vytvori label 
    L4.grid(row=3, column=0)      
                  
def odcitani():            # provede po stisku tlacitka
    x = float( E1.get() ) # metoda get - text z ENTRY
    y = float( E2.get() )
    rozdil.set( str( x - y ) ) # metoda set() vlozi text na vlostnost z    
   
    L4 = Label(okno,textvariable=rozdil)# vytvori label 
    L4.grid(row=3, column=1) 

# -----------------------------------------------------------    
okno = Tk()                       # vytvori okno  
soucet=StringVar()                # promenna
rozdil=StringVar() 

inicializaceOkna()                # zavola funkci

#obsahOkna    nemam tady jako funkci
# label Jmeno               
L1 = Label(okno, text="první èíslo:")   # vytvori label (popisek) 
L1.grid(row=0, column=0)          # umisteni        
E1 = Entry(okno)
E1.grid(row=0, column=1)
E1.insert(INSERT,"0") # vlozi text do policka
           
# label Prijmeni 
L2 = Label(okno, text="druhé èíslo:",fg="blue",bg="white")   # vytvori label (popisek) 
L2.grid(row=1, column=0)               # umisteni                     
E2 = Entry(okno)
E2.grid(row=1, column=1)
E2.insert(INSERT,"0") 
    
# button      
B1 = Button(okno, text="Souèet", bg="yellow", command=scitani)
                          # vytvori tlacitko
                          # ommand=scitani   co se stane po stisknuti 
B1.grid(row=2, column=0) 
B2 = Button(okno, text="Rozdíl", bg="blue", command=odcitani)
                           # vytvori tlacitko
                           # ommand=odcitani  co se stane po stisknuti 
B2.grid(row=2, column=1)

zviditelneniOkna()     # zavola funkci