import pygame
import sys

from Scripts.tilemap import Tilemap
from Scripts.entities import PhysicsEntity
from Scripts.utils import load_image, load_images
class Game:
    def __init__(self):

        #game init
        pygame.init()
        pygame.display.set_caption('Bunninja')

        self.screen = pygame.display.set_mode((640,480))
        self.display = pygame.Surface((320,240))
        self.clock = pygame.time.Clock()


      
        self.movement = [False, False]
        self.assets = {
            'decor': load_images('tiles/decor'),
            'grass': load_images('tiles/grass'),
            'stone': load_images('tiles/stone'),
            'large_decor': load_images('tiles/large_decor'),
            'player': load_image('entities/player.png')
        }

        print(self.assets)

        self.player = PhysicsEntity(self, 'player', (50,50), (8,15))
        self.tilemap = Tilemap(self, tile_size=16)

    def run(self):
        while True:
            self.display.fill((64,224,208))
            self.tilemap.render(self.display)
            self.player.update(self.tilemap, (self.movement[1] - self.movement[0], 0))
            self.player.render(self.display)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        self.movement[0] = True
                    if event.key == pygame.K_RIGHT:
                        self.movement[1] = True
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT:
                        self.movement[0] = False
                    if event.key == pygame.K_RIGHT:
                        self.movement[1] = False

            self.screen.blit(pygame.transform.scale(self.display, (640,480)), (0,0))
            pygame.display.update()
            self.clock.tick(60)

Game().run()

