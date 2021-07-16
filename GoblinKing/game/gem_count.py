from core.actor import Actor
from game import constants


class GemCount(Actor):
    def __init__(self, **args):
        super().__init__(**args)
        self.center_x = constants.SCREEN_WIDTH / 2 - 20
        self.center_y = constants.SCREEN_HEIGHT - 10
        self._gem_count = 0
        self._new_gems = 0
        self.texture = constants.GEM[1]
        self.scale = 0.3

    def add_gem(self):
        self._new_gems += 1

    def update(self):
        self._gem_count += self._new_gems
        self._new_gems = 0

    def get_count(self):
        return self._gem_count
