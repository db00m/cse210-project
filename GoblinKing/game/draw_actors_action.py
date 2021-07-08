from core.action import Action
import arcade


class DrawActorsAction(Action):
    
    def __init__(self, engine):
        super().__init__(engine)

    def execute(self, cast, cue, callback):
        self._draw_maze(cast)
        self._draw_player(cast)
        self._draw_timer(cast)
        self._draw_score(cast)
        
    def _draw_maze(self, cast):
        walls = cast.get_actors("walls")
        for block in walls:
            block.draw()
            
    def _draw_player(self, cast):
        player = cast.get_actors("player")
        player[0].draw() #There is only one
    
    def _draw_timer(self, cast):
        timer = cast.get_actors("timer")
        output = f"Time elapsed: {timer[0].elapsed_time}"
        arcade.draw_text(output, timer[0].center_x, timer[0].center_y, arcade.color.WHITE, 16)

    def _draw_score(self, cast):
        score = cast.get_actors("score")
        output = f"Score: {score[0].score}"
        arcade.draw_text(output, score[0].center_x, score[0].center_y, arcade.color.WHITE, 16)