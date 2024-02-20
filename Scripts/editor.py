import pygame
import sys

from tilemap import Tilemap
from utils import load_image, load_images
RENDER_SCALE = 2

class Editor:
    def __init__(self):

        #game init
        pygame.init()
        pygame.display.set_caption('Bunninja')

        self.screen = pygame.display.set_mode((640,480))
        self.display = pygame.Surface((320,240))
        self.clock = pygame.time.Clock()


      
        self.movement = [False, False, False, False]
        self.assets = {
            'decor': load_images('tiles/decor'),
            'grass': load_images('tiles/grass'),
            'stone': load_images('tiles/stone'),
            'large_decor': load_images('tiles/large_decor')
        }

        self.tilemap = Tilemap(self, tile_size=16)

        self.scroll = [0,0]
        self.tille_list = list(self.assets)
        self.tile_group = 0
        self.tile_variant = 0

    def run(self):
        while True:
            self.display.fill((0,0,0))


            current_tile_img = self.assets[self.tille_list[self.tile_group]][self.tile_variant]
            current_tile_img.set_alpha(100)
            self.display.blit(current_tile_img, (5,5))

    

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
                        self.movement[2] = True
                    if event.key == pygame.K_s:
                        self.movement[3] = True
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_a:
                        self.movement[0] = False
                    if event.key == pygame.K_d:
                        self.movement[1] = False
                    if event.key == pygame.K_w:
                        self.movement[2] = False
                    if event.key == pygame.K_s:
                        self.movement[3] = False

            self.screen.blit(pygame.transform.scale(self.display, (640,480)), (0,0))
            pygame.display.update()
            self.clock.tick(60)

Editor().run()

