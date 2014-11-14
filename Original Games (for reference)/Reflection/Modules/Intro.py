"""
Run the introduction to the game Reflection
"""

import pygame

class Intro(object):
    def __init__(self, Game):
        """
        Initialize the Intro class
        """
        self.frame = 1
        self.Game = Game
        self.past_enter_pressed = False

        self.background_image = pygame.image.load("Images/Intro Background.png")
        self.background_rect = self.background_image.get_rect()

        self.font = pygame.font.Font(None, self.Game.window_width/30)
        self.intro_text = self.font.render("Intro", True, (225, 225, 225))
        self.intro_text_rect = self.intro_text.get_rect()

        self.enter_text = self.font.render("Enter", True, (225, 225, 225))
        self.enter_rect = self.enter_text.get_rect()
        self.enter_rect.right = self.Game.window_width
        self.enter_rect.bottom = self.Game.window_height

    def update(self):
        """
        Update the intro screen
        """
        if self.Game.enter_pressed == True and self.past_enter_pressed == False:
            self.frame += 1

        self.past_enter_pressed = self.Game.enter_pressed

    def draw(self):
        """
        Draw the intro text on the screen
        """

        self.Game.screen.blit(self.background_image, self.background_rect)
        self.Game.screen.blit(self.enter_text, self.enter_rect)
        
        if self.frame == 1:
            self.intro_text = self.font.render("Life has always been, and always will be, one of the great mysteries of time.", True, (225, 225, 225))
        if self.frame == 2:
            self.intro_text = self.font.render("It is intriguing, inspiring...", True, (225, 225, 225))
        if self.frame == 3:
            self.intro_text = self.font.render("...and yet, so powerfully finite.", True, (225, 225, 225))
        if self.frame == 4:
            self.intro_text = self.font.render("In death, your mind is now open to all dimensions; you now can see all realities.", True, (225, 225, 225))
        if self.frame == 5:
            self.font = pygame.font.Font(None, self.Game.window_width/40)
            self.intro_text = self.font.render("However, before you move on to the next step in your journey, look back upon the events of your previous life.", True, (225, 225, 225))
        if self.frame == 6:
            self.intro_text = self.font.render("Look back, so that you may take the lessons you learned and the memories you shared with you to the second life.", True, (225, 225, 225))
        if self.frame == 7:
            self.font = pygame.font.Font(None, self.Game.window_width/30)
            self.intro_text = self.font.render("Eventually, given time, you may become one of us.", True, (225, 225, 225))
        if self.frame == 8:
            self.intro_text = self.font.render("This, however, is your time.", True, (225, 225, 225))
        if self.frame == 9:
            self.intro_text = self.font.render("This is your time of Reflection.", True, (225, 225, 225))
        if self.frame == 10:
            self.Game.game_state = "Main Menu"

        self.intro_text_rect = self.intro_text.get_rect()
        self.intro_text_rect.centerx = self.Game.screen.get_rect().centerx
        self.intro_text_rect.centery = self.Game.screen.get_rect().centery
        self.Game.screen.blit(self.intro_text, self.intro_text_rect)
