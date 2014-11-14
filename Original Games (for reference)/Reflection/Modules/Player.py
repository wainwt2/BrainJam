"""
The player class for the game Reflection.  This processes the events of the player, updates the player character based on the events, and
"""

import pygame #Import built in python modules

class Player(object):
    def __init__(self, x, y, dimensions_list, World, floor_dict, Game, screen):
        """
        Initialize the player class
        """

        self.image = pygame.image.load("Images/Player.png")
        
        self.Rect = self.image.get_rect()

        self.x = x
        self.old_x = x
        self.y = y
        self.old_y = y
        
        self.jump = False
        self.fall = False #Set to True if the player is on the ground.  Set to false if the player is not on the ground
        self.vspeed = 0
        self.hspeed = 0
        self.gravity = 1
        self.move_speed = 10

        self.dimensions_list = dimensions_list
        self.World = World
        self.floor_dict = floor_dict
        self.Game = Game
        self.screen = screen

        self.memory_hit = False
        self.memory_collected = False

        self.trail_counter = 0
        self.Player_Trail_dict = dict()

    def update(self):
        """
        Update the player class based on the keystroke of the player
        """

        self.old_x = self.x
        self.old_y = self.y

        future_rect = self.image.get_rect() #Create another player rectangle to check if there is a collision before moving the player

        if self.World.current_dimension == self.dimensions_list[0]: #Down dimension
            #Check sideways movement
            if self.Game.a_pressed == True:
                #Create a new rect where the player wants to go.  If that rect doesn't collide with anything move the player.  If it does, don't move the player.
                player_collision = False
                future_rect.left = self.x-self.move_speed
                future_rect.top = self.y
                for rect in self.floor_dict[self.World.current_dimension]:
                    rect = pygame.Rect(rect[0], rect[1], 50, 50)
                    if future_rect.colliderect(rect):
                        player_collision = True
                if player_collision == False:
                    self.x = future_rect.left
            if self.Game.d_pressed == True:
                player_collision = False
                future_rect.left = self.x+self.move_speed
                future_rect.top = self.y
                for rect in self.floor_dict[self.World.current_dimension]:
                    rect = pygame.Rect(rect[0], rect[1], 50, 50)
                    if future_rect.colliderect(rect):
                        player_collision = True
                if player_collision == False:
                    self.x = future_rect.left

            #Check jumping
            if self.Game.w_pressed == True:
                check_rect = pygame.Rect(self.x, self.y+1, 50, 50)
                for rect in self.floor_dict[self.World.current_dimension]:
                    rect = pygame.Rect(rect[0], rect[1], 50, 50)
                    if check_rect.colliderect(rect):
                        self.vspeed = -15
                        break

            #Set gravity                  
            check_rect = pygame.Rect(self.x, self.y+1, 50, 50)
            player_in_air = True
            for rect in self.floor_dict[self.World.current_dimension]:
                rect = pygame.Rect(rect[0], rect[1], 50, 50)
                if check_rect.colliderect(rect):
                    player_in_air = False
                    self.y = rect.top-50
            if player_in_air:
                self.vspeed += self.gravity
                self.y += self.vspeed
                self.x += self.hspeed
            else:
                if self.Game.w_pressed == False:
                    self.vspeed = 0
                    self.hspeed = 0
                else:
                    self.y += self.vspeed
                    self.x += self.hspeed
                    
        elif self.World.current_dimension == self.dimensions_list[1]: #Left dimension
            #Check sideways movement
            if self.Game.w_pressed == True:
                #Create a new rect where the player wants to go.  If that rect doesn't collide with anything move the player.  If it does, don't move the player.
                player_collision = False
                future_rect.top = self.y-self.move_speed
                future_rect.left = self.x
                for rect in self.floor_dict[self.World.current_dimension]:
                    rect = pygame.Rect(rect[0], rect[1], 50, 50)
                    if future_rect.colliderect(rect):
                        print future_rect, rect
                        player_collision = True
                if player_collision == False:
                    self.y = future_rect.top
            if self.Game.s_pressed == True:
                player_collision = False
                future_rect.top = self.y+self.move_speed
                future_rect.left = self.x
                for rect in self.floor_dict[self.World.current_dimension]:
                    rect = pygame.Rect(rect[0], rect[1], 50, 50)
                    if future_rect.colliderect(rect):
                        player_collision = True
                if player_collision == False:
                    self.y = future_rect.top

            #Check jumping
            if self.Game.d_pressed == True:
                check_rect = pygame.Rect(self.x-1, self.y, 50, 50)
                for rect in self.floor_dict[self.World.current_dimension]:
                    rect = pygame.Rect(rect[0], rect[1], 50, 50)
                    if check_rect.colliderect(rect):
                        self.hspeed = 15
                        break

            #Set gravity                  
            check_rect = pygame.Rect(self.x-1, self.y, 50, 50)
            player_in_air = True
            for rect in self.floor_dict[self.World.current_dimension]:
                rect = pygame.Rect(rect[0], rect[1], 50, 50)
                if check_rect.colliderect(rect):
                    player_in_air = False
                    self.x = rect.right
            if player_in_air:
                self.hspeed -= self.gravity
                self.x += self.hspeed
                self.y += self.vspeed
            else:
                if self.Game.d_pressed == False:
                    self.hspeed = 0
                    self.vspeed = 0
                else:
                    self.x += self.hspeed
                    self.y += self.vspeed

        elif self.World.current_dimension == self.dimensions_list[2]: #Right dimension
            #Check sideways movement
            if self.Game.w_pressed == True:
                #Create a new rect where the player wants to go.  If that rect doesn't collide with anything move the player.  If it does, don't move the player.
                player_collision = False
                future_rect.top = self.y-self.move_speed
                future_rect.left = self.x
                for rect in self.floor_dict[self.World.current_dimension]:
                    rect = pygame.Rect(rect[0], rect[1], 50, 50)
                    if future_rect.colliderect(rect):
                        print future_rect, rect
                        player_collision = True
                if player_collision == False:
                    self.y = future_rect.top
            if self.Game.s_pressed == True:
                player_collision = False
                future_rect.top = self.y+self.move_speed
                future_rect.left = self.x
                for rect in self.floor_dict[self.World.current_dimension]:
                    rect = pygame.Rect(rect[0], rect[1], 50, 50)
                    if future_rect.colliderect(rect):
                        player_collision = True
                if player_collision == False:
                    self.y = future_rect.top

            #Check jumping
            if self.Game.a_pressed == True:
                check_rect = pygame.Rect(self.x+1, self.y, 50, 50)
                for rect in self.floor_dict[self.World.current_dimension]:
                    rect = pygame.Rect(rect[0], rect[1], 50, 50)
                    if check_rect.colliderect(rect):
                        self.hspeed = -15
                        break

            #Set gravity                  
            check_rect = pygame.Rect(self.x+1, self.y, 50, 50)
            player_in_air = True
            for rect in self.floor_dict[self.World.current_dimension]:
                rect = pygame.Rect(rect[0], rect[1], 50, 50)
                if check_rect.colliderect(rect):
                    player_in_air = False
                    self.x = rect.left-50
            if player_in_air:
                self.hspeed += self.gravity
                self.x += self.hspeed
                self.y += self.vspeed
            else:
                if self.Game.a_pressed == False:
                    self.hspeed = 0
                    self.vspeed = 0
                else:
                    self.x += self.hspeed
                    self.y += self.vspeed
                    
        elif self.World.current_dimension == self.dimensions_list[3]:
            #Check sideways movement
            if self.Game.a_pressed == True:
                #Create a new rect where the player wants to go.  If that rect doesn't collide with anything move the player.  If it does, don't move the player.
                player_collision = False
                future_rect.left = self.x-self.move_speed
                future_rect.top = self.y
                for rect in self.floor_dict[self.World.current_dimension]:
                    rect = pygame.Rect(rect[0], rect[1], 50, 50)
                    if future_rect.colliderect(rect):
                        player_collision = True
                if player_collision == False:
                    self.x = future_rect.left
            if self.Game.d_pressed == True:
                player_collision = False
                future_rect.left = self.x+self.move_speed
                future_rect.top = self.y
                for rect in self.floor_dict[self.World.current_dimension]:
                    rect = pygame.Rect(rect[0], rect[1], 50, 50)
                    if future_rect.colliderect(rect):
                        player_collision = True
                if player_collision == False:
                    self.x = future_rect.left

            #Check jumping
            if self.Game.s_pressed == True:
                check_rect = pygame.Rect(self.x, self.y-1, 50, 50)
                for rect in self.floor_dict[self.World.current_dimension]:
                    rect = pygame.Rect(rect[0], rect[1], 50, 50)
                    if check_rect.colliderect(rect):
                        self.vspeed = 15
                        break

            #Set gravity                  
            check_rect = pygame.Rect(self.x, self.y-1, 50, 50)
            player_in_air = True
            for rect in self.floor_dict[self.World.current_dimension]:
                rect = pygame.Rect(rect[0], rect[1], 50, 50)
                if check_rect.colliderect(rect):
                    player_in_air = False
                    self.y = rect.bottom
            if player_in_air:
                self.vspeed -= self.gravity
                self.y += self.vspeed
                self.x += self.hspeed
            else:
                if self.Game.s_pressed == False:
                    self.vspeed = 0
                    self.hspeed = 0
                else:
                    self.y += self.vspeed
                    self.x += self.hspeed
        
        self.Rect.left = self.x #Move the player to their x, y, position
        self.Rect.top = self.y

        #Restart the room if the player is outside the boundaries of the screen
        if self.x >= self.Game.window_width+100 or self.x+150 <= 0 or self.y >= self.Game.window_height+100 or self.y+100 <= 0:
            self.World.memory_x_modifier = 0
            self.World.memory_y_modifier = 0
            self.World.first_time = True

        #Check if collided with memory or door
        if self.Rect.colliderect(self.World.memoryRect):
            self.memory_hit = True
        if self.Rect.colliderect(self.World.doorRect) and self.memory_collected == True:
            if self.World.level < 12:
                self.World.level += 1
                self.World.first_time = True
            else:
                self.Game.game_state = "Ending"

        #Update the player trail
        self.trail_counter += 1
        self.Player_Trail_dict[self.trail_counter] = Player_Trail(self.x, self.old_x, self.y, self.old_y, pygame.image.load("Images/Player.png"), self.screen)
        for trail in self.Player_Trail_dict:
            self.Player_Trail_dict[trail].update()

    def draw(self):
        """
        Draw the player on the screen
        """
        self.screen.blit(self.image, self.Rect)

        #Draw the player trail
        for trail in self.Player_Trail_dict:
            self.Player_Trail_dict[trail].draw()

class Player_Trail(object):
    def __init__(self, x, old_x, y, old_y, image, screen):
        """
        Initialize one part of the player trail
        """

        self.screen = screen

        self.life = 25

        self.image = image
        self.rect = self.image.get_rect()
        self.rect.left = x
        self.old_x = old_x
        self.rect.top = y
        self.old_y = old_y

    def update(self):
        """
        Take one away from life, and delete it if life is less than 0
        """
        self.life -= 1
        if self.life >= 0:
            self.stretched_image = pygame.transform.scale(self.image, (self.rect.width/25*self.life, self.rect.height/25*self.life))
            self.stretched_rect = self.stretched_image.get_rect()
            self.stretched_rect.x = self.rect.left+((self.rect.width-self.stretched_rect.width)/2)
            self.stretched_rect.y = self.rect.top+((self.rect.height-self.stretched_rect.height)/2)

    def draw(self):
        """
        Draw the player trail on the screen
        """
        if self.life >= 0:
            if self.old_x != self.rect.left or self.old_y != self.rect.top:
                self.screen.blit(self.stretched_image, self.stretched_rect)
        else:
            del self
               
