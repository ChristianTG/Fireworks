import pygame as pg
import random as r
import numpy as np
gravity = 1

colors = {
    "GREEN": (0, 237, 24, 255),
    "RED": (255, 0, 68, 255),
    "BLUE": (0, 34, 255, 255),
    "PURPLE": (212, 0, 227, 255),
    "ORANGE": (255, 111, 0, 255)
        }

class Particle:
    
    def __init__(self, x, y, color=None):
        self.pos = np.array((x, y), float)
        self.vel = np.array((r.randint(-5, 5), r.randint(-5, 5)), float)
        self.acc = np.array((0, 0), float)
        if color:   # Color from parent Firework
            self.color = color
        else:
            self.color = r.choice(list(colors.values()))    # Fireworks pick their own color
        self.lifespan = 255
        self.slowdown = 0.98
        self.size = 7

    def update(self):
        self.vel += self.acc
        self.pos += self.vel
        self.vel = self.vel * self.slowdown
        
        self.lifespan -= 5
        if self.lifespan < 0: 
            self.lifespan = 0
        self.color = (self.color[0], self.color[1], self.color[2], self.lifespan)
        
        
                
        
    def show(self, screen):
        s = pg.Surface((self.size, self.size), pg.SRCALPHA)
        s.fill(self.color)
        screen.blit(s, (self.pos[0], self.pos[1]))
        #pg.draw.rect(screen, self.color, pg.Rect(self.pos[0], self.pos[1], self.size, self.size))
        

class Firework(Particle):
    
    def __init__(self, x, y):
        super().__init__(x, y)
        self.vel = np.array((0, -r.randint(30, 40)), float)
        self.acc = np.array((0, gravity), float)
        self.exploded = False
        self.particles =  []
        self.number_of_children = 30
        self.size = 10
    
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
        for i in range (self.number_of_children):
            self.particles.append(Particle(self.pos[0], self.pos[1], self.color))
        
        