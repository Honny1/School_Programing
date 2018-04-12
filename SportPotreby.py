# ++++++++ class SportPotreby +++++++++++++++++++++++++++++++++++++++++++++++++
class SportPotreby:
    ''' Vlastnosti: cislo, typ, pujceno, pujcovne '''

    def __init__(self, cislo, typ, pujcovne):
        self.cislo = cislo
        self.typ = typ
        self.pujcovne = pujcovne
        self.pujceno = False
        print("Nova sport potreba")

    def __str__(self):
        vystup = "Sportovni potreba cislo: " + str(self.cislo)
        vystup += " typ: " + (self.typ)
        vystup += " , pujcovne: " + str(self.pujcovne) + "Kc, "
        if self.pujceno:  # if self.pujceno==True:
            vystup += " pujceno"
        else:
            vystup += " na sklade"
        return vystup

    def pujcit(self):
        self.pujceno = True

    def vratit(self):
        self.pujceno = False
