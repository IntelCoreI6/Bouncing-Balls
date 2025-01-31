import pygame
import sys
from pygame.locals import *

# Initialize Pygame
pygame.init()
pygame.display.set_caption("Key Press Display")

# Setup display
WIDTH = 800
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

# Setup font
font = pygame.font.Font(None, 48)

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Main game loop
while True:
    clock.tick(60)
    screen.fill(WHITE)
    
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        
        if event.type == KEYDOWN:
            # Get key name
            key_name = pygame.key.name(event.key)
            print(f"Key pressed: {key_name}")
            
            # Render text
            text = font.render(f"Key pressed: {key_name}", True, BLACK)
            text_rect = text.get_rect(center=(WIDTH/2, HEIGHT/2))
            screen.blit(text, text_rect)
    
    pygame.display.flip()