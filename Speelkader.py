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
        self.highscore = 0
        self.geschiedenis = []
        self.speed = 7
        self.moeilijk = False
    def ballenmaker(self):
        self.ballenlijst = []
        for _ in range(self.aantal):
            straal = randint(self.min, self.max)
            kleur = choice(kleuren)
            bal = Bal(randint(straal, self.breedte-straal), randint(straal, self.hoogte-straal), kleur, straal, randint(-self.speed, self.speed), randint(-self.speed, self.speed))
            self.ballenlijst.append(bal)
    def bewegen(self):
        for bal in self.ballenlijst:
            bal.beweeg()
            if self.moeilijk:
                #bal.kleur = choice(kleuren)
                bal.straal = randint(10 , bal.straal+10)
                if randint(-1, 1) == 0:
                    bal.bew_hor = bal.bew_ver*-1.02
                elif randint(-1, 1) == 1:
                    bal.bew_ver = bal.bew_hor*-1.02

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






