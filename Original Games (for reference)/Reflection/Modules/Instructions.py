"""
Displays the instructions on the screen for the player to read
"""

import pygame

class Instructions(object):
    def __init__(self, Game):
        """
        Initialize the Instructions object
        """

        self.Game = Game

        self.background = pygame.image.load("Images/Intro Background.png")
        self.background_rect = self.background.get_rect()

        self.font = pygame.font.Font(None, self.Game.window_width/30)

        self.text_file = open("Modules/Instructions.txt", "r")

        self.text_list = []
        self.rect_list = []
        y = 50
        for line in self.text_file:
            line = line.strip()
            line = self.font.render(line, True, (225, 225, 225))
            self.text_list.append(line)
            
            line_rect = line.get_rect()
            line_rect.top = y
            line_rect.left = 10
            self.rect_list.append(line_rect)
            
            y+= line_rect.height

        self.back_text = self.font.render("Press Enter or Backspace to go to the Main Menu", True, (225, 225, 225))
        self.back_rect = self.back_text.get_rect()
        self.back_rect.right = self.Game.window_width

    def update(self):
        """
        Update the Instructions class (go back to the main menu if the player has pressed enter or backspace
        """
        
        if self.Game.enter_pressed == True or self.Game.backspace_pressed == True:
            self.Game.game_state = "Main Menu"

    def draw(self):
        """
        Draw the instructions text and backgroundon the screen
        """

        self.Game.screen.blit(self.background, self.background_rect)

        for index in range(len(self.text_list)):
            self.Game.screen.blit(self.text_list[index], self.rect_list[index])

        self.Game.screen.blit(self.back_text, self.back_rect)
