import pygame
from circleshape import CircleShape
from constants import PLAYER_SHOOT_SPEED, SHOT_RADIUS


class Shot(CircleShape):
    
    def __init__(self, x, y, radius):
        super().__init__(x,y,radius)        
        self.radius = SHOT_RADIUS
        
    def draw(self,surface):
        pygame.draw.circle(surface, 'white', self.position, self.radius, width=2)

        
    def update(self, dt):
        self.position += self.velocity * dt
        
    