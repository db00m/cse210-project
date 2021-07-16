from core.actor import Actor
from game import constants

class Score(Actor):
    def __init__(self, **args):
        super().__init__(**args)
        self.center_x = constants.SCREEN_WIDTH - 100
        self.center_y = constants.SCREEN_HEIGHT - 30
        self.score = 0
    
    def update(self, bonus):
        self.add_score(bonus)

    def add_score(self, bonus):
        self.score += bonus
        
    def current_score(self):
        return self.score
    
    def calculate_time_score(self, time):
        base_score = constants.COMPLETION_SCORE
        subtract_score = constants.SCORE_DECREASE * (time // 60)
        if subtract_score <= base_score:
            self.score += (base_score - subtract_score)
        elif subtract_score > base_score:
            self.score += 0
