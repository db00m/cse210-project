from core.actor import Actor
from game import constants


class Player(Actor):

    def __init__(self):
        super().__init__()
        self.center_x = 100
        self.center_y = 80
        self.texture = constants.PLAYER_IDLE
        self._change_x = 0
        self.change_y = 0

    
    def walk(self,direction):
        if direction == constants.LEFT:
            self.change_x = -constants.MOVE_SPEED
        elif direction == constants.RIGHT:
            self.change_x = constants.MOVE_SPEED
        elif direction == constants.UP:
            self.change_y = constants.MOVE_SPEED
        elif direction == constants.DOWN:
            self.change_y = -constants.MOVE_SPEED
        
    def stop(self):
        self.change_y = 0
        self.change_x = 0
        
    def update(self):
        self._update_position()

        

    def _update_position(self):
        self.center_x += self.change_x
        self.center_y += self.change_y