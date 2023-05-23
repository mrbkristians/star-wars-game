import sys
import pygame

from settings import Settings
from rocket import RocketModel
from bullets import Bullet

class FlyingRocket:
    '''Overall class to manage game assets and behavior'''
    def __init__(self):
        '''Initialize the game and create game resources'''
        pygame.init()

        self.settings = Settings()
        self.screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
        self.settings.screen_width = self .screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        self.rocket = RocketModel(self)
        self.bullets = pygame.sprite.Group()
              
        pygame.display.set_caption("Flying Rocket")
    
    def run_game(self):
        '''Start the main loop for the game'''
        while True:
            #Watch for the keyboard and mouse events.
            self._check_events()
            self.rocket.update()
            self._update_bullets()
            self._update_screen()

            pygame.display.flip()
            
    def _check_events(self):
        '''Respond to keypresses and mouse events'''
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    self._check_keydown_events(event)                       
                elif event.type == pygame.KEYUP:
                    self._check_keyup_events(event) 

    def _check_keydown_events(self, event):
        '''Respond to keypresses'''
        if event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()
        elif event.key == pygame.K_RIGHT:
            self.rocket.moving_right = True  
        elif event.key == pygame.K_LEFT:
            self.rocket.moving_left = True
        elif event.key == pygame.K_UP:
            self.rocket.moving_up = True
        elif event.key == pygame.K_DOWN:
            self.rocket.moving_down = True

    def _check_keyup_events(self, event):
        '''Response to keyup event'''
        if event.key == pygame.K_RIGHT:
            self.rocket.moving_right = False
        if event.key == pygame.K_LEFT:
            self.rocket.moving_left = False
        if event.key == pygame.K_UP:
            self.rocket.moving_up = False
        if event.key == pygame.K_DOWN:
            self.rocket.moving_down = False
    
    def _fire_bullet(self):
        '''Create a new bullet and add it to the bullets groupe'''
        if len(self.bullets) < self.settings.bullets_allowed:     
            dir_x = 0
            dir_y = 0
            
            if self.rocket.moving_up:
                dir_y = -1
            elif self.rocket.moving_down:
                dir_y = 1   
            elif self.rocket.moving_left:
                dir_x = -1    
            elif self.rocket.moving_right:
                dir_x = 1   
                
            new_bullet = Bullet(self, dir_x, dir_y, self.rocket.direction)
            self.bullets.add(new_bullet)

    def _update_bullets(self):
        '''Update bullet position'''
        # update bullet positio
        self.bullets.update()
        # Get rid of bullets that have disappeared
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0 or bullet.rect.top >= self.screen.get_height() or \
                bullet.rect.right <= 0 or bullet.rect.left >= self.screen.get_width():
                self.bullets.remove(bullet)
        
    def _update_screen(self):
        '''Update images on the screen and flip to the new screen'''
        self.screen.fill(self.settings.bg_color)
        self.rocket.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()

if __name__ == "__main__":
    ai = FlyingRocket()
    ai.run_game()