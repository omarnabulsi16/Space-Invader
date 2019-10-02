class GameStats:
    def __init__(self, ai_settings):
        self.ai_settings = ai_settings
        self.reset_stats()
        # Start game in an inactive state.
        self.game_active = False
        # make sure high scores arent reset
        self.high_score = 0
        self.ships_left = self.ai_settings.ship_limit
        self.score = 0
        self.level = 1

    def reset_stats(self):
        self.ships_left = self.ai_settings.ship_limit
        self.score = 0
        self.level = 1