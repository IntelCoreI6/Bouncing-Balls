from Figuur import Figuur
from math import sqrt

class Bal(Figuur):
    def __init__(self, cox, coy, kleur, straal, bew_hor, bew_ver):
        super().__init__(cox, coy, kleur)
        self.straal = straal
        self.bew_hor = bew_hor
        self.bew_ver = bew_ver
    def geraakt(self, coo):
        if sqrt((coo[0]-self.cox)**2 + (coo[1]- self.coy)**2) <= self.straal:
            print("geraakt")
            return True
        else:
            return False
    def beweeg(self):
        self.cox += self.bew_hor
        self.coy += self.bew_ver