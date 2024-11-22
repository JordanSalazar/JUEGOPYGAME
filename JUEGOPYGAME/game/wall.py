import pygame
from .config import *
#
from .player import Player


class Wall(pygame.sprite.Sprite):

    def __init__(self, left, bottom):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.Surface((40, 80))
        self.image.fill(RED)

        self.rect = self.image.get_rect()
        self.rect.left = left
        self.rect.bottom = bottom

        self.vel_x = SPEED

        # generamos un rectangulo para que este en la superficie de los obstaculos
        self.rect_top = pygame.Rect(self.rect.x, self.rect.y, self.rect.width, 1) # en la parte superior de cada obstaculo con un ancho igual y 1 pixel de alto


    def update(self):
        self.rect.left -= self.vel_x

        # actualizar posicion de rectangulo sobre obstaculos
        self.rect_top.x = self.rect.x # asi nos celsioramos que el rectangulo siempre se encuentre en la parte superior 


    def stop(self):
        self.vel_x = 0