from Bal import Bal
from random import randint, choice
kleuren = [[255,0,0], [0,0,0], [0,0,255], [0,255,0], [255,255,0]]
class Speelkader:
    def __init__(self, breedte, hoogte, aantal, minimum, maximum):
        self.breedte = breedte
        self.hoogte = hoogte
        self.aantal = aantal
        self.min = minimum
        self.max = maximum
    def ballenmaker(self):
        self.ballenlijst = []
        for _ in range(self.aantal):
            straal = randint(self.min, self.max)
            kleur = choice(kleuren)
            bal = Bal(randint(straal, self.breedte-straal), randint(straal, self.hoogte-straal), kleur, straal, randint(-5, 5), randint(-5, 5))
            self.ballenlijst.append(bal)
    def bewegen(self):
        for bal in self.ballenlijst:
            bal.beweeg()
    def geraakt(self, coo):
        geraakte = None
        for bal in self.ballenlijst:
            if bal.geraakt(coo):
                geraakte = bal
        if geraakte:
            self.ballenlijst.remove(geraakte)

    def gebotst(self):
        for bal in self.ballenlijst:
            if bal.cox <= bal.straal or (bal.cox + bal.straal) >= self.breedte:
                bal.bew_hor = bal.bew_hor *-1   
            if (bal.coy - bal.straal <= 0) or (bal.coy + bal.straal >= self.hoogte):
                bal.bew_ver *= -1






