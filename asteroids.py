import pygame
from circleShape import CircleShape
from constants import *
import random

class Asteroids(CircleShape):
    def __init__(self,x,y,radius):
        super().__init__(x,y,radius)

    def draw(self,screen):
        pygame.draw.circle(screen,'white',self.position,self.radius,2)

    def update(self,dt):
        self.position+=self.velocity*dt
        

    def split(self):
        self.kill()
        if self.radius<= ASTEROID_MIN_RADIUS:
            return
        else:
            rnd=random.uniform(20,50)
            ast1=pygame.Vector2(self.position.x,self.position.y).rotate(rnd)
            ast2=pygame.Vector2(self.position.x,self.position.y).rotate(-rnd)
            rad=self.radius-ASTEROID_MIN_RADIUS
            asteroid1=Asteroids(self.position.x,self.position.y,rad)
            asteroid2=Asteroids(self.position.x,self.position.y,rad)
            asteroid1.velocity=ast1*1.2
            asteroid2.velocity=ast2*1.2
            return asteroid1,asteroid2

