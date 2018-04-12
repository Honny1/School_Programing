from tkinter import *

def inicializaceOkna():
    okno.title("Zadání")              # titulek 
    okno.geometry("300x200+400+100")  # velikost a umisteni 
    
def obsahOkna():   
    # label Jmeno               
    L1 = Label(okno, text="Jméno:")   # vytvori label (popisek) 
    L1.grid(row=0, column=0)          # umisteni
            
    # vstupni okno
    E1 = Entry(okno, textvariable=Jmeno, width=20)
        # realizuje vstup z klavesnice do promenne Jmeno
    E1.grid(row=0, column=1)
            
    # label Prijmeni 
    L2 = Label(okno, text="Pøíjmení:")   # vytvori label (popisek) 
    L2.grid(row=2, column=0)             # umisteni
                    
    E2 = Entry(okno, textvariable=Prijmeni, width=20)
       # realizuje vstup z klavesnice do promenne Prijmeni
    E2.grid(row=2, column=1)  
    
    # button      
    B1 = Button(okno, text="Výsledek", bg="yellow", command=tisk)
                    # vytvori tlacitko
                    # ommand=tisk   co se stane po stisknuti-zavola fci tisk()
    B1.grid(row=3, column=0) 

def zviditelneniOkna():
    okno.mainloop()

def tisk():            # provede po stisku tlacitka
    # label pro vystup                               
    L3 = Label(okno,text="celé jm:", )# vytvori label 
    L3.grid(row=4, column=0)  
    L4 = Label(okno,textvariable=Jmeno)# vytvori label 
    L4.grid(row=5, column=0)      
    L5 = Label(okno,textvariable=Prijmeni)
    L5.grid(row=5, column=2)        
    
    

#  +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
okno = Tk()                       # vytvori okno    
Jmeno=StringVar()                 # promenna pro vstup       
Prijmeni=StringVar()    

inicializaceOkna()                # zavola funkce
obsahOkna()
zviditelneniOkna() 




        