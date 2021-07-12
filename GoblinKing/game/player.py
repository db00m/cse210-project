from core.actor import Actor
from game import constants
import arcade


class Player(Actor):

    def __init__(self):
        super().__init__()
        self.center_x = 50
        self.center_y = 50
        self.texture = constants.PLAYER_IDLE
        self.scale = constants.SCALE
        self._change_x = 0
        self.change_y = 0
        self._items = arcade.SpriteList()
        self._was_hit = False
        self._water = 0


    
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
        
    def update(self):
        self._update_position()
        self._update_item_list()
        self.check_win()
            
        
    def _update_position(self):
        self.center_x += self.change_x
        self.center_y += self.change_y
        if self._was_hit:
            self.change_x = 0
            self.change_y = 0
            self._was_hit = False

    def _update_item_list(self):
        for i in range(len(self._items)):
            item = self._items[i]
            item.center_x = 30 * i + 10
            item.center_y = 13
            item.scale = constants.WATER_SCALE/2
            
    def pick_up_item(self, item):
        if item.get_type() == "water":
            self._items.append(item)
            self._water += 1
            

    def has_water(self):
        return self._water > 0
        
    def use_water(self):
        self._water -= 1
        return self._items.pop()
        

    def get_items(self):
        return self._items

    def check_win(self):
        return self.center_y > constants.SCREEN_HEIGHT or self.center_x > constants.SCREEN_WIDTH

            