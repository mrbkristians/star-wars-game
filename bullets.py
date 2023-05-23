import pygame
import pygame.sprite



class Bullet(pygame.sprite.Sprite):
    '''A class to manage bullet fire'''
    def __init__(self, ai_game, dir_x, dir_y, direction):
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.bullet_color

        # Create a bullet (0,0) and then set correct position
        if direction == 3 or direction == 4:
            self.rect = pygame.Rect(0, 0, self.settings.bullet_width, self.settings.bullet_height)
        elif direction == 1 or direction == 2:
            self.rect = pygame.Rect(0, 0, self.settings.bullet_height, self.settings.bullet_width)

        # Set the bullet's position based on the rocket's position and rotation
        self._set_bullet_position(ai_game.rocket.rect.center, ai_game.rocket.rect.width, ai_game.rocket.rect.height, direction)

         # store the bullet position as a decimal value
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

        # Adjust bullet direction based on rocket rotation
        self.dir_x = dir_x
        self.dir_y = dir_y

        self.update()
        
    def _set_bullet_position(self, rocket_center, rocket_width, rocket_height, direction):
        '''Set the bullet's position based on the rocket's position and rotation'''
        if direction == 3:
            self.rect.centerx = rocket_center[0]
            self.rect.bottom = rocket_center[1] - rocket_height // 2
        elif direction == 4:
            self.rect.centerx = rocket_center[0]
            self.rect.top = rocket_center[1] + rocket_height // 2
        elif direction == 2:
            self.rect.left = rocket_center[0] - rocket_height // 2
            self.rect.centery = rocket_center[1]
        elif direction == 1:
            self.rect.right = rocket_center[0] + rocket_height // 2
            self.rect.centery = rocket_center[1]

    def update(self):
        '''Move the bullet up the screen'''
        # update the rect position
        self.x += self.settings.bullet_speed * self.dir_x
        self.y += self.settings.bullet_speed * self.dir_y
        
        # Update the rect position
        self.rect.x = int(self.x)
        self.rect.y = int(self.y)
        

    def draw_bullet(self):
        '''Draw the bullet to the screen'''
        pygame.draw.rect(self.screen, self.color, self.rect)