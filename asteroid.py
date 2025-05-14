import pygame
from circleshape import CircleShape
import random

from constants import ASTEROID_MIN_RADIUS


class Asteroid(CircleShape):
    
    def __init__(self, x, y, radius):
        super().__init__(x,y,radius)        
        self.radius = radius
        
    def draw(self,surface):
        pygame.draw.circle(surface, 'white', self.position, self.radius, width=2)

        
    def update(self, dt):
        self.position += self.velocity * dt
    
    def split(self):
        rand_angle = random.uniform(20,50)
        if self.radius <= ASTEROID_MIN_RADIUS:
            self.kill()
            return 
        else:
            angle1 = self.velocity.rotate(rand_angle)
            angle2 = self.velocity.rotate(-rand_angle)
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            asteroid1 = Asteroid(self.position[0],self.position[1],new_radius)
            asteroid2 = Asteroid(self.position[0],self.position[1],new_radius)
            asteroid1.velocity = angle1 * 1.2
            asteroid2.velocity = angle2 * 1.2
            self.kill()
