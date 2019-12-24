
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

 
#load hình
def load_image(imagename):
    return pygame.image.load(imagename)     

class bird:
    global moveup, movedown, gravity, cactusrect, firerect
    speed = 10
    downspeed = 10

    def __init__(self):
        self.image = load_image('bird3.png')
        self.imagerect = self.image.get_rect()
        self.imagerect.topleft = (30,window_height/2)
        self.score = 0

    


def terminate():        #kết thúc chương trình
    pygame.quit()
    sys.exit()

def waitforkey():
    while True :                                        #chờ người chơi bắt đầu
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            if event.type == pygame.KEYDOWN:     #thoát chương trình nếu nhấn ESC
                if event.key == pygame.K_ESCAPE:
                    terminate()
                return



mainClock = pygame.time.Clock()
Canvas = pygame.display.set_mode((window_width,window_height))
pygame.display.set_caption('DANG VAN HIEN')

#phông chữ và âm thanh

font = pygame.font.SysFont(None, 48)
scorefont = pygame.font.SysFont(None, 30)


#load hình ảnh bắt đầu
startimage = load_image('start1.png')
startimagerect = startimage.get_rect()
startimagerect.centerx = window_width/2
startimagerect.centery = window_height/2
 


#load nhạc
pygame.mixer.music.load('nhacnen.wav')
gameover = pygame.mixer.Sound('mario_dies.wav')



#drawtext('HIEN', font, Canvas,(window_width/3), (window_height/3))
Canvas.blit(startimage, startimagerect)

#hiển thị màn hình chờ
pygame.display.update()
waitforkey()

#start for the main code

topscore = 0
Dragon = dragon()

while True:

    flame_list = []
    player = bird()
    moveup = movedown = gravity = False
    flameaddcounter = 0

    gameover.stop()
    pygame.mixer.music.play(-1,0.0)

    

    while True:     #the main game loop
        
        for event in pygame.event.get():
            if event.type == QUIT:
                terminate()

            if event.type == KEYUP:
                
                if event.key == K_UP:
                    movedown = False
                    moveup = True
                    gravity = False

                if event.key == K_DOWN:
                    movedown = True
                    moveup = False
                    gravity = False

            if event.type == KEYDOWN:

                if event.key == K_UP:
                    moveup = True
                    movedown = False
                    gravity = True
                if event.key == K_DOWN:
                    movedown = True
                    gravity = False
                    moveup = False

           
                    
                if event.key == K_ESCAPE:
                    terminate()

        flameaddcounter += 1
       # check_level(player.score)
        
       
        if flameaddcounter == addnewflamerate:

            flameaddcounter = 0
            newflame = flames()
            flame_list.append(newflame)

        
        #tạo đạn 
        for f in flame_list:
            flames.update(f)

        #remove
        for f in flame_list:
            if f.imagerect.left <= 0:
                flame_list.remove(f)

      
    #    Dragon.update()

      
        screen = pygame.display.set_mode((1200,600))

        bg = pygame.image.load("bg2.png")
       
    
        Canvas.blit(bg,(0,0))        

   
    
      
        Canvas.blit(player.image, player.imagerect)
        Canvas.blit(Dragon.image, Dragon.imagerect)
        

     
        
        for f in flame_list:
            Canvas.blit(f.surface, f.imagerect)

               

      

        pygame.display.update()

        mainClock.tick(fps)
    
        



        
    


        
               
                                                     
                    
            
        

    
