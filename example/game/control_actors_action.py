import arcade
from core.action import Action


class ControlActorsAction(Action):
    
    def __init__(self):
        super().__init__()

    def execute(self, cast, cue, callback):
        cue_info = cue.get_info()
        key = cue_info["key"]
        cast["player"]
        
        
        # TODO: Write the logic for player movement here:
        if key == arcade.key.UP:
            pass
            
    