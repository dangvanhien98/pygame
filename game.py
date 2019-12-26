
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

#tốc độ game
fps = 25  
level = 0
addnewflamerate = 20 #tốc độ bắn đạn



class dragon:

    global firerect, imagerect, Canvas
    up = False
    down = True
    velocity = 10 # tốc độ di chuyển rồng
    
    def __init__(self):
        self.image = load_image('image/dragon.png')
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

 
    #trả về chiều cao        
    def return_height(self):
        h = self.imagerect.top
        return h


class flames:
    #tốc độ đạn
    flamespeed = 20

    def __init__(self):
        self.image = load_image('image/ant.png')
        self.imagerect = self.image.get_rect()
        #rồng đạn theo rồng
        self.height = Dragon.return_height() + 30
        self.surface = pygame.transform.scale(self.image, (30,30))
        #điểm bắt đầu của đạn
        self.imagerect = pygame.Rect(window_width - 105, self.height, 30, 30)

    #đường bay đạn phía trước    
    def update(self):
            self.imagerect.left -= self.flamespeed

    #def collision(self):
    #   if self.imagerect.left == 0:
    #       return False
    #  else:
    #       return True

class bird:
    global moveup, movedown, gravity, cactusrect, firerect
    speed = 10
    downspeed = 10

    def __init__(self):
        self.image = load_image('image/bird3.png')
        self.imagerect = self.image.get_rect()
        self.imagerect.topleft = (30,window_height/2)
        self.score = 0

    def update(self):
        
        if (moveup and (self.imagerect.top > cactusrect.bottom)): #and (self.imagerect.top > cactusrect.bottom)
            self.imagerect.top -= self.speed
            self.score += 1
            
        if (movedown and (self.imagerect.bottom < firerect.top)): # and (self.imagerect.bottom < firerect.top)
            self.imagerect.bottom += self.downspeed
            self.score += 1
        
        #trọng lực tự rơi xuống    
       # if (gravity and (self.imagerect.bottom < firerect.top)):
        #    self.imagerect.bottom += self.speed


#kết thúc chương trình
def terminate():        
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
            
            
#va chạm
def flamehitsbrid(playerrect, flames):      #kiểm tra va chạm
    for f in flame_list:
        if playerrect.colliderect(f.imagerect):
            return True
        return False

def drawtext(text, font, surface, x, y):        #hiển thị số liệu
    textobj = font.render(text, 1, white)
    textrect = textobj.get_rect()
    textrect.topleft = (x,y)
    surface.blit(textobj, textrect)

#tăng level độ khó
def check_level(score):
    global window_height, level, cactusrect, firerect
    if score in range(0,200):
        firerect.top = window_height - 50
        cactusrect.bottom = 50
        level = 1
    elif score in range(200, 400):
        firerect.top = window_height - 100
        cactusrect.bottom = 100
        level = 2
    elif score in range(400,800):
        level = 3
        firerect.top = window_height-150
        cactusrect.bottom = 150
    elif score in range(800,1200):
        level = 4
        firerect.top = window_height - 200
        cactusrect.bottom = 200

#load hình
def load_image(imagename):
    return pygame.image.load(imagename)

    

#start program


mainClock = pygame.time.Clock()
Canvas = pygame.display.set_mode((window_width,window_height))
pygame.display.set_caption('DANG VAN HIEN')

#phông chữ và âm thanh

font = pygame.font.SysFont(None, 48)
scorefont = pygame.font.SysFont(None, 30)

#hình ảnh tường lửa dưới
fireimage = load_image('image/fire_bricks.png')
firerect = fireimage.get_rect()

#hình ảnh tường xương rồng trên
cactusimage = load_image('image/cactus_bricks.png')
cactusrect = cactusimage.get_rect()

#load hình ảnh bắt đầu
startimage = load_image('image/start1.png')
startimagerect = startimage.get_rect()
startimagerect.centerx = window_width/2
startimagerect.centery = window_height/2

#load hình ảnh kết thúc
endimage = load_image('image/endgame.png')
endimagerect = startimage.get_rect()
endimagerect.centerx = window_width/2
endimagerect.centery = window_height/2

#load nhạc
pygame.mixer.music.load('music/nhacnen.wav')
gameover = pygame.mixer.Sound('music/mario_dies.wav')

# chuyển đến màn hình bắt đầu

#drawtext('HIEN', font, Canvas,(window_width/3), (window_height/3))
#hiển thị màn hình chờ
Canvas.blit(startimage, startimagerect)
pygame.display.update()
waitforkey()

#start for the main code

topscore = 0
Dragon = dragon()

while True:
    flame_list = []
    player = bird()
    moveup = movedown = False
    flameaddcounter = 0
    gameover.stop()
    pygame.mixer.music.play(-1,0.0)

    
    #vòng lặp trò chơi
    while True:             
        for event in pygame.event.get():
            if event.type == QUIT:
                terminate()

            if event.type == KEYUP:
                
                if event.key == K_UP:
                    movedown = False
                    moveup = True
                  #  gravity = False

                if event.key == K_DOWN:
                    movedown = True
                    moveup = False
                   # gravity = False

            if event.type == KEYDOWN:

                if event.key == K_UP:
                    moveup = True
                    movedown = False
                 #   gravity = True
                if event.key == K_DOWN:
                    movedown = True
                 #   gravity = False
                    moveup = False

            if event.type == KEYUP:

                if event.key == K_SPACE:
                    moveup = False
                    movedown = False
                  #  gravity = False
                    
                    
                if event.key == K_ESCAPE:
                    terminate()

        flameaddcounter += 1
        check_level(player.score)
        
       
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

        player.update()
        Dragon.update()

      
        screen = pygame.display.set_mode((1200,600))
        bg = pygame.image.load("image/bg2.png")
       
    
        Canvas.blit(bg,(0,0))        

    
        Canvas.blit(fireimage, firerect)
        Canvas.blit(cactusimage, cactusrect)
        Canvas.blit(player.image, player.imagerect)
        Canvas.blit(Dragon.image, Dragon.imagerect)
        

        drawtext('Score : %s | Top score : %s | Level : %s' %(player.score, topscore, level), scorefont, Canvas, 350, cactusrect.bottom + 10)
        
        for f in flame_list:
            Canvas.blit(f.surface, f.imagerect)

               
        #kiểm tra va chạm 
        if flamehitsbrid(player.imagerect, flame_list):
            if player.score > topscore:
                topscore = player.score
            break
        
        #kiểm tra va chạm vào tưởng lửa và xương rồng 
        if ((player.imagerect.top <= cactusrect.bottom) or (player.imagerect.bottom >= firerect.top)):
            if player.score > topscore:
                topscore = player.score
            break

        pygame.display.update()

        #tần suất game
        mainClock.tick(fps)
    
    pygame.mixer.music.stop()
    gameover.play()
    Canvas.blit(endimage, endimagerect)
    pygame.display.update()
    waitforkey()
        
    


        
               
                                                     
                    
            
        

    
