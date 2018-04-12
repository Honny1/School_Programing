from SportPotreby import *


class lyze(SportPotreby):
    ''' Vlastnosti: cislo, typ, pujceno, pujcovne, osoby'''

    def __init__(self, cislo, typ, pujcovne, delka):
        SportPotreby.__init__(self, cislo, typ, pujcovne)  # dedicnost
        # vola konstruktor predka
        self.delka = delka
        print("Jsou to lyže")  # pomocny vypis

    def __str__(self):
        vystup = SportPotreby.__str__(self)  # vola metodu predka
        vystup += "\nlyže typu: " + self.typ + " delka: " + str(self.delka)+"cm"
        return vystup