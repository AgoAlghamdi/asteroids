import pygame
from constants import *
from player import Player
from asteroids import Asteroids
from asteroidfield import AsteroidField
import sys
from shots import shot

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock=pygame.time.Clock()

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Player.containers = (updatable,drawable)
    Asteroids.containers= (asteroids,updatable,drawable)
    AsteroidField.containers=(updatable)
    shot.containers=(shots,updatable,drawable)
    astero_field=AsteroidField()# spawn astro field
    player=Player(x=SCREEN_WIDTH/2, y=SCREEN_HEIGHT/2)# spawn player in middle of screen
    dt=0
    
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        
        updatable.update(dt)

        for asteroid in asteroids:
            if asteroid.collides_with(player):
                print("Game over!")
                sys.exit()
            for bullets in shots:
                if asteroid.collides_with(bullets):
                    asteroid.split()
                    bullets.kill()


        screen.fill("black")

        for stuff in drawable:
            stuff.draw(screen)

        pygame.display.flip()

        dt=clock.tick(60)/1000
        







if __name__ == "__main__":
    main()