import pygame
import sys
from pygame.locals import *
import random
from time import sleep

# game setup constants
WINDOWWIDTH = 640
WINDOWHEIGHT = 480
FPS = 60
BLANK = None

FPSCLOCK = pygame.time.Clock()


# dictate player boundaries
SIDE_BOUNDARY = 20
Y_TOP_BOUNDARY = 40
Y_BOT_BOUNDARY = WINDOWHEIGHT - 40
PLAYER_WIDTH = 15
PLAYER_HEIGHT = 50


# direction variables
UP = 'up'
DOWN = 'down'
LEFT = 'left'
RIGHT = 'right'

# color variables
BLACK = pygame.Color(0, 0, 0)
WHITE = pygame.Color(255, 255, 255)

# game surfaces
DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
background = DISPLAYSURF.convert()
background.fill(WHITE)
player_sur = pygame.Surface((PLAYER_WIDTH, PLAYER_HEIGHT))

class Player():
    """
    A pong paddle
    """

    def __init__(self, game, side, state):
        """

        :param surface: Which surface the player is on.
        :param side: Which side the player is on.
        """

        self.player = player_sur.convert()
        self.player.fill((255, 0, 0))
        self.speed = 10  # determines how fast the player(s) move
        self.side = side
        self.game = game
        self.state = state
        self.delay = 3

        if side == LEFT:
            self.top_l_x = SIDE_BOUNDARY

        elif side == RIGHT:
            self.top_l_x = WINDOWWIDTH - SIDE_BOUNDARY - PLAYER_WIDTH
        else:
            assert ()

        self.top_l_y = Y_TOP_BOUNDARY
        self.bot_r_x = self.top_r_x = self.top_l_x + PLAYER_WIDTH
        self.bot_r_y = Y_TOP_BOUNDARY + PLAYER_HEIGHT
        self.render()

    def render(self):
        DISPLAYSURF.blit(self.player, (self.top_l_x, self.top_l_y))

    def move(self, dir):

        if self.delay == 0:
            if dir == DOWN and self.bot_r_y + self.speed <= Y_BOT_BOUNDARY:
                self.top_l_y += self.speed
                self.bot_r_y += self.speed


            elif dir == UP and self.top_l_y - self.speed >= Y_TOP_BOUNDARY:
                self.top_l_y -= self.speed
                self.bot_r_y -= self.speed
        else:
            self.delay -= 1

    def rect(self):
        if self.side == LEFT:
            return Rect(self.top_l_x, self.top_l_y, PLAYER_WIDTH, PLAYER_HEIGHT)
        else:
            return Rect(self.top_r_x - PLAYER_WIDTH, self.top_l_y, PLAYER_WIDTH, PLAYER_HEIGHT)


    def ai(self):
        if self.state == UP:
            if self.game.game_ball.pos[1] > self.top_l_y + PLAYER_HEIGHT/2:
                self.move(DOWN)
            else:
                self.move(UP)


class Ball:
    def __init__(self, Game, lplayer, rplayer, player):
        """
        :param surface: Which surface the ball is on.
        :param player:  Dictates which side the ball starts on.
        """
        self.ball_h = 8  # must be even
        self.ball = pygame.Surface((self.ball_h, self.ball_h))
        self.ball.fill(BLACK)
        self.game = Game
        self.direction = []
        self.speed = 8
        self.players = [lplayer, rplayer]

        if player.side == LEFT:
            self.origin = (player.top_r_x + PLAYER_WIDTH, (self.ball_h / 2) + Y_TOP_BOUNDARY + (PLAYER_HEIGHT / 2))
            self.direction.append(RIGHT)
        else:
            self.origin = (player.top_l_x - PLAYER_WIDTH - self.ball_h, 2 + Y_TOP_BOUNDARY + PLAYER_HEIGHT / 2)
            self.direction.append(LEFT)

        if random.random() < .5:
            self.direction.append(DOWN)
        else:
            self.direction.append(UP)

        self.pos = [self.origin[0], self.origin[1]]

        DISPLAYSURF.blit(self.ball, (self.origin[0], self.origin[1]))

    def bounce(self):
        """
        Tests if ball is hitting boundaries, if so, it calculates bounce position.
        """

        ball_rect = pygame.Rect(self.pos[0], self.pos[1], self.ball_h, self.ball_h)

        # bounce of the top you start going down
        if self.pos[1] <= Y_TOP_BOUNDARY:
            self.direction[1] = DOWN

        elif self.pos[1] + self.ball_h >= Y_BOT_BOUNDARY:
            self.direction[1] = UP


        if self.pos[0] + self.ball_h >= WINDOWWIDTH - SIDE_BOUNDARY:
            self.game.point(LEFT)

        elif self.pos[0] <= SIDE_BOUNDARY:
            self.game.point(RIGHT)

        else:
            if self.players[0].rect().colliderect(ball_rect):
                    self.direction[0] = RIGHT

            elif self.players[1].rect().colliderect(ball_rect):
                    self.direction[0] = LEFT


    def move(self):
        """
        Moves the ball based on the direction.
        """

        if self.direction[0] == LEFT:
            self.pos[0] -= self.speed
            if self.direction[1] == UP:
                self.pos[1] -= self.speed

            elif self.direction[1] == DOWN:
                self.pos[1] += self.speed

        else:
            self.pos[0] += self.speed
            if self.direction[1] == UP:
                self.pos[1] -= self.speed

            elif self.direction[1] == DOWN:
                self.pos[1] += self.speed

    def render(self):
        self.bounce()
        DISPLAYSURF.blit(self.ball, (self.pos[0], self.pos[1]))


class game:
    def __init__(self):

        pygame.init()

        self.pressed_down = self.pressed_up = False

        pygame.display.set_caption('Pong Hit')
        DISPLAYSURF.fill(WHITE)

        self.score = [0, 0]
        self.font = pygame.font.SysFont("calibri", 40)
        self.score1 = self.font.render(str(self.score[0]), True, BLACK)
        self.score2 = self.font.render(str(self.score[1]), True, BLACK)

        self.lplayer = Player(self, LEFT, DOWN)
        self.rplayer = Player(self, RIGHT, UP)
        self.rplayer.delay = 3
        self.game_ball = Ball(self, self.lplayer, self.rplayer, self.lplayer)

    def reset(self):
        self.score1 = self.font.render(str(self.score[0]), True, BLACK)
        self.score2 = self.font.render(str(self.score[1]), True, BLACK)

        self.lplayer = Player(self, LEFT, DOWN)
        self.rplayer = Player(self, RIGHT, UP)
        self.game_ball = Ball(self, self.lplayer, self.rplayer, self.lplayer)
        sleep(1)

    def main(self):

        while True:  # main game loop

            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_UP:
                        self.pressed_up = True

                    elif event.key == K_DOWN:
                        self.pressed_down = True


                elif event.type == KEYUP:
                    if event.key == K_UP:
                        self.pressed_up = False

                    elif event.key == K_DOWN:
                        self.pressed_down = False

                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()

            if self.pressed_up:
                self.lplayer.move(UP)
            elif self.pressed_down:
                self.lplayer.move(DOWN)

            self.rplayer.ai()

            self.game_ball.move()


            DISPLAYSURF.blit(background, (0, 0))
            self.lplayer.render()
            self.rplayer.render()
            self.game_ball.render()
            DISPLAYSURF.blit(self.score1, (WINDOWWIDTH/2 - 20, 10))
            DISPLAYSURF.blit(self.score2, (WINDOWWIDTH/2 + 20, 10))


            pygame.display.update()
            FPSCLOCK.tick(FPS)

    def point (self, side):
        if side == LEFT:
            self.score[0] += 1
            self.reset()

        else:
            self.score[1] += 1
            self.reset()

if __name__ == "__main__":
    Game = game()
    Game.main()