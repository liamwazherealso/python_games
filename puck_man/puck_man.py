#Did you know that the original name for Pac-Man was Puck-Man? You'd think it was because he looks like a hockey puck
# but it actually comes from the Japanese phrase 'Paku-Paku,' which means to flap one's mouth open and closed. They
# changed it because they thought Puck-Man would be too easy to vandalize, you know, like people could just scratch off
# the P and turn it into an F or whatever. - Scott Pilgrim vs. The world
import glob

import pygame, sys
from pygame.locals import *


WINDOW_H = 248
WINDOW_W = 224

FPS = 60
FPSCLOCK = pygame.time.Clock()
displaySurface = pygame.display.set_mode((WINDOW_W, WINDOW_H))

GREEN = pygame.Color(0, 255, 0)
PELLET_COLOR = pygame.Color(250, 185, 176)
RED = pygame.Color(255, 0, 0)

pel_group = pygame.sprite.Group()

UP = 'up'
DOWN = 'down'
LEFT = 'left'
RIGHT = 'right'
NONE = 'none'

GAME_SCORE = 0

class Path():

    """
    Creates the valid coordinate for the centers of the sprites
    """

    def __init__(self):

        self.path_list = []
        self.pell_list = []

        # the boundary is 4 pixels, path dia is 8
        bd = 4
        pr = 8

        count = 0
        r1y = pr + bd
        for x in range(pr + bd, 108 - pr):
            temp = (x, r1y)
            self.path_list.append(temp)
            if count % 8 == 0:
                self.pell_list.append(temp)
            count += 1

        for x in range(116 + pr, WINDOW_W - pr - bd):
            temp = (x, r1y)
            self.path_list.append(temp)
            if count % 8 == 0:
                self.pell_list.append(temp)
            count += 1

        r2y = 36 + pr
        for x in range(pr + bd, WINDOW_W - pr - bd):
            temp = (x, r2y)
            self.path_list.append(temp)
            if count % 8 == 0:
                self.pell_list.append(temp)
            count += 1

        r3y = 60 + pr
        for x in range(pr + bd, 60 - pr):
            temp = (x, r3y)
            self.path_list.append(temp)
            if count % 8 == 0:
                self.pell_list.append(temp)
            count += 1

        for x in range(68 + pr, 108 - pr):
            temp = (x, r3y)
            self.path_list.append(temp)
            if count % 8 == 0:
                self.pell_list.append(temp)
            count += 1

        for x in range(116 + pr, 156 - pr):
            temp = (x, r3y)
            self.path_list.append(temp)
            if count % 8 == 0:
                self.pell_list.append(temp)
            count += 1

        for x in range(164 + pr, WINDOW_W - pr - bd):
            temp = (x, r3y)
            self.path_list.append(temp)
            if count % 8 == 0:
                self.pell_list.append(temp)
            count += 1

        r4y = 84 + pr
        for x in range(68 + pr, 156 - pr):
            temp = (x, r4y)
            self.path_list.append(temp)
            if count % 8 == 0:
                self.pell_list.append(temp)
            count += 1

        r5y = 108 + pr
        for x in range(pr, 84 - pr):
            temp = (x, r5y)
            self.path_list.append(temp)
            if count % 8 == 0:
                self.pell_list.append(temp)
            count += 1

        for x in range(140 + pr, WINDOW_W - pr):
            temp = (x, r5y)
            self.path_list.append(temp)
            if count % 8 == 0:
                self.pell_list.append(temp)
            count += 1

        r6y = 132 + pr
        for x in range(68 + pr, 156 - pr):
            temp = (x, r6y)
            self.path_list.append(temp)
            if count % 8 == 0:
                self.pell_list.append(temp)
            count += 1

        r7y = 156 + pr
        for x in range(bd + pr, 108 - pr):
            temp = (x, r7y)
            self.path_list.append(temp)
            if count % 8 == 0:
                self.pell_list.append(temp)
            count += 1

        for x in range(116 + pr, WINDOW_W - bd - pr):
            temp = (x, r7y)
            self.path_list.append(temp)
            if count % 8 == 0:
                self.pell_list.append(temp)
            count += 1

        r8y = 180 + pr

        for x in range(bd + pr, 36 - pr):
            temp = (x, r8y)
            self.path_list.append(temp)
            if count % 8 == 0:
                self.pell_list.append(temp)
            count += 1

        for x in range(44 + pr, 180 - pr):
            temp = (x, r8y)
            self.path_list.append(temp)
            if count % 8 == 0:
                self.pell_list.append(temp)
            count += 1

        for x in range(188 + pr, WINDOW_W - bd - pr):
            temp = (x, r8y)
            self.path_list.append(temp)
            if count % 8 == 0:
                self.pell_list.append(temp)
            count += 1

        r9y = 204 + pr
        for x in range(bd + pr, 60 - pr):
            temp = (x, r9y)
            self.path_list.append(temp)
            if count % 8 == 0:
                self.pell_list.append(temp)
            count += 1

        for x in range(68 + pr, 108 - pr):
            temp = (x, r9y)
            self.path_list.append(temp)
            if count % 8 == 0:
                self.pell_list.append(temp)
            count += 1

        for x in range(116 + pr, 156 - pr):
            temp = (x, r9y)
            self.path_list.append(temp)
            if count % 8 == 0:
                self.pell_list.append(temp)
            count += 1

        for x in range(164 + pr, 220 - pr):
            temp = (x, r9y)
            self.path_list.append(temp)
            if count % 8 == 0:
                self.pell_list.append(temp)
            count += 1

        r10y = 228 + pr
        for x in range(bd + pr, WINDOW_W - bd - pr):
            temp = (x, r10y)
            self.path_list.append(temp)
            if count % 8 == 0:
                self.pell_list.append(temp)
            count += 1

        # adding columns
        c1x = 20 - pr
        for y in range(bd + pr, 76 - pr):
            temp = (c1x, y)
            self.path_list.append(temp)
            if count % 8 == 0:
                self.pell_list.append(temp)
            count += 1

        for y in range(156 + pr, 196 - pr):
            temp = (c1x, y)
            self.path_list.append(temp)
            if count % 8 == 0:
                self.pell_list.append(temp)
            count += 1

        # looks like this is where the dead pixel is coming from.
        for y in range(204 + pr, WINDOW_H - pr - bd):
            temp = (c1x, y)
            self.path_list.append(temp)
            if count % 8 == 0:
                self.pell_list.append(temp)
            count += 1

        c2x = 36 - pr
        for y in range(180 + pr, 220 - pr):
            temp = (c2x, y)
            self.path_list.append(temp)
            if count % 8 == 0:
                self.pell_list.append(temp)
            count += 1

        c3x = 60 - pr
        for y in range(bd + pr, 221 - pr):
            temp = (c3x, y)
            self.path_list.append(temp)
            if count % 8 == 0:
                self.pell_list.append(temp)
            count += 1

        c4x = 84 - pr
        for y in range(36 + pr, 76 - pr):
            temp = (c4x, y)
            self.path_list.append(temp)
            if count % 8 == 0:
                self.pell_list.append(temp)
            count += 1

        for y in range(84 + pr, 172 - pr):
            temp = (c4x, y)
            self.path_list.append(temp)
            if count % 8 == 0:
                self.pell_list.append(temp)
            count += 1

        for y in range(180 + pr, 220 - pr):
            temp = (c4x, y)
            self.path_list.append(temp)
            if count % 8 == 0:
                self.pell_list.append(temp)
            count += 1

        c5x = 108 - pr
        for y in range(bd + pr, 52 - pr):
            temp = (c5x, y)
            self.path_list.append(temp)
            if count % 8 == 0:
                self.pell_list.append(temp)
            count += 1

        for y in range(60 + pr, 100 - pr):
            temp = (c5x, y)
            self.path_list.append(temp)
            if count % 8 == 0:
                self.pell_list.append(temp)
            count += 1

        for y in range(156 + pr, 196 - pr):
            temp = (c5x, y)
            self.path_list.append(temp)
            if count % 8 == 0:
                self.pell_list.append(temp)
            count += 1

        for y in range(204 + pr, WINDOW_H - pr - bd):
            temp = (c5x, y)
            self.path_list.append(temp)
            if count % 8 == 0:
                self.pell_list.append(temp)
            count += 1

        c6x = WINDOW_W - 108 + pr
        for y in range(bd + pr, 52 - pr):
            temp = (c6x, y)
            self.path_list.append(temp)
            if count % 8 == 0:
                self.pell_list.append(temp)
            count += 1

        for y in range(60 + pr, 100 - pr):
            temp = (c6x, y)
            self.path_list.append(temp)
            if count % 8 == 0:
                self.pell_list.append(temp)
            count += 1

        for y in range(156 + pr, 196 - pr):
            temp = (c6x, y)
            self.path_list.append(temp)
            if count % 8 == 0:
                self.pell_list.append(temp)
            count += 1

        for y in range(204 + pr, WINDOW_H - pr - bd):
            temp = (c6x, y)
            self.path_list.append(temp)
            if count % 8 == 0:
                self.pell_list.append(temp)
            count += 1

        c7x = WINDOW_W - 84 + pr
        for y in range(36 + pr, 77 - pr):
            temp = (c7x, y)
            self.path_list.append(temp)
            if count % 8 == 0:
                self.pell_list.append(temp)
            count += 1

        for y in range(84 + pr, 172 - pr):
            temp = (c7x, y)
            self.path_list.append(temp)
            if count % 8 == 0:
                self.pell_list.append(temp)
            count += 1

        for y in range(180 + pr, 221 - pr):
            temp = (c7x, y)
            self.path_list.append(temp)
            if count % 8 == 0:
                self.pell_list.append(temp)
            count += 1

        c8x = WINDOW_W - 60 + pr
        for y in range(bd + pr, 220 - pr):
            temp = (c8x, y)
            self.path_list.append(temp)
            if count % 8 == 0:
                self.pell_list.append(temp)
            count += 1

        c9x = WINDOW_W - 36 + pr
        for y in range(180 + pr, 220 - pr):
            temp = (c9x, y)
            self.path_list.append(temp)
            if count % 8 == 0:
                self.pell_list.append(temp)
            count += 1

        c10x = WINDOW_W - 20 + pr
        for y in range(bd + pr, 77 - pr):
            temp = (c10x, y)
            self.path_list.append(temp)
            if count % 8 == 0:
                self.pell_list.append(temp)
            count += 1

        for y in range(156 + pr, 197 - pr):
            temp = (c10x, y)
            self.path_list.append(temp)
            if count % 8 == 0:
                self.pell_list.append(temp)
            count += 1

        for y in range(204 + pr, WINDOW_H + 1 - pr - bd):
            temp = (c10x, y)
            self.path_list.append(temp)
            if count % 8 == 0:
                self.pell_list.append(temp)
            count += 1

    def draw_path(self):
        """
        debug: see if coordinates were correct
        :return:
        """
        for coordinate in self.path_list:
            pygame.draw.line(displaySurface, GREEN, coordinate, coordinate)

        for coordinate in self.pell_list:
            pygame.draw.line(displaySurface, RED, coordinate, coordinate)

pell_path = Path().pell_list
path = Path().path_list

class Pellet(pygame.sprite.Sprite):
    """
    The pellets that that puck man eats.
    """

    def __init__(self, pos):
        pygame.sprite.Sprite.__init__(self)
        self.pos = pos
        self.alive = True

    def kill(self):
        self.alive = False

    def pell_maker(self):
        """
        Adds all pellets for games in a group which it returns
        """

        for coordinate in pell_path:
            Small_Pellet(coordinate).add(pel_group)

    def pell_draw(self):
        for pellet in pel_group:
            if pellet.alive:
                pellet.draw()


class Small_Pellet(Pellet):

    def draw(self):

        pygame.draw.rect(displaySurface, PELLET_COLOR, (self.pos[0] - 1, self.pos[1] - 1, 2, 2))

class Big_Pellet(Pellet):

    def draw(self):
        pygame.draw.circle(displaySurface, PELLET_COLOR, (self.pos[0], self.pos[1]), 2)

class Character(pygame.sprite.Sprite):
    """
    Base class for characters, this is a child of the Sprite class defined in pygame, inheriting this allows us to use
    the sprite interface which is basically all the methods a simple sprite needs.
    """

    def __init__(self, name, pos):
        self.name = name
        self.pos = pos
        self.thresh = 4
        self.dir = 'static'

    def move(self, dir):
        """
        Moves the character, thresh allows for char not to be exactly on the correct pixel line to change direction.
        Useful for the player (they don't have to align perfectly with a vertical line if they want to go in a vertical
        direction.)
        :param dir:
        :return:
        """
        valid = False
        if dir == UP:
            for x in range(self.pos[0] - self.thresh, self.pos[0] + self.thresh):
                if (x, self.pos[1]) in path and (x, self.pos[1] - 1) in path:
                    self.pos = (x, self.pos[1] - 1)
                    self.dir = dir
                    valid = True

        elif dir == DOWN:
            for x in range(self.pos[0] - self.thresh, self.pos[0] + self.thresh):
                if (x, self.pos[1]) in path and (x, self.pos[1] + 1) in path:
                    self.pos = (x, self.pos[1] + 1)
                    self.dir = dir
                    valid = True

        elif dir == LEFT:
            for y in range(self.pos[1] - self.thresh, self.pos[1] + self.thresh):
                if (self.pos[0], y) in path and (self.pos[0] - 1, y) in path:
                    self.pos = (self.pos[0] - 1, y)
                    self.dir = dir
                    valid = True

        elif dir == RIGHT:
            for y in range(self.pos[1] - self.thresh, self.pos[1] + self.thresh):
                if (self.pos[0], y) in path and (self.pos[0] + 1, y) in path:
                    self.pos = (self.pos[0] + 1, y)
                    self.dir = dir
                    valid = True

        return valid


class PuckMan(Character):

    def __init__(self, name, pos):
        self.name = "Puck Man"
        self.pos = (WINDOW_W / 2, 188)
        self.surf = pygame.Surface([12, 13])
        self.thresh = 4
        self.dir = 'static'

        self.ani_speed_init = 10
        self.ani_speed = self.ani_speed_init

        self.ani_l = glob.glob("img/pm_l*.png")
        self.ani_l.sort()
        temp = self.ani_l
        self.ani_l.reverse()
        self.ani_l.extend(temp)

        self.ani_r = glob.glob("img/pm_r*.png")
        self.ani_r.sort()
        temp = self.ani_r
        self.ani_r.reverse()
        self.ani_r.extend(temp)

        self.ani_u = glob.glob("img/pm_u*.png")
        self.ani_u.sort()
        temp = self.ani_u
        self.ani_u.reverse()
        self.ani_u.extend(temp)

        self.ani_d = glob.glob("img/pm_d*.png")
        self.ani_d.sort()
        temp = self.ani_d
        self.ani_d.reverse()
        self.ani_d.extend(temp)


        self.ani_pos = 0
        self.ani_max = len(self.ani_l)-1

        self.image = pygame.image.load(self.ani_l[self.ani_pos])
        self.add()

    def add(self):
        if self.dir == LEFT:
            if self.ani_speed == 0:
                self.image = pygame.image.load(self.ani_l[self.ani_pos])
        elif self.dir == RIGHT:
            if self.ani_speed == 0:
                self.image = pygame.image.load(self.ani_r[self.ani_pos])
        elif self.dir == UP:
            if self.ani_speed == 0:
                self.image = pygame.image.load(self.ani_u[self.ani_pos])
        elif self.dir == DOWN:
            if self.ani_speed == 0:
                self.image = pygame.image.load(self.ani_d[self.ani_pos])
        self.surf.fill((0, 0, 0))
        self.surf.blit(self.image, (0, 0))

        if self.ani_pos == self.ani_max:
            self.ani_pos = 0
        else:
            self.ani_pos += 1

        if self.ani_speed == 0:
            self.ani_speed = self.ani_speed_init
        else:
            self.ani_speed -= 1


        displaySurface.blit(self.surf, (self.pos[0] - 6, self.pos[1] - 6))

class Game():

    def __init__(self):
        pygame.init()
        self.puckMan = PuckMan("Puck Man", (WINDOW_W / 2, 188))

        self.down_press = self.up_press =  self.left_press = self.right_press = False
        self.pellet = Pellet((0, 0))
        self.pellet.pell_maker()
        pygame.display.set_caption('Puck Man')
        self.background = pygame.image.load('puck_man_background.png')


    def main(self):
        while True:
            #Set value for key true if pushed down, false if up

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

            # move holds whether or not the movement worked
            move = False
            if self.up_press:
                move = self.puckMan.move(UP)
            elif self.down_press:
                move = self.puckMan.move(DOWN)
            elif self.left_press:
                move = self.puckMan.move(LEFT)
            elif self.right_press:
                move = self.puckMan.move(RIGHT)
            # no move worked, so we move in the direction it was before
            if not move:
                self.puckMan.move(self.puckMan.dir)

            # add surfaces then render directly after

            displaySurface.blit(self.background, (0, 0))

            self.pellet.pell_draw()
            self.puckMan.add()
            pygame.display.update()
            FPSCLOCK.tick(FPS)


if __name__ == '__main__':
    game = Game()
    game.main()






