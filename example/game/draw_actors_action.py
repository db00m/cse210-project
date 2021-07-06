from core.action import Action


class DrawActorsAction(Action):
    
    def __init__(self, engine):
        super().__init__(engine)

    def execute(self, cast, cue, callback):
        self._draw_maze(cast)
        
    def _draw_maze(self, cast):
        walls = cast.get_actors("walls")
        for block in walls:
            block.draw()
    