import pygame,sys,time
from pygame.locals import *


def teken_bal (bal):
    coordinaat = [bal["cox"],bal["coy"]]
    pygame.draw.circle (scherm,bal["kleur"],coordinaat,bal["straal"])

def teken_tekst (tekst,lettergrootte,kleur,cox,coy,lettertype = None):
    ltype = pygame.font.Font (lettertype,lettergrootte) # bepaalt het lettertype en -grootte van je tekst, None betekent dat het standaard lettertype gebruikt wordt
    grafische_tekst = ltype.render (tekst,True,kleur) # render je tekst, zet het om in een grafische vorm
    coordinaat = [cox,coy] # coördinaat van de linkerbovenhoek van je tekst
    scherm.blit (grafische_tekst,coordinaat) # teken je tekst op het canvas


breedte_scherm = 1000
hoogte_scherm = 500
afmetingen = [breedte_scherm,hoogte_scherm]
rood = [255,0,0]
wit = [255,255,255]
bal = {"cox":150,"coy":200,"kleur":rood,"straal": 10, "bew_hor": 2, "bew_ver":-2}#let op bal is een dictionary in dit voorbeeld
tekst = "Hier komt tekst"

#### INITIALIZEREN SCHERM ####
pygame.init()
pygame.display.set_caption ("Botsende ballen")
scherm = pygame.display.set_mode(afmetingen)

while True:
    for event in pygame.event.get():
        if event.type == QUIT:            
            pygame.quit()
            sys.exit()
        if event.type == MOUSEBUTTONDOWN:#als er een muisknop ingedrukt wordt op je scherm
            positie_muis = pygame.mouse.get_pos()
            tekst = f"x-coördinaat : {positie_muis[0]} en y-coördinaat : {positie_muis[1]}."
        if event.type == pygame.KEYDOWN: # als er een toets op je toetsenbord ingedrukt wordt...
               if event.key == pygame.K_LEFT: # controleer welke knop er ingedrukt is, is het de knop met pijltje naar links dan...
                            tekst = "links"
           
    scherm.fill(wit)
    teken_bal(bal)
    teken_tekst (tekst,50,rood,100,10)
    pygame.display.update()
    
    time.sleep (0.1)