import pygame, sys, random
from pygame.locals import *

# Colors in pygame can be given in an argument as a tuple of three numbers
# ("this", "is", "a", "tuple"), ["this", 'is', 'a', 'list']
# The three arguments correspond to the amount of R, G, B in the color
# RED = pygame.Color((255, 0, 0))

class gradient():
    """
    A container for the methods and the fields. I can still construct a object of this class although it does not have
    an __init__ method.
    """

    # what height the current gradient should be drawn from
    y_coor = 0


    def turn_black(self):
        self.x_coor = 0
        # the amount of red
        self.rval = 0
        self.gval = 0
        self.bval = 0

    def gradient(self, r_ord, g_ord):
        """
        Creates Gratient by choosing order of color values to increase.
        Always starts at black.
        """
        self.turn_black()

        # This method is called in the main loop where it asks the user which color value to increase first

        for step in range(1, 4):
            if r_ord == step:
                self.r_gradient()
            elif g_ord == step:
                self.g_gradient()
            else:
                self.b_gradient()

        # when gradient is done increase the height of where you would draw from
        self.y_coor = (self.y_coor + 50) % 300
        

    def r_gradient(self):
        """
        Draws red gradient, by drawing a vertical line of the current color, then increasing red, then increasing the x
        where the line is drawn.
        """
        for x in range(1, 256): # Excludes 256 in list
            # line( Surface to be drawn on, color, point 1, point 2), recall that the larger the y the lower on the
            # screen
            pygame.draw.line(DISPLAYSURF, (self.rval, self.gval, self.bval), (self.x_coor, self.y_coor),
                             (self.x_coor, self.y_coor + 49))
            self.x_coor += 1
            self.rval = x
            # When this loop ends x_coord and rval are increased 255
            # updates the display of DISPLAYSURF, how this method is linked to DISPLAYSURF I will show later
            pygame.display.update()


        # increases rval to 256 in last iteration which is invalid, so I decrease it
        self.rval -= 1

    def g_gradient(self):
        for x in range(1, 256):
             pygame.draw.line(DISPLAYSURF, (self.rval, self.gval, self.bval), (self.x_coor, self.y_coor),
                              (self.x_coor, self.y_coor + 49))
             self.x_coor += 1 
             self.gval = x
             pygame.display.update()

    def b_gradient(self):
        for x in range(1, 256):
            pygame.draw.line(DISPLAYSURF, (self.rval, self.gval, self.bval), (self.x_coor, self.y_coor),
                             (self.x_coor, self.y_coor + 49))
            self.x_coor += 1
            self.bval = x
            pygame.display.update()


    def all_gradient(self):
        """
        My silly way of making a random generator for all the combinations
        """
        options = range(0,7)

        for x in range(0,7):
            option = random.choice(options)
            options.remove(option)
            
            if option == 0:
                self.gradient(1, 2)
            elif option == 1:
                self.gradient(1, 3)
            elif option == 2:
                self.gradient(2, 1)
            elif option == 3:
                self.gradient(2, 3)
            elif option == 4:
                self.gradient(3, 1)
            elif option == 5:
                self.gradient(3, 2)
      
# if you directly execute this python script this test will be True, otherwise (you imported) nothing will happen.
if __name__ == "__main__":
    # gets pygame to run
    pygame.init()
    #creates surface and also links it to the display
    DISPLAYSURF = pygame.display.set_mode((768, 300))
    # should be called set_title
    pygame.display.set_caption('Drawing')
    # fill the whole surface with white
    DISPLAYSURF.fill((255, 255, 255))
    pygame.display.update()

    Gradient = gradient()

    while True: # main game loop
        answer = raw_input("Would you like to draw a gradient? Type (y/n)\n")

        if answer == "y":
            next_answer = raw_input("Would you like to pick the gradient? (y/n)\n")

            if next_answer == "y":
                g_order = raw_input("What would you like the order to be?\n(Give a string of 2 numbers, "
                                    "representing the order r/g.\n")
                
                if g_order.isalnum() and len(g_order) == 2:
                    # casting the elements of the answer into a int and using them as arguments
                    Gradient.gradient(int(g_order[0]), int(g_order[1]))

                else:
                    print "Invalid input"

            elif next_answer == "n":
                Gradient.all_gradient()
             
            else:
                print "Invalid input"
 
        else:
            pygame.quit()
            sys.exit()