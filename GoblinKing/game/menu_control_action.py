import arcade
from core.action import Action
from game import constants
from core.cue import Cue
from game.game_scene import GameScene


class MenuContolAction(Action):
    def __init__(self, engine):
        super().__init__(engine)

    def execute(self, cast, cue, callback):
        cue_info = cue.get_info()
        key = cue_info["key"]

        if key == arcade.key.ENTER:
            callback.on_scene_finished(GameScene())
