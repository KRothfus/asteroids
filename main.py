import sys
import pygame
from asteroid import Asteroid
from constants import *
from player import Player
from asteroidfield import AsteroidField
from shot import Shot


def main():
    print(f'Starting Asteroids!\nScreen width: {SCREEN_WIDTH}\nScreen height: {SCREEN_HEIGHT}')
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    x = SCREEN_WIDTH/2
    y= SCREEN_HEIGHT/2
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    
    Player.containers = (updatable,drawable)
    player = Player(x,y)
    
    Asteroid.containers = (asteroids, updatable, drawable)
    
    AsteroidField.containers = (updatable,)
    AsteroidField()
    
    Shot.containers = (shots, updatable, drawable)
    
    while True:
        for event in pygame.event.get():
            if event.type ==pygame.QUIT:
                return
            
        screen.fill('black')
        updatable.update(dt)
        
        for rock in asteroids:
            if rock.collided(player):
                sys.exit('Game over!')
                
        for rock in asteroids:
            for shot in shots:
                if rock.collided(shot):
                    rock.split()
                    shot.kill()
                
                
        for thing in drawable:
            thing.draw(screen)
        
        pygame.display.flip()
        dt = clock.tick(60)/1000
        

if __name__=="__main__":
    main()