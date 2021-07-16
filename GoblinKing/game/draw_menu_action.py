from core.action import Action
import arcade


class DrawMenuAction(Action):
    def __init__(self, engine):
        super().__init__(engine)

    def execute(self, cast, cue, callback):
        self._draw_background(cast)
        title = cast.first_actor("title")
        title.draw()
        arcade.draw_text(
            "Press 'Enter' to Start",
            title.center_x - 100,
            title.center_y - 300,
            arcade.color.BLACK,
            16,
        )

    def _draw_background(self, cast):
        walls = cast.get_actors("background")
        for block in walls:
            block.draw()
