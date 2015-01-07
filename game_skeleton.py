import pygame, sys
from pygame.locals import *

WINDOW_H = 292
WINDOW_W = 224

FPS = 60
FPSCLOCK = pygame.time.Clock()
displaySurface = pygame.display.set_mode((WINDOW_W, WINDOW_H))

class Game():

    def __init__(self):
        pygame.init()


    def main(self):
        while True:
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    pass

                elif event.type == KEYUP:
                    pass

                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()


            pygame.display.update()
            FPSCLOCK.tick(FPS)


if __name__ == '__main__':
    game = Game()
    game.main()
