import pygame
import sys

from Scripts.entities import PhysicsEntity
from Scripts.utils import load_image
class Game:
    def __init__(self):

        #game init
        pygame.init()
        pygame.display.set_caption('Bunninja')

        self.screen = pygame.display.set_mode((640,480))
        self.clock = pygame.time.Clock()


      
        self.movement = [False, False]
        self.assets = {
            'player': load_image('entities/player.png')
        }

        self.player = PhysicsEntity(self, 'player', (50,50), (8,15))

    def run(self):
        while True:
            self.screen.fill((64,224,208))

            self.player.update((self.movement[1] - self.movement[0], 0))
            self.player.render(self.screen)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_a:
                        self.movement[0] = True
                    if event.key == pygame.K_d:
                        self.movement[1] = True
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_a:
                        self.movement[0] = False
                    if event.key == pygame.K_d:
                        self.movement[1] = False

            pygame.display.update()
            self.clock.tick(60)

Game().run()


