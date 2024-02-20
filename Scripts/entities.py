import pygame
class PhysicsEntity:
    def __init__(self, game, e_type, pos, size):
        self.game = game
        self.type = type
        self.pos = list(pos)
        self.size = size
        self.vel = [0,0]
        self.collisions = {'up':False, 'down':False, 'left':False, 'right':False}
        
    def rect(self):
        return pygame.Rect(self.pos[0], self.pos[1], self.size[0], self.size[1])
    

    def update(self, tilemap, movement=(0,0)):
        self.collisions = {'up':False, 'down':False, 'left':False, 'right':False}
        frame_movement = (movement[0]+self.vel[0], movement[1]+self.vel[1])

        self.pos[0] += frame_movement[0]
        entity_rect = self.rect()
        for rect in self.game.tilemap.physics_rects_around(self.pos):
            if entity_rect.colliderect(rect):
                if frame_movement[0] > 0:
                    entity_rect.right = rect.left
                    self.collisions['right'] = True
                if frame_movement[0] < 0:
                    entity_rect.left = rect.right
                    self.collisions['left'] = True
                self.pos[0] = entity_rect.x

        self.pos[1] += frame_movement[1]
        entity_rect = self.rect()
        for rect in tilemap.physics_rects_around(self.pos):
            if entity_rect.colliderect(rect):
                if frame_movement[1] > 0:
                    entity_rect.bottom = rect.top
                    self.collisions['down'] = True
                if frame_movement[1] < 0:
                    entity_rect.top = rect.bottom
                    self.collisions['up'] = True
                self.pos[1] = entity_rect.y
        

        self.vel[1] = min(5, self.vel[1] + 0.1)

        if self.collisions['down'] or self.collisions['up']:
            self.vel[1] = 0

    def render(self, surf):
        surf.blit(self.game.assets['player'], self.pos)

