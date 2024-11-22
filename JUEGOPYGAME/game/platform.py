import pygame
from .config import *

# CLase Platform hereda de 'pygame.sprite.Sprite'
class Platform(pygame.sprite.Sprite):
    
    def __init__(self):
        # Ejecutamos el metodo init de la clase padre
        pygame.sprite.Sprite.__init__(self)

        # Generar plataforma (superficie)
        self.image = pygame.Surface((WIDTH, 40))
        self.image.fill(GREEN)

        # Rectangulo de la superficie
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = HEIGHT - 40