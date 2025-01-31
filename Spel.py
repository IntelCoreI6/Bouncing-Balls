import pygame,sys,time
from pygame.locals import *
from Bal import Bal
from Speelkader import Speelkader
from Timer import Timer
def teken_tekst (tekst,lettergrootte,kleur,cox,coy,lettertype = None):
    ltype = pygame.font.Font (lettertype,lettergrootte) # bepaalt het lettertype en -grootte van je tekst, None betekent dat het standaard lettertype gebruikt wordt
    grafische_tekst = ltype.render (tekst,True,kleur) # render je tekst, zet het om in een grafische vorm
    coordinaat = [cox,coy] # coördinaat van de linkerbovenhoek van je tekst
    scherm.blit (grafische_tekst,coordinaat) # teken je tekst op het canvas


def teken_bal (bal):
    coordinaat = [bal.cox,bal.coy]
    pygame.draw.circle (scherm,bal.kleur,coordinaat,bal.straal)

breedte_scherm = 1000
hoogte_scherm = 500
afmetingen = [breedte_scherm,hoogte_scherm]
rood = [255,0,0]
wit = [255,255,255]
#bal = Bal(100, 100, rood, 16, 0.01, 0.01)
speelkader = Speelkader(breedte_scherm, hoogte_scherm, 10, 10, 50)
timer = Timer(9)

pygame.init()
pygame.display.set_caption ("Botsende ballen")
scherm = pygame.display.set_mode(afmetingen)
clock = pygame.time.Clock()
speelkader.ballenmaker()

while True:
    clock.tick(30)
    for event in pygame.event.get():
        if event.type == QUIT:            
            pygame.quit()
            sys.exit()
        if event.type == MOUSEBUTTONDOWN:#als er een muisknop ingedrukt wordt op je scherm
            speelkader.geraakt(pygame.mouse.get_pos())
        if event.type == pygame.KEYDOWN:
               if event.key == pygame.K_RETURN and timer.running == False:
                    print("Game is running")
                    timer.start_de_klok()
                    speelkader.ballenmaker()
    scherm.fill(wit)
    if timer.running:
        for bal in speelkader.ballenlijst:
            teken_bal(bal)
        speelkader.bewegen()
        speelkader.gebotst()
        timer.controleer_klok()
        teken_tekst (f"tijd resterend: {timer.seconden}",50,rood,100,10)
        teken_tekst (f"score: {speelkader.aantal - len(speelkader.ballenlijst)}",50,rood,breedte_scherm-150,10)
    else:
        teken_tekst ("klik op enter om te starten",50,rood,10,10)
        teken_tekst (f"score: {speelkader.aantal - len(speelkader.ballenlijst)}",100 ,rood,350,250)


    pygame.display.update()