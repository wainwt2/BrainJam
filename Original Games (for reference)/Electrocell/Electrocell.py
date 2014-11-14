import pygame, sys, random, pygame.locals
#Names: Microvolt, Electrocell
###############################################################################
###############################################################################
class Backdrop(object):
    def __init__(self,filename,x,y):
        self.img = pygame.image.load(filename).convert_alpha()
        self.x = x
        self.y = y
    def draw(self, screen):
        screen.blit(self.img,(self.x,self.y))        

class Scrolling_Backdrop(object):
    def __init__(self):
        self.img = pygame.image.load("Pics/Outlines.png").convert_alpha()
        self.move = 0
        self.actual_move = 0
    def draw(self,screen,move):
        screen.blit(self.img,(0-move,0-move))

class Menu_Button(object):
    def __init__(self,filename,x,y,width,height):
        self.img = pygame.image.load(filename).convert_alpha()
        self.rect = self.img.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.width = width
        self.height = height
        self.highlight = 0
    def update(self):
        if pygame.mouse.get_pos()[0] - self.rect.x >= 0 and pygame.mouse.get_pos()[0] - self.rect.x < self.width and pygame.mouse.get_pos()[1] - self.rect.y >= 0 and pygame.mouse.get_pos()[1] - self.rect.y < self.height:
            if self.highlight == 0 and puzzle_mode == "Title":
                mouse_over.play()
            self.highlight = 1
        else:
            self.highlight = 0
            
    def draw(self,screen):
        screen.blit(self.img,self.rect,pygame.Rect(0,self.height*self.highlight,self.width,self.height))
        
class Box(object):
    def __init__(self,x,y,species):
        self.img = pygame.image.load("Pics/SP1.png").convert_alpha()
        self.rect = self.img.get_rect()
        self.rect.x = x
        self.rect.y = y
        # -: Blank  V: Vertical  H: Horizontal  D: Diagonal  R: Obstacle
        if species == '-':
            self.var = 0
        elif species == 'V':
            self.var = 1
        elif species == 'H':
            self.var = 2
        elif species == 'D':
            self.var = 3
        elif species == 'R':
            self.var = 4
        self.frame = 0
        self.anim = 0
    def update(self):
        self.frame += 1
        if self.frame >= 10:
            self.anim += 1
            self.frame = 0
        if self.anim > 3:
            self.anim = 0
    def draw(self, screen):
        screen.blit(self.img,self.rect,pygame.Rect(100*self.anim,100*self.var,100,100))
    def clicked_on(self,i,j):
        if box_array[(i,j)].var == 1:
            if j != 0 and j != 6 and box_array[(i,j+1)].var == 0 and box_array[(i,j-1)].var == 0:
                box_array[(i,j+1)].var = 1
                box_array[(i,j-1)].var = 1
                box_array[(i,j)].var = 0
        elif box_array[(i,j)].var == 2:
            if i != 0 and i != 8 and box_array[(i+1,j)].var == 0 and box_array[(i-1,j)].var == 0:
                box_array[(i+1,j)].var = 2
                box_array[(i-1,j)].var = 2
                box_array[(i,j)].var = 0
        elif box_array[(i,j)].var == 3:
            if i != 0 and i != 8 and j != 0 and j != 6 and box_array[(i+1,j+1)].var == 0 and box_array[(i-1,j-1)].var == 0 and box_array[(i+1,j-1)].var == 0 and box_array[(i-1,j+1)].var == 0:
                box_array[(i+1,j+1)].var = 3
                box_array[(i-1,j-1)].var = 3
                box_array[(i+1,j-1)].var = 3
                box_array[(i-1,j+1)].var = 3                
                box_array[(i,j)].var = 0
            
class Game(object):
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((900,700))
        self.clock = pygame.time.Clock()
        self.turbo_sec = 0
        self.current_time = 0
        self.stop_time = 0
        self.turbo_min = 0
        self.ready_to_return = 0
        self.is_help = 0
        self.wait = -1
        self.font = pygame.font.Font(None,32)
        self.font2 = pygame.font.Font(None,32)
        self.r_time = [99,59]
        self.puzzle_backdrop = Backdrop("Pics/Backdrop.png",0,0)
        self.title_backdrop1 = Backdrop("Pics/Title1.png",0,0)
        self.title_backdrop2 = Backdrop("Pics/Title2.png",0,0)
        self.timer_box = Backdrop("Pics/Timerbox.png",0,0)
        self.inst1 = Backdrop("Pics/P1Instructions.png",200,200)
        self.inst2 = Backdrop("Pics/P1Instructions2.png",600,300)
        self.inst3 = Backdrop("Pics/P2Instructions.png",500,400)
        self.helpscreen = Backdrop("Pics/Helpscreen.png",100,100)
        self.credits = Backdrop("Pics/Credits.png",100,610)
        self.besttime = Backdrop("Pics/Besttime.png",405,305)
        self.puzcomp = Backdrop("Pics/PuzzleComplete.png",200,100)
        self.turcomp = Backdrop("Pics/TurboComplete.png",200,100)
        self.outlines = Scrolling_Backdrop()
        self.pmode = Menu_Button("Pics/Pmode.png",65,245,412,67)
        self.tmode = Menu_Button("Pics/Tmode.png",55,345,392,67)
        self.help = Menu_Button("Pics/Help.png",35,445,219,67)
        self.xbutton = Menu_Button("Pics/Xbutton.png",775,75,50,50)
    def process_title_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                global puzzle_mode
                global kind
                global level                
                if self.pmode.highlight == 1:
                    mode_select.play()
                    puzzle_mode = "Puzzle"
                    kind = "grid"
                    level = "1"
                    read_file(kind,level)
                    title_theme.stop()
                    puzzle_theme.play(loops = -1)                    
                elif self.tmode.highlight == 1:
                    mode_select.play()
                    puzzle_mode = "Turbo"
                    kind = "grid"
                    level = str(random.randint(1,10))
                    title_theme.stop()
                    turbo_theme.play(loops = -1)
                    read_file(kind,level)
                    g.stop_time = g.current_time
                elif self.help.highlight == 1 and self.is_help == 0:
                    help_select.play()
                    self.is_help = 1
                    self.help.highlight = 0
                elif self.xbutton.highlight == 1 and self.is_help == 1:
                    help_quit.play()
                    self.is_help = 0    
    def process_puzzle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                if event.key == pygame.K_q or event.key == pygame.K_RETURN and g.ready_to_return == 1:
                    global puzzle_mode
                    global turbo_list
                    g.turbo_sec = 0
                    g.turbo_min = 0
                    turbo_list = [1,2,3,4,5,6,7,8,9,10]
                    puzzle_theme.stop()
                    turbo_theme.stop()
                    title_theme.play(loops = -1)
                    puzzle_mode = "Title"
                    g.ready_to_return = 0
                if event.key == pygame.K_r:
                    global kind
                    global level
                    read_file(kind,level)
            if event.type == pygame.MOUSEBUTTONDOWN:
                for item in box_array.values():
                    if pygame.mouse.get_pos()[0] - item.rect.x >= 0 and pygame.mouse.get_pos()[0] - item.rect.x < 100 and pygame.mouse.get_pos()[1] - item.rect.y >= 0 and pygame.mouse.get_pos()[1] - item.rect.y < 100:
                        item.clicked_on(item.rect.x/100,item.rect.y/100)

                        
    def update(self):
        if puzzle_mode == "Title":
            self.outlines.move += 1
            if self.outlines.move >= 10:
                self.outlines.actual_move += 1
            if self.outlines.actual_move >= 100:
                self.outlines.actual_move = 0
            if self.is_help == 0:
                self.pmode.update()
                self.tmode.update()
                self.help.update()
            else:
                self.xbutton.update()
            self.stop_time = self.current_time
        self.current_time = pygame.time.get_ticks()

      
    def draw_title_screen(self):
        self.title_backdrop2.draw(self.screen)
        self.outlines.draw(self.screen,self.outlines.actual_move)
        self.title_backdrop1.draw(self.screen)
        self.pmode.draw(self.screen)
        self.tmode.draw(self.screen)
        self.help.draw(self.screen)
        if self.is_help == 1:
            self.helpscreen.draw(self.screen)
            self.credits.draw(self.screen)
            self.xbutton.draw(self.screen)
    def draw_boxes(self):
        self.puzzle_backdrop.draw(self.screen)
        for item in box_array.values():
            if g.wait == -1:
                item.update()
            item.draw(self.screen)
        if level == "1" and puzzle_mode == "Puzzle":
            g.inst1.draw(self.screen)
            g.inst2.draw(self.screen)
        if level == "2" and puzzle_mode == "Puzzle":
            g.inst3.draw(self.screen)  
        if self.ready_to_return == 1 and puzzle_mode == "Puzzle":
            g.puzcomp.draw(self.screen)
        if self.ready_to_return == 1 and puzzle_mode == "Turbo":
            g.turcomp.draw(self.screen)
    def draw_timer(self,xzero):
        if puzzle_mode == "Turbo":
            g.timer_box.draw(self.screen)
            t_surf = self.font.render(str(self.turbo_min) + ":" + xzero + str(self.turbo_sec), 1, (89,87,67)).convert_alpha()
            t_rect = t_surf.get_rect()
            t_rect.center = (48,68)
            self.screen.blit(t_surf,t_rect)
            
    def draw_time_score(self,xzero):
        self.besttime.draw(self.screen)
            
        t2_surf = self.font2.render(str(self.turbo_min) + ":" + xzero + str(self.turbo_sec), 1, (50,50,50)).convert_alpha()
        t2_rect = t2_surf.get_rect()
        t2_rect.center = (447,341)
        self.screen.blit(t2_surf,t2_rect) 
            
        t3_surf = self.font2.render(str(b_time[0]) + ":" + xzero + str(b_time[1]), 1, (50,50,50)).convert_alpha()
        t3_rect = t3_surf.get_rect()
        t3_rect.center = (447,378)  
        self.screen.blit(t3_surf,t3_rect) 
###############################################################################
###############################################################################
#High Score ---
file = open("best_time.txt")
firstline = file.readline().split()
print firstline
b_time = [int(firstline[0]),int(firstline[1])]
# ---
puzzle_mode = "Title"
kind = "Title"
level = "Title"
#Music ---
pygame.mixer.init()
title_theme = pygame.mixer.Sound("Music/Disco con Tutti.ogg")
puzzle_theme = pygame.mixer.Sound("Music/How it Begins.ogg")
turbo_theme = pygame.mixer.Sound("Music/Enter the Party.ogg")
mouse_over = pygame.mixer.Sound("Music/PWAP2.WAV")
mode_select = pygame.mixer.Sound("Music/BONUS6.WAV")
help_select = pygame.mixer.Sound("Music/BONUS3.WAV")
help_quit = pygame.mixer.Sound("Music/INVSHOT.WAV")
applause = pygame.mixer.Sound("Music/Clapping 2.wav")
hiscore_sound = pygame.mixer.Sound("Music/BONUS4.WAV")
# ---
title_theme.play(loops = -1)
g = Game()
box_array = dict()
turbo_list = [1,2,3,4,5,6,7,8,9,10]

def read_file(kind,level):
    file = open("Levels/" +kind+level+".txt")
    j = 0
    for line in file:
        parse = line.split()
        for i in range(len(parse)):
            box_array[(i,j)] = Box(100*i,100*j,parse[i])
        j += 1
def test_level(kind,levelnum):
    count = 0
    for item in box_array.values():
        if item.var != 0:
            count += 1
    global level
    global puzzle_mode
    
    if count == 62 and puzzle_mode == "Puzzle":
        if g.wait < 0 and g.ready_to_return == 0:
            g.wait = pygame.time.get_ticks()
        if pygame.time.get_ticks() - g.wait >= 500 and g.wait != -1:
            g.wait = -1
        if levelnum != "10" and g.wait == -1:
            read_file("grid",str(int(levelnum)+1))
            level = str(int(levelnum)+1)
        elif levelnum == "10":
            if g.ready_to_return == 0:
                hiscore_sound.play()
                applause.play()
            g.ready_to_return = 1
        
    elif count == 62 and puzzle_mode == "Turbo":
        global turbo_list
        if len(turbo_list) > 1:
            turbo_list.remove(int(levelnum))
            rand = str(random.choice(turbo_list))
            read_file("grid",rand)
            level = str(rand)
        elif g.ready_to_return == 0:
            turbo_list = []
            global b_time
            hiscore_sound.play()
            applause.play()
            g.r_time = [g.turbo_min,g.turbo_sec]
            if g.r_time[0] < b_time[0] or g.r_time[0] == b_time[0] and g.r_time[1] < b_time[1]:
                b_time[0] = g.r_time[0]
                b_time[1] = g.r_time[1]
                file = open("best_time.txt","w")
                file.write(str(b_time[0]) + " " + str(b_time[1]))
            g.ready_to_return = 1

def turbo_timer():
    if g.ready_to_return == 0:
        if g.current_time - g.stop_time >= 1000:
            g.stop_time = g.current_time
            g.turbo_sec += 1
            if g.turbo_sec >= 60:
                g.turbo_min += 1
                g.turbo_sec = 0

while True:
    g.clock.tick(50)
    g.update()
    
    if puzzle_mode == "Title":
        g.process_title_events()
        g.draw_title_screen()   
    elif puzzle_mode == "Puzzle" or puzzle_mode == "Turbo":
        g.process_puzzle_events()
        g.draw_boxes()
    if puzzle_mode == "Turbo":
        turbo_timer()
        g.draw_timer("0"*(-len(str(g.turbo_sec))+2))
    if puzzle_mode == "Turbo" and g.ready_to_return == 1:
        g.draw_time_score("0"*(-len(str(g.turbo_sec))+2))
    pygame.display.flip()
    test_level(kind,level)