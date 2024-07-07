import pygame
import sys

# Inicialize o Pygame
pygame.init()

# Defina as dimensões da tela
screen_width = 1000
screen_height = 800

# Crie a tela
tela = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Space Invaders by Gabriel J Santos")

# Defina a cor do quadrado (R, G, B)
test_color = (200, 200, 200)  # Vermelho
grid_color = (100, 100, 100)
background_color=(0, 0, 0)
