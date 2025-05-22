class GameStats():
    """Track statistics for Alien Invasion"""
    
    def __init__(self, ai_settings):
        """Initialize stats"""
        self.ai_settings = ai_settings
        self.reset_stats()
        self.game_active = False
#        try:
        with open(ai_settings.high_score_filename) as score_store:
            self.high_score = int(score_store.readline())

    def reset_stats(self):
        """Initialize game stats at run time"""
        self.ships_left = self.ai_settings.ship_limit
        self.score = 0
        self.level = 1