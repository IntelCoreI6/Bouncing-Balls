import pygame,sys,time
from pygame.locals import *
from Bal import Bal
import asyncio
import pygame_gui
import pygame_gui.elements
import time
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

class Timer:
    def __init__(self, seconden):
        self.game_time = seconden
        self.seconden = seconden
        self.tijd = 0
    def start_de_klok(self):
        self.tijd = time.time()
    def controleer_klok(self):
        if time.time() - self.tijd >= 1:
            self.seconden -= 1
            self.tijd = time.time()
        if self.seconden <= 0:
            self.seconden = 0  # Ensure the timer does not go negative
    def reset(self):
        self.seconden = self.game_time
        self.tijd = 0

def teken_tekst (tekst,lettergrootte,kleur,cox,coy,lettertype = None):
    ltype = pygame.font.Font (lettertype,lettergrootte) # bepaalt het lettertype en -grootte van je tekst, None betekent dat het standaard lettertype gebruikt wordt
    grafische_tekst = ltype.render (tekst,True,kleur) # render je tekst, zet het om in een grafische vorm
    coordinaat = [cox,coy] # coördinaat van de linkerbovenhoek van je tekst
    scherm.blit (grafische_tekst,coordinaat) # teken je tekst op het canvas

# Load a nicer font for the game title
title_font = "freesansbold.ttf"

def teken_bal (bal):
    coordinaat = [bal.cox,bal.coy]
    pygame.draw.circle (scherm,bal.kleur,coordinaat,bal.straal)

def teken_rechthoek (x,y,breedte,hoogte,kleur):
    pygame.draw.rect(scherm,kleur,(x,y,breedte,hoogte))

def rechthoek_geraakt(coo, breedte_scherm, hoogte_scherm):
    x = breedte_scherm // 2
    y = hoogte_scherm // 2 + 220
    h = 15
    b = h
    if coo[0] >= x and coo[0] <= x + b and coo[1] >= y and coo[1] <= y + h:
        speelkader.moeilijk = not speelkader.moeilijk
    else:
        return False


breedte_scherm = 1000
hoogte_scherm = 500
afmetingen = [breedte_scherm,hoogte_scherm]
rood = [255,0,0]
wit = [255,255,255]
grijs = [128, 128, 128]
zwart = [0,0,0]
groen = [0, 255, 0]
#bal = Bal(100, 100, rood, 16, 0.01, 0.01)
speelkader = Speelkader(breedte_scherm, hoogte_scherm, 10, 10, 50)
timer = Timer(9)
game_state = "menu"  # Possible states: "menu", "running", "game_over"

pygame.init()
pygame.display.set_caption ("Botsende ballen")
scherm = pygame.display.set_mode(afmetingen)
clock = pygame.time.Clock()
speelkader.ballenmaker()

# Initialize pygame_gui
manager = pygame_gui.UIManager(afmetingen)

# Create sliders for configuration
slider_height = 30

speed_slider = pygame_gui.elements.UIHorizontalSlider(
    relative_rect=pygame.Rect((breedte_scherm // 2 - 250, hoogte_scherm // 2 - 60 + 25), (300, slider_height)),
    start_value=speelkader.speed,
    value_range=(1, 25),
    manager=manager
)

aantal_slider = pygame_gui.elements.UIHorizontalSlider(
    relative_rect=pygame.Rect((breedte_scherm // 2 - 250, hoogte_scherm // 2 + 10 + 25), (300, slider_height)),
    start_value=speelkader.aantal,
    value_range=(1, 100),
    manager=manager
)

min_size_slider = pygame_gui.elements.UIHorizontalSlider(
    relative_rect=pygame.Rect((breedte_scherm // 2 - 250, hoogte_scherm // 2 + 80 + 25), (300, slider_height)),
    start_value=speelkader.min,
    value_range=(5, 50),
    manager=manager
)

max_size_slider = pygame_gui.elements.UIHorizontalSlider(
    relative_rect=pygame.Rect((breedte_scherm // 2 - 250, hoogte_scherm // 2 + 850 + 25), (300, slider_height)),
    start_value=speelkader.max,
    value_range=(5, 50),
    manager=manager
)

timer_slider = pygame_gui.elements.UIHorizontalSlider(
    relative_rect=pygame.Rect((breedte_scherm // 2 - 250, hoogte_scherm // 2 + 150 + 25), (300, slider_height)),
    start_value=timer.seconden,
    value_range=(1, 60),
    manager=manager
)

def main():
    for bal in speelkader.ballenlijst:
        teken_bal(bal)
    speelkader.bewegen()
    speelkader.gebotst()
    timer.controleer_klok()
    teken_tekst (f"time remaining: {timer.seconden}",50,rood,10,10)
    teken_tekst (f"score: {speelkader.aantal - len(speelkader.ballenlijst)}",50,rood,breedte_scherm-150,10)
    if timer.seconden <= 0:
        global game_state
        game_state = "game_over"

def menu():
    teken_tekst("Bouncing Balls", 70, rood, breedte_scherm // 2 - 250, hoogte_scherm // 2 -230, title_font)
    teken_tekst("Press Enter to Start the Game", 40, grijs, breedte_scherm // 2 - 250, hoogte_scherm // 2-130)
    teken_tekst(f"Highscore: {speelkader.highscore}", 40, rood, breedte_scherm // 2 - 250, hoogte_scherm // 2 -95)
    teken_tekst(f"Ball Speed: {speelkader.speed}", 30, zwart, breedte_scherm // 2 - 250, hoogte_scherm // 2 - 60)
    teken_tekst(f"Number of Balls: {speelkader.aantal}", 30, zwart, breedte_scherm // 2 - 250, hoogte_scherm // 2 + 10)
    teken_tekst(f"Ball Size: min = {speelkader.min}, max = {speelkader.max}", 30, zwart, breedte_scherm // 2 - 250, hoogte_scherm // 2 + 80)
    teken_tekst(f"Game Time: {timer.seconden} seconds", 30, zwart, breedte_scherm // 2 - 250, hoogte_scherm // 2 + 150)
    teken_tekst(f"Extreme difficulty", 30, zwart, breedte_scherm // 2 - 250, hoogte_scherm // 2 + 220)
    if speelkader.moeilijk:
        kleur = groen
    else:
        kleur = zwart
    teken_rechthoek(breedte_scherm // 2, hoogte_scherm // 2 + 220 , 15, 15, kleur)
    manager.draw_ui(scherm)

def game_over():
    score = speelkader.aantal - len(speelkader.ballenlijst)
    teken_tekst("Game Over", 100, rood, breedte_scherm // 2 - 250, hoogte_scherm // 2 - 150, title_font)
    teken_tekst("Press Enter to Restart", 50, rood, breedte_scherm // 2 - 250, hoogte_scherm // 2 - 50)
    teken_tekst(f"Final Score: {score}", 50, rood, breedte_scherm // 2 - 250, hoogte_scherm // 2 + 50)
    speelkader.geschiedenis.append(score)
    if score > speelkader.highscore:
        speelkader.highscore = score

while True:
    time_delta = clock.tick(30) / 1000.0
    for event in pygame.event.get():
        if event.type == QUIT:            
            pygame.quit()
            sys.exit()
        if event.type == MOUSEBUTTONDOWN:
            speelkader.geraakt(pygame.mouse.get_pos())
            rechthoek_geraakt(pygame.mouse.get_pos(),breedte_scherm, hoogte_scherm)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                if game_state == "menu":
                    timer.start_de_klok()
                    speelkader.ballenmaker()
                    game_state = "running"
                elif game_state == "game_over":
                    game_state = "menu"
                    timer.reset()
                    speelkader.ballenlijst.clear()
        manager.process_events(event)

    manager.update(time_delta)
    scherm.fill(wit)
    if game_state == "running":
        main()
    elif game_state == "menu":
        menu()
        speelkader.speed = speed_slider.get_current_value()
        speelkader.aantal = int(aantal_slider.get_current_value())
        speelkader.min = int(min_size_slider.get_current_value())
        speelkader.max = int(max_size_slider.get_current_value())
        timer.seconden = int(timer_slider.get_current_value())
    elif game_state == "game_over":
        game_over()

    pygame.display.update()
