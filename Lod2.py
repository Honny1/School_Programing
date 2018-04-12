from SportPotreby import *


class Lod2(SportPotreby):
    ''' Vlastnosti: cislo, typ, pujceno, pujcovne, osoby'''

    def __init__(self, cislo, typ, pujcovne, osoby):
        SportPotreby.__init__(self, cislo, typ, pujcovne)  # dedicnost
        # vola konstruktor predka
        self.osoby = osoby
        print("Je to lod")  # pomocny vypis

    def __str__(self):
        vystup = SportPotreby.__str__(self)  # vola metodu predka
        vystup += "\nLod typu: " + self.typ + " pro osob:: " + str(self.osoby)
        return vystup