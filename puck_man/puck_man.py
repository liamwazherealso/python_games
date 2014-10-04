#Did you know that the original name for Pac-Man was Puck-Man? You'd think it was because he looks like a hockey puck
# but it actually comes from the Japanese phrase 'Paku-Paku,' which means to flap one's mouth open and closed. They
# changed it because they thought Puck-Man would be too easy to vandalize, you know, like people could just scratch off
#  the P and turn it into an F or whatever. - Scott Pilgrim vs. The world

import pygame, sys
from pygame.locals import *



WINDOW_H = 248
WINDOW_W = 224

FPS = 60
FPSCLOCK = pygame.time.Clock()
displaySurface = pygame.display.set_mode((WINDOW_W, WINDOW_H))
GREEN = pygame.Color(0,255,0)

UP = 'up'
DOWN = 'down'
LEFT = 'left'
RIGHT = 'right'

class Path():

    """
    Creates the valid coordinate for the centers of the sprites
    """

    def __init__(self):

        self.path_list = []

        # the boundary is 4 pixels, path dia is 8
        bd = 4
        pr = 8

        r1y = pr + bd
        for x in range(pr + bd, 108 - pr):
            self.path_list.append((x, r1y))

        for x in range(116 + pr, WINDOW_W - pr - bd):
            self.path_list.append((x, r1y))

        r2y = 36 + pr
        for x in range(pr + bd, WINDOW_W - pr - bd):
            self.path_list.append((x, r2y))

        r3y = 60 + pr
        for x in range(pr + bd, 60 - pr):
            self.path_list.append((x, r3y))

        for x in range(68 + pr, 108 - pr):
            self.path_list.append((x, r3y))

        for x in range(116 + pr, 156 - pr):
            self.path_list.append((x, r3y))

        for x in range(164 + pr, WINDOW_W - pr - bd):
            self.path_list.append((x, r3y))

        r4y = 84 + pr
        for x in range(68 + pr, 156 - pr):
            self.path_list.append((x, r4y))

        r5y = 108 + pr
        for x in range(pr, 84 - pr):
            self.path_list.append((x, r5y))

        for x in range(140 + pr, WINDOW_W - pr):
            self.path_list.append((x, r5y))

        r6y = 132 + pr
        for x in range(68 + pr, 156 - pr):
            self.path_list.append((x, r6y))

        r7y = 156 + pr
        for x in range(bd + pr, 108 - pr):
            self.path_list.append((x, r7y))

        for x in range(116 + pr, WINDOW_W - bd - pr):
            self.path_list.append((x, r7y))

        r8y = 180 + pr
        for x in range(bd + pr, 36 - pr):
            self.path_list.append((x, r8y))

        for x in range(44 + pr, 180 - pr):
            self.path_list.append((x, r8y))

        for x in range(188 + pr, WINDOW_W - bd - pr):
            self.path_list.append((x, r8y))

        r9y = 204 + pr
        for x in range(bd + pr, 60 - pr):
            self.path_list.append((x, r9y))

        for x in range(68 + pr, 108 - pr):
            self.path_list.append((x, r9y))

        for x in range(116 + pr, 156 - pr):
            self.path_list.append((x, r9y))

        for x in range(164 + pr, 220 - pr):
            self.path_list.append((x, r9y))

        r10y = 228 + pr
        for x in range(bd + pr, WINDOW_W - bd - pr):
            self.path_list.append((x, r10y))

        # adding columns
        c1x = 20 - pr
        for y in range(bd + pr, 76 - pr):
            self.path_list.append((c1x, y))

        for y in range(158 + pr, 196 - pr):
            self.path_list.append((c1x, y))

        # looks like this is where the dead pixel is coming from.
        for y in range(204 + pr, WINDOW_H - pr - bd):
            self.path_list.append((c1x, y))

        c2x = 36 - pr
        for y in range(180 + pr, 220 - pr):
            self.path_list.append((c2x, y))


        c3x = 60 - pr
        for y in range(bd + pr, 220 - pr):
            self.path_list.append((c3x, y))

        c4x = 84 - pr
        for y in range(36 + pr, 76 - pr):
            self.path_list.append((c4x, y))

        for y in range(84 + pr, 172 - pr):
            self.path_list.append((c4x, y))

        for y in range(180 + pr, 220 - pr):
            self.path_list.append((c4x, y))

        c5x = 108 - pr
        for y in range(bd + pr, 52 - pr):
            self.path_list.append((c5x, y))
        for y in range(60 + pr, 100 - pr):
            self.path_list.append((c5x, y))
        for y in range(156 + pr, 196 - pr):
            self.path_list.append((c5x, y))
        for y in range(204 + pr, WINDOW_H - pr - bd):
            self.path_list.append((c5x, y))

        c6x = WINDOW_W - 108 + pr
        for y in range(bd + pr, 52 - pr):
            self.path_list.append((c6x, y))
        for y in range(60 + pr, 100 - pr):
            self.path_list.append((c6x, y))
        for y in range(156 + pr, 196 - pr):
            self.path_list.append((c6x, y))
        for y in range(204 + pr, WINDOW_H - pr - bd):
            self.path_list.append((c6x, y))

        c7x = WINDOW_W - 84 + pr
        for y in range(36 + pr, 76 - pr):
            self.path_list.append((c7x, y))

        for y in range(84 + pr, 172 - pr):
            self.path_list.append((c7x, y))

        for y in range(180 + pr, 220 - pr):
            self.path_list.append((c7x, y))

        c8x = WINDOW_W - 60 + pr
        for y in range(bd + pr, 220 - pr):
            self.path_list.append((c8x, y))

        c9x = WINDOW_W - 36 + pr
        for y in range(180 + pr, 220 - pr):
            self.path_list.append((c9x, y))

        c10x = WINDOW_W - 20 + pr
        for y in range(bd + pr, 76 - pr):
            self.path_list.append((c10x, y))

        for y in range(158 + pr, 196 - pr):
            self.path_list.append((c10x, y))

        for y in range(204 + pr, WINDOW_H - pr - bd):
            self.path_list.append((c10x, y))

    def draw_path(self):
        """
        debug: see if coordinates were correct
        :return:
        """
        for coordinate in self.path_list:
            pygame.draw.line(displaySurface, GREEN, coordinate, coordinate)



path = Path().path_list

class Character(pygame.sprite.Sprite):
    """
    Base class for characters, this is a child of the Sprite class defined in pygame, inheriting this allows us to use
    the sprite interface which is basically all the methods a simple sprite needs.
    """

    def __init__(self, name, pos):
        self.name = name
        self.pos = pos
        self.thresh = 4

    def move(self, dir):
        """
        Moves the character, thresh allows for char not to be exactly on the correct pixel line to change direction.
        Useful for the player (they don't have to align perfectly with a vertical line if they want to go in a vertical
        direction.)
        :param dir:
        :return:
        """
        if dir == UP:
            for x in range(self.pos[0] - self.thresh, self.pos[0] + self.thresh):
                if (x, self.pos[1]) in path and (x, self.pos[1] - 1) in path:
                    self.pos = (x, self.pos[1] - 1)
        elif dir == DOWN:
            for x in range(self.pos[0] - self.thresh, self.pos[0] + self.thresh):
                if (x, self.pos[1]) in path and (x, self.pos[1] + 1) in path:
                    self.pos = (x, self.pos[1] + 1)
        elif dir == LEFT:
            for y in range(self.pos[1] - self.thresh, self.pos[1] + self.thresh):
                if (self.pos[0], y) in path and (self.pos[0] - 1, y) in path:
                    self.pos = (self.pos[0] - 1, y)
        elif dir == RIGHT:
            for y in range(self.pos[1] - self.thresh, self.pos[1] + self.thresh):
                if (self.pos[0], y) in path and (self.pos[0] + 1, y) in path:
                    self.pos = (self.pos[0] + 1, y)


class PuckMan(Character):
    def __init__(self, name, pos):
        self.name = "Puck Man"
        self.pos = (WINDOW_W / 2, 188)
        self.image = pygame.image.load('pm_1.png')
        self.surf = pygame.Surface([12, 13])
        self.thresh = 4

    def add(self):
        self.surf.blit(self.image, (0, 0))
        displaySurface.blit(self.surf, (self.pos[0] - 6, self.pos[1] - 6))




class Game():
    def __init__(self):
        pygame.init()
        self.puckMan = PuckMan("Puck Man", (WINDOW_W / 2, 188))

        self.down_press = self.up_press =  self.left_press = self.right_press = False

        pygame.display.set_caption('Puck Man')
        self.background = pygame.image.load('puck_man_background.png')

    def main(self):
        while True:
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_UP:
                        self.up_press = True

                    elif event.key == K_DOWN:
                        self.down_press = True

                    elif event.key == K_LEFT:
                        self.left_press = True

                    elif event.key == K_RIGHT:
                        self.right_press = True

                elif event.type == KEYUP:
                    if event.key == K_UP:
                        self.up_press = False

                    elif event.key == K_DOWN:
                        self.down_press = False

                    elif event.key == K_LEFT:
                        self.left_press = False

                    elif event.key == K_RIGHT:
                        self.right_press = False

                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()

            if self.up_press:
                self.puckMan.move(UP)
            elif self.down_press:
                self.puckMan.move(DOWN)
            elif self.left_press:
                self.puckMan.move(LEFT)
            elif self.right_press:
                self.puckMan.move(RIGHT)

            displaySurface.blit(self.background, (0, 0))
            self.puckMan.add()
            pygame.display.update()
            FPSCLOCK.tick(FPS)


if __name__ == '__main__':
    game = Game()
    game.main()






