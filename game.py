
#Import modules

import pygame, random, sys
from pygame.locals import *
pygame.init()

#màn hình

window_height=600 
window_width=1200

blue = (0,0,255)
black = (0,0,0)
white = (255, 255, 255)

fps = 25  
level = 0
addnewflamerate = 20 #tốc độ bắn đạn

#defining the required function

class dragon:

    global firerect, imagerect, Canvas
    up = False
    down = True
    velocity = 10 # tốc độ di chuyển rồng
    
    def __init__(self):
        self.image = load_image('dragon.png')
        self.imagerect = self.image.get_rect()
        self.imagerect.right = window_width
        self.imagerect.top = window_height/2

    def update(self):
        # không cho rồng đi lên khỏi màn hình
        if (self.imagerect.top < cactusrect.bottom):
            self.up = False
            self.down = True

         # không cho rồng đi xuống khỏi màn hình
        if (self.imagerect.bottom > firerect.top):
            self.up = True
            self.down = False
        
        #di chuyển xuống    
        if (self.down):
            self.imagerect.bottom += self.velocity

        #di chuyển lên    
        if (self.up):
            self.imagerect.top -= self.velocity

        Canvas.blit(self.image, self.imagerect)

    def return_height(self):

        h = self.imagerect.top
        return h

class flames:
    #tốc độ đạn
    flamespeed = 20

    def __init__(self):
        self.image = load_image('ant.png')
        self.imagerect = self.image.get_rect()
        #đạn theo rồng
        self.height = Dragon.return_height() + 20
        self.surface = pygame.transform.scale(self.image, (30,30))
        #điểm bắt đầu của đạn
        self.imagerect = pygame.Rect(window_width - 105, self.height, 30, 30)

    #đường bay đạn phía trước    
    def update(self):
            self.imagerect.left -= self.flamespeed

    def collision(self):
        if self.imagerect.left == 0:
            return True
        else:
            return False






        
    


        
               
                                                     
                    
            
        

    
