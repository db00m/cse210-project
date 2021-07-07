from core.action import Action


class DrawActorsAction(Action):
    
    def __init__(self, engine):
        super().__init__(engine)

    def execute(self, cast, cue, callback):
        self._draw_maze(cast)
        self._draw_player(cast)
        
    def _draw_maze(self, cast):
        walls = cast.get_actors("walls")
        for block in walls:
            block.draw()
            
    def _draw_player(self, cast):
        player = cast.get_actors("player")
        player[0].draw() #There is only one
    