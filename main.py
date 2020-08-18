import pygame as pg
import firework as f
import random as r

pg.init()
clock = pg.time.Clock()
screen_size = (800, 800)
screen = pg.display.set_mode(screen_size)
pg.display.set_caption("Fireworks")

fireworks = []


def instantiate(p):
    p /= 100 # p = probability of instantiating each frame
    
    if r.uniform(0, 1) <= p:
        fireworks.append(f.Particle(r.randint(0, 800), 800))
    

def game():      
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                return
        
        instantiate(10)
        screen.fill((61, 52, 235))
        for firework in fireworks:
            firework.update()
            firework.show(screen)
        clock.tick(60)
        pg.display.flip()
    


if __name__ == "__main__":
    game()