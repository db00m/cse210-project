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
        
    def jump(self):
        if not self._is_jumping:
            self._is_jumping = True
            self._is_walking = False
            self.change_y = constants.PLAYER_JUMP_SPEED
    
    def walk(self):
        self._is_jumping = False
        self._is_walking = True
        self.change_y = 0
        
    def update(self):
        self._update_position()
        self._check_jumping()
        self._check_walking()
        self._check_falling()
        
    def _check_falling(self):
        if self.change_y < -1:
            self.texture = constants.PLAYER_FALLING

    def _check_jumping(self):
        if self.change_y > 0:
            self.texture = constants.PLAYER_JUMPING

    def _check_walking(self):
        if self._is_walking:
            self._current_frame += 1
            if self._current_frame >= constants.PLAYER_ANIMATION_RATE:
                num_textures = len(constants.PLAYER_WALKING)
                self._current_frame = 0
                self._texture_index = (self._texture_index + 1) % num_textures
                self.texture = constants.PLAYER_WALKING[self._texture_index]

    def _update_position(self):
        self.change_y -= constants.GRAVITY   
        self.center_y += self.change_y