import pygame, sys
from pygame.locals import *
from subprocess import Popen, PIPE
from threading import Thread
from Queue import Queue, Empty
from os import getcwd

WINDOW_H = 400
WINDOW_W = 400

FPS = 60
FPSCLOCK = pygame.time.Clock()
displaySurface = pygame.display.set_mode((WINDOW_W, WINDOW_H))
pixArray = pygame.PixelArray(displaySurface)

screenDraw = Queue()  # setup for gathering points to turn on from main.c

def stream_watcher(identifier, stream):
    for line in stream: # take in string
        if line == 'break\n':  # if the new pixels are all added to the queue, close the thread
            break
        else:
            line = line.split()
            screenDraw.put([int(line[0]), int(line[1])])  # each line has "# #" format"""

    if not stream.closed:
        stream.close()


class Game():
    def __init__(self):
        pygame.init()
        self.end = False

    def main(self):
        while True and not self.end:
            proc = Popen(getcwd() + '/main', stdout=PIPE)

            Thread(target=stream_watcher, name='stdout-watcher', args=('STDOUT', proc.stdout)).start()

            for event in pygame.event.get():
                if event.type == QUIT:
                    self.end = True
                    pygame.quit()
                    sys.exit()

            while not screenDraw.empty():
                coor = screenDraw.get()
                pixArray[coor[0]][coor[1]] = (255, 0, 255)

            pygame.display.update()
            FPSCLOCK.tick(FPS)


if __name__ == '__main__':
    game = Game()
    game.main()
