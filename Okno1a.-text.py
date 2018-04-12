from tkinter import *
        
def inicializaceOkna():
        okno.title("Ruzne pismo")             # titulek
        okno.geometry("300x200+200+200")  # velikost a umisteni okna 
    
def obsahOkna():
        # texty
        text=Text()                            # vlozi objekt text
        text.pack()                            # zobrazi ho
        text.insert(END, "ahoj, ")             # vlozi text na pozici
        text.insert(END, "svete ")
        text.tag_config("modre", foreground="blue", underline=1)  # nastaveni
        text.insert(END, "\nje to napsano modrou barvou", "modre")
        text.insert(END, "\n")
        text.tag_config("cervene", foreground="red", underline=1, font="Arial 20 bold")
        text.insert(END, "je to cervene", "cervene")
       
                                     
def zviditelneniOkna():
        okno.mainloop()
#  +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++         
okno = Tk()                       # vytvori okno                  
inicializaceOkna()                # zavola funkce
obsahOkna()
zviditelneniOkna() 

   
