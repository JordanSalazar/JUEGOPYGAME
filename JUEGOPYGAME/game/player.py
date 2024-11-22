import pygame
from .config import *

# Clase que hereda de la clase 'pygame.sprite.Sprite'
class Player(pygame.sprite.Sprite):

    def __init__(self, left, bottom):
        # Ejecutamos el metodo init de la clase padre
        pygame.sprite.Sprite.__init__(self)

        # Generar una superficie
        self.image = pygame.Surface((40, 40))
        self.image.fill(BLUE)

        self.rect = self.image.get_rect()
        self.rect.left = left
        self.rect.bottom = bottom

        self.pos_y = self.rect.bottom
        self.velocidad_y = 0

        # Validar salto solo en plataforma
        self.can_jump = False

        # atrivututo para parar el movimiento del jugador
        self.playing = True

    
    # Colisión entre obstaculos
    def collide_with(self, sprites):
        objects = pygame.sprite.spritecollide(self, sprites, False)
        if objects:
            return objects[0]


    def collide_botom(self, wall):
        return self.rect.colliderect(wall.rect_top)
    

    def skid(self, wall):
        self.pos_y = wall.rect.top
        self.velocidad_y = 0
        self.can_jump = True


    def validate_plataform(self, platform):
        # Verificar colicion entre sprites (jugador y plataforma)
        result = pygame.sprite.collide_rect(self, platform)
        if result:
            self.velocidad_y = 0
            self.pos_y = platform.rect.top
            self.can_jump = True


    # Salto del jugador
    def jump(self):
        if self.can_jump:
            self.velocidad_y = -23
            self.can_jump = False


    def update_pos(self):
        
        # 1.2 = Gravedad
        self.velocidad_y += PLAYER_GARAVEDAD
        # Implementando una aceleracion sobre el atributo 'pos_y'
        self.pos_y += self.velocidad_y + 0.5 * PLAYER_GARAVEDAD


    def update(self):
        # la actualizacion se hara si o solo si 'playing' es verdadero
        if self.playing:

            self.update_pos()
            # Actualizar 'self.rect.bottom'
            self.rect.bottom = self.pos_y


    def stop(self):
        self.playing = False

