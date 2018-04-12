from Kun import *

class Dostih:
    #vlastnosti: nazev, seznam_koni, vitez dostihu
    def __init__(self, nazev):
        self.nazev = nazev
        self.seznam_koni = []
        self.vitez = None
        
    def __str__(self):
        vystup = "Dostih " + self.nazev + ", seznam koni:\n"
        for kun in self.seznam_koni:
            vystup += str(kun) + "\n"
        vystup += "vitez: " + str(self.vitez)
        return vystup
    
     # pridani kone do seznamu koni prihlasenych na dostih (2 body)
    def prihlasit_kone_do_dostihu(self, kun):
        self.seznam_koni.append(kun)

    def vyhlaseni_viteze(self, jmeno_kone):
        for kun in self.seznam_koni:
            if kun.jmeno == jmeno_kone:
                self.vitez = kun
                kun.vyhra_v_dostihu()
                return