class Settings():
    """A class to store all settings for Alien Invasion"""
    
    def __init__(self):
        """Initialize the game's settings"""
        # Screen Settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (50, 200, 100)
        
        # Ship Settings
        self.ship_limit = 2
        
        # Bullet settings
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.charged_bullet_color = (255, 0, 0)
        self.bullets_allowed = 3
        self.charge_speed = 5
        self.charge_limit = 800
        
        # Alien settings
        self.alien_drop_speed = 10
        
        # Game scaling
        self.speedup_scale = 1.1
        self.score_scale = 1.5
        
        self.high_score = 0
        self.high_score_filename = 'high_score.txt'
        
        self.initialize_dynamic_settings()
        self.boss_hp = 1000
        self.boss_speed = 1
        self.boss_appear_level = 3 
        
    def initialize_dynamic_settings(self):
        """Initialize settings that change throughout the game"""
        self.ship_speed_factor = 1.5
        self.bullet_speed_factor = 4.5
        self.alien_speed_factor = 1
        # fleet_direction of 1 = right -1 = LEFT
        self.fleet_direction = 1
        self.alien_points = 50
        self.boss_active = False
        
    def increase_speed(self):
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale
        self.alien_points = int(self.alien_points * self.score_scale)

    