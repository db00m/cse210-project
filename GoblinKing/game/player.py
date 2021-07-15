from core.actor import Actor
from game import constants
import arcade


class Player(Actor):

    def __init__(self, water_spray):
        super().__init__()
        self.center_x = 50
        self.center_y = 50
        self._water_spray = water_spray
        self.texture = constants.PLAYER_IDLE
        self.scale = 0.25
        self.change_x = 0
        self.change_y = 0
        self._gems = arcade.SpriteList()
        self._waters = arcade.SpriteList()
        self._was_hit = False
        self._water = 0
        self.lives = 3


    
    def walk(self,direction):
        if direction == constants.LEFT:
            self.change_x = -constants.MOVE_SPEED
        elif direction == constants.RIGHT:
            self.change_x = constants.MOVE_SPEED
        elif direction == constants.UP:
            self.change_y = constants.MOVE_SPEED
        elif direction == constants.DOWN:
            self.change_y = -constants.MOVE_SPEED
        
    def hit(self):
        self.change_y *= -1
        self.change_x *= -1
        self._was_hit = True
        self.lives -= 1
        
    def update(self):
        self._update_position()
        self._update_item_list()
            
        
    def get_spray(self):
        return self._water_spray
        
    def _update_position(self):
        self.center_x += self.change_x
        self.center_y += self.change_y
        if self._was_hit:
            self.change_x = 0
            self.change_y = 0
            self._was_hit = False
        self._water_spray.move(self)

    def _update_item_list(self):
        for i in range(len(self._waters)):
            water = self._waters[i]
            water.center_x = 30 * i + 10
            water.center_y = 13
            water.scale = constants.WATER_SCALE/2
            
    def pick_up_item(self, item):
        if item.get_type() == "water":
            self._waters.append(item)
            self._water += 1
        else:
            self._gems.append(item)
            
    def get_gems(self):
        return len(self._gems)
    
    def has_water(self):
        return self._water > 0
        
    def use_water(self):
        self._water -= 1
        return self._waters.pop()
        
    def get_water(self):
        return self._water

    def check_complete(self):
        return self.center_y > constants.SCREEN_HEIGHT or self.center_x > constants.SCREEN_WIDTH
    
    def check_death(self):
        return self.lives < 0
    
    def check_win(self):
        return self.get_gems() >= 20
