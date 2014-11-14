"""
The class that is called after the player beats the last level.  It simply tells them to rest in peace, and then brings them back to the main menu when they hit enter.
"""

import pygame

class Ending(object):
    def __init__ (self, Game):
        """
        Initialize the ending object
        """
        self.Game = Game

        self.background_image = pygame.image.load("Images/Intro Background.png")
        self.background_rect = self.background_image.get_rect()

        self.font = pygame.font.Font(None, self.Game.window_width/30)
        self.ending_text = self.font.render("Rest In Peace", True, (225, 225, 225))
        self.ending_text_rect = self.ending_text.get_rect()
        self.ending_text_rect.centerx = self.Game.screen.get_rect().centerx
        self.ending_text_rect.centery = self.Game.screen.get_rect().centery

        self.enter_text = self.font.render("Enter", True, (225, 225, 225))
        self.enter_rect = self.enter_text.get_rect()
        self.enter_rect.right = self.Game.window_width
        self.enter_rect.bottom = self.Game.window_height

    def update(self):
        """
        Take the player to the main menu if they've pressed enter
        """

        if self.Game.enter_pressed == True:
            self.Game.game_state = "Main Menu"

    def draw(self):
        """
        Draw the ending text on the screen
        """

        self.Game.screen.blit(self.background_image, self.background_rect)
        self.Game.screen.blit(self.enter_text, self.enter_rect)
        self.Game.screen.blit(self.ending_text, self.ending_text_rect)
