import pygame,random,sys,math
from pygame.locals import *

TILE_SIZE=100
WIDTH=1600
HEIGHT=1200
GRAVITY=40

pygame.init()
pygame.display.list_modes()[0]
screen=pygame.display.set_mode((WIDTH,HEIGHT),FULLSCREEN)
magic_brick1=pygame.image.load("magic_brick.png")
magic_brick2=pygame.image.load("magic_brick2.png")
magic_brick1_1x2=pygame.image.load("rect1x2p1.png")
magic_brick2_1x2=pygame.image.load("rect1x2p2.png")
magic_brick1_1x3=pygame.image.load("rect1x3p1.png")
magic_brick2_1x3=pygame.image.load("rect1x3p2.png")
magic_brick1_1x4=pygame.image.load("rect1x4p1.png")
magic_brick2_1x4=pygame.image.load("rect1x4p2.png")
glow=pygame.image.load("glow.png").convert_alpha()
glow1x2=pygame.image.load("glow1x2.png")
ground_block1=pygame.image.load("castleground1.png")
ground_block2=pygame.image.load("castleground2.png")
sprite_sheet=pygame.image.load("WizardWalk3 100 199.png").convert_alpha()
standing_image=pygame.image.load("WizardStand3 100 199.png").convert_alpha()
key_image=pygame.image.load("Bronze key picture.png").convert_alpha()
text = pygame.font.Font(None, 72)
grabbedBlock=None
grabNum=None

#sprite_sheet.fill((255,0,0))
#standing_image.fill((255,0,0))

class Block:
    def __init__(self,x,y,magic,dimensions=(1,1)):
        self.rect=pygame.Rect(x,y,dimensions[0]*TILE_SIZE,dimensions[1]*TILE_SIZE)
        self.vel_y=0#only y velocity because gravity is the only force acting on it
        self.picture1=(random.random()<.5)
        self.magic=magic
    
    def whratio(self):
        if self.rect.width>=self.rect.height:           #returns the ratio of width to height of the block, minus 1.
            return self.rect.width/self.rect.height-1   #so, a 1x1 block returns 0, a 2x1 block returns 1, a 3x1 block returns 2, etc.
        else:                                 #vertical rectangle blocks return negative values, so...
            return -self.rect.height/self.rect.width+1  #a 1x2 block returns -1, a 1x3 block returns -2, etc.
    
    def update(self,world,dt):
        self.vel_y+=GRAVITY
        self.rect.y+=self.vel_y*dt/1000.0
        for block in world.magicList+world.groundList:
                if block==self:
                    continue
                if block.rect.colliderect(self.rect):
                    self.rect.bottom=block.rect.y
                    self.vel_y=0
        if self.rect.colliderect(world.wizard.rect) and self.rect.centery<world.wizard.rect.centery:
            world.reset(world.room)
        if self.rect.bottom>HEIGHT:
            self.vel_y=0
            self.bottom=HEIGHT
    
    def draw(self,screen,time):
        if self.magic and random.random()<.2:
            self.picture1=not self.picture1
        if self.magic:
            if self.whratio()==0:
                screen.blit(magic_brick1 if self.picture1 else magic_brick2,self.rect)
            elif self.whratio()==-1:
                screen.blit(magic_brick1_1x2 if self.picture1 else magic_brick2_1x2,self.rect)
            elif self.whratio()==1:
                screen.blit(pygame.transform.rotate(magic_brick1_1x2 if self.picture1 else magic_brick2_1x2,90),self.rect)
            elif self.whratio()==-2:
                screen.blit(magic_brick1_1x3 if self.picture1 else magic_brick2_1x3,self.rect)
            elif self.whratio()==2:
                screen.blit(pygame.transform.rotate(magic_brick1_1x3 if self.picture1 else magic_brick2_1x3,90),self.rect)
            elif self.whratio()==-3:
                screen.blit(magic_brick1_1x4 if self.picture1 else magic_brick2_1x4,self.rect)
            elif self.whratio()==3:
                screen.blit(pygame.transform.rotate(magic_brick1_1x4 if self.picture1 else magic_brick2_1x4,90),self.rect)
        else:
            screen.blit(ground_block1 if self.picture1 else ground_block2,self.rect)
            
class Wizard(object): #Player
    def __init__(self, x, y,world):
        #The porperties of the player character
        self.rect = pygame.Rect(x,y,100,199) #Wizard Rectangle
        self.vel_x = 200 # Velocity variables that change based on the events on the screen
        self.vel_y = 0
        self.right = True #boolean: true if the player is facing right, false if he is facing left
        self.moving = False #boolean: true if the player is moving
        self.elapsed = 0
        self.updateRate = 250
        self.frame = 0
        self.jump = False
        self.fall = False #Set to True if the player is on the ground.  Set to false if the player is on the ground
        self.key = False
    
    def update(self,deltatime):
        #Changes the player character's status/position based on events that have taken place
        dt = deltatime / 1000.0

        #Makes the player fall if they are in the air.  Also makes them stop moving downwards if they are on the ground
        if self.fall == True:
            self.vel_y += GRAVITY
        elif self.fall == False:
            self.vel_y = 0
            
        #Makes the player jump if they have pressed the up key
        if self.jump == True:
            self.vel_y = -77*GRAVITY**.5
            
        if self.rect.colliderect(world.key_rect):
            self.key = True
        
        #Change the player direction based on the movement direction
        if self.moving:
            self.elapsed += deltatime
            if self.elapsed > self.updateRate:
                self.frame = (self.frame + 1) % 5
                self.elapsed = 0
        else:
            self.frame=0
        self.rect.move_ip(((1 if self.right else -1) if self.moving else 0) * self.vel_x * dt, self.vel_y * dt)
        if self.rect.left<0:
            self.rect.x=0
        if self.rect.right>WIDTH:
            if self.key: #If they player is touching the key and touches the right of the screen, go to the next level
                self.rect.x = 0
                world.reset(world.room+1)
                return
            else:
                self.rect.right=WIDTH
        if self.rect.top<0:
            self.rect.top=0
            self.vel_y=0
        if self.rect.top >= HEIGHT:
            self.rect.topleft = (0, 901)
            self.world.reset(world.room)
        for block in world.groundList+world.magicList:
            if self.rect.colliderect(block.rect) and self.rect.bottom>block.rect.top+5:
                if self.rect.right<block.rect.left+15:
                    moving=False
                    self.rect.right=block.rect.left
                if self.rect.left>block.rect.right-15:
                    moving=False
                    self.rect.left=block.rect.right
    
    def draw(self, screen):
        #Draws the player onto the screen
        if self.moving:
            image=sprite_sheet.subsurface(100*self.frame,0,100,199)
            screen.blit(image if self.right else pygame.transform.flip(image,True,False),self.rect)
        else:
            screen.blit(standing_image if self.right else pygame.transform.flip(standing_image,True,False),self.rect)
            
class World(object):
    def __init__(self):
        self.reset(1) #Initializes the player
        
    def reset(self,room):
        #Initializes the tiles based on the room the player is in
        
        self.wizard=Wizard(0,901,self)
        self.room=room
        grabbedBlock=None
        grabNum=None
        self.groundList = [] #List of static ground blocks
        self.magicList = []  #List of semi-dynamic "magic blocks"
        self.tilelist = open("ROOM "+str(room)+".txt").readlines()#List that tells the computer where to draw each tile
        
        #for loop that goes through the list of lists
        for x in range(len(self.tilelist)):
            # for loop that breaks apart the individual lists and draws each tile
            for n, i in enumerate(self.tilelist[x].split(' ')):
                if i == "G": #Checks if the tile is ground
                    self.groundList.append(Block(n*TILE_SIZE,x*TILE_SIZE,False)) #creates a list of tiles with tuples for their images and rectangles
                if i == "M": #Checks if the tile is a magic block
                    self.magicList.append(Block(n*TILE_SIZE, x*TILE_SIZE,True)) #Adds magic bricks to the magicList
                if i == "Q":
                    self.magicList.append(Block(n*TILE_SIZE,x*TILE_SIZE,True,dimensions=(1,2)))
                if i == "W":
                    self.magicList.append(Block(n*TILE_SIZE,x*TILE_SIZE,True,dimensions=(1,3)))
                if i == "E":
                    self.magicList.append(Block(n*TILE_SIZE,x*TILE_SIZE,True,dimensions=(1,4)))
                if i == "K":
                    self.key_rect = pygame.Rect(n*TILE_SIZE, x*TILE_SIZE, TILE_SIZE, TILE_SIZE)
                    
    def update(self,dt):
        self.wizard.update(dt)
        
    def draw(self,screen):
        self.wizard.draw(screen)

world = World() #Initialize the world
                    
clock=pygame.time.Clock()
mousex=mousey=0
leftClick=rightClick=False

dt = 60
time=0

while True:

    dt=pygame.time.get_ticks()-time
    time=pygame.time.get_ticks()
    clock.tick(30)
    world.wizard.jump = False #Set jump to false (unless switched to True later in the code)
    
    for block in world.magicList+world.groundList:
        if world.wizard.rect.colliderect(block.rect): #Checks if the player is colliding with the ground or a magic block
            if world.wizard.rect.centery<=block.rect.centery:
                world.wizard.rect.bottom = block.rect.top+2
                world.wizard.fall = False
                break
            else:
                world.wizard.rect.top = block.rect.bottom+1
    else:
        world.wizard.fall = True
    
    for event in pygame.event.get():
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()
            elif event.key==pygame.K_SPACE:
                world.wizard.rect.x=0
                world.reset(world.room+1)
            elif event.key==pygame.K_s:
                if grabbedBlock:
                    grabbedBlock.rect.width,grabbedBlock.rect.height=grabbedBlock.rect.height,grabbedBlock.rect.width
                    if grabbedBlock.whratio()<0:
                        grabbedBlock.rect.y-=(math.fabs(grabbedBlock.whratio())-grabNum)*TILE_SIZE
                        grabbedBlock.rect.x+=grabNum*TILE_SIZE
                        grabNum=grabbedBlock.rect.height/TILE_SIZE-1-grabNum
                    elif grabbedBlock.whratio()>0:
                        grabbedBlock.rect.x+=(math.fabs(grabbedBlock.whratio())-grabNum-1)*TILE_SIZE
                        grabbedBlock.rect.y+=grabNum*TILE_SIZE
            elif event.key == pygame.K_a or event.key == pygame.K_LEFT:
                world.wizard.moving=True
                world.wizard.right=False
            elif event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                world.wizard.moving=True
                world.wizard.right=True
            elif event.key == pygame.K_w or event.key == pygame.K_UP:
                if world.wizard.jump == False and world.wizard.fall == False: #Sets jump to true only if the key was just pressed and the player is not falling
                    world.wizard.jump = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                world.wizard.moving=False
            elif event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                world.wizard.moving=False
        elif event.type==pygame.MOUSEBUTTONDOWN:
            mousex,mousey=event.pos
            if event.button==1:
                leftClick=True
                for block in world.magicList: #test to see if it grabs something
                    if block.rect.collidepoint(mousex,mousey):
                        grabbedBlock=block
                        world.magicList.remove(block)
                        grabbedBlock.vel_y=0
                        if grabbedBlock.whratio()==0:
                            grabNum=0
                        elif grabbedBlock.whratio()>0:
                            grabNum=(mousex-grabbedBlock.rect.x)/TILE_SIZE
                        else:
                            grabNum=(mousey-grabbedBlock.rect.y)/TILE_SIZE
                        break
        if event.type==pygame.MOUSEBUTTONUP:
            mousex,mousey=event.pos
            if event.button==1:
                leftClick=False
        if event.type==pygame.MOUSEMOTION:
            if grabbedBlock:
                grabbedBlock.rect.x=int(event.pos[0]/TILE_SIZE-(grabNum if grabbedBlock.whratio()>0 else 0))*TILE_SIZE
                grabbedBlock.rect.y+=event.pos[1]-mousey
            mousex,mousey=event.pos
            
    screen.fill((100,100,100))
    
    roomDisplayText = text.render("Room:"+str(world.room), 1, (255, 0, 0))
    roomDisplayRect = roomDisplayText.get_rect()
    roomDisplayRect.topleft = (0,0)
    screen.blit(roomDisplayText, roomDisplayRect)
    
    #Update the world
    world.update(dt)
        
    #Draw the player and the world
    world.draw(screen)
    for block in world.magicList:
        block.update(world,dt)
        block.draw(screen,time)
    for block in world.groundList:
        block.draw(screen,time)
    if grabbedBlock:
        if not leftClick:
            for block in world.magicList+world.groundList:
                if grabbedBlock.rect.colliderect(block.rect):
                    break
            else:
                if not grabbedBlock.rect.colliderect(world.wizard.rect):
                    world.magicList.append(grabbedBlock)
                    grabbedBlock=None
                    grabNum=None
        if grabbedBlock:
            grabbedBlock.draw(screen,time)
            if grabbedBlock.whratio()==0:
                screen.blit(glow,glow.get_rect().move(grabbedBlock.rect.x-25,grabbedBlock.rect.y-25))
            elif grabbedBlock.whratio()==-1:
                screen.blit(glow1x2,glow1x2.get_rect().move(grabbedBlock.rect.x-25,grabbedBlock.rect.y-25))
            elif grabbedBlock.whratio()==1:
                screen.blit(pygame.transform.rotate(glow1x2,90),glow1x2.get_rect().move(grabbedBlock.rect.x-25,grabbedBlock.rect.y-25))
            elif grabbedBlock.whratio()==-2:
                screen.blit(glow1x3,glow1x3.get_rect().move(grabbedBlock.rect.x-25,grabbedBlock.rect.y-25))
            elif grabbedBlock.whratio()==2:
                screen.blit(pygame.transform.rotate(glow1x3,90),glow1x3.get_rect().move(grabbedBlock.rect.x-25,grabbedBlock.rect.y-25))
            elif grabbedBlock.whratio()==-3:
                screen.blit(glow1x4,glow1x4.get_rect().move(grabbedBlock.rect.x-25,grabbedBlock.rect.y-25))
            elif grabbedBlock.whratio()==3:
                screen.blit(pygame.transform.rotate(glow1x4,90),glow1x4.get_rect().move(grabbedBlock.rect.x-25,grabbedBlock.rect.y-25))
            #screen.blit(glow,pygame.Rect(grabbedblock.rect.x*TILE_SIZE-25,grabbedblock.rect.y-25,150,150))
    if world.wizard.key == False:
        screen.blit(key_image, world.key_rect)
    
    pygame.display.flip()