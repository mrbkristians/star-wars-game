import pygame



class RocketModel:
    '''Class to manage rocket'''
    def __init__(self, ai_game):
        '''Initialize the rocket and set its starting position'''
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()
        # load img and its rect
        self.image = pygame.image.load("/Volumes/fuckTheSystem/game_try/my_proj/img/starwars2.bmp").convert_alpha()
        self.rect = self.image.get_rect()
        # define rocket size
        
        self.rotated_image = self.image
        # new ship starting position
        self.rect.midbottom = self.screen_rect.midbottom
        
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

    def update(self):
        '''Update the rocket position'''
        self.direction = 0
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.rocket_speed
            self.rotated_image = pygame.transform.rotate(self.image, -90)
            self.direction = 1
        elif self.moving_left and self.rect.left > 0:
            self.x -= self.settings.rocket_speed
            self.rotated_image = pygame.transform.rotate(self.image, 90)
            self.direction = 2
        elif self.moving_up and self.rect.top > 0:
            self.y -= self.settings.rocket_speed
            self.rotated_image = self.image
            self.direction = 3
        elif self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.y += self.settings.rocket_speed
            self.rotated_image = pygame.transform.rotate(self.image, 180)
            self.direction = 4

        # update rect object from self.x
        self.rect.x = self.x
        self.rect.y = self.y

    def blitme(self):
        '''Draw rocket at it's current location'''
        self.screen.blit(self.rotated_image, self.rect)

