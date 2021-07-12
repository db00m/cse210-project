import arcade
from core.action import Action
from game import constants
from core.cue import Cue


class ControlActorsAction(Action):
    
    def __init__(self, engine):
        super().__init__(engine)

    def execute(self, cast, cue, callback):
        cue_info = cue.get_info()
        key = cue_info["key"]
        player = cast.get_actors("player")[0] #There is only one
        
        # If a key is pressed, this code moves the player accordingly:
        if cue.get_name() == Cue.ON_KEY_PRESS:
            
            if key == arcade.key.UP:
                player.walk(constants.UP)
            elif key == arcade.key.DOWN:
                player.walk(constants.DOWN)
            elif key == arcade.key.RIGHT:
                player.walk(constants.RIGHT)
            elif key == arcade.key.LEFT:
                player.walk(constants.LEFT)
                

                
        # If a key is released, this code stops moving the player:
        elif cue.get_name() == Cue.ON_KEY_RELEASE:
            player.stop()
            
            

    