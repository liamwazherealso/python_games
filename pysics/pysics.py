# This is my attempt, at a 2d physics simulator for simple mechanics
import pygame
import math
import sys

class Vec:
    """
    Class that defines a 2d vector and some useful functions with it.
    Vectors contain the actual values, but have also a length scaled by the simulation.
    """

    def __init__(self, i, j):
        """
        :param i: x length
        :param j: y length
        """
        self.vec = [i, j]
        self.pos = [0, 0]
        self.svec = self.vec
        self.scalar = 1

    def __add__(self, other):
        self.vec = [self.vec[0] + other[0], self.vec[1] + other[1]]
        self.scale()
        return Vec(self.vec[0] + other[0], self.vec[1] + other[1])

    def mul(self, other):
        """
        :param other: either a scalar or a vector.
        :return: the vector
        """
        if len(str(other)) == 1:
            self.vec = [self.vec[0] * other, self.vec[1] * other]
            return self.vec
        else:
            self.vec = [self.vec[0] * other[0], self.vec[1] * other[1]]
            return self.vec

    def __getitem__(self, item):
        return self.vec[item]

    def __str__(self):
        return str(self.vec)

    def pos(self, x, y):
        self.pos = [x, y]

    def scale(self):
        """
        Function for applying scale of the simulation to the vector so it can be displayed properly.
        Does not change the 'true' vector information
        :return:
        """
        self.svec = [self.vec[0] * self.scalar, self.vec[1] * self.scalar]

class Simulation:
    """
    A class that makes an interface for the pygame to pysics objects
    """

    def __init__(self, scale, window_w, window_h, surface):
        self.window_w = window_w
        self.window_h = window_h
        self.scale = scale
        self.surface = surface
        self.vectors = []

    def add_Vec(self, i, j):
        """
        Used to add vectors to my list and create a new vector
        """
        self.vectors.append(Vec(i, j))

    def draw_vectors(self):
        """
        draw all the vectors given in the simulation, this draws a red line and a blue end to represent an arrow
        :return:
        """

        for v in self.vectors:
            if v.vec[0] != 0:
                theta = math.atan(v.vec[1]/v.vec[0])
            else:
                theta = math.pi/2

            sin = math.sin(theta)
            cos = math.cos(theta)
            # draw main line
            pygame.draw.line(self.surface, (255, 0, 0), (v.pos[0], self.window_h - v.pos[1] - 1),
                             (v.vec[0] - self.scale * cos, self.window_h - v.vec[1] + self.scale * sin - 1))
            # draw green line to indicate direction
            pygame.draw.line(self.surface, (0, 255, 0), (v.vec[0] - self.scale * cos, self.window_h - v.vec[1]
                            - 1+self.scale * sin), (v.vec[0], self.window_h - v.vec[1]-1-self.scale*sin))

            print "{:.7} {:7.2f} {:7.2f} {:7.2f}".format(v.vec, cos, sin, math.degrees(theta))
        sys.exit(0)


class Obj():
    """
    Though making every object have it's own class, it may be beneficial.
    """

    def __init__(self, pos, mass, rect, vel, acc):
        """
        mass: kg, I am not doing unit conversion so I am gonna stick with kg.
        shape: pygame shape object. Size information is drawn from this.
        vel: Initial velocity vector
        acc: Initial acceleration vector, not adding jerk
        """
        self.mass = mass
        self.rect = rect
        self.vel = vel
        self.acc = acc
        self.pos = pos
        self.cm = [self.rect.width/2,  self.rect.height/2]

    def mov(self, time):
        for i in range(1):
            self.vel[i] = self.acc[i] * time
            self.pos[i] = self.pos[i] + self.vel[i] * time + .5 * math.pow(self.acc[i], 2)

    def col(self, o):
        """
        :param o: The other object in the collision.
        """
        vi1 = self.vel
        vi2 = o.vel

        for i in range(1):

            self.vel[i] = (self.mass - o.mass)/(self.mass + o.mass) * vi1[i] + (2*o.mass)/(self.mass + o.mass) * vi2[i]
            o.vel[i] = (2*o.mass)/(self.mass + o.mass) * vi2[i] - (self.mass - o.mass)/(self.mass + o.mass) * vi1[i]
