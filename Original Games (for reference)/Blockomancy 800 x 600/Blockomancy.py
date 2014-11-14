import pygame,random,sys,math
from pygame.locals import *

pygame.init()
pygame.display.list_modes()[0]

TILE_SIZE=None
ground_block1 = None
ground_block2 = None
world = None
WIDTH = None
HEIGHT = None
GRAVITY = None
screen = None
backgroundImage = None
backgroundStretchedImage = None
backgroundRect = menuImage = None
menuCreditsImage = None
menuCreditsStretchedImage =  None
magic_brick1 =  magic_brick2 =  None
magic_brick1_1x2 =  None
magic_brick2_1x2 =  None
glow = glow1x2 = None
sprite_sheet = None
standing_image = None
key_image = staffImage = text = None
scrollingCreditsImage = None
scrollingCreditsRect = None
darkWizardStandImage = None
darkWizardRect = None
darkWizardLife = None

def start():
    global TILE_SIZE ,WIDTH ,HEIGHT, GRAVITY, screen, backgroundImage, backgroundStretchedImage, backgroundRect, menuImage, menuCreditsImage, menuCreditsStretchedImage
    global magic_brick1, magic_brick2,  magic_brick1_1x2,  magic_brick2_1x2, glow, glow1x2
    global ground_block1, ground_block2, sprite_sheet, standing_image, key_image, staffImage, text, world, scrollingCreditsImage, scrollingCreditsRect, darkWizardStandImage
    global darkWizardRect, darkWizardLife

    WIDTH=800 #Change this to make the window bigger or smaller
    HEIGHT = WIDTH*3/4 #Keep width/height ratio 4:3
    TILE_SIZE=WIDTH/16
    GRAVITY=20
    screen=pygame.display.set_mode((WIDTH,HEIGHT))#,FULLSCREEN)
    backgroundImage =pygame.image.load("Wall picture.png").convert_alpha()
    backgroundStretchedImage = pygame.transform.scale(backgroundImage, (WIDTH, HEIGHT))
    backgroundRect = backgroundStretchedImage.get_rect()
    
    menuImage = pygame.image.load("Title Screen Picture.png").convert_alpha()
    menuCreditsImage=pygame.image.load("Credits from menu picture.png").convert_alpha()
    menuCreditsStretchedImage=pygame.transform.scale(menuCreditsImage, (WIDTH, HEIGHT))
    
    magic_brick1=pygame.image.load("magic_brick.png")
    magic_brick1 = pygame.transform.scale(magic_brick1, (TILE_SIZE, TILE_SIZE))
    magic_brick2=pygame.image.load("magic_brick2.png")
    magic_brick2 = pygame.transform.scale(magic_brick2, (TILE_SIZE, TILE_SIZE))
    magic_brick1_1x2=pygame.image.load("rect1x2p1.png")
    magic_brick1_1x2 = pygame.transform.scale(magic_brick1_1x2, (TILE_SIZE, TILE_SIZE*2))
    magic_brick2_1x2=pygame.image.load("rect1x2p2.png")
    magic_brick2_1x2 = pygame.transform.scale(magic_brick2_1x2, (TILE_SIZE, TILE_SIZE*2))
    glow=pygame.image.load("glow.png").convert_alpha()
    glow = pygame.transform.scale(glow, (TILE_SIZE+25, TILE_SIZE+25))
    glow1x2=pygame.image.load("glow1x2.png")
    glow1x2 = pygame.transform.scale(glow1x2, (TILE_SIZE+25, (TILE_SIZE*2+25)))
    
    ground_block1=pygame.image.load("castleground1.png")
    ground_block1 = pygame.transform.scale(ground_block1, (TILE_SIZE, TILE_SIZE))
    ground_block2=pygame.image.load("castleground2.png")
    ground_block2 = pygame.transform.scale(ground_block2, (TILE_SIZE, TILE_SIZE))
    
    sprite_sheet=pygame.image.load("full animation 3.png").convert_alpha()
    sprite_sheet = pygame.transform.scale(sprite_sheet, (TILE_SIZE*26, TILE_SIZE*2))
    standing_image=pygame.image.load("full animation 3 stat.png").convert_alpha()
    standing_image = pygame.transform.scale(standing_image, (TILE_SIZE-1, TILE_SIZE*2-1))
    
    key_image=pygame.image.load("Bronze key picture.png").convert_alpha()
    key_image = pygame.transform.scale(key_image, (TILE_SIZE, TILE_SIZE))
    staffImage=pygame.image.load("Staff picture.png").convert_alpha()
    staffImage = pygame.transform.scale(staffImage, (TILE_SIZE, TILE_SIZE))
    
    text = pygame.font.Font("CHILLER.ttf", WIDTH/22)
    
    scrollingCreditsImage=pygame.image.load("Scrolling Credits Text.png")
    scrollingCreditsImage = pygame.transform.scale(scrollingCreditsImage, (376, 792))
    scrollingCreditsRect=scrollingCreditsImage.get_rect()
    
    darkWizardStandImage=pygame.image.load("Dark Wizard a4 resize picture.png")
    darkWizardStandImage = pygame.transform.scale(darkWizardStandImage, (50, 107))
    darkWizardRect=darkWizardStandImage.get_rect()
    darkWizardRect.topleft = (693, 95)
    darkWizardLife="Living"
    world = World()

def killEverything():
    global TILE_SIZE ,WIDTH ,HEIGHT, GRAVITY, screen, backgroundImage, backgroundStretchedImage, backgroundRect, menuImage, menuCreditsImage, menuCreditsStretchedImage
    global magic_brick1, magic_brick2,  magic_brick1_1x2,  magic_brick2_1x2, glow, glow1x2
    global ground_block1, bround_block2, sprite_sheet, standing_image, key_image, staffImage, text
    
    TILE_SIZE = None
    WIDTH = None
    HEIGHT = None
    GRAVITY = None
    screen = None
    backgroundImage = None
    backgroundStretchedImage = None
    backgroundRect = None
    menuImage = None
    menuCreditsImage = None
    menuCreditsStretchedImage =  None
    magic_brick1 = None
    magic_brick2 = None
    magic_brick1_1x2 = None
    magic_brick2_1x2 = None
    glow = glow1x2 = None
    ground_block1 = None
    bround_block2 = None
    sprite_sheet = None
    standing_image = None
    key_image = None
    staffImage = None
    text = None
    
    return

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
            self.vel_y=15
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
        else:
            screen.blit(ground_block1 if self.picture1 else ground_block2,self.rect)
            
class Wizard(object): #Player
    def __init__(self, x, y,world):
        #The porperties of the player character
        self.rect = pygame.Rect(x,y,50,99) #Wizard Rectangle
        self.vel_x = 100 # Velocity variables that change based on the events on the screen
        self.vel_y = 0
        self.right = True #boolean: true if the player is facing right, false if he is facing left
        self.moving = False #boolean: true if the player is moving
        self.elapsed = 0
        self.updateRate = 45
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
            self.vel_y = -60*GRAVITY**.5
            
        if self.rect.colliderect(world.key_rect):
            self.key = True
        
        #Change the player direction based on the movement direction
        if self.moving:
            self.elapsed += deltatime
            if self.elapsed > self.updateRate:
                self.frame = (self.frame + 1) % 26
                self.elapsed = 0
        else:
            self.frame=0
        self.rect.move_ip(((1 if self.right else -1) if self.moving else 0) * self.vel_x * dt, self.vel_y * dt)
        if self.rect.left<0:
            self.rect.x=0
        if self.rect.right>WIDTH and not self.key:
            self.rect.right=WIDTH
        if self.rect.top<0:
            self.rect.top=0
            self.vel_y=0
        if self.rect.top >= HEIGHT:
            self.rect.topleft = (0, 450)
            world.reset(world.room)
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
            image=sprite_sheet.subsurface(50*self.frame,0,50,99)
            screen.blit(image if self.right else pygame.transform.flip(image,True,False),self.rect)
        else:
            screen.blit(standing_image if self.right else pygame.transform.flip(standing_image,True,False),self.rect)
            
class World(object):
    def __init__(self):
        self.reset(1) #Initializes the player
        
    def reset(self,room):
        #Initializes the tiles based on the room the player is in
        
        self.wizard=Wizard(0,450,self)
        self.grabbedBlock=None
        self.grabNum=None
        self.room=room
        self.groundList = [] #List of static ground blocks
        self.magicList = []  #List of semi-dynamic "magic blocks"
        try:
            self.tilelist = open("ROOM "+str(room)+".txt").readlines()#List that tells the computer where to draw each tile
        except IOError:
            credits()
            
        if room == 25: #Play final boss music in room 25
            AnyMeansNecessary = pygame.mixer.music.load("Hammerfall - Any Means Necessary (8-Bit).wav")
            pygame.mixer.music.play(-1, 0.0)
        
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
        return False
                    
    def update(self,dt):
        self.wizard.update(dt)
        
    def draw(self,screen):
        self.wizard.draw(screen)
        

def mainMenu ():
    #Displays the main menu at the beginning of the game
    InisMona = pygame.mixer.music.load("Eluveitie- Inis Mona 8-Bit.wav") #Play menu music
    pygame.mixer.music.play(-1, 0.0)
    while True:
        menuStretchedImage = pygame.transform.scale(menuImage, (WIDTH, HEIGHT))
        menuRect = menuStretchedImage.get_rect()
        screen.blit(menuStretchedImage, menuRect)
        pygame.display.flip()
        
        for event in pygame.event.get():
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                elif event.key == pygame.K_1:
                    storyBoard1()
                    game()
                elif event.key == pygame.K_2:
                    creditsMenu()
     
def storyBoard1():
    BlackWinterDay = pygame.mixer.music.load("8-bit  Black Winter Day - Amorphis.wav") #Play storyboard music
    pygame.mixer.music.play(-1, 0.0)
    storyPicture = 1 #Which picture to display
    previousProgress = False #Was the enter key pressed down last time
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key==pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                if event.key == K_RETURN: #Move to the next frame if the enter key is pressed
                    if previousProgress == False:
                        previousProgress = True
                        storyPicture += 1
            if event.type == pygame.KEYUP:
                if event.key == K_RETURN:
                    previousProgress = False #Only allow the player to progress one frame at a time
                    
        if storyPicture == 5: #If the player pressed enter on the last picture, go to the main game
            return
        
        storyImage = pygame.image.load("Dialog picture "+str(storyPicture)+".png")
        storyStretchedImage = pygame.transform.scale(storyImage, (WIDTH, HEIGHT))
        storyRect = storyStretchedImage.get_rect()
        screen.blit(storyStretchedImage, storyRect)
        
        pressEnterText = text.render("Press Enter", 1, (225, 225, 225))
        pressEnterRect = pressEnterText.get_rect()
        pressEnterRect.topleft = (WIDTH/2-(pressEnterRect.width/2),HEIGHT-pressEnterRect.height)
        screen.blit(pressEnterText, pressEnterRect)
        
        pygame.display.flip()
        
def creditsMenu():
    menuCreditsRect = menuCreditsStretchedImage.get_rect()
    while True:
        screen.blit(menuCreditsStretchedImage, menuCreditsRect)
        pressEnterText = text.render("Press Enter", 1, (225, 225, 225))
        pressEnterRect = pressEnterText.get_rect()
        pressEnterRect.topleft = (WIDTH/2-(pressEnterRect.width/2),HEIGHT-pressEnterRect.height)
        screen.blit(pressEnterText, pressEnterRect)
        
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key==pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                if event.key==pygame.K_RETURN:
                    return
        pygame.display.flip()
        
def credits():
    
    creditsImage = pygame.image.load("Credits picture.png").convert_alpha()
    creditsStretchedImage = pygame.transform.scale(creditsImage, (WIDTH, HEIGHT))
    creditsRect = creditsStretchedImage.get_rect()
    scrollingCreditsRect.topleft = (WIDTH/2, HEIGHT)
    upCounter = 0
    InisMona = pygame.mixer.music.load("Eluveitie- Inis Mona 8-Bit.wav") #Play Credits music
    pygame.mixer.music.play(-1, 0.0)
    while True:
        screen.blit(creditsStretchedImage, creditsRect)
        screen.blit(scrollingCreditsImage, scrollingCreditsRect)
        upCounter += 1 #Scroll up one out of every four frames
        upCounter = upCounter % 12
        if upCounter == 1:
            scrollingCreditsRect.top -= 1
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key==pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
        if scrollingCreditsRect.bottom <= 0:
                killEverything()
                start()
                mainMenu()
                    
def wallText ():    
    #Write messages on the wall to tell the player how to play the game
    tutorialText = text.render("Collect a key and move to the right side of the screen to complete a level", 1, (255, 0, 0)) #Display the room number on the wall
    tutorialRect = tutorialText.get_rect()
    textx = 0
    texty = tutorialRect.height
    
    if world.room == 1:
        tutorialText = text.render("Collect a key and move to the right side of the screen to complete a level", 1, (255, 0, 0)) #Display the room number on the wall
        tutorialRect = tutorialText.get_rect()
        tutorialRect.topleft = (textx,texty)
        screen.blit(tutorialText, tutorialRect)
        
    if world.room == 2:
        tutorialText = text.render("Blocks can be used as stairs...remember that", 1, (255, 0, 0)) #Display the room number on the wall
        tutorialRect = tutorialText.get_rect()
        tutorialRect.topleft = (textx,texty)
        screen.blit(tutorialText, tutorialRect)
        
    if world.room == 3:
        tutorialText = text.render("Click and drag magic blocks to levitate them", 1, (255, 0, 0)) #Display the room number on the wall
        tutorialRect = tutorialText.get_rect()
        tutorialRect.topleft = (textx,texty)
        screen.blit(tutorialText, tutorialRect)
        
    if world.room == 4:
        tutorialText = text.render("Let's see if you can figure this one out for yorself", 1, (255, 0, 0)) #Display the room number on the wall
        tutorialRect = tutorialText.get_rect()
        tutorialRect.topleft = (textx,texty)
        screen.blit(tutorialText, tutorialRect)
        
    if world.room == 5:
        tutorialText = text.render("Magic blocks stay up when dropped in chasms...but not for long", 1, (255, 0, 0)) #Display the room number on the wall
        tutorialRect = tutorialText.get_rect()
        tutorialRect.topleft = (textx,texty)
        screen.blit(tutorialText, tutorialRect)
        
    if world.room == 6:
        tutorialText = text.render("WARNING: Falling blocks have been known to kill people", 1, (255, 0, 0)) #Display the room number on the wall
        tutorialRect = tutorialText.get_rect()
        tutorialRect.topleft = (textx,texty)
        screen.blit(tutorialText, tutorialRect)
        
    if world.room == 7:
        tutorialText = text.render("Pressing s while dragging a block rotates it 90 degrees", 1, (255, 0, 0)) #Display the room number on the wall
        tutorialRect = tutorialText.get_rect()
        tutorialRect.topleft = (textx,texty)
        screen.blit(tutorialText, tutorialRect)
        
    if world.room == 8:
        tutorialText = text.render("WARNING: Falling off the bottom of the screen results in death", 1, (255, 0, 0)) #Display the room number on the wall
        tutorialRect = tutorialText.get_rect()
        tutorialRect.topleft = (textx,texty)
        screen.blit(tutorialText, tutorialRect)

def game():
    global darkWizardLife
    clock=pygame.time.Clock()
    mousex=mousey=0
    leftClick=rightClick=False

    dt = 60
    time=0
    
    Isara = pygame.mixer.music.load("Eluveitie - Isara 8-Bit.wav") #Play main game music
    pygame.mixer.music.play(-1, 0.0)


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
                elif event.key==pygame.K_p:
                    world.wizard.rect.x=0
                    if world.reset(world.room+1):
                        return
                elif event.key==pygame.K_s: #Make this right click!
                    if world.grabbedBlock:
                        world.grabbedBlock.rect.width,world.grabbedBlock.rect.height=world.grabbedBlock.rect.height,world.grabbedBlock.rect.width
                        if world.grabbedBlock.whratio()<0:
                            world.grabbedBlock.rect.y-=(math.fabs(world.grabbedBlock.whratio())-world.grabNum)*TILE_SIZE
                            world.grabbedBlock.rect.x+=world.grabNum*TILE_SIZE
                            world.grabNum=world.grabbedBlock.rect.height/TILE_SIZE-1-world.grabNum
                        elif world.grabbedBlock.whratio()>0:
                            world.grabbedBlock.rect.x+=(math.fabs(world.grabbedBlock.whratio())-world.grabNum-1)*TILE_SIZE
                            world.grabbedBlock.rect.y+=world.grabNum*TILE_SIZE
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
                            world.grabbedBlock=block
                            world.magicList.remove(block)
                            world.grabbedBlock.vel_y=0
                            if world.grabbedBlock.whratio()==0:
                                world.grabNum=0
                            elif world.grabbedBlock.whratio()>0:
                                world.grabNum=(mousex-world.grabbedBlock.rect.x)/TILE_SIZE
                            else:
                                world.grabNum=(mousey-world.grabbedBlock.rect.y)/TILE_SIZE
                            break
            if event.type==pygame.MOUSEBUTTONUP:
                mousex,mousey=event.pos
                if event.button==1:
                    leftClick=False
            if event.type==pygame.MOUSEMOTION:
                if world.grabbedBlock:
                    world.grabbedBlock.rect.x=int(event.pos[0]/TILE_SIZE-(world.grabNum if world.grabbedBlock.whratio()>0 else 0))*TILE_SIZE
                    world.grabbedBlock.rect.y+=event.pos[1]-mousey
                mousex,mousey=event.pos
                
        screen.blit(backgroundStretchedImage, backgroundRect)
        
        wallText()
        
        
        #Update the world
        world.update(dt)
        if world.wizard.rect.right>WIDTH and world.wizard.key:
            if world.reset(world.room+1):
                return
            
        #Draw the player and the world
        world.draw(screen)
        for block in world.magicList:
            block.update(world,dt)
            block.draw(screen,time)
        for block in world.groundList:
            block.draw(screen,time)
        if world.grabbedBlock:
            if not leftClick:
                for block in world.magicList+world.groundList:
                    if world.grabbedBlock.rect.colliderect(block.rect):
                        break
                else:
                    if not world.grabbedBlock.rect.colliderect(world.wizard.rect):
                        world.magicList.append(world.grabbedBlock)
                        world.grabbedBlock=None
                        world.grabNum=None
            if world.grabbedBlock:
                world.grabbedBlock.draw(screen,time)
                if world.grabbedBlock.whratio()==0:
                    screen.blit(glow,glow.get_rect().move(world.grabbedBlock.rect.x-12,world.grabbedBlock.rect.y-12))
                elif world.grabbedBlock.whratio()==-1:
                    screen.blit(glow1x2,glow1x2.get_rect().move(world.grabbedBlock.rect.x-12,world.grabbedBlock.rect.y-12))
                elif world.grabbedBlock.whratio()==1:
                    screen.blit(pygame.transform.rotate(glow1x2,90),glow1x2.get_rect().move(world.grabbedBlock.rect.x-12,world.grabbedBlock.rect.y-12))
                elif world.grabbedBlock.whratio()==-2:
                    screen.blit(pygame.transform.rotate(glow1x4,90),glow1x4.get_rect().move(world.grabbedBlock.rect.x-12,world.grabbedBlock.rect.y-12))
                #screen.blit(glow,pygame.Rect(world.grabbedBlock.rect.x*TILE_SIZE-25,world.grabbedBlock.rect.y-25,150,150))
        roomDisplayText = text.render("Room:"+str(world.room), 1, (255, 0, 0)) #Display the room number on the wall
        roomDisplayRect = roomDisplayText.get_rect()
        roomDisplayRect.topleft = (0,0)
        screen.blit(roomDisplayText, roomDisplayRect)
        
        if world.wizard.key == False:
            if world.room == 25:
                if darkWizardLife == "Living":
                    screen.blit(darkWizardStandImage, darkWizardRect)
                elif darkWizardLife == "Dead":
                    screen.blit(staffImage, world.key_rect)
                for block in world.magicList:
                    if block.rect.colliderect(darkWizardRect) and block.rect.bottom <= darkWizardRect.top+10: #and block.rect.centery<darkWizardRect.centery:
                        darkWizardLife = "Dead"
                #print darkWizardLife
            elif world.room != 25:
                screen.blit(key_image, world.key_rect)
        
        pygame.display.flip()
        
start()
mainMenu()
