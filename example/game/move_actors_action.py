from core.action import Action


class MoveActorsAction(Action):
    
    def __init__(self,engine):
        super().__init__(engine)
        self._engine = engine

    def execute(self, cast, cue, callback):
        self._move_player(cast)
        
    def _move_player(self, cast):
        player = cast.first_actor("player")
        player.update()


        
