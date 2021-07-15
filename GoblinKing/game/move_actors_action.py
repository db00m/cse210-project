from core.action import Action


class MoveActorsAction(Action):
    
    def __init__(self,engine):
        super().__init__(engine)
        self._engine = engine
    def execute(self, cast, cue, callback):
        self._move_player(cast)
        self._update(cast)
        
    def _move_player(self, cast):
        player = cast.first_actor("player")
        self._engine.update()
        player.update()
    
    def _update(self, cast):
        timer = cast.get_actors("timer")[0]
        timer.update()
        gem_count = cast.first_actor("gem count")
        gem_count.update()

        


        
        