import pygame
import sys
from .config import *
from .platform import Platform
from .player import Player
from .wall import Wall
import random


# clase principal
class Game:
    def __init__(self):
        pygame.init()

        self.surface = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption(TITLE)

        self.running = True

        self.playing = True

        self.clock = pygame.time.Clock()


    # iniciar el juego    
    def start(self):
        self.new()


    # generar un nuevo juego    
    def new(self):
        self.generate_elements()
        self.run()



    # generar los diferentes elementos que ocupemos en el juego
    def generate_elements(self):

        # Generamos elementos
        self.platform = Platform()
        self.player = Player(100, self.platform.rect.top - 200)

        # Creacion de grupo 'sprites'
        self.sprites = pygame.sprite.Group()
        self.walls = pygame.sprite.Group()

        # Agregamos elementos al grupo 'sprites'
        self.sprites.add(self.platform)
        self.sprites.add(self.player)

        # Ejecucion del metodo 'generate_walls'
        self.generate_walls()


    def generate_walls(self):

        last_position = WIDTH + 100
        if not len(self.walls) > 0:

            for w in range(0, MAX_WALLS):

                left = random.randrange(last_position + 200, last_position + 400)
                wall = Wall(left, self.platform.rect.top)

                last_position = wall.rect.right

                self.sprites.add(wall)
                self.walls.add(wall)


    # ejecuta el juego    
    def run(self):
        #clock = pygame.time.Clock()
        while self.running:
            self.clock.tick(FPS)
            self.events()
            self.draw()
            self.update()
            #clock.tick(60)  # Ajusta la tasa de refresco aquí


    # escuchara diferentes eventos que puedan susitarce    
    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                pygame.quit()
                sys.exit()

        # Tecla precionada
        key = pygame.key.get_pressed()
        # Validacion si tecla es  == SPACE
        if key[pygame.K_SPACE]:
            # Ejecucion de metodo jump
            self.player.jump()


    # pintara los elementos del video juego    
    def draw(self):
        self.surface.fill(BLACK)

        self.sprites.draw(self.surface)


    # actualizar la pantalla    
    def update(self):
        # la actualizacion se hara si y solo si 'playing' es verdadero
        if self.playing:
            pygame.display.flip()

            # validar colision antes que la actualizacion
            wall = self.player.collide_with(self.walls)
            if wall:
                if self.player.collide_botom(wall):
                    self.player.skid(wall)
                else:
                    self.stop()

            # Ejecutar el metodo 'update'
            self.sprites.update()

            # Ejecutar metodo 'validate_plataform'
            self.player.validate_plataform(self.platform)

            self.update_elements(self.walls)
            self.generate_walls()



    # eliminar elementos que no se visualizan en pantalla para liberar memoria RAM
    def update_elements(self, elements):
        for element in elements:
            if not element.rect.right > 0:
                element.kill()


    # detener video juego    
    def stop(self):
        self.player.stop()
        self.stop_elements(self.walls)

        self.playing = False


    def stop_elements(self, elements):
        for element in elements:
            element.stop()