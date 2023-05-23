class Settings:
    '''class to store all settings for project'''
    def __init__(self):
        '''initialize the game settings'''
        # Screen settings
        
        self.bg_color = (0, 250, 0)

        self.rocket_speed = 2.5

        self.bullet_offset = 3

        #bullet settings
        self.bullet_speed = 4.0
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 10       