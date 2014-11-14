"""
The main class for the game Reflection.  It is the first one that the main class calls, and handles the initial menu screen.
Author: Thomas Wainwright
Game: Reflection
"""

import pygame

class Main_Menu(object):
        def __init__(self, Game, screen, World):
                """
                Loads the images for the title menu.
                """
                
                #Initialize menu background 
                self.background_image = pygame.image.load("Images/Menu Background.png").convert_alpha()
                self.background_rect = pygame.Rect(0, 0, Game.window_width, Game.window_height)

                #Initialize the font
                self.selection_font = pygame.font.Font(None, Game.window_width/10)
                self.Reflection_font = pygame.font.Font(None, Game.window_width/8)

                self.Reflection_text = self.Reflection_font.render("Reflection", True, (225, 225, 225))
                self.Reflection_text_rect = self.Reflection_text.get_rect()
                self.Reflection_text_rect.centerx = screen.get_rect().right*.75
                self.Reflection_text_rect.top = screen.get_rect().bottom*.1
                
                self.play_text = self.selection_font.render("Play", True, (225, 225, 225))
                self.play_text_rect = self.play_text.get_rect()
                self.play_text_rect.centerx = screen.get_rect().right*.75 #Puts the text in the right third of the screen
                self.play_text_rect.centery = screen.get_rect().centery*.75 #Puts the text in the middle of the screen vertically
            
                self.instructions_text = self.selection_font.render("Instructions", True, (225, 225, 225))
                self.instructions_text_rect = self.instructions_text.get_rect()
                self.instructions_text_rect.centerx = screen.get_rect().right*.75
                self.instructions_text_rect.centery = screen.get_rect().centery*.75+(self.instructions_text_rect.height*1.25) #Puts the text in the middle of the screen vertically and moves it down to make room for the other options
                
                self.level_select_text = self.selection_font.render("Level Select", True, (225,225, 225))
                self.level_select_text_rect = self.level_select_text.get_rect()
                self.level_select_text_rect.centerx = screen.get_rect().right*.75
                self.level_select_text_rect.centery = screen.get_rect().centery*.75+(self.level_select_text_rect.height*2.5)
                        
                #Initialize the selection sprite
                self.selection_image = pygame.image.load("Images/Menu Select Sprite.png").convert_alpha()

                #Allow the game class to be referenced later in the Main_Menu class
                self.Game = Game
                self.World = World
                
        def update(self, screen):
                """
                Updates the menu, taking into account where the mouse is and whether or not the player has clicked
                """       

                #Avoid continuing to draw the sprite if the mouse moves outside the text
                self.selection_sprite_left = 0 #Add to the object so it can be checked in the draw function
                selection_sprite_top = 0
                selection_text_rect = None

                #Create values to store whether or not the player has clicked on an option
                play_select = False
                instructions_select = False
                level_select_select = False

                #Check if the player is hovering over an option
                if self.play_text_rect.collidepoint(self.Game.mousex, self.Game.mousey):
                        self.selection_sprite_left = self.play_text_rect.centerx-169 #The menu select icon is 338 pixels wide
                        selection_sprite_top = self.play_text_rect.top
                        selection_text_rect = self.play_text_rect
                        play_select = True
                elif self.instructions_text_rect.collidepoint(self.Game.mousex, self.Game.mousey):
                        self.selection_sprite_left = self.instructions_text_rect.left
                        selection_sprite_top = self.instructions_text_rect.top
                        selection_text_rect = self.instructions_text_rect
                        instructions_select = True
                elif self.level_select_text_rect.collidepoint(self.Game.mousex, self.Game.mousey):
                        self.selection_sprite_left = self.level_select_text_rect.left
                        selection_sprite_top = self.level_select_text_rect.top
                        selection_text_rect = self.level_select_text_rect
                        level_select_select = True
                                        
                if self.selection_sprite_left != 0:
                        self.selection_rect = pygame.Rect(self.selection_sprite_left, selection_sprite_top, selection_text_rect.width, selection_text_rect.height)

                #Update the game state if the player clicks on an option
                if self.Game.mouse_clicked == True:
                        if play_select == True:
                                self.Game.game_state = 'Play'
                                self.World.level = 1
                                self.World.first_time = True
                        if instructions_select == True:
                                self.Game.game_state = 'Instructions'
                        if level_select_select == True:
                                self.Game.game_state = 'Level Select'
                                        
        def draw(self, screen):
                """
                Draw the items on the screen
                """
                
                #Draw the background first, followed by the selection sprite (if the player is hovering over an option) followed by the menu text
                screen.blit(self.background_image, self.background_rect)

                if self.selection_sprite_left != 0:
                        screen.blit(self.selection_image, self.selection_rect)

                screen.blit(self.Reflection_text, self.Reflection_text_rect)
                screen.blit(self.play_text, self.play_text_rect)
                screen.blit(self.instructions_text, self.instructions_text_rect)
                screen.blit(self.level_select_text, self.level_select_text_rect)
