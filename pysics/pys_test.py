import sys

import pygame
from pygame.locals import *

from pysics.pysics import *


pygame.init()

WINDOW_W = 640
WINDOW_H = 480
display = pygame.display.set_mode()

BLACK = (0, 0, 0)
WHITE = pygame.Color(255, 255, 255)
display = pygame.display.set_mode((WINDOW_W, WINDOW_H))
background = display.convert()
background.fill(BLACK)
display.blit(background, (0, 0))

sim = Simulation(1, WINDOW_W, WINDOW_H, display)
sim.add_Vec(200, 200)

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

