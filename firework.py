import pygame as pg
import random as r
import numpy as np
gravity = 1

colors = []

class Particle:
    
    def __init__(self, x, y):
        self.pos = np.array((x, y))
        self.vel = np.array((r.randint(-5, 5), r.randint(-10, 0)))
        self.acc = np.array((0, gravity))
        self.color = ((255, 255, 255, 255))
        self.lifespan = 255

    def update(self):
        self.vel += self.acc
        self.pos += self.vel
        
        self.lifespan -= 10
        if self.lifespan < 0: 
            self.lifespan = 0
        self.color = (self.color[0], self.color[1], self.color[2], self.lifespan)
        
        
                
        
    def show(self, screen):
        size = 10
        pg.draw.rect(screen, self.color, pg.Rect(self.pos[0], self.pos[1], size, size))
        

class Firework(Particle):
    
    def __init__(self, x, y):
        super().__init__(x, y)
        self.vel = np.array((0, -r.randint(30, 40)))
        self.exploded = False
        self.particles =  []
    
    def update(self):
        if not self.exploded:
            self.vel += self.acc
            self.pos += self.vel
            
            if self.vel[1] >= 0:
                self.exploded = True
                self.instantiate()
                
    
    def show(self, screen):
        if not self.exploded:
            super().show(screen)
        
    def instantiate(self):
        for i in range (5):
            self.particles.append(Particle(self.pos[0], self.pos[1]))
        
        