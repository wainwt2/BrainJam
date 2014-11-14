"""
The main module for the game Reflection.  This class is mainly used to call other classes saved in the modules folder of the game package.
Players click this module to play the Reflection game, it is the only one without its own folder.
Author: Thomas Wainwright
Game: Reflection
"""

import pygame, pygame.locals, sys
import Modules #Import python files store in modules folder

class Game(object):
    def __init__ (self):
        """
        Initializes the game
        """
        
        pygame.init()
        self.window_width = 800
        self.window_height = int(.75*self.window_width)
        self.screen = pygame.display.set_mode((self.window_width, self.window_height))
        
        self.game_state = "Intro"

        #Tracks the states of the keys and mouse
        self.mouse_clicked = False
        
        #Helps prevent the game from lagging
        self.clock = pygame.time.Clock()

        #Store mouse and key states

        #Stores mouse states
        self.mouse_clicked = False
        self.left_pressed = False
        #Arrow keys
        self.left_pressed = False
        self.right_pressed = False
        self.up_pressed = False
        self.down_pressed = False
        #WASD keys
        self.w_pressed = False
        self.a_pressed = False
        self.s_pressed = False
        self.d_pressed = False
        #enter and backspace keys
        self.enter_pressed = False
        self.backspace_pressed = False

    def update(self):
        """
        Updates the game
        """

        self.mousex, self.mousey = pygame.mouse.get_pos()

        #Check the state of the keys and mouse
        for event in pygame.event.get():
            if event.type == pygame.locals.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                #Escape key
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                #Arrow keys
                if event.key == pygame.K_UP:
                    self.up_pressed = True
                if event.key == pygame.K_DOWN:
                    self.down_pressed = True
                if event.key == pygame.K_LEFT:
                    self.left_pressed = True
                if event.key == pygame.K_RIGHT:
                    self.right_pressed = True
                #WASD Keys
                if event.key == pygame.K_w:
                    self.w_pressed = True
                if event.key == pygame.K_s:
                    self.s_pressed = True
                if event.key == pygame.K_a:
                    self.a_pressed = True
                if event.key == pygame.K_d:
                    self.d_pressed = True
                #Enter and backspace keys
                if event.key == pygame.K_RETURN:
                    self.enter_pressed = True
                if event.key == pygame.K_BACKSPACE:
                    self.backspace_pressed = True
            if event.type == pygame.KEYUP:
                #Arrow keys
                if event.key == pygame.K_UP:
                    self.up_pressed = False
                if event.key == pygame.K_DOWN:
                    self.down_pressed = False
                if event.key == pygame.K_LEFT:
                    self.left_pressed = False
                if event.key == pygame.K_RIGHT:
                    self.right_pressed = False
                #WASD keys
                if event.key == pygame.K_w:
                    self.w_pressed = False
                if event.key == pygame.K_s:
                    self.s_pressed = False
                if event.key == pygame.K_a:
                    self.a_pressed = False
                if event.key == pygame.K_d:
                    self.d_pressed = False
                #Enter and backspace keys
                if event.key == pygame.K_RETURN:
                    self.enter_pressed = False
                if event.key == pygame.K_BACKSPACE:
                    self.backspace_pressed = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                self.mouse_clicked = True
            if event.type == pygame.MOUSEBUTTONUP:
                self.mouse_clicked = False
                
Game = Game()
Intro = Modules.Intro.Intro(Game)
World = Modules.World.World(Game, 1)
Main_Menu = Modules.Main_Menu.Main_Menu(Game, Game.screen, World)
Instructions = Modules.Instructions.Instructions(Game)
Level_Select = Modules.Level_Select.Level_Select(Game, World)
End = Modules.Ending.Ending(Game)
    
while True:
    Game.clock.tick(30)
    Game.update()
    if Game.game_state == "Intro":
        Intro.update()
        Intro.draw()
    if Game.game_state == "Main Menu":
        Main_Menu.update(Game.screen)
        Main_Menu.draw(Game.screen)
    if Game.game_state == "Play":
        World.update()
        World.draw(Game.screen)
    if Game.game_state == "Instructions":
        Instructions.update()
        Instructions.draw()
    if Game.game_state == "Level Select":
        Level_Select.update()
        Level_Select.draw()
    if Game.game_state == "Ending":
        End.update()
        End.draw()

    pygame.display.flip()

sys.exit()
