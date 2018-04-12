class Kun:
    #vlastnosti: jmeno, rok_narozeni, pocet_vitezstvi
    def __init__(self, jmeno, rok_narozeni):
        self.jmeno = jmeno
        self.rok_narozeni = rok_narozeni        
        self.pocet_vitezstvi = 0
        
    def __str__(self):
        vystup = "Kun " + self.jmeno + ", narozen: " + str(self.rok_narozeni)
        vystup += ", zvitezil: " + str(self.pocet_vitezstvi) + "x"
        return vystup
    
    # koni, ktery vyhral dostih, se zvedne pocet vitezstvi o 1 (2 body)
    def vyhra_v_dostihu(self):
        self.pocet_vitezstvi=+1