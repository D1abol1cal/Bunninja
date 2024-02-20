import pygame
import sys

from Scripts.tilemap import Tilemap
from Scripts.entities import PhysicsEntity
from Scripts.utils import load_image, load_images
from Scripts.clouds import Clouds
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
            'player': load_image('entities/player.png'),
            'background': load_image('background.png'),
            'clouds': load_images('clouds')
        }

        print(self.assets)
        self.clouds = Clouds(self.assets['clouds'], count=16)
        self.player = PhysicsEntity(self, 'player', (50,50), (8,15))
        self.tilemap = Tilemap(self, tile_size=16)

        self.scroll = [0,0]

    def run(self):
        while True:
            self.display.blit(self.assets['background'], (0,0))
            self.scroll[0] += (self.player.rect().centerx - self.display.get_width() / 2 - self.scroll[0]) / 30
            self.scroll[1] += (self.player.rect().centery - self.display.get_height() / 2 - self.scroll[1]) / 30
            render_scroll = (int(self.scroll[0]), int(self.scroll[1]))    

            self.clouds.update()
            self.clouds.render(self.display, offset=render_scroll)

            self.tilemap.render(self.display, offset=render_scroll)

            self.player.update(self.tilemap, (self.movement[1] - self.movement[0], 0))
            self.player.render(self.display, offset=render_scroll)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_a:
                        self.movement[0] = True
                    if event.key == pygame.K_d:
                        self.movement[1] = True
                    if event.key == pygame.K_w:
                        self.player.vel[1] = -3
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_a:
                        self.movement[0] = False
                    if event.key == pygame.K_d:
                        self.movement[1] = False

            self.screen.blit(pygame.transform.scale(self.display, (640,480)), (0,0))
            pygame.display.update()
            self.clock.tick(60)

Game().run()

