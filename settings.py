class Settings:
    def __init__(self):
        self.screen_width = 1200
        self.screen_height = 700
        self.bg_color = (0, 0, 0)
        self.ship_limit = 3
        self.ship_speed_factor = 20
        self.bullet_speed_factor = 16
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.bullets_allowed = 1
        self.fleet_drop_speed = 10
        self.fleet_direction = 1
        self.speedup_scale = 1.1
        self.game_speed = 60
        self.alien_speed_factor = 1
        self.speed_buffer = 2
        self.audio_level = 0
        self.alien_tracker = 0
        self.alien_mtracker = 0
        self.fleet_direction = 1
        
    def increase_speed(self):
        self.alien_speed_factor *= self.speedup_scale

    def reset(self):
        # initialize settings that change throughout the game
        self.alien_speed_factor = 1
        self.speed_buffer = 2
        self.audio_level = 0
        self.alien_tracker = 0
        self.alien_mtracker = 0