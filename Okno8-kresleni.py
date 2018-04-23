# kreleni na platno
from tkinter import *

okno = Tk()                       # vytvori okno 
okno.geometry("500x300+200+200")  # velikost a umisteni 
okno.title("kresleni")  
platno = Canvas(okno, width=400, height=280, bg="yellow")  # vytvori v okne platno
platno.pack()
        
platno.create_line(50, 100, 200, 220, fill="red", dash=(8, 4)) # usecka
platno.create_rectangle(150, 25, 250, 75, fill="blue")         # obdelnik 
oval = platno.create_oval(50,100,150,250)                      # oval (elipsa) 

circle=platno.create_oval(150,150,260,260,fill="green")            # oval (kruznice) 
platno.create_text(200,100,text="geometrie")

   
# vyzkousejte ruzne hodnoty cisel
# co to znamena?
# zmente a pridejte dalsi parametry
# napr. mente barvu obrysu a vzorku
# nakreslete nejaky obrazek (domecek, hvezdicku....)
# muzete vyuzit napr. cyklus pro kopirovani tvaru dokola
# podrobnejsi popis a inspiraci hledejte zde:
# http://www.python-course.eu/tkinter_canvas.php
#        x0  y0   x1  y1
body = [10,40,40,40,50,10,60,40,90,40,65,60,75,90,50,70,25,90,35,60]
platno.create_polygon(body, fill='orange', outline='red')
okno.mainloop()