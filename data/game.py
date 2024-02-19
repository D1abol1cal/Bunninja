import pygame

pygame.init()

screen = pygame.display.set_mode((640,480))
clock = pygame.time.Clock()

while True:
    pygame.display.update()
    clock.tick(60)