import sys
import pygame
from pygame.locals import *
from pysics import *

pygame.init()

WINDOW_W = 480
WINDOW_H = 480
display = pygame.display.set_mode()

BLACK = (0, 0, 0)
WHITE = pygame.Color(255, 255, 255)
display = pygame.display.set_mode((WINDOW_W, WINDOW_H))
background = display.convert()
background.fill(BLACK)
display.blit(background, (0, 0))

sim = Simulation(4, WINDOW_W, WINDOW_H, display)
sim.add_Vec(220, 220)
sim.add_Vec(50, 0)
sim.add_Vec(0, 50)
sim.add_Vec(30, 40)
sim.add_Vec(40, 30)
sim.add_Vec(50, 0)
sim.add_Vec(0, 50)
sim.add_Vec(40, 20)
sim.add_Vec(20, 40)

def main():

    while True:  # main game loop

        for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
        display.blit(background, (0, 0))
        sim.draw_vectors()
        pygame.display.update()

if __name__ == "__main__":
    main()

