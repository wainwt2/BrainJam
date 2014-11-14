"""
The class that handles items in the world once the player has started playing a level.
Author: Thomas Wainwright
Usage: Reflection game
"""

import pygame, random #Import built in python modules
import Modules #Import the player class so it can be called

class World(object):
    def __init__ (self, Game, level):
        """
        Initialize the World class
        """

        self.first_time = True

        #Inialize the world information
        self.Game = Game
        self.level = level
        self.level_file_list = []
        self.floor_dict = dict()

        #Load the dimension tiles
        self.forest_tile = pygame.image.load("Images/Forest Tile.png")
        self.mountain_tile = pygame.image.load("Images/Mountain Tile.png")
        self.underground_tile = pygame.image.load("Images/Underground Tile.png")
        self.desert_tile = pygame.image.load("Images/Desert Tile.png")
        self.tundra_tile = pygame.image.load("Images/Tundra Tile.png")

        #Initialize dimension rectangles
        self.left_dimension_tile_rect = pygame.Rect(self.Game.window_width-100, self.Game.window_height-50, 50, 50)
        self.right_dimension_tile_rect = pygame.Rect(self.Game.window_width-50, self.Game.window_height-50, 50, 50)
        self.up_dimension_tile_rect = pygame.Rect(self.Game.window_width-200, self.Game.window_height-50, 50, 50)
        self.down_dimension_tile_rect = pygame.Rect(self.Game.window_width-150, self.Game.window_height-50, 50, 50)

        #Initialize background images
        self.forest_background = pygame.image.load("Images/Forest Background.png")
        self.mountain_background = pygame.image.load("Images/Mountain Background.png")
        self.underground_background = pygame.image.load("Images/Underground Background.png")
        self.desert_background = pygame.image.load("Images/Desert Background.png")
        self.tundra_background = pygame.image.load("Images/Tundra Background.png")

        #Initialize dimension logos
        self.dimension_logo_box = pygame.image.load("Images/Memory Strip.png")
        self.dimension_logo_box_rect = self.dimension_logo_box.get_rect()
        self.dimension_logo_box_rect.left = 0
        self.dimension_logo_box_rect.bottom = self.Game.window_height
        self.forest_logo = pygame.image.load("Images/Forest Tile.png")
        self.mountain_logo = pygame.image.load("Images/Mountain Tile.png")
        self.underground_logo = pygame.image.load("Images/Underground Tile.png")
        self.desert_logo = pygame.image.load("Images/Desert Tile.png")
        self.tundra_logo = pygame.image.load("Images/Tundra Tile.png")

        #Initialize tutorial arrow images
        self.w_arrow = pygame.image.load("Images/Up Arrow.png")
        self.a_arrow = pygame.image.load("Images/Left Arrow.png")
        self.s_arrow = pygame.image.load("Images/Down Arrow.png")
        self.d_arrow = pygame.image.load("Images/Right Arrow.png")

        #Initialze the memory images
        self.memory1_image = pygame.image.load("Images/Baby Rattle.png")
        self.memory2_image = pygame.image.load("Images/Kickball.png")
        self.memory3_image = pygame.image.load("Images/Electric Guitar.png")
        self.memory4_image = pygame.image.load("Images/Graduate Cap.png")
        self.memory5_image = pygame.image.load("Images/Briefcase.png")
        self.memory6_image = pygame.image.load("Images/Love Letter.png")
        self.memory7_image = pygame.image.load("Images/Daddy Card.png")
        self.memory8_image = pygame.image.load("Images/Coach Shirt.png")
        self.memory9_image = pygame.image.load("Images/College Box.png")
        self.memory10_image = pygame.image.load("Images/Hawiian Shirt.png")
        self.memory11_image = pygame.image.load("Images/Walker.png")
        self.memory12_image = pygame.image.load("Images/Hospital Bed.png")

        #Initialize door images
        self.memory_image = pygame.image.load("Images/Baby Rattle.png")
        self.portal_image = pygame.image.load("Images/Door Down.png")
        self.shiny_portal_image = pygame.image.load("Images/Glowing Door.png")

        #Initialize the memory and door locations
        self.memoryRect = pygame.Rect(0, 0, 0, 0)
        self.doorRect = pygame.Rect(0, 0, 0, 0)

        self.level_file = open("Levels/level"+str(self.level)+".txt", "r")

        #Initialize the "Back to menu" and "Instructions" graphics
        self.option_font = pygame.font.Font(None, self.Game.window_width/20)
        self.instructions_font = pygame.font.Font(None, self.Game.window_width/30)
        self.menu_text = self.option_font.render("Back to Menu", True, (225, 225, 225))
        self.menu_rect = self.menu_text.get_rect()
        self.menu_rect.left = 0
        self.menu_rect.top = 0
        self.instructions_text = self.option_font.render("Instructions", True, (225, 225, 225))
        self.instructions_rect = self.instructions_text.get_rect()
        self.instructions_rect.left = self.Game.window_width/2-self.instructions_rect.width/2
        self.instructions_rect.top = 0
        self.instructions_background= pygame.image.load("Images/Intro Background.png")
        self.instructions_background_rect = self.instructions_background.get_rect()
        self.display_instructions = False

        #Initialize the Dimension logo letter text
        self.logo_font = pygame.font.Font(None, self.Game.window_width/17)
        
        self.w_text = self.logo_font.render("^", True, (255, 255, 255))
        self.arrow_stem_text = self.logo_font.render("|", True, (255, 255, 255))
        self.w_rect = self.w_text.get_rect()
        self.arrow_stem_rect = self.arrow_stem_text.get_rect()
        self.w_rect.right = self.Game.window_width-150
        self.w_rect.bottom = self.Game.window_height
        self.arrow_stem_rect.right = self.Game.window_width-155
        self.arrow_stem_rect.bottom = self.Game.window_height+15
        
        self.a_text = self.logo_font.render("<-", True, (255, 255, 255))
        self.a_rect = self.a_text.get_rect()
        self.a_rect.right = self.Game.window_width-50
        self.a_rect.bottom = self.Game.window_height
        
        self.s_text = self.logo_font.render("v", True, (255, 255, 255))
        self.s_rect = self.s_text.get_rect()
        self.arrow_stem_2_rect = self.arrow_stem_text.get_rect()
        self.s_rect.right = self.Game.window_width-100
        self.s_rect.bottom = self.Game.window_height+5
        self.arrow_stem_2_rect.right = self.Game.window_width-105
        self.arrow_stem_2_rect.bottom = self.Game.window_height-15
        
        self.d_text = self.logo_font.render("->", True, (255, 255, 255))
        self.d_rect = self.d_text.get_rect()
        self.d_rect.right = self.Game.window_width
        self.d_rect.bottom = self.Game.window_height

        #Set the memory position modifier in order to make the memories float up and down
        self.memory_x_modifier = 0
        self.memory_y_modifier = 0
        self.memory_y_modifier_positive = True;

        #Counter to create a trail for moving memories
        self.memory_trail_counter = 0
        self.memory_trail_dict = dict()

    def update(self):
        """
        Checks to see if the player has changed dimensions or obtained a memory
        """

        self.level_file = open("Levels/level"+str(self.level)+".txt", "r")

        #Update the level text
        self.level_text = self.option_font.render("Level "+str(self.level), True, (225, 225, 225))
        self.level_rect = self.level_text.get_rect()
        self.level_rect.right = self.Game.window_width
        self.level_rect.top = 0

        #Find the player's position if this is the first frame in the level
        x = 0
        y = 0
        if self.first_time == True:
            for line in self.level_file:
                line = line.strip()
                dimensions = line.split()
                tile_list = open("Levels/Level"+str(self.level)+dimensions[4]+".txt", "r")
                for ytile in tile_list:
                    ytile = ytile.strip()
                    for xtile in ytile.split():
                        if xtile == "P":
                            playerx = x
                            playery = y
                        x += 50
                    y += 50

        #Check if changed dimensions
        if self.Game.down_pressed == True:
            if self.level_file_list[0] != 'None':
                self.current_dimension = self.level_file_list[0]
                self.portal_image = pygame.image.load("Images/Door Down.png")
        if self.Game.left_pressed == True:
            if self.level_file_list[1] != 'None':
                self.current_dimension = self.level_file_list[1]
                self.portal_image = pygame.image.load("Images/Door Left.png")
        if self.Game.right_pressed == True:
            if self.level_file_list[2] != 'None':
                self.current_dimension = self.level_file_list[2]
                self.portal_image = pygame.image.load("Images/Door Right.png")
        if self.Game.up_pressed == True:
            if self.level_file_list[3] != 'None':
                self.current_dimension = self.level_file_list[3]
                self.portal_image = pygame.image.load("Images/Door Up.png")

        #Initialze the current memory icon
        if self.level == 1:
            self.memory_image = self.memory1_image
        elif self.level == 2:
            self.memory_image = self.memory2_image
        elif self.level == 3:
            self.memory_image = self.memory3_image
        elif self.level == 4:
            self.memory_image = self.memory4_image
        elif self.level == 5:
            self.memory_image = self.memory5_image
        elif self.level == 6:
            self.memory_image = self.memory6_image
        elif self.level == 7:
            self.memory_image = self.memory7_image
        elif self.level == 8:
            self.memory_image = self.memory8_image
        elif self.level == 9:
            self.memory_image = self.memory9_image
        elif self.level == 10:
            self.memory_image = self.memory10_image
        elif self.level == 11:
            self.memory_image = self.memory11_image
        elif self.level == 12:
            self.memory_image = self.memory12_image

        #Move the memory position up and down
        if self.memory_y_modifier <= -10:
            self.memory_y_modifier_positive = True
        elif self.memory_y_modifier >= 10:
            self.memory_y_modifier_positive = False

        if self.memory_y_modifier_positive == True:
            self.memory_y_modifier += 1
        else:
            self.memory_y_modifier -= 1

        #Check if the player has clicked on the back to menu  or instructions options
        if self.menu_rect.collidepoint(self.Game.mousex, self.Game.mousey):
            self.menu_text = self.option_font.render("Back to Menu", True, (255, 242, 0))
            if self.Game.mouse_clicked == True:
                self.Game.game_state = "Main Menu"
        else:
            self.menu_text = self.option_font.render("Back to Menu", True, (255, 255, 255))
        if self.instructions_rect.collidepoint(self.Game.mousex, self.Game.mousey):
            self.instructions_text = self.option_font.render("Instructions", True, (255, 242, 0))
            if self.Game.mouse_clicked == True:
                self.display_instructions = True
        else:
            self.instructions_text = self.option_font.render("Instructions", True, (255, 255, 255))

        #Take down the instructions if they are being displayed and the player hits enter
        #or backspace
        if self.display_instructions == True and (self.Game.enter_pressed == True or self.Game.backspace_pressed == True):
            self.display_instructions = False
        


    def draw(self, screen):
        """
        Reads files containing information about the current level, and uses them to draw the level on the screen
        Notes:
            - In the first file, 0 is the down dimension, 1 is left dimension, 2 is right dimension, 3 is up dimension, and 5 is starting dimension
        """

        level_file = open("Levels/level"+str(self.level)+".txt", "r") #Because it was for some reason giving an error otherwise
        
        for line in level_file:
            self.level_file_list = line.strip()
            self.level_file_list = line.split()

            if self.first_time == True:
                self.current_dimension = self.level_file_list[4]             

        #Make the last item the current dimension so it goes on top, draw the background
        if self.current_dimension == "Forest":
            self.level_file_list[4] = "Forest"
            screen.blit(self.forest_background, pygame.Rect(0, 0, self.Game.window_width, self.Game.window_height))
        elif self.current_dimension == "Mountain":
            self.level_file_list[4] = "Mountain"
            screen.blit(self.mountain_background, pygame.Rect(0, 0, self.Game.window_width, self.Game.window_height))
        elif self.current_dimension == "Underground":
            self.level_file_list[4] = "Underground"
            screen.blit(self.underground_background, pygame.Rect(0, 0, self.Game.window_width, self.Game.window_height))
        elif self.current_dimension == "Desert":
            self.level_file_list[4] = "Desert"
            screen.blit(self.desert_background, pygame.Rect(0, 0, self.Game.window_width, self.Game.window_height))
        elif self.current_dimension == "Tundra":
            self.level_file_list[4] = "Tundra"
            screen.blit(self.tundra_background, pygame.Rect(0, 0, self.Game.window_width, self.Game.window_height))

        #Draw the tiles on the screen
        for dimension in self.level_file_list:
            if dimension != "None": #Use none as a keyword in the file to skip over a dimension
                self.floor_dict[dimension] = []
                dimension_tiles = open("Levels/Level"+str(self.level)+dimension+".txt", "r")

                x = 0
                y = 0

                for line in dimension_tiles:
                    line = line.strip()
                    line = line.split()

                    for tile in line:
                        if tile == "F":
                            screen.blit(self.forest_tile, pygame.Rect(x, y, 50, 50))
                            self.floor_dict[dimension].append((x, y))
                        if tile == "M":
                            screen.blit(self.mountain_tile, pygame.Rect(x, y, 50, 50))
                            self.floor_dict[dimension].append((x, y))
                        if tile == "U":
                            screen.blit(self.underground_tile, pygame.Rect(x, y, 50, 50))
                            self.floor_dict[dimension].append((x, y))
                        if tile == "D":
                            screen.blit(self.desert_tile, pygame.Rect(x, y, 50, 50))
                            self.floor_dict[dimension].append((x, y))
                        if tile == "T":
                            screen.blit(self.tundra_tile, pygame.Rect(x, y, 50, 50))
                            self.floor_dict[dimension].append((x, y))
                        if tile == "R":
                            self.memoryRect = pygame.Rect(x+self.memory_x_modifier, y+self.memory_y_modifier, 50, 50)
                        if tile == "O":
                            self.doorRect = pygame.Rect(x, y, 50, 50)
                        if dimension == self.current_dimension:
                            if tile == "W":
                                    screen.blit(self.w_arrow, pygame.Rect(x, y, 50, 50))
                            if tile == "A":
                                screen.blit(self.a_arrow, pygame.Rect(x, y, 50, 50))
                            if tile == "S":
                                screen.blit(self.s_arrow, pygame.Rect(x, y, 50, 50))
                            if tile == "C":
                                screen.blit(self.d_arrow, pygame.Rect(x, y, 50, 50))

                        x += 50

                    x = 0
                    y += 50

                y = 0

        #Draw the dimension logos on the screen
        screen.blit(self.dimension_logo_box, self.dimension_logo_box_rect)
        for dimension_index in range(len(self.level_file_list)):
            if self.level_file_list[dimension_index] != "None":
                if dimension_index == 0:
                    if self.level_file_list[dimension_index] == "Forest":
                        screen.blit(self.forest_logo, self.down_dimension_tile_rect) #Logo images are 50X50 pixels
                    if self.level_file_list[dimension_index] == "Mountain":
                        screen.blit(self.mountain_logo, self.down_dimension_tile_rect)
                    if self.level_file_list[dimension_index] == "Underground":
                        screen.blit(self.underground_logo, self.down_dimension_tile_rect)
                    if self.level_file_list[dimension_index] == "Desert":
                        screen.blit(self.desert_logo, self.down_dimension_tile_rect)
                    if self.level_file_list[dimension_index] == "Tundra":
                        screen.blit(self.tundra_logo, self.down_dimension_tile_rect)
                    screen.blit(self.s_text, self.s_rect)
                    screen.blit(self.arrow_stem_text, self.arrow_stem_2_rect)
                if dimension_index == 1:
                    if self.level_file_list[dimension_index] == "Forest":
                        screen.blit(self.forest_logo, self.left_dimension_tile_rect)
                    if self.level_file_list[dimension_index] == "Mountain":
                        screen.blit(self.mountain_logo, self.left_dimension_tile_rect)
                    if self.level_file_list[dimension_index] == "Underground":
                        screen.blit(self.underground_logo, self.left_dimension_tile_rect)
                    if self.level_file_list[dimension_index] == "Desert":
                        screen.blit(self.desert_logo, self.left_dimension_tile_rect)
                    if self.level_file_list[dimension_index] == "Tundra":
                        screen.blit(self.tundra_logo, self.left_dimension_tile_rect)
                    screen.blit(self.a_text, self.a_rect)
                if dimension_index == 2:
                    if self.level_file_list[dimension_index] == "Forest":
                        screen.blit(self.forest_logo, self.right_dimension_tile_rect)
                    if self.level_file_list[dimension_index] == "Mountain":
                        screen.blit(self.mountain_logo, self.right_dimension_tile_rect)
                    if self.level_file_list[dimension_index] == "Underground":
                        screen.blit(self.underground_logo, self.right_dimension_tile_rect)
                    if self.level_file_list[dimension_index] == "Desert":
                        screen.blit(self.desert_logo, self.right_dimension_tile_rect)
                    if self.level_file_list[dimension_index] == "Tundra":
                        screen.blit(self.tundra_logo, self.right_dimension_tile_rect)
                    screen.blit(self.d_text, self.d_rect)
                if dimension_index == 3:
                    if self.level_file_list[dimension_index] == "Forest":
                        screen.blit(self.forest_logo, self.up_dimension_tile_rect)
                    if self.level_file_list[dimension_index] == "Mountain":
                        screen.blit(self.mountain_logo, self.up_dimension_tile_rect)
                    if self.level_file_list[dimension_index] == "Underground":
                        screen.blit(self.underground_logo, self.up_dimension_tile_rect)
                    if self.level_file_list[dimension_index] == "Desert":
                        screen.blit(self.desert_logo, self.up_dimension_tile_rect)
                    if self.level_file_list[dimension_index] == "Tundra":
                        screen.blit(self.tundra_logo, self.up_dimension_tile_rect)
                    screen.blit(self.w_text, self.w_rect)
                    screen.blit(self.arrow_stem_text, self.arrow_stem_rect)

        #Tell the player module to draw the player
        if self.first_time == True:
            current_dimension_tiles = open("Levels/Level"+str(self.level)+self.current_dimension+".txt", "r")
            x = 0
            y = 0
            for line in current_dimension_tiles:
                line = line.strip()
                line = line.split()
                for tile in line:
                    if tile == "P":
                        self.Player_Character = Modules.Player.Player(x, y, self.level_file_list, self, self.floor_dict, self.Game, self.Game.screen)
                        break
                    x += 50
                x = 0
                y += 50
                
        self.first_time = False
        self.Player_Character.update()
        self.Player_Character.draw()

        #Draw the memory in the room if it hasn't been collected yet.  Draw it on the bottom belt if it has.
        #Draw the door on the screen if the memory has been collected
        if self.Player_Character.memory_hit == False:
            screen.blit(self.memory_image, self.memoryRect)
        elif self.Player_Character.memory_hit == True:
            if self.Player_Character.memory_collected == False:
                #Give the moving memory a trail
                self.memory_trail_counter += 1
                self.memory_trail_dict[self.memory_trail_counter] = Modules.Player.Player_Trail(self.memoryRect.left, 0, self.memoryRect.top, 0, pygame.image.load("Images/Memory Trail.png"), self.Game.screen)
                self.memory_trail_counter += 1
                
                for trail in self.memory_trail_dict:
                    self.memory_trail_dict[trail].update()

                for trail in self.memory_trail_dict:
                    self.memory_trail_dict[trail].draw()
                self.memory_image = pygame.image.load("Images/Memory Head.png")
                
                #Make the memory icon move to the memory belt in a curved path.
                if self.memoryRect.left <= (self.level-1)*50:
                    self.memory_x_modifier += ((self.level-1)*50-self.memoryRect.left)/10+5
                else:
                    self.memory_x_modifier -= (self.memoryRect.left-(self.level-1)*50)/10+5
                if self.memoryRect.top < self.Game.window_height-50:
                    self.memory_y_modifier += (self.Game.window_height-50-self.memoryRect.top)/10+5
                else:
                    self.memory_y_modifier -= (self.memoryRect.top-self.Game.window_height-50)/10+5
                screen.blit(self.memory_image, self.memoryRect)

                #Check if the memory icon is in range of its location
                if self.memoryRect.left >= (self.level-1)*50-10 and self.memoryRect.left <= (self.level-1)*50+10:
                    if (self.memoryRect.top >= self.Game.window_height-60) and (self.memoryRect.top <= self.Game.window_height-40):
                        self.Player_Character.memory_collected = True
                        self.memory_trail_dict = dict()
                    
            elif self.Player_Character.memory_collected == True:
                self.memory_x_modifier = 0
                self.memory_y_modifier = 0
                screen.blit(self.memory_image, pygame.Rect(50*(self.level-1), self.Game.window_height-50, 50, 50))
                if self.level < 12:
                    screen.blit(self.portal_image, self.doorRect)
                else:
                    screen.blit(self.shiny_portal_image, self.doorRect)

        #Draw the previously collected memories on the memory belt
        if self.level > 1:
            screen.blit(self.memory1_image, pygame.Rect(0, self.Game.window_height-50, 50, 50))
        if self.level > 2:
            screen.blit(self.memory2_image, pygame.Rect(50, self.Game.window_height-50, 50, 50))
        if self.level > 3:
            screen.blit(self.memory3_image, pygame.Rect(100, self.Game.window_height-50, 50, 50))
        if self.level > 4:
            screen.blit(self.memory4_image, pygame.Rect(150, self.Game.window_height-50, 50, 50))
        if self.level > 5:
            screen.blit(self.memory5_image, pygame.Rect(200, self.Game.window_height-50, 50, 50))
        if self.level > 6:
            screen.blit(self.memory6_image, pygame.Rect(250, self.Game.window_height-50, 50, 50))
        if self.level > 7:
            screen.blit(self.memory7_image, pygame.Rect(300, self.Game.window_height-50, 50, 50))
        if self.level > 8:
            screen.blit(self.memory8_image, pygame.Rect(350, self.Game.window_height-50, 50, 50))
        if self.level > 9:
            screen.blit(self.memory9_image, pygame.Rect(400, self.Game.window_height-50, 50, 50))
        if self.level > 10:
            screen.blit(self.memory10_image, pygame.Rect(450, self.Game.window_height-50, 50, 50))
        if self.level > 11:
            screen.blit(self.memory11_image, pygame.Rect(500, self.Game.window_height-50, 50, 50))

        #Draw the back to menu option in the top left corner, the instructions option in the middle
        #and the current level in the top right corner
        screen.blit(self.menu_text, self.menu_rect)
        screen.blit(self.instructions_text, self.instructions_rect)
        screen.blit(self.level_text, self.level_rect)

        #Display the instructions if the player clicks on the "Instructions" option
        if self.display_instructions == True:
            screen.blit(self.instructions_background, self.instructions_background_rect)
            instructions_y = 50
            for line in open("Modules/Instructions.txt", "r"):
                line = line.strip()
                line = self.instructions_font.render(line, True, (225, 225, 225))
                line_rect = line.get_rect()
                line_rect.top = instructions_y
                line_rect.left = 10
                instructions_y += line_rect.height
                screen.blit(line, line_rect)
            back_text = self.instructions_font.render("Press Enter or Backspace to return to the game", True, (225, 225, 225))
            back_text_rect = back_text.get_rect()
            screen.blit(back_text, back_text_rect)
