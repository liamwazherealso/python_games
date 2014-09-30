#Did you know that the original name for Pac-Man was Puck-Man? You'd think it was because he looks like a hockey puck
# but it actually comes from the Japanese phrase 'Paku-Paku,' which means to flap one's mouth open and closed. They
# changed it because they thought Puck-Man would be too easy to vandalize, you know, like people could just scratch off
#  the P and turn it into an F or whatever. - Scott Pilgrim vs. The world

import pygame, sys
from pygame.locals import *


WINDOW_H = 248
WINDOW_W = 224


class Path():
    """
    We can make the programming of the game map simpler (I think) by just creating valid paths.
    """

    def __init__(self):

        self.path_list = []

        # the boundary is 4 pixels, path dia is 8
        bd = 4
        pr = 16

        r1y = pr + bd
        for x in range(pr + bd, 108 - pr):
            self.path_list.append((x, r1y))

        for x in range(116, WINDOW_W - pr - bd):
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

        r6y = 128 + pr
        for x in range(68 + pr, 156 - pr):
            self.path_list.append((x, r6y))

        r7y = 156 + pr
        for x in range(pd + pr, 108 - pr):
            self.path_list.append((x, r7y))

        for x in range(116 + pr, WINDOW_W - bd - pr):
            self.path_list.append((x, r7y))

        r8y = 180 + pr
        for x in range(bd + pr, 36 - pr):
            self.path_list.append((x, r8y))

        for x in range(188 + pr, WINDOW_W - pr):
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
            self.path_list.append((x, r9y))