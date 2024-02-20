import pygame
class PhysicsEntity:
    def __init__(self, game, e_type, pos, size):
        self.game = game
        self.type = type
        self.pos = list(pos)
        self.size = size
        self.vel = [0,0]

    def update(self, movement=(0,0)):
        frame_movement = (movement[0]+self.vel[0], movement[1]+self.vel[1])
        self.pos[0] += frame_movement[0]
        self.pos[1] += frame_movement[1]    

    def render(self, surf):
        surf.blit(self.game.assets['player'], self.pos)

