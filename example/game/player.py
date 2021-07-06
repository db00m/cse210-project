from core.actor import Actor
from game import constants


class Player(Actor):

    def __init__(self):
        super().__init__()
        self.center_x = constants.CENTER_X
        self.center_y = constants.CENTER_Y
        self.texture = constants.PLAYER_IDLE
        self._is_jumping = False
        self._is_walking = False
        self._current_frame = 0
        self._texture_index = 0
        self._num_jumps = 0
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
        
        
    def update(self):
        self._update_position()
        self._check_jumping()
        self._check_walking()
        self._check_falling()
        

    def _update_position(self):
        self.center_x += self.change_x
        self.center_y += self.change_y