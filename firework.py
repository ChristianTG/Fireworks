import pygame as pg
import random as r
import numpy as np
gravity = 1

colors = []

class Particle:
    
    def __init__(self, x, y):
        self.pos = np.array((x, y))
        self.vel = np.array((0, -r.randint(30, 40)))
        self.acc = np.array((0, gravity))
        self.color = ((255, 255, 255))
    
    def update(self):
        self.vel += self.acc
        self.pos += self.vel
        
    def show(self, screen):
        size = 10
        pg.draw.rect(screen, self.color, pg.Rect(self.pos[0], self.pos[1], size, size))
        