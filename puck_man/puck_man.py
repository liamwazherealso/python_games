# Did you know that the original name for Pac-Man was Puck-Man? You'd think it was because he looks like a hockey puck
# but it actually comes from the Japanese phrase 'Paku-Paku,' which means to flap one's mouth open and closed. They
# changed it because they thought Puck-Man would be too easy to vandalize, you know, like people could just scratch off
# the P and turn it into an F or whatever. - Scott Pilgrim vs. The world

import glob
from time import sleep
import pygame, sys
import math
from pygame.locals import *
import time

WINDOW_H = 292
WINDOW_W = 224

FPS = 60
FPSCLOCK = pygame.time.Clock()
displaySurface = pygame.display.set_mode((WINDOW_W, WINDOW_H))

GREEN = pygame.Color(0, 255, 0)
PELLET_COLOR = pygame.Color(250, 185, 176)
RED = pygame.Color(255, 0, 0)
BLUE = pygame.Color(0, 0, 255)
WHITE = pygame.Color(255, 255, 255)

pel_group = pygame.sprite.Group()

UP = 'up'
DOWN = 'down'
LEFT = 'left'
RIGHT = 'right'
NONE = 'none'

BIG = 'big'
SMALL = 'small'

directions = [UP, DOWN, LEFT, RIGHT]
pygame.mixer.init(44100, -16, 2, 2048)


chompSnd = pygame.mixer.Sound('snd/chomp.wav')


class Score():
    def __init__(self):
        self.score = 0
        self.font = pygame.font.SysFont("liberationserif", 10)
        self.mes = self.font.render("HIGH SCORE", True, WHITE)

    def add(self, points):
        self.score += points
        self.render()

    def render(self):
        msg = str(self.score)
        surfScore = self.font.render(msg, True, WHITE)
        displaySurface.blit(self.mes, (WINDOW_W/2 - 25, 0))
        displaySurface.blit(surfScore, (WINDOW_W/2 - 10, 12))


class Path():

    """
    Creates the valid coordinate for the centers of the sprites
    """

    def __init__(self):

        self.path_list = []
        self.pell_list = []
        self.big_pell_list = []
        self.gpath_list = []

        # the boundary is 4 pixels, path dia is 8
        bd = 4
        pr = 8

        count = 0
        r1y = pr + bd
        for x in range(pr + bd, 108 - pr + 1):
            temp = (x, r1y)
            self.path_list.append(temp)
            if count % 8 == 0:
                self.pell_list.append(temp)
            count += 1

        count = 0
        for x in range(116 + pr, WINDOW_W - pr - bd + 1):
            temp = (x, r1y)
            self.path_list.append(temp)
            if count % 8 == 0:
                self.pell_list.append(temp)
            count += 1

        count = 0
        r2y = 36 + pr
        for x in range(pr + bd, WINDOW_W - pr - bd + 1):
            temp = (x, r2y)
            self.path_list.append(temp)
            if count % 8 == 0:
                self.pell_list.append(temp)
            count += 1

        count = 0
        r3y = 60 + pr
        for x in range(pr + bd, 60 - pr + 1):
            temp = (x, r3y)
            self.path_list.append(temp)
            if count % 8 == 0:
                self.pell_list.append(temp)
            count += 1

        count = 0
        for x in range(68 + pr, 108 - pr + 1):
            temp = (x, r3y)
            self.path_list.append(temp)
            if count % 8 == 0:
                self.pell_list.append(temp)
            count += 1

        count = 0
        for x in range(116 + pr, 156 - pr + 1):
            temp = (x, r3y)
            self.path_list.append(temp)
            if count % 8 == 0:
                self.pell_list.append(temp)
            count += 1

        count = 0
        for x in range(164 + pr, WINDOW_W - pr - bd + 1):
            temp = (x, r3y)
            self.path_list.append(temp)
            if count % 8 == 0:
                self.pell_list.append(temp)
            count += 1

        r4y = 84 + pr
        count = 0
        for x in range(68 + pr, 156 - pr + 1):
            temp = (x, r4y)
            self.path_list.append(temp)
            if count % 8 == 0:
                self.pell_list.append(temp)
            count += 1

        r5y = 108 + pr
        count = 4
        for x in range(pr, 84 - pr + 1):
            temp = (x, r5y)
            self.path_list.append(temp)
            if count % 8 == 0:
                self.pell_list.append(temp)
            count += 1

        count = 0
        for x in range(140 + pr, WINDOW_W - pr + 1):
            temp = (x, r5y)
            self.path_list.append(temp)
            if count % 8 == 0:
                self.pell_list.append(temp)
            count += 1

        r6y = 132 + pr
        count = 0
        for x in range(68 + pr, 156 - pr + 1):
            temp = (x, r6y)
            self.path_list.append(temp)
            if count % 8 == 0:
                self.pell_list.append(temp)
            count += 1

        r7y = 156 + pr
        count = 0
        for x in range(bd + pr, 108 - pr + 1):
            temp = (x, r7y)
            self.path_list.append(temp)
            if count % 8 == 0:
                self.pell_list.append(temp)
            count += 1

        count = 0
        for x in range(116 + pr, WINDOW_W - bd - pr + 1):
            temp = (x, r7y)
            self.path_list.append(temp)
            if count % 8 == 0:
                self.pell_list.append(temp)
            count += 1

        r8y = 180 + pr
        count = 0
        for x in range(bd + pr, 36 - pr + 1):
            temp = (x, r8y)
            self.path_list.append(temp)
            if count % 8 == 0:
                self.pell_list.append(temp)
            count += 1

        count = 0
        for x in range(44 + pr, 180 - pr + 1):
            temp = (x, r8y)
            self.path_list.append(temp)
            if count % 8 == 0:
                self.pell_list.append(temp)
            count += 1

        count = 0
        for x in range(188 + pr, WINDOW_W - bd - pr + 1):
            temp = (x, r8y)
            self.path_list.append(temp)
            if count % 8 == 0:
                self.pell_list.append(temp)
            count += 1

        count = 0
        r9y = 204 + pr
        for x in range(bd + pr, 60 - pr + 1):
            temp = (x, r9y)
            self.path_list.append(temp)
            if count % 8 == 0:
                self.pell_list.append(temp)
            count += 1

        count = 0
        for x in range(68 + pr, 108 - pr + 1):
            temp = (x, r9y)
            self.path_list.append(temp)
            if count % 8 == 0:
                self.pell_list.append(temp)
            count += 1

        count = 0
        for x in range(116 + pr, 156 - pr + 1):
            temp = (x, r9y)
            self.path_list.append(temp)
            if count % 8 == 0:
                self.pell_list.append(temp)
            count += 1

        count = 0
        for x in range(164 + pr, 220 - pr + 1):
            temp = (x, r9y)
            self.path_list.append(temp)
            if count % 8 == 0:
                self.pell_list.append(temp)
            count += 1

        r10y = 228 + pr
        count = 0
        for x in range(bd + pr, WINDOW_W - bd - pr + 1):
            temp = (x, r10y)
            self.path_list.append(temp)
            if count % 8 == 0:
                self.pell_list.append(temp)
            count += 1

        # adding columns

        # This extra counter just pops up 4 times when I add the big pellets

        c1x = 20 - pr
        count = 0
        count2 = 0
        for y in range(bd + pr, 76 - pr + 1):
            temp = (c1x, y)
            self.path_list.append(temp)
            if count % 8 == 0:
                count2 += 1
                if count2 == 3:
                    self.big_pell_list.append(temp)
                else:
                    self.pell_list.append(temp)
            count += 1

        count = 0
        count2 = 0
        for y in range(156 + pr, 196 - pr + 1):
            temp = (c1x, y)
            self.path_list.append(temp)
            if count % 8 == 0:
                count2 += 1
                if count2 == 4:
                    self.big_pell_list.append(temp)
                else:
                    self.pell_list.append(temp)
            count += 1

        # looks like this is where the dead pixel is coming from.
        count = 0
        for y in range(204 + pr, WINDOW_H - pr - bd - 44):
            temp = (c1x, y)
            self.path_list.append(temp)
            if count % 8 == 0:
                self.pell_list.append(temp)
            count += 1

        c2x = 36 - pr
        count = 0
        for y in range(180 + pr, 220 - pr):
            temp = (c2x, y)
            self.path_list.append(temp)
            if count % 8 == 0:
                self.pell_list.append(temp)
            count += 1

        c3x = 60 - pr
        count = 0
        for y in range(bd + pr, 221 - pr):
            temp = (c3x, y)
            self.path_list.append(temp)
            if count % 8 == 0:
                self.pell_list.append(temp)
            count += 1

        c4x = 84 - pr
        count = 0
        for y in range(36 + pr, 76 - pr + 1):
            temp = (c4x, y)
            self.path_list.append(temp)
            if count % 8 == 0:
                self.pell_list.append(temp)
            count += 1

        count = 0
        for y in range(84 + pr, 172 - pr + 1):
            temp = (c4x, y)
            self.path_list.append(temp)
            if count % 8 == 0:
                self.pell_list.append(temp)
            count += 1

        count = 0
        for y in range(180 + pr, 220 - pr + 1):
            temp = (c4x, y)
            self.path_list.append(temp)
            if count % 8 == 0:
                self.pell_list.append(temp)
            count += 1

        c5x = 108 - pr
        count = 0
        for y in range(bd + pr, 52 - pr + 1):
            temp = (c5x, y)
            self.path_list.append(temp)
            if count % 8 == 0:
                self.pell_list.append(temp)
            count += 1

        count = 0
        for y in range(60 + pr, 100 - pr + 1):
            temp = (c5x, y)
            self.path_list.append(temp)
            if count % 8 == 0:
                self.pell_list.append(temp)
            count += 1

        count = 0
        for y in range(156 + pr, 196 - pr + 1):
            temp = (c5x, y)
            self.path_list.append(temp)
            if count % 8 == 0:
                self.pell_list.append(temp)
            count += 1

        count = 0
        for y in range(204 + pr, WINDOW_H - pr*2 - bd - 36 + 1):
            temp = (c5x, y)
            self.path_list.append(temp)
            if count % 8 == 0:
                self.pell_list.append(temp)
            count += 1

        count = 0
        c6x = WINDOW_W - 108 + pr
        for y in range(bd + pr, 52 - pr + 1):
            temp = (c6x, y)
            self.path_list.append(temp)
            if count % 8 == 0:
                self.pell_list.append(temp)
            count += 1

        count = 0
        for y in range(60 + pr, 100 - pr + 1):
            temp = (c6x, y)
            self.path_list.append(temp)
            if count % 8 == 0:
                self.pell_list.append(temp)
            count += 1

        count = 0
        for y in range(156 + pr, 196 - pr+ 1):
            temp = (c6x, y)
            self.path_list.append(temp)
            if count % 8 == 0:
                self.pell_list.append(temp)
            count += 1

        count = 0
        for y in range(204 + pr, WINDOW_H - pr*2 - bd - 36 + 1):
            temp = (c6x, y)
            self.path_list.append(temp)
            if count % 8 == 0:
                self.pell_list.append(temp)
            count += 1

        c7x = WINDOW_W - 84 + pr
        count = 0
        for y in range(36 + pr, 77 - pr):
            temp = (c7x, y)
            self.path_list.append(temp)
            if count % 8 == 0:
                self.pell_list.append(temp)
            count += 1

        count = 0
        for y in range(84 + pr, 172 - pr + 1):
            temp = (c7x, y)
            self.path_list.append(temp)
            if count % 8 == 0:
                self.pell_list.append(temp)
            count += 1

        count = 0
        for y in range(180 + pr, 221 - pr):
            temp = (c7x, y)
            self.path_list.append(temp)
            if count % 8 == 0:
                self.pell_list.append(temp)
            count += 1

        c8x = WINDOW_W - 60 + pr
        count = 0
        for y in range(bd + pr, 220 - pr + 1):
            temp = (c8x, y)
            self.path_list.append(temp)
            if count % 8 == 0:
                self.pell_list.append(temp)
            count += 1

        c9x = WINDOW_W - 36 + pr
        count = 0
        for y in range(180 + pr, 220 - pr + 1):
            temp = (c9x, y)
            self.path_list.append(temp)
            if count % 8 == 0:
                self.pell_list.append(temp)
            count += 1

        c10x = WINDOW_W - 20 + pr
        count = 0
        count2 = 0
        for y in range(bd + pr, 77 - pr):
            temp = (c10x, y)
            self.path_list.append(temp)
            if count % 8 == 0:
                count2 += 1
                if count2 == 3:
                    self.big_pell_list.append(temp)
                else:
                    self.pell_list.append(temp)
            count += 1

        count = 0
        count2 = 0
        for y in range(156 + pr, 197 - pr):
            temp = (c10x, y)
            self.path_list.append(temp)
            if count % 8 == 0:
                count2 += 1
                if count2 == 4:
                    self.big_pell_list.append(temp)
                else:
                    self.pell_list.append(temp)

            count += 1

        count = 0
        for y in range(204 + pr, WINDOW_H - 36 - pr*2 - bd):
            temp = (c10x, y)
            self.path_list.append(temp)
            if count % 8 == 0:
                self.pell_list.append(temp)
            count += 1

        # getting rid of duplicate points
        l = range(len(self.pell_list))
        l.reverse()
        for i in l:
            temp = self.pell_list.pop(i)
            if temp in self.pell_list:
                pass
            else:
                self.pell_list.append(temp)

        temp = []
        for pair in self.pell_list:
            temp.append((pair[0], pair[1] + 24))
        self.pell_list = temp

        temp = []
        for pair in self.big_pell_list:
            temp.append((pair[0], pair[1] + 24))
        self.big_pell_list = temp

        # removes the parts of r5 that the ghost cannot go in.
        self.g = self.path_list
        self.gpath_list = list(self.path_list)

        for x in range(pr, 84 - pr*4 + 1):
            temp = (x, r5y)
            self.gpath_list.remove(temp)

        for x in range(140 + pr*4, WINDOW_W - pr + 1):
            temp = (x, r5y)
            self.gpath_list.remove(temp)

        self.path_list = self.g
        temp = []
        for pair in self.path_list:
            temp.append((pair[0], pair[1] + 24))
        self.path_list = temp

        temp = []
        for pair in self.gpath_list:
            temp.append((pair[0], pair[1] + 24))
        self.gpath_list = temp

    def draw_path(self):
        """
        debug: see if coordinates were correct
        :return:
        """
        for coordinate in self.big_pell_list:
            pygame.draw.line(displaySurface, GREEN, coordinate, coordinate)

        #for coordinate in self.pell_list:
        #    pygame.draw.line(displaySurface, RED, coordinate, coordinate)

pathway = Path()
pell_path = pathway.pell_list
big_pell_list = pathway.big_pell_list
path = pathway.path_list
gpath = pathway.gpath_list


class Pellet(pygame.sprite.Sprite):
    """
    The pellets that that puck man eats.
    """

    def __init__(self, pos, score):
        pygame.sprite.Sprite.__init__(self)
        self.pos = pos
        self.alive = True
        self.score = score
        self.big = False

    def kill(self):
        if self.alive:
            self.score.add(10)
            self.alive = False
            chompSnd.play(0, 340, 0)
        return SMALL

    def pell_maker(self):
        """
        Adds all pellets for games in a group which it returns
        """

        for coordinate in pell_path:
            Small_Pellet(coordinate, self.score).add(pel_group)

        for coordinate in big_pell_list:
            Big_Pellet(coordinate, self.score).add(pel_group)

    def pell_draw(self):
        for pellet in pel_group:
            if pellet.alive:
                pellet.draw()


class Small_Pellet(Pellet):

    def draw(self):
        if self.alive:
            pygame.draw.rect(displaySurface, PELLET_COLOR, (self.pos[0] - 1, self.pos[1] - 1, 2, 2))

    def rect(self):
        return pygame.Rect((self.pos[0] - 1, self.pos[1] - 1, 2, 2))


class Big_Pellet(Pellet):

    def __init__(self, pos, score):
        pygame.sprite.Sprite.__init__(self)
        self.pos = pos
        self.big = True
        self.alive = True
        self.score = score

    def draw(self):
        pygame.draw.circle(displaySurface, PELLET_COLOR, (self.pos[0], self.pos[1]), 4)

    def kill(self):
        if self.alive:
            self.score.add(10)
            self.alive = False
            chompSnd.play(0, 340, 0)
        return BIG

    def rect(self):
        return pygame.Rect((self.pos[0] - 1, self.pos[1] - 1, 4, 4))


class Ghost(pygame.sprite.Sprite):
    """
    Base class for characters, this is a child of the Sprite class defined in pygame, inheriting this allows us to use
    the sprite interface which is basically all the methods a simple sprite needs.
    """

    def __init__(self, name, pos):
        self.name = name
        self.pos = pos
        self.relpos = 0
        self.thresh = 4
        self.pos = [0, 0]
        self.dir = 'static'
        self.gridcounter = [4, 8]
        self.pre = " "
        self.ani_speed = 0
        self.dead = False

        # release: if the ghost is still being released
        # center:  if it has reached the center point of the start box
        # vertic:  if the ghost is going vertical
        # ai:      if the ai is taking control
        #           [relea, verti, ai, run]
        self.flag = [False, False, False, False]

        self.ani_d = glob.glob("img/" + self.pre + "_d*.png")
        self.ani_d.sort()

        self.ani_u = glob.glob("img/" + self.pre + "_u*.png")
        self.ani_u.sort()

        self.ani_l = glob.glob("img/" + self.pre + "_l*.png")
        self.ani_l.sort()

        self.ani_r = glob.glob("img/" + self.pre + "_r*.png")
        self.ani_r.sort()

        self.ani_death = glob.glob("img/g_d*")
        self.ani_death.sort()

        self.ani_pos = 0
        self.ani_max = 1

        self.image = pygame.image.load(self.ani_l[self.ani_pos])
        self.add()

    def release(self):
        """
        release: gets ghost out of box after respond time.
        :return:
        """

        # it is still in the ghost house and it is not at the center
        if not self.flag[1] and not self.flag[2]:
            # 112 is the x coor that the ghost must reach to start moving vertically out of the box
            dist = 112 - self.pos[0]
            if dist < 0:
                self.dir = LEFT

            elif dist > 0:
                self.dir = RIGHT

            else:
                self.flag[1] = True

        # the ghost is moving vertically
        else:
            self.dir = UP
            if self.pos[1] == 116:
                self.dir = NONE
                # ai is on and will stop release from being called
                self.flag[2] = True

    def unrelease(self):
        """
        unrelease: gets ghost in the box after death.
        :return:
        """

        # 112 is the x coor that the ghost must reach to start moving vertically out of the box
        dist = 140 - self.pos[1]
        if dist > 0:
            self.dir = DOWN

        elif dist == 0:
            self.dead = False
            self.flag[0] = True

    def move(self):
        """
        Moves the character, thresh allows for char not to be exactly on the correct pixel line to change direction.
        Useful for the player (they don't have to align perfectly with a vertical line if they want to go in a vertical
        direction.)
        :param dir:
        :return:
        """

        if self.dir == UP:
                self.pos[1] -= 1
                self.gridcounter[1] = (self.gridcounter[1] - 1) % 8
                if self.gridcounter[1] == 0:
                    self.grid[1] -= 1

        elif self.dir == DOWN:
                self.pos[1] += 1
                self.gridcounter[1] = (self.gridcounter[1] + 1) % 8
                if self.gridcounter[1] == 0:
                    self.grid[1] += 1

        elif self.dir == LEFT:
                self.pos[0] -= 1
                self.gridcounter[0] = (self.gridcounter[0] - 1) % 8
                if self.gridcounter[0] == 0:
                    self.grid[0] -= 1

        elif self.dir == RIGHT:
                self.pos[0] += 1
                self.gridcounter[0] = (self.gridcounter[0] + 1) % 8
                if self.gridcounter[0] == 0:
                    self.grid[0] += 1

    def add(self):
        """
        Method for rendering the ghost. Takes care of animation as well as rendering the sprite upon the surface.
        :return:
        """
        self.move()

        if self.flag[3] and not self.dead:  # it is on run mode so the animation length is different
            self.ani_pos = (self.ani_pos + 1) % 4
        elif self.dead:
            self.ani_pos = 0
        else:
            self.ani_pos = (self.ani_pos + 1) % 2

        if self.dir == LEFT and not self.flag[3]:
            if self.ani_speed == 0 and not self.dead:
                self.image = pygame.image.load(self.ani_l[self.ani_pos])

        elif self.dir == RIGHT and not self.flag[3]:
            if self.ani_speed == 0:
                self.image = pygame.image.load(self.ani_r[self.ani_pos])

        elif self.dir == UP and not self.flag[3]:
            if self.ani_speed == 0:
                self.image = pygame.image.load(self.ani_u[self.ani_pos])

        elif self.dir == DOWN and not self.flag[3]:
            if self.ani_speed == 0:
                self.image = pygame.image.load(self.ani_d[self.ani_pos])

        elif self.flag[3]:
            if self.ani_speed == 0 and not self.dead:
                self.image = pygame.image.load(self.ani_death[self.ani_pos])

            elif self.ani_speed == 0 and self.dead:
                self.image = pygame.image.load('img/eye_l.png')

        self.ani_speed = (self.ani_speed + 1) % 10
        # self.image.fill()
        self.surf = pygame.Surface((13, 12))
        self.surf.blit(self.image, (0, 0))
        displaySurface.blit(self.surf, (self.pos[0] - 6, self.pos[1] - 6), special_flags=(pygame.BLEND_RGBA_ADD))

    def rect(self):
        return pygame.Rect(self.pos[0]-6, self.pos[1]-6, 12, 13)

    def reverse(self):
            if self.dir == UP:
                self.dir = DOWN
            elif self.dir == DOWN:
                self.dir = UP
            elif self.dir == LEFT:
                self.dir = RIGHT
            elif self.dir == RIGHT:
                self.dir = LEFT


class Blinky(Ghost):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.name = "Blinky"
        self.pos = [WINDOW_W/2, 116]
        self.flag = [False, False, False, False]
        self.thresh = 0
        self.relpos = 0
        self.dir = 'static'
        self.grid = [14, 18]
        self.gridcounter = [self.pos[0] % 8, 4]
        self.dead = False
        self.pre = "bl"
        self.ani_speed = 0
        self.surf = pygame.Surface([14, 13])
        self.scatter = False

        self.ani_d = glob.glob("img/" + self.pre + "_d*.png")
        self.ani_d.sort()

        self.ani_u = glob.glob("img/" + self.pre + "_u*.png")
        self.ani_u.sort()

        self.ani_l = glob.glob("img/" + self.pre + "_l*.png")
        self.ani_l.sort()

        self.ani_r = glob.glob("img/" + self.pre + "_r*.png")
        self.ani_r.sort()

        self.ani_death = glob.glob("img/g_d*")
        self.ani_death.sort()

        self.ani_pos = 0
        self.ani_max = 1

        self.image = pygame.image.load(self.ani_l[self.ani_pos])
        self.add()

    def ai(self, pmcoor):

        index = 3
        minimum = 40
        hyp = 0

        if self.dead:
            pmcoor = [13, 14]


        # if the ai is on
        if self.flag[2]:
            # Which directions are valid
            valid = [False, False, False, False]
            # direction must be on path and not the reverse of current direction
            if (self.pos[0], self.pos[1] - 1) in gpath and self.dir != DOWN:
                valid[0] = True

            if (self.pos[0], self.pos[1] + 1) in gpath and self.dir != UP:
                valid[1] = True

            if (self.pos[0] - 1, self.pos[1]) in gpath and self.dir != RIGHT:
                valid[2] = True

            if (self.pos[0] + 1, self.pos[1]) in gpath and self.dir != LEFT:
                valid[3] = True

            for i in range(len(valid)):
                if valid[i]:
                    if directions[i] == RIGHT:
                        hyp = math.sqrt(math.pow(pmcoor[0] - self.grid[0] - 1, 2) + math.pow(pmcoor[1]
                                                                                              - self.grid[1], 2))
                    elif directions[i] == DOWN:
                        hyp = math.sqrt(math.pow(pmcoor[0] - self.grid[0], 2) + math.pow(pmcoor[1]
                                                                                              - self.grid[1]-1, 2))

                    elif directions[i] == LEFT:
                        hyp = math.sqrt(math.pow(pmcoor[0] - self.grid[0] + 1, 2) + math.pow(pmcoor[1]
                                                                                              - self.grid[1], 2))

                    elif directions[i] == UP:
                        hyp = math.sqrt(math.pow(pmcoor[0] - self.grid[0], 2) + math.pow(pmcoor[1]
                                                                                              - self.grid[1]+1, 2))

                    if hyp < minimum:
                        minimum = hyp
                        index = i

            self.dir = directions[index]

            if self.flag[3]:
                    if self.dir == UP and valid[1]:
                        self.dir = DOWN
                    elif self.dir == DOWN and valid[0]:
                        self.dir = UP
                    elif self.dir == LEFT and valid[3]:
                        self.dir = RIGHT
                    elif self.dir == RIGHT and valid[2]:
                        self.dir = LEFT

        elif self.flag[0]:
            self.release()

        if self.dead:
            if self.grid == pmcoor and self.gridcounter == [0, 4]:

                self.unrelease()


class Inky(Ghost):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.name = "Inky"
        self.pos = [WINDOW_W/2 - 16, 142]
        self.flag = [False, False, False, False]
        self.thresh = 0
        self.relpos = 0
        self.dir = 'static'
        self.grid = [12, 18]
        self.gridcounter = [self.pos[0] % 8, self.pos[1] % 8]
        self.dead = False
        self.pre = "in"
        self.ani_speed = 0
        self.surf = pygame.Surface([14, 13], pygame.SRCALPHA)
        self.scatter = False
        self.ani_d = glob.glob("img/" + self.pre + "_d*.png")
        self.ani_d.sort()

        self.ani_u = glob.glob("img/" + self.pre + "_u*.png")
        self.ani_u.sort()

        self.ani_l = glob.glob("img/" + self.pre + "_l*.png")
        self.ani_l.sort()

        self.ani_r = glob.glob("img/" + self.pre + "_r*.png")
        self.ani_r.sort()

        self.ani_death = glob.glob("img/g_d*")
        self.ani_death.sort()

        self.ani_pos = 0
        self.ani_max = 1

        self.image = pygame.image.load(self.ani_l[self.ani_pos])
        self.add()

    def ai(self, pmcoor):

        index = 3
        minimum = 40
        hyp = 0

        if self.dead:
            pmcoor = [13, 14]
            if self.grid == pmcoor and self.gridcounter == [3, 3]:
                self.unrelease()

        # if the ai is on
        if self.flag[2]:
            # Which directions are valid
            valid = [False, False, False, False]
            # direction must be on path and not the reverse of current direction
            if (self.pos[0], self.pos[1] - 1) in gpath and self.dir != DOWN:
                valid[0] = True

            if (self.pos[0], self.pos[1] + 1) in gpath and self.dir != UP:
                valid[1] = True

            if (self.pos[0] - 1, self.pos[1]) in gpath and self.dir != RIGHT:
                valid[2] = True

            if (self.pos[0] + 1, self.pos[1]) in gpath and self.dir != LEFT:
                valid[3] = True

            for i in range(len(valid)):
                if valid[i]:
                    if directions[i] == RIGHT:
                        hyp = math.sqrt(math.pow(pmcoor[0] - self.grid[0] - 1, 2) + math.pow(pmcoor[1]
                                                                                              - self.grid[1], 2))
                    elif directions[i] == DOWN:
                        hyp = math.sqrt(math.pow(pmcoor[0] - self.grid[0], 2) + math.pow(pmcoor[1]
                                                                                              - self.grid[1]-1, 2))

                    elif directions[i] == LEFT:
                        hyp = math.sqrt(math.pow(pmcoor[0] - self.grid[0] + 1, 2) + math.pow(pmcoor[1]
                                                                                              - self.grid[1], 2))

                    elif directions[i] == UP:
                        hyp = math.sqrt(math.pow(pmcoor[0] - self.grid[0], 2) + math.pow(pmcoor[1]
                                                                                              - self.grid[1]+1, 2))

                    if hyp < minimum:
                        minimum = hyp
                        index = i

            self.dir = directions[index]

            if self.flag[3]:
                    if self.dir == UP and valid[1]:
                        self.dir = DOWN
                    elif self.dir == DOWN and valid[0]:
                        self.dir = UP
                    elif self.dir == LEFT and valid[3]:
                        self.dir = RIGHT
                    elif self.dir == RIGHT and valid[2]:
                        self.dir = LEFT

        elif self.flag[0]:
            self.release()


class Pinky(Ghost):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.name = "Pinky"
        self.pos = [WINDOW_W/2 - 1, 142]
        self.flag = [False, False, False, False]
        self.thresh = 0
        self.relpos = 0
        self.dir = 'static'
        self.grid = [14, 18]
        self.gridcounter = [self.pos[0] % 8, 4]
        self.dead = False
        self.pre = "Pi"
        self.ani_speed = 0
        self.surf = pygame.Surface([14, 13])
        self.scatter = False

        self.ani_d = glob.glob("img/" + self.pre + "_d*.png")
        self.ani_d.sort()

        self.ani_u = glob.glob("img/" + self.pre + "_u*.png")
        self.ani_u.sort()

        self.ani_l = glob.glob("img/" + self.pre + "_l*.png")
        self.ani_l.sort()

        self.ani_r = glob.glob("img/" + self.pre + "_r*.png")
        self.ani_r.sort()

        self.ani_death = glob.glob("img/g_d*")
        self.ani_death.sort()

        self.ani_pos = 0
        self.ani_max = 1

        self.image = pygame.image.load(self.ani_l[self.ani_pos])
        self.add()

    def ai(self, pmcoor, pmdir):

        index = 3
        minimum = 40
        hyp = 0

        if self.dead:
            pmcoor = [13, 14]
            if self.grid == pmcoor and self.gridcounter == [3, 3]:
                self.unrelease()

        tempcoor = pmcoor
        # if the ai is on
        if self.flag[2]:

            # Switching the target tile based on the direction
            if pmdir == UP:
                tempcoor = [pmcoor[0]-4, pmcoor[1]-4]
            elif pmdir == LEFT:
                tempcoor = [pmcoor[0] - 4, pmcoor[1]]
            elif pmdir == RIGHT:
                tempcoor = [pmcoor[0] + 4, pmcoor[1]]
            elif pmdir == DOWN:
                tempcoor = [pmcoor[0], pmcoor[1] - 4]


            # Which directions are valid
            valid = [False, False, False, False]
            # direction must be on path and not the reverse of current direction
            if (self.pos[0], self.pos[1] - 1) in gpath and self.dir != DOWN:
                valid[0] = True

            if (self.pos[0], self.pos[1] + 1) in gpath and self.dir != UP:
                valid[1] = True

            if (self.pos[0] - 1, self.pos[1]) in gpath and self.dir != RIGHT:
                valid[2] = True

            if (self.pos[0] + 1, self.pos[1]) in gpath and self.dir != LEFT:
                valid[3] = True

            for i in range(len(valid)):
                # find the hyp of the current location of the ghost and the target tile
                if valid[i]:
                    if directions[i] == RIGHT:
                        hyp = math.sqrt(math.pow(tempcoor[0] - self.grid[0] - 1, 2) + math.pow(tempcoor[1]
                                                                                              - self.grid[1], 2))
                    elif directions[i] == DOWN:
                        hyp = math.sqrt(math.pow(tempcoor[0] - self.grid[0], 2) + math.pow(tempcoor[1]
                                                                                              - self.grid[1]-1, 2))

                    elif directions[i] == LEFT:
                        hyp = math.sqrt(math.pow(tempcoor[0] - self.grid[0] + 1, 2) + math.pow(tempcoor[1]
                                                                                              - self.grid[1], 2))

                    elif directions[i] == UP:
                        hyp = math.sqrt(math.pow(tempcoor[0] - self.grid[0], 2) + math.pow(tempcoor[1]
                                                                                              - self.grid[1]+1, 2))

                    if hyp < minimum:
                        minimum = hyp
                        index = i

            self.dir = directions[index]

            if self.flag[3]:
                    if self.dir == UP and valid[1]:
                        self.dir = DOWN
                    elif self.dir == DOWN and valid[0]:
                        self.dir = UP
                    elif self.dir == LEFT and valid[3]:
                        self.dir = RIGHT
                    elif self.dir == RIGHT and valid[2]:
                        self.dir = LEFT

        elif self.flag[0]:
            self.release()


class Clyde(Ghost):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.name = "Clyde"
        self.pos = [WINDOW_W/2 + 15, 142]
        self.flag = [False, False, False, False]
        self.thresh = 0
        self.relpos = 0
        self.dir = 'static'
        self.grid = [16, 18]
        self.gridcounter = [self.pos[0] %8, 4]
        self.dead = False
        self.pre = "cl"
        self.ani_speed = 0
        self.surf = pygame.Surface([14, 13])


        self.ani_d = glob.glob("img/" + self.pre + "_d*.png")
        self.ani_d.sort()
        self.scatter = False
        self.ani_u = glob.glob("img/" + self.pre + "_u*.png")
        self.ani_u.sort()

        self.ani_l = glob.glob("img/" + self.pre + "_l*.png")
        self.ani_l.sort()

        self.ani_r = glob.glob("img/" + self.pre + "_r*.png")
        self.ani_r.sort()

        self.ani_death = glob.glob("img/g_d*")
        self.ani_death.sort()

        self.ani_pos = 0
        self.ani_max = 1

        self.image = pygame.image.load(self.ani_l[self.ani_pos])
        self.add()

    def ai(self, pmcoor):

        index = 3
        minimum = 40
        hyp = 0

        if self.dead:
            pmcoor = [13, 14]
            if self.grid == pmcoor and self.gridcounter == [3, 3]:
                self.unrelease()

        # if the ai is on
        if self.flag[2]:
            # Which directions are valid
            valid = [False, False, False, False]
            # direction must be on path and not the reverse of current direction
            if (self.pos[0], self.pos[1] - 1) in gpath and self.dir != DOWN:
                valid[0] = True

            if (self.pos[0], self.pos[1] + 1) in gpath and self.dir != UP:
                valid[1] = True

            if (self.pos[0] - 1, self.pos[1]) in gpath and self.dir != RIGHT:
                valid[2] = True

            if (self.pos[0] + 1, self.pos[1]) in gpath and self.dir != LEFT:
                valid[3] = True

            for i in range(len(valid)):
                if valid[i]:
                    if directions[i] == RIGHT:
                        hyp = math.sqrt(math.pow(pmcoor[0] - self.grid[0] - 1, 2) + math.pow(pmcoor[1]
                                                                                              - self.grid[1], 2))
                    elif directions[i] == DOWN:
                        hyp = math.sqrt(math.pow(pmcoor[0] - self.grid[0], 2) + math.pow(pmcoor[1]
                                                                                              - self.grid[1]-1, 2))

                    elif directions[i] == LEFT:
                        hyp = math.sqrt(math.pow(pmcoor[0] - self.grid[0] + 1, 2) + math.pow(pmcoor[1]
                                                                                              - self.grid[1], 2))

                    elif directions[i] == UP:
                        hyp = math.sqrt(math.pow(pmcoor[0] - self.grid[0], 2) + math.pow(pmcoor[1]
                                                                                              - self.grid[1]+1, 2))

                    if hyp < minimum:
                        minimum = hyp
                        index = i

            self.dir = directions[index]

            if self.flag[3]:
                    if self.dir == UP and valid[1]:
                        self.dir = DOWN
                    elif self.dir == DOWN and valid[0]:
                        self.dir = UP
                    elif self.dir == LEFT and valid[3]:
                        self.dir = RIGHT
                    elif self.dir == RIGHT and valid[2]:
                        self.dir = LEFT

        elif self.flag[0]:
            self.release()


class PuckMan(pygame.sprite.Sprite):

    def __init__(self, name, pos):
        self.name = "Puck Man"
        self.pos = (WINDOW_W / 2, 188 + 24)
        self.surf = pygame.Surface([12, 13])
        self.thresh = 4
        self.dir = 'static'
        self.dead = False
        self.lives = 2
        self.gridcount = [8, 4]
        self.grid = [14, 26]
        self.reset = False

        self.lives_img = pygame.image.load("img/pm_l1.png")

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

        self.ani_death = glob.glob("img/pd_die*.png")
        self.ani_death.sort()
        self.ani_pos = 0
        self.ani_max = len(self.ani_l)-1

        self.image = pygame.image.load(self.ani_l[self.ani_pos])
        self.add()


    def die(self):
        if not self.dead:
            self.lives -= 1
            self.dead = True
            self.ani_pos = 0
            self.ani_speed = 0
            self.cnt = 8
            self.ani_death_done = False
            self.dir = NONE

    def add(self):
        if self.dir == LEFT and not self.dead:
            if self.ani_speed == 0:
                self.image = pygame.image.load(self.ani_l[self.ani_pos])
        elif self.dir == RIGHT and not self.dead:
            if self.ani_speed == 0:
                self.image = pygame.image.load(self.ani_r[self.ani_pos])
        elif self.dir == UP and not self.dead:
            if self.ani_speed == 0:
                self.image = pygame.image.load(self.ani_u[self.ani_pos])
        elif self.dir == DOWN and not self.dead:
            if self.ani_speed == 0:
                self.image = pygame.image.load(self.ani_d[self.ani_pos])

        if self.dead:

            if self.ani_speed == 0:
                self.image = pygame.image.load(self.ani_death[self.ani_pos])
                self.cnt -= 1
                self.ani_pos += 1

            if self.cnt == 0:
                self.ani_death_done = True
                self.reset = True

        self.surf.fill((0, 0, 0))
        self.surf.blit(self.image, (0, 0))


        if self.ani_pos == self.ani_max and not self.dead:
            self.ani_pos = 0

        elif self.dead and self.ani_death_done:
            sleep(3)
            self.dead = False
            self.ani_pos = 0
            self.dir = LEFT

        elif not self.dead:
            self.ani_pos += 1

        if self.ani_speed == 0:
            self.ani_speed = self.ani_speed_init
        else:
            self.ani_speed -= 1

        x = 5
        for int in range(self.lives):
            displaySurface.blit(self.lives_img, (x, 276))
            x += 14

        displaySurface.blit(self.surf, (self.pos[0] - 6, self.pos[1] - 6))

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

                    self.gridcount[1] = (self.gridcount[1] - 1) % 8
                    if self.gridcount[1] == 0:
                        self.grid[1] -= 1

        elif dir == DOWN:
            for x in range(self.pos[0] - self.thresh, self.pos[0] + self.thresh):
                if (x, self.pos[1]) in path and (x, self.pos[1] + 1) in path:
                    self.pos = (x, self.pos[1] + 1)
                    self.dir = dir
                    valid = True

                    self.gridcount[1] = (self.gridcount[1] + 1) % 8
                    if self.gridcount[1] == 0:
                        self.grid[1] += 1


        elif dir == LEFT:
            for y in range(self.pos[1] - self.thresh, self.pos[1] + self.thresh):
                if (self.pos[0], y) in path and (self.pos[0] - 1, y) in path:
                    self.pos = (self.pos[0] - 1, y)
                    self.dir = dir
                    valid = True

                    self.gridcount[0] = (self.gridcount[0] - 1) % 8
                    if self.gridcount[0] == 0:
                        self.grid[0] -= 1


        elif dir == RIGHT:
            for y in range(self.pos[1] - self.thresh, self.pos[1] + self.thresh):
                if (self.pos[0], y) in path and (self.pos[0] + 1, y) in path:
                    self.pos = (self.pos[0] + 1, y)
                    self.dir = dir
                    valid = True

                    self.gridcount[0] = (self.gridcount[0] + 1) % 8
                    if self.gridcount[0] == 0:
                        self.grid[0] += 1

        if self.pos == (8, 140):
            self.pos = (WINDOW_W - 8, 140)
            self.grid = [28, 18]
            self.gridcount = [4, 4]

        elif self.pos == (WINDOW_W - 8, 140):
            self.pos = (8, 140)
            self.grid = [1, 18]
            self.gridcount = [4, 4]

        return valid

    def rect(self):
        return pygame.Rect(self.pos[0]-6, self.pos[1]-6, 12, 13)


class Game():

    def __init__(self):
        pygame.init()
        self.score = Score()
        self.ghostrun = False
        self.pell_count = 0
        self.puckMan = PuckMan("Puck Man", (WINDOW_W / 2, 188))
        self.blinky = Blinky()
        self.clyde = Clyde()
        self.inky = Inky()
        self.pinky = Pinky()
        self.ghost_group = pygame.sprite.Group()
        self.ghost_group.add(self.pinky)
        self.ghost_group.add(self.inky)
        self.ghost_group.add(self.clyde)
        self.ghost_group.add(self.blinky)
        self.scatter = False
        self.scatter_time = 0

        self.time_keeper = 0
        self.time_counter = 0

        # how many pellets pm has to eat till the ghosts come out
        self.blinky_counter = [6, 5]
        self.clyde_counter = [15, 10]
        self.pinky_counter = [20, 20]
        self.inky_counter = [20, 20]
        self.time_keeper = 0
        self.down_press = self.up_press = self.left_press = self.right_press = False
        self.pellet = Pellet((0, 0), self.score)
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

                    elif event.key == K_d:
                        self.run_scatter()
                        for ghost in self.ghost_group:
                            ghost.dead = True

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

            if not self.puckMan.dead:
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

            if self.pell_count == self.blinky_counter[0] or self.time_counter == self.blinky_counter[1]:
                self.blinky.flag[0] = True

            if self.pell_count == self.clyde_counter[0] or self.time_counter == self.clyde_counter[1]:
                self.clyde.flag[0] = True

            if self.pell_count == self.inky_counter[0] or self.time_counter == self.inky_counter[1]:
                self.inky.flag[0] = True

            if self.pell_count == self.pinky_counter[0] or self.time_counter == self.pinky_counter[1]:
                self.pinky.flag[0] = True

            #TODO replace with sprite group
            for pellet in pel_group:
                if pellet.rect().colliderect(self.puckMan.rect()) and pellet.alive:
                    if pellet.kill() == BIG:

                        self.run_scatter()
                    self.pell_count += 1


            # add surfaces then render directly after
            displaySurface.blit(self.background, (0, 0))

            # The ghost need to stop moving if the puckman is ded
            if not self.puckMan.dead:
                self.blinky.ai(self.puckMan.grid)
                self.clyde.ai(self.puckMan.grid)
                self.inky.ai(self.puckMan.grid)
                self.pinky.ai(self.puckMan.grid, self.puckMan.dir)

            else:
                self.blinky.dir = NONE
                self.clyde.dir = NONE
                self.inky.dir = NONE
                self.pinky.dir = NONE

            self.score.render()
            self.pellet.pell_draw()
            self.puckMan.add()

            self.blinky.add()
            self.clyde.add()
            self.inky.add()
            self.pinky.add()


            for ghost in self.ghost_group:
                if self.puckMan.rect().colliderect(ghost) and not self.scatter:
                    self.puckMan.dir = NONE
                    self.life = self.puckMan.lives
                    self.puckMan.die()

                elif self.puckMan.rect().colliderect(ghost) and self.scatter:
                    ghost.dead = True


            if self.puckMan.reset:
                self.reset_death()

            # this clause is executed every second
            test_time = int(time.time())
            if test_time - self.time_keeper > 1:
                self.time_keeper = test_time
                self.time_counter += 1

                if self.scatter and self.scatter_time < 4:
                    self.scatter_time += 1

                elif self.scatter and self.scatter_time == 4:
                    for ghost in self.ghost_group:
                        ghost.flag[3] = True

            pygame.display.update()
            FPSCLOCK.tick(FPS)

    def run_scatter(self):
        """
        Turns on scatter mode if it is called when scatter is not on, does the opposite in the other case
        :return:

        if self.scatter:
            self.scatter = False

            for ghost in self.ghost_group:
                ghost.flag[3] = False
        else:"""
        self.scatter = True

        for ghost in self.ghost_group:
            ghost.flag[3] = True
            ghost.reverse()

        self.scatter_time = 0

    def reset_death(self):
        self.puckMan.pos = (WINDOW_W / 2, 188 + 24)
        self.puckMan.thresh = 4
        self.puckMan.dir = 'static'
        self.puckMan.dead = False
        self.puckMan.gridcount = [8, 4]
        self.puckMan.grid = [14, 26]
        self.puckMan.reset = False
        self.pell_count = self.time_counter = 0
        self.puckMan.lives = self.life
        self.puckMan.image = pygame.image.load(self.puckMan.ani_l[self.puckMan.ani_pos])

        self.blinky = Blinky()
        self.clyde = Clyde()
        self.inky = Inky()
        self.pinky = Pinky()
        self.ghost_group = pygame.sprite.Group()
        self.ghost_group.add(self.pinky)
        self.ghost_group.add(self.inky)
        self.ghost_group.add(self.clyde)
        self.ghost_group.add(self.blinky)

        self.down_press = self.up_press = self.left_press = self.right_press = False


if __name__ == '__main__':
    game = Game()
    game.main()






