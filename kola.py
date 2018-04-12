from SportPotreby import *


class kola(SportPotreby):
    ''' Vlastnosti: cislo, typ, pujceno, pujcovne, osoby'''

    def __init__(self, cislo, typ, pujcovne, velikost):
        SportPotreby.__init__(self, cislo, typ, pujcovne)  # dedicnost
        # vola konstruktor predka
        self.velikost = velikost
        print("Je to lod")  # pomocny vypis

    def __str__(self):
        vystup = SportPotreby.__str__(self)  # vola metodu predka
        vystup += "\nkolo typu: " + self.typ + " velikost: " + str(self.velikost)
        return vystup