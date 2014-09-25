import pygame, sys, random
from pygame.locals import *

class gradient():
    x_coor = 0 
    y_coor = 0
    rval = 0 
    gval = 0
    bval = 0

    def turn_black(self):
        self.x_coor = 0
        self.rval = 0
        self.gval = 0
        self.bval = 0

    def gradient(self, r_ord, g_ord, b_ord): 
        """ 
        Creates Gratient by choosing order of color values to increase.
        Always starts at black.
        """
        self.turn_black()
        
        for step in range(1,4):
            if r_ord == step:
                self.r_gradient()
            elif g_ord == step:
                self.g_gradient()
            else:
                self.b_gradient()
        self.y_coor = (self.y_coor + 50) % 300
        

    def r_gradient(self):
        for x in range(0, 256): # Excludes 256 in list
            pygame.draw.line(DISPLAYSURF, (self.rval, self.gval, self.bval), (self.x_coor, self.y_coor), ( self.x_coor, self.y_coor + 49), 1 )
            self.x_coor += 1 
            self.rval += 1
            pygame.display.update()
        # increases rval to 256 in last iteration which is invalid, so I decrease it
        self.rval -= 1

    def g_gradient(self):
        for x in range(0, 256):
             pygame.draw.line(DISPLAYSURF, (self.rval, self.gval, self.bval), (self.x_coor, self.y_coor), ( self.x_coor, self.y_coor + 49), 1 )
             self.x_coor += 1 
             self.gval += 1
             pygame.display.update()

        self.gval -= 1 

    def b_gradient(self):
        for x in range(0, 256):
            pygame.draw.line(DISPLAYSURF, (self.rval, self.gval, self.bval), (self.x_coor, self.y_coor), ( self.x_coor, self.y_coor + 49), 1 )
            self.x_coor += 1 
            self.bval += 1
            pygame.display.update()

        self.bval -= 1

    def all_gradient(self):
        """
        My silly way of making a random generator for all the combinations
        """
        options = range(0,7)

        for x in range(0,7):
            option = random.choice(options)
            options.remove(option)
            
            if option == 0:
                self.gradient(1,2,3)
            elif option == 1:
                self.gradient(1,3,2)
            elif option == 2:
                self.gradient(2,1,3)
            elif option == 3:
                self.gradient(2,3,1)
            elif option == 4:
                self.gradient(3,1,2)
            elif option == 5:
                self.gradient(3,2,1)
      

if __name__ == "__main__":
    # initial pygame setup
    pygame.init()
    DISPLAYSURF = pygame.display.set_mode((768,300), 0 , 32)
    pygame.display.set_caption('Drawing')
    DISPLAYSURF.fill((255,255,255))
    pygame.display.update()

    Gradient = gradient()

    while True: # main game loop
         answer = raw_input("Would you like to draw a gratient? Type (y/n)\n")
         if answer == "y":

             next_answer = raw_input("Would you like to pick the gratient? (y/n)\n")

             if next_answer == "y": 
                 g_order = raw_input("What would you like the order to be?\n(Give a string of 3 number, representing the order r/g/b.\n")
                 if g_order.isalnum() and len(g_order) == 3:
                     Gradient.gradient(int(g_order[0]),int(g_order[1]),int(g_order[2]))
     
                 else:
                     print "Invalid input"

             elif next_answer == "n":
                 Gradient.all_gradient()
             
             else:
                 print "Invalid input"
 
         else:
             pygame.quit()
             sys.exit()

   
         for event in pygame.event.get():
             if event.type == QUIT:
                 pygame.quit()
                 sys.exit()
         
