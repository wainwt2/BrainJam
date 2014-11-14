"""
Bring up the level selection screen.  It allows the player to start at any level in the game.
"""

import pygame

class Level_Select(object):
    def __init__(self, Game, World):
        """
        Initialize the Level_Select object
        """

        self.Game = Game
        self.World = World
        
        self.background_image = pygame.image.load("Images/Intro Background.png")
        self.background_rect = self.background_image.get_rect()

        self.font = pygame.font.Font(None, self.Game.window_width/15)
        self.small_font = pygame.font.Font(None, self.Game.window_width/30)

        self.back_text = self.small_font.render("Press Enter or Backspace to go to the Main Menu", True, (225, 225, 225))
        self.back_rect = self.back_text.get_rect()
        self.back_rect.right = self.Game.window_width

        self.selection = None

        self.one_text = self.font.render("1", True, (225, 225, 225))
        self.one_rect = self.one_text.get_rect()
        self.one_rect.left = self.Game.window_width/5
        self.one_rect.top = self.Game.window_height/4
        
        self.two_text = self.font.render("2", True, (225, 225, 225))
        self.two_rect = self.two_text.get_rect()
        self.two_rect.left = self.Game.window_width/5*2
        self.two_rect.top = self.Game.window_height/4
        
        self.three_text = self.font.render("3", True, (225, 225, 225))
        self.three_rect = self.three_text.get_rect()
        self.three_rect.left = self.Game.window_width/5*3
        self.three_rect.top = self.Game.window_height/4
        
        self.four_text = self.font.render("4", True, (225, 225, 225))
        self.four_rect = self.four_text.get_rect()
        self.four_rect.left = self.Game.window_width/5*4
        self.four_rect.top = self.Game.window_height/4
        
        self.five_text = self.font.render("5", True, (225, 225, 225))
        self.five_rect = self.five_text.get_rect()
        self.five_rect.left = self.Game.window_width/5
        self.five_rect.top = self.Game.window_height/2
        
        self.six_text = self.font.render("6", True, (225, 225, 225))
        self.six_rect = self.six_text.get_rect()
        self.six_rect.left = self.Game.window_width/5*2
        self.six_rect.top = self.Game.window_height/2
        
        self.seven_text = self.font.render("7", True, (225, 225, 225))
        self.seven_rect = self.seven_text.get_rect()
        self.seven_rect.left = self.Game.window_width/5*3
        self.seven_rect.top = self.Game.window_height/2
        
        self.eight_text = self.font.render("8", True, (225, 225, 225))
        self.eight_rect = self.eight_text.get_rect()
        self.eight_rect.left = self.Game.window_width/5*4
        self.eight_rect.top = self.Game.window_height/2
        
        self.nine_text = self.font.render("9", True, (225, 225, 225))
        self.nine_rect = self.nine_text.get_rect()
        self.nine_rect.left = self.Game.window_width/5
        self.nine_rect.top = self.Game.window_height/4*3
        
        self.ten_text = self.font.render("10", True, (225, 225, 225))
        self.ten_rect = self.ten_text.get_rect()
        self.ten_rect.left = self.Game.window_width/5*2
        self.ten_rect.top = self.Game.window_height/4*3
        
        self.eleven_text = self.font.render("11", True, (225, 225, 225))
        self.eleven_rect = self.eleven_text.get_rect()
        self.eleven_rect.left = self.Game.window_width/5*3
        self.eleven_rect.top = self.Game.window_height/4*3
        
        self.twelve_text = self.font.render("12", True, (225, 225, 225))
        self.twelve_rect = self.twelve_text.get_rect()
        self.twelve_rect.left = self.Game.window_width/5*4
        self.twelve_rect.top = self.Game.window_height/4*3

    def update(self):
        """
        Update the level select object:
        - Check if the player has the mouse over a level, highlight it if they do
        - Check if the player has clicked on a level, bring them to that level if they have
        - Check if the player has hit enter or backspace, go back if they have
        """

        self.selection = None

        if self.one_rect.collidepoint(self.Game.mousex, self.Game.mousey):
            self.selection = "One"
            if self.Game.mouse_clicked == True:
                self.Game.game_state = "Play"
                self.World.level = 1
                self.World.first_time = True
        elif self.two_rect.collidepoint(self.Game.mousex, self.Game.mousey):
            self.selection = "Two"
            if self.Game.mouse_clicked == True:
                self.Game.game_state = "Play"
                self.World.level = 2
                self.World.first_time = True
        elif self.three_rect.collidepoint(self.Game.mousex, self.Game.mousey):
            self.selection = "Three"
            if self.Game.mouse_clicked == True:
                self.Game.game_state = "Play"
                self.World.level = 3
                self.World.first_time = True
        elif self.four_rect.collidepoint(self.Game.mousex, self.Game.mousey):
            self.selection = "Four"
            if self.Game.mouse_clicked == True:
                self.Game.game_state = "Play"
                self.World.level = 4
                self.World.first_time = True
        elif self.five_rect.collidepoint(self.Game.mousex, self.Game.mousey):
            self.selection = "Five"
            if self.Game.mouse_clicked == True:
                self.Game.game_state = "Play"
                self.World.level = 5
                self.World.first_time = True
        elif self.six_rect.collidepoint(self.Game.mousex, self.Game.mousey):
            self.selection = "Six"
            if self.Game.mouse_clicked == True:
                self.Game.game_state = "Play"
                self.World.level = 6
                self.World.first_time = True
        elif self.seven_rect.collidepoint(self.Game.mousex, self.Game.mousey):
            self.selection = "Seven"
            if self.Game.mouse_clicked == True:
                self.Game.game_state = "Play"
                self.World.level = 7
                self.World.first_time = True
        elif self.eight_rect.collidepoint(self.Game.mousex, self.Game.mousey):
            self.selection = "Eight"
            if self.Game.mouse_clicked == True:
                self.Game.game_state = "Play"
                self.World.level = 8
                self.World.first_time = True
        elif self.nine_rect.collidepoint(self.Game.mousex, self.Game.mousey):
            self.selection = "Nine"
            if self.Game.mouse_clicked == True:
                self.Game.game_state = "Play"
                self.World.level = 9
                self.World.first_time = True
        elif self.ten_rect.collidepoint(self.Game.mousex, self.Game.mousey):
            self.selection = "Ten"
            if self.Game.mouse_clicked == True:
                self.Game.game_state = "Play"
                self.World.level = 10
                self.World.first_time = True
        elif self.eleven_rect.collidepoint(self.Game.mousex, self.Game.mousey):
            self.selection = "Eleven"
            if self.Game.mouse_clicked == True:
                self.Game.game_state = "Play"
                self.World.level = 11
                self.World.first_time = True
        elif self.twelve_rect.collidepoint(self.Game.mousex, self.Game.mousey):
            self.selection = "Twelve"
            if self.Game.mouse_clicked == True:
                self.Game.game_state = "Play"
                self.World.level = 12
                self.World.first_time = True

        if self.Game.enter_pressed == True or self.Game.backspace_pressed == True:
            self.Game.game_state = "Main Menu"

    def draw(self):
        """
        Draw the level select screen
        """

        self.Game.screen.blit(self.background_image, self.background_rect)

        self.Game.screen.blit(self.back_text, self.back_rect)

        self.one_text = self.font.render("1", True, (225, 225, 225))
        self.two_text = self.font.render("2", True, (225, 225, 225))
        self.three_text = self.font.render("3", True, (225, 225, 225))
        self.four_text = self.font.render("4", True, (225, 225, 225))
        self.five_text = self.font.render("5", True, (225, 225, 225))
        self.six_text = self.font.render("6", True, (225, 225, 225))
        self.seven_text = self.font.render("7", True, (225, 225, 225))
        self.eight_text = self.font.render("8", True, (225, 225, 225))
        self.nine_text = self.font.render("9", True, (225, 225, 225))
        self.ten_text = self.font.render("10", True, (225, 225, 225))
        self.eleven_text = self.font.render("11", True, (225, 225, 225))
        self.twelve_text = self.font.render("12", True, (225, 225, 225))
        
        if self.selection == "One":
            self.one_text = self.font.render("1", True, (255, 242, 0))
        elif self.selection == "Two":
            self.two_text = self.font.render("2", True, (225, 242, 0))
        elif self.selection == "Three":
            self.three_text = self.font.render("3", True, (225, 242, 0))
        elif self.selection == "Four":
            self.four_text = self.font.render("4", True, (225, 242, 0))
        elif self.selection == "Five":
            self.five_text = self.font.render("5", True, (225, 242, 0))
        elif self.selection == "Six":
            self.six_text = self.font.render("6", True, (225, 242, 0))
        elif self.selection == "Seven":
            self.seven_text = self.font.render("7", True, (225, 242, 0))
        elif self.selection == "Eight":
            self.eight_text = self.font.render("8", True, (225, 242, 0))
        elif self.selection == "Nine":
            self.nine_text = self.font.render("9", True, (225, 242, 0))
        elif self.selection == "Ten":
            self.ten_text = self.font.render("10", True, (225, 242, 0))
        elif self.selection == "Eleven":
            self.eleven_text = self.font.render("11", True, (225, 242, 0))
        elif self.selection == "Twelve":
            self.twelve_text = self.font.render("12", True, (225, 242, 0))

        self.Game.screen.blit(self.one_text, self.one_rect)
        self.Game.screen.blit(self.two_text, self.two_rect)
        self.Game.screen.blit(self.three_text, self.three_rect)
        self.Game.screen.blit(self.four_text, self.four_rect)
        self.Game.screen.blit(self.five_text, self.five_rect)
        self.Game.screen.blit(self.six_text, self.six_rect)
        self.Game.screen.blit(self.seven_text, self.seven_rect)
        self.Game.screen.blit(self.eight_text, self.eight_rect)
        self.Game.screen.blit(self.nine_text, self.nine_rect)
        self.Game.screen.blit(self.ten_text, self.ten_rect)
        self.Game.screen.blit(self.eleven_text, self.eleven_rect)
        self.Game.screen.blit(self.twelve_text, self.twelve_rect)
