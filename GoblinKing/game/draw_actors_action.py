from core.action import Action
from game import constants
import arcade


class DrawActorsAction(Action):
    def __init__(self, engine):
        super().__init__(engine)

    def execute(self, cast, cue, callback):
        self._draw_maze(cast)
        self._draw_player(cast)
        self._draw_objects(cast)
        self._draw_timer(cast)
        self._draw_score(cast)
        self._draw_gem_count(cast)
        self._draw_lives(cast)

    def _draw_maze(self, cast):
        walls = cast.get_actors("walls")
        for block in walls:
            block.draw()

    def _draw_player(self, cast):
        player = cast.first_actor("player")
        self.lives = player.get_lives()
        player.get_spray().draw()
        player.draw()  # There is only one

    def _draw_objects(self, cast):
        items = cast.get_actors("items")

        for item_list in items:
            for item in item_list:
                item.draw()

    def _draw_timer(self, cast):
        timer = cast.get_actors("timer")
        output = f"Time elapsed: {timer[0].display_time}"
        arcade.draw_text(
            output, timer[0].center_x, timer[0].center_y + 5, arcade.color.BLACK, 16
        )

    def _draw_score(self, cast):
        score = cast.get_actors("score")
        output = f"Score: {score[0].score}"
        arcade.draw_text(
            output,
            score[0].center_x - 75,
            score[0].center_y + 5,
            arcade.color.BLACK,
            16,
        )

    def _draw_gem_count(self, cast):
        gem_count = cast.first_actor("gem count")
        count = gem_count.get_count()
        output = f"{count}/{constants.GEM_TARGET}"
        gem_count.draw()
        arcade.draw_text(
            output,
            gem_count.center_x + 20,
            gem_count.center_y - 10,
            arcade.color.BLACK,
            16,
        )

    def _draw_lives(self, cast):
        lives = cast.get_actors("lives")
        for life in lives:
            life.draw()
        if self.lives == 2:
            lives[2].lose_heart()
        elif self.lives == 1:
            lives[1].lose_heart()
        elif self.lives == 0:
            lives[0].lose_heart()
        else:
            pass
