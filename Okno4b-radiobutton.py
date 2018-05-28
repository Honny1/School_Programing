# radiobutton
from tkinter import *
 #  u kazdeho objektu lze misto grid pouzit .pack()
def inicializaceOkna():
        okno.geometry("500x300+40+15")  # velikost a umisteni 
        okno.title("MU / ENA  ")       # titulek 
        okno.option_add('*Font', 'Arial 12') #  pismo  pro cele okno 
                                             #(pokud nezmenime pro jednotlive objekty)  
                                             
def obsahOkna():  
            
        Radiobutton(okno, text="Muz", variable=v, value=1).grid(row=0, column=0)  
       #  nebo takhle
       #  Radiobutton(okno, text="Muz", variable=v, value=1).pack()
       #  nebo takhle
       #  Radiobutton(okno, text="Muz", variable=v, value=1,command= volani nejake funkce).pack()
        Radiobutton(okno, text="Zena", variable=v, value=2).grid(row=1, column=0)  
        B1 = Button(okno, text="vyber", bg="yellow", command=vyber)
                                    # vytvori tlacitko
                                    # ommand - co se stane po stisknuti (udalost)
        B1.grid(row=2, column=0)  
        
def zviditelneniOkna():
        okno.mainloop()
    
def vyber():            # provede po stisku tlacitka     
        x=v.get()
        
        L1 = Label(okno, text="jmeno:")   # vytvori label (popisek) 
        L1.grid(row=3, column=0)          # umisteni        
        E1 = Entry(okno, width=20)
        E1.grid(row=3, column=1)
        #  nebo takhle misto 2 radu nad tim
        #  E1 = Entry(okno, width=20).pack()
        L2 = Label(okno, text="prijmeni")   # vytvori label (popisek) 
        L2.grid(row=4, column=0)               # umisteni                
        E2 = Entry(okno, width=20)
        E2.grid(row=4, column=1)          
        
        if (x==2):
                L3 = Label(okno, text="rodne")
                L3.grid(row=5, column=0)  
                E3 = Entry(okno, width=20)
                E3.grid(row=5, column=1)                    
                        
# ******************************************************************    
okno = Tk()                       # vytvori okno 
v = IntVar()                      # promenna
inicializaceOkna()                # zavola funkce
obsahOkna()
zviditelneniOkna() 
                                     



                                    
                                     


   




        